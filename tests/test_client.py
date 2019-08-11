import fecho
import pytest

MIN_VALID_COOKIE = """[
{
    "name": "c_user",
    "value": ""
},
{
    "name": "datr",
    "value": ""
},
{
    "name": "dpr",
    "value": ""
},
{
    "name": "fr",
    "value": ""
},
{
    "name": "presence",
    "value": ""
},
{
    "name": "sb",
    "value": ""
},
{
    "name": "spin",
    "value": ""
},
{
    "name": "wd",
    "value": ""
},
{
    "name": "xs",
    "value": ""
}
]"""


class TestCookies:
    def test_invalid_cookie_type(self):
        with pytest.raises(fecho.InvalidCookie):
            client = fecho.Client([{}])

    def test_invalid_cookie_keys(self):
        with pytest.raises(fecho.InvalidCookie):
            client = fecho.Client("""[{"name":"c_user"}]""")

    def test_valid_cookie(self):
        client = fecho.Client(MIN_VALID_COOKIE)


class TestURLs:
    def test_invalid_schema(self):
        client = fecho.Client(MIN_VALID_COOKIE)
        with pytest.raises(fecho.InvalidURL):
            client.get("www.google.com")

    def test_valid_schema(self):
        client = fecho.Client(MIN_VALID_COOKIE)
        with pytest.raises(fecho.InvalidCookie):
            client.get("https://www.google.com")
