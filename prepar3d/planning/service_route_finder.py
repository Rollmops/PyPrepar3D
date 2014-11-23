from html.parser import HTMLParser
import re
import urllib

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
        k_parser.feed(urllib.urlopen(self._base_url).read())
                
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
            
            request_data = '&'.join(['%s=%s' % (key, value) for key, value in data.iteritems()])
            
            route_request = urllib2.Request(self._base_url + self._find_script)
            route_request.add_header('Referer', self._base_url)
            route_request.add_header('Connection', 'keep-alive')
            
            route_repsonse = urllib2.urlopen(route_request, request_data).read()
            
