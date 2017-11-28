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

class MiscellaneousAssembler():
    def __init__(self, assembler):
        self.assembler = assembler

    def get_application(self, tag):
        name = GLOB.get_attribute(tag, "name")
        tagID = GLOB.get_attribute(tag, "id")

        components = []
        for component in tag.children:
            if isinstance(component, Tag):
                if component.name not in NAMES.APPLICATION_CHILDREN:
                    raise GtkmlException("Invalid child")
            components.append(self.assembler.get_object(component))

        app = OBJ.Application()
        app.name = name
        app.components = components
        OBJECT_POOL.set_object(tagID, app, [])
        return app

    def get_python(self, tag):
        python = OBJ.Python()
        src = GLOB.get_attribute(tag, "src")
        python.src = str(src)
        print(src)
        print(python.src)
        g = python.src
        python.load()
        python.execute()