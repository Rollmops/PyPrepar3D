import json
import codecs
from urllib import request


def get_json_from_url(url):
    req = request.Request(url)
    opener = request.build_opener()
    reader = codecs.getreader("utf-8")
    return json.load(reader(opener.open(req)))
