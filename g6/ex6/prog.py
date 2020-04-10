import cherrypy

class Actions(object):
    @cherrypy.expose
    def doLogin(self, username=None, password=None):
        return "TODO: verificar as credenciais do utilizador " + username

class Root(object):

    def __init__(self):
        self.actions = Actions()

    @cherrypy.expose
    def index(self):
        return "Eu sou o index Root"

    @cherrypy.expose
    def form(self):
        cherrypy.response.headers["Content-Type"] = "text/html"
        return open("/mnt/c/Users/joaoe/Documents/GitHub/labi_python/g6/ex6/form.html", "r").read()


if __name__ == "__main__":
    cherrypy.tree.mount(Root(), "/")
    cherrypy.server.start()