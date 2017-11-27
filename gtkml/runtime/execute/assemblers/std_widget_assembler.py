import gi

from gtkml.gtkml.enums import Sizes

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


from gtkml.exception.gtmkl_exception import GtkmlException
from gtkml.runtime.object_pool import OBJECT_POOL, ENVIRONMENT
import gtkml.runtime.execute.assembly_tools.glob as GLOB
import gtkml.gtkml.tag_frame_objects as OBJ

from gtkml.gtkml.tag import Tag
import gtkml.gtkml.static.names as NAMES


class StandardWidgetAssembler():
    def __init__(self, assembler):
        self.assembler = assembler

    def get_button(self, tag):
        button = OBJ.Button()
        button.value = Gtk.Button()

        tagID = GLOB.get_attribute(tag, "id")
        onclick_str = GLOB.get_attribute(tag, "onclick")

        text = tag.text
        if isinstance(button.value, Gtk.Button):
            button.value.set_label(text)

        if onclick_str is not None:
            print(onclick_str)
            button.onclick = ENVIRONMENT[onclick_str]

        for tag in tag.children:
            if isinstance(tag, Tag):
                print(tag.name)
                if tag.name in NAMES.UNIVERSAL:
                    pass
                else:
                    raise GtkmlException("Invalid child!")
        OBJECT_POOL.set_object(tagID, button, [])
        return button

    def get_label(self, tag):
        label = OBJ.Label()
        label.value = Gtk.Label()

        tagID = GLOB.get_attribute(tag, "id")

        text = tag.text
        if isinstance(label.value, Gtk.Label):
            label.value.set_text(text)

        for tag in tag.children:
            if isinstance(tag, Tag):
                if tag.name in NAMES.UNIVERSAL:
                    pass
                else:
                    raise GtkmlException("Invalid child!")
        OBJECT_POOL.set_object(tagID, label, "")
        return label

    def get_entry(self, tag):
        entry = OBJ.Entry()
        entry.value = Gtk.Entry()

        tagID = GLOB.get_attribute(tag, "id")

        text = tag.text
        if isinstance(entry.value, Gtk.Entry):
            entry.value.set_text(text)

        for tag in tag.children:
            if isinstance(tag, Tag):
                if tag.name in NAMES.UNIVERSAL:
                    pass
                else:
                    raise GtkmlException("Invalid child!")
        OBJECT_POOL.set_object(tagID, entry, [])
        return entry
