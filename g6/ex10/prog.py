import os
import cherrypy
PATH = os.path.abspath(os.path.dirname(__file__))

class Root(object):
    @cherrypy.expose
    
    def index(self):
        return "Eu sou o índice do Root (Root.index)"

def main():
    conf = {
            "/file": {
                	            "tools.staticfile.on": True,
                                "tools.staticfile.filename": os.path.join(PATH, "dummy.html")}
            }
    cherrypy.tree.mount(Root(), '/', config=conf)
    cherrypy.server.start()

if __name__ == "__main__":
    main()