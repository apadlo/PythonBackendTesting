import requests

from utilities.configurations import getConfig

api_base = getConfig()["API"]["endpoint"].rstrip("/")


def after_scenario(context, scenario):
    if "library" in scenario.tags:

        response_deleteBook = requests.post(
            f"{api_base}/Library/DeleteBook.php",
            json={"ID": context.bookId},
            headers={"Content-Type": "application/json"},
            timeout=15,
        )

        assert response_deleteBook.status_code == 200
        res_json = response_deleteBook.json()

        print(res_json["msg"])
        assert res_json["msg"] == "book is successfully deleted"
