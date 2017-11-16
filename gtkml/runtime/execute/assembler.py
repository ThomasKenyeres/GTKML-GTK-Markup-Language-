import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import gtkml.gtkml.tag_frame_objects as OBJ
from gtkml.gtkml.tag import Tag
#from gtkml.runtime.runtime import RUNTIME

class ObjectAssembler:
    def __init__(self):
        pass

    def get_object(self, tag):
        name = tag.name
        if name == "application": return self._get_application(tag)
        if name == "window": return self._get_window(tag)
        if name == "header": return self._get_header(tag)
        if name == "body": return self._get_body(tag)
        if name == "title": return self._get_title(tag)

    def _get_application(self, tag):
        name = None
        if "name" in tag.attributes:
            name = tag.attributes["name"]

        components = []
        for component in tag.children:
            print("comp.: " + str(component))
            components.append(self.get_object(component))

        app = OBJ.Application()
        app.name = name
        app.components = components
        #print(app.name)
        return app

    def _get_window(self, tag):
        #print(tag.name)
        title = None
        if "title" in tag.attributes:
            title = tag.attributes["title"]
        #print(title)

        visible = False
        if "show" in tag.attributes:
            if tag.attributes["show"] == "True":
                visible = True
        print("visible: " + str(visible))

        children = []
        for item in tag.children:
            children.append(item)

        window = OBJ.Window()
        win = Gtk.Window()
        win.connect("delete-event", Gtk.main_quit)


        if title is not None:
            win.set_title(title)
            window.value = win
            #window = Gtk.Window()
            #window.set_title(title)
            return window
        else:
            window.value = win

        window.visible = visible
        return window

def test1():
    assembler = ObjectAssembler()
    tag = Tag("window")
    # assembler.get_object(tag)
    # print(">" + tag.name + "<")
    # tag.parse("<window title='Hi you crazy! '></window>")
    tag.parse("<application><window title='Hi you crazy!' show='True'></window></application>")
    # print(">" + tag.name + "<")
    # win = assembler.get_object(tag)
    app = assembler.get_object(tag)
    print(">>> " + str(app))
    app.run()
    # win.show()
    Gtk.main()

def test2():
    xml = """
    <application>
        <window title='Hi you crazy!' show='True'>
        </window>
        
        <window title='Wazzup dude?' show='True'>
        </window>
    </application>
    """

    assembler = ObjectAssembler()
    tag = Tag("application")
    tag.parse(xml)

    app = assembler.get_object(tag)
    print(">>> " + str(app))
    app.run()

    Gtk.main()

if __name__ == '__main__':
    test2()