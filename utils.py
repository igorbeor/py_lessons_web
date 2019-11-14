from werkzeug.urls import url_parse


def base36_encode(number):
    assert number >= 0, "positive integer required"
    if number == 0:
        return "0"
    base36 = []
    while number != 0:
        number, i = divmod(number, 36)
        base36.append("0123456789abcdefghijklmnopqrstuvwxyz"[i])
    return "".join(reversed(base36))


def is_valid_url(url):
    parts = url_parse(url)
    return parts.scheme in ("http", "https")


def get_hostname(url):
    return url_parse(url).netloc
