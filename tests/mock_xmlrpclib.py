import xmlrpclib

def ServerProxy(url):
    server = Server()
    return server

def raw_input(msg):pass

def getpass(msg):pass


class Server(object):
    def __init__(self):
        self.metaWeblog = metaWeblog()

class metaWeblog(object):
    def __init__(self):pass
    def getRecentPosts(self, n, username, password):pass

class Fault(Exception):pass

