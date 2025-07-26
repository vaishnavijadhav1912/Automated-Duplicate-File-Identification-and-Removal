import urllib.request
import urllib.error
import socket



def is_connected():
    url = 'http://www.google.com/'
    try:
        urllib.request.urlopen(url, timeout=2)
        return True
    except (urllib.error.URLError, socket.timeout):
        pass
    
    

