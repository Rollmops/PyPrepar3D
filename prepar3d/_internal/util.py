import urllib2
import json

def get_json_from_url(url):
    req = urllib2.Request(url)
    opener = urllib2.build_opener()
    return json.load(opener.open(req))