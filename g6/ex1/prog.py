import cherrypy

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "Hello World!"

cherrypy.tree.mount(HelloWorld(), "/")
cherrypy.server.start()