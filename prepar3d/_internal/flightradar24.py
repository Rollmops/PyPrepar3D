from urllib.parse import urlparse, urljoin

from prepar3d._internal.util import get_json_from_url


class Flightradar24:
    def __init__(self, load_all=True, server=None, base_url="http://www.flightradar24.com", zone="full"):
        self.url_base = base_url
        self.zone = zone
        if load_all is True:
            self.refresh_data(server, zone=zone)
        elif server is None:
            self.refresh_best_server()

    def refresh_best_server(self):
            self.url_balance = "balance.json"
            all_servers = get_json_from_url(urljoin(self.url_base, self.url_balance))
            self.server = min(all_servers, key=all_servers.get)

    def refresh_data(self, server=None, zone="full"):
        if server is None:
            self.refresh_best_server()
        else:
            self.server = server
        self.airports = get_json_from_url(urljoin(self.url_base, "_json/airports.php"))["rows"]
        self.airlines = get_json_from_url(urljoin(self.url_base, "_json/airlines.php"))["rows"]
        self.zones = get_json_from_url(urljoin(self.url_base, "js/zones.js.php"))

        self.refresh_aircrafts(zone=zone)

    def refresh_aircrafts(self, zone="full"):
        url = urljoin("http://" + self.server, "zones/%s_all.json" % zone)
        self.aircrafts = get_json_from_url(url)
