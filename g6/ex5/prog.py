import cherrypy

class Root(object):

    @cherrypy.expose
    def index(self):
        return "Eu sou o index Root"

    @cherrypy.expose
    def form(self):
        cherrypy.response.headers["Content-Type"] = "text/html"
        return open("/mnt/c/Users/joaoe/Documents/GitHub/labi_python/g6/ex5/form.html", "r").read()


if __name__ == "__main__":
    cherrypy.tree.mount(Root(), "/")
    cherrypy.server.start()