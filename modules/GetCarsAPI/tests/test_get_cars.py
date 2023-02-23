import json
import os

from src.app import handler

def test_event():

    event_path = os.path.join(os.path.dirname(__file__), "event.json")

    with open(event_path, "r", encoding="utf-8") as event_file:
        event = json.loads(event_file.read())

    res = handler(event, None)

    assert res["statusCode"] == 200
    assert json.loads(res["body"])["body"] == "eyJ0ZXN0IjoiYm9keSJ0"
