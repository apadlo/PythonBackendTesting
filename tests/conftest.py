import json
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

import pytest
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


@pytest.fixture(scope="session")
def api_session():
    """Requests session with retries for transient API failures."""
    retry = Retry(
        total=3,
        backoff_factor=0.2,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=frozenset(["GET", "POST", "PUT", "DELETE"]),
        raise_on_status=False,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session = requests.Session()
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    yield session
    session.close()


@pytest.fixture(scope="session")
def default_timeout():
    return 10


@pytest.fixture(scope="session")
def mock_library_server():
    class Handler(BaseHTTPRequestHandler):
        flaky_get_counter = 0

        def _json(self, payload, code=200):
            encoded = json.dumps(payload).encode("utf-8")
            self.send_response(code)
            self.send_header("Content-Type", "application/json;charset=UTF-8")
            self.send_header("Content-Length", str(len(encoded)))
            self.end_headers()
            self.wfile.write(encoded)

        def do_GET(self):
            if self.path.startswith("/Library/GetBook.php"):
                Handler.flaky_get_counter += 1
                if Handler.flaky_get_counter == 1:
                    self._json({"error": "transient"}, code=503)
                    return
                self._json([
                    {"book_name": "Learn with Java", "isbn": "RGHCC", "aisle": "222"},
                    {"book_name": "Learn with Python", "isbn": "PY111", "aisle": "111"},
                ])
                return
            self._json({"error": "not found"}, code=404)

        def do_POST(self):
            if self.path == "/Library/Addbook.php":
                self._json({"Msg": "successfully added", "ID": "RGHCC222"})
                return
            if self.path == "/Library/DeleteBook.php":
                self._json({"msg": "book is successfully deleted"})
                return
            self._json({"error": "not found"}, code=404)

        def log_message(self, format, *args):
            return

    server = HTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()

    host, port = server.server_address
    yield f"http://{host}:{port}"

    server.shutdown()
    thread.join(timeout=2)
