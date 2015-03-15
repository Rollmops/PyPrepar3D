from html.parser import HTMLParser
import re
from urllib.request import urlopen, Request
from urllib.parse import urlencode

from prepar3d.planning.service_base import ServiceBase


class ServiceRouteFinder(ServiceBase):
    
    def __init__(self):
        self._base_url = 'http://rfinder.asalink.net/free/'
        self._find_script = 'autoroute_rtx.php'
        
    
    class _RouteFinderHTMLParser(HTMLParser):
        def __init__(self):
            HTMLParser.__init__(self)
            self.k_value = None
    
        def handle_starttag(self, tag, attrs):
            if tag == 'input':
                if ('name', 'k') in attrs and ('type', 'hidden') in attrs:
                    for attr in attrs: 
                        if attr[0] == 'value':
                            self.k_value = attr[1]
    
    
    def find(self, departure, destination, cycle, flightlevel_from, flightlevel_to, level, use_star='Y', use_sid='Y'):

        # retrieve k value from start page
        k_parser = ServiceRouteFinder._RouteFinderHTMLParser()
        k_parser.feed(urlopen(self._base_url).read().decode())
                
        if k_parser.k_value is not None:
            
            data = {'id1': departure,
                    'ic1':'',
                    'id2': destination,
                    'ic2':'',
                    'minalt': flightlevel_from,
                    'maxalt': flightlevel_to,
                    'lvl': level,
                    'dbid': cycle,
                    'usesid':use_sid,
                    'usestar': use_star,
                    'easet':'Y',
                    'rnav':'Y',
                    'natis':'',
                    'k': k_parser.k_value}
            
            request_data = urlencode(data).encode()
            route_request = Request(self._base_url + self._find_script, request_data)
            route_repsonse = urlopen(route_request).read().decode()
            print(route_repsonse)
            pattern = r'.*:\s+(?P<num_fixes>\d+)\s+fixes,\s+(?P<distance>\d+\.\d+).*'
            pattern = re.match(pattern, route_repsonse, re.DOTALL)
            if pattern:
                print(pattern.groupdict())
            
