from payLoad import addBookPayload
from utilities.configurations import getConfig
from utilities.resources import ApiResources


def test_add_book_payload_structure():
    payload = addBookPayload("isbn123", "456")

    assert payload == {
        "name": "Learn Appium Automation with Java",
        "isbn": "isbn123",
        "aisle": "456",
        "author": "John Hoe",
    }


def test_api_resources_paths_are_stable():
    assert ApiResources.addBook == "/Library/Addbook.php"
    assert ApiResources.delBook == "/Library/DeleteBook.php"


def test_config_has_safe_defaults_without_properties_file():
    config = getConfig()
    assert config["API"]["endpoint"].startswith("http")
