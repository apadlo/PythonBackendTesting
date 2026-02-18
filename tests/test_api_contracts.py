import pytest

from payLoad import addBookPayload


@pytest.mark.parametrize(
    "isbn,aisle",
    [
        ("RGHCC", "222"),
        ("ABCD1", "101"),
    ],
)
def test_add_book_and_delete_contract(mock_library_server, api_session, default_timeout, isbn, aisle):
    headers = {"Content-Type": "application/json"}
    payload = addBookPayload(isbn, aisle)

    add_resp = api_session.post(
        f"{mock_library_server}/Library/Addbook.php",
        json=payload,
        headers=headers,
        timeout=default_timeout,
    )

    assert add_resp.status_code == 200
    add_json = add_resp.json()
    assert {"Msg", "ID"}.issubset(add_json.keys())
    assert "successfully added" in add_json["Msg"]

    del_resp = api_session.post(
        f"{mock_library_server}/Library/DeleteBook.php",
        json={"ID": add_json["ID"]},
        headers=headers,
        timeout=default_timeout,
    )
    assert del_resp.status_code == 200
    assert del_resp.json() == {"msg": "book is successfully deleted"}


def test_get_books_retry_timeout_and_schema(mock_library_server, api_session, default_timeout):
    resp = api_session.get(
        f"{mock_library_server}/Library/GetBook.php",
        params={"AuthorName": "Rahul Shetty"},
        timeout=default_timeout,
    )

    assert resp.status_code == 200
    assert "application/json" in resp.headers["Content-Type"]

    books = resp.json()
    assert isinstance(books, list)
    assert books, "Expected at least one book in response"

    for book in books:
        assert set(["book_name", "isbn", "aisle"]).issubset(book.keys())
        assert all(isinstance(book[field], str) and book[field] for field in ["book_name", "isbn", "aisle"])

    actual = next(book for book in books if book["isbn"] == "RGHCC")
    assert actual == {"book_name": "Learn with Java", "isbn": "RGHCC", "aisle": "222"}
