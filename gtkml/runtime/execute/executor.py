import gi

from gtkml.gtkml.tag_frame_objects import Application
from gtkml.gtkml.tag import Tag
#from gtkml.runtime.real_runtime import RUNTIME

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from gtkml.runtime.execute.object_builder import ObjectBuilder


class Executor():
    def __init__(self, tag):
        self.__builder = ObjectBuilder()
        self.__tag = tag

    def execute(self):
        e = self.__builder.build(self.__tag)
        if isinstance(e, Application):
            e.run()
            Gtk.main()





if __name__ == '__main__':
    from gtkml.parser.parser import DOMParser

    xml = """
    <application>
        <window title='Hi you crazy!' show='True'>
        </window>
        
        <window title='Wazzup dude?' show='True'>
        </window>
    </application>
    """

    parser = DOMParser()
    executor = Executor(parser.parse(xml))
    executor.execute()
    #Gtk.main()