from utils import base36_encode
import re


def insert_url(redis, url):
    short_id = redis.get("reverse-url:" + url)
    if short_id is not None:
        return short_id
    url_num = redis.incr("last-url-id")
    short_id = base36_encode(url_num)
    redis.set("url-target:" + short_id, url)
    redis.set("reverse-url:" + url, short_id)
    return short_id


def get_url(redis, short_id):
    return redis.get("url-target:" + short_id)


def increment_url(redis, short_id):
    redis.incr("click-count:" + short_id)


def get_count(redis, short_id):
    return int(redis.get("click-count:" + short_id) or 0)


def get_list_urls(redis):
    keys = redis.keys("url-target:*")
    return [{
        'id': re.search(r'\d+', key.decode('utf-8')).group(0),
        'url': redis.get(key).decode('utf-8')}
        for key in keys]
