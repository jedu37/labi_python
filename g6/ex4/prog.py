import cherrypy

class Html(object):
    @cherrypy.expose
    def index(self):
        return "Eu sou o índice do Html"
    
    @cherrypy.expose
    def red(self):
        f = open("/mnt/c/Users/joaoe/Documents/GitHub/labi_python/g6/ex4/redpage.html","r")
        page = f.read()
        f.close()
        return page
    
    @cherrypy.expose
    def blue(self):
        f = open("/mnt/c/Users/joaoe/Documents/GitHub/labi_python/g6/ex4/bluepage.html","r")
        page = f.read()
        f.close()
        return page
    
    @cherrypy.expose
    def purple(self):
        f = open("/mnt/c/Users/joaoe/Documents/GitHub/labi_python/g6/ex4/purplepage.html","r")
        page = f.read()
        f.close()
        return page
    
    @cherrypy.expose
    def yellow(self):
        f = open("/mnt/c/Users/joaoe/Documents/GitHub/labi_python/g6/ex4/yellowpage.html","r")
        page = f.read()
        f.close()
        return page


class Root(object):
    def __init__(self):
        self.html = Html()

    @cherrypy.expose
    
    def index(self):
        return "Eu sou o index Root"

if __name__ == "__main__":
    cherrypy.tree.mount(Root(), "/")
    cherrypy.server.start()