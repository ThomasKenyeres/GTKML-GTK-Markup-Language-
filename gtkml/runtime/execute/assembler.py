import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import gtkml.gtkml.gtk_frame_objects as OBJ
from gtkml.gtkml.tag import Tag


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
        pass

    def _get_window(self, tag):
        #print(tag.name)
        title = tag.attributes["title"]
        #print(title)
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
            return window

if __name__ == '__main__':
    assembler = ObjectAssembler()
    tag = Tag("window")
    #assembler.get_object(tag)
    #print(">" + tag.name + "<")
    tag.parse("<window title='Hi there you crazy '></window>")
    #print(">" + tag.name + "<")
    win = assembler.get_object(tag)
    win.show()
    Gtk.main()
