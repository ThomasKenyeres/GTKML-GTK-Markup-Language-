import gi

from gtkml.gtkml.enums import Sizes

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


from gtkml.exception.gtmkl_exception import GtkmlException
from gtkml.runtime.object_pool import OBJECT_POOL
import gtkml.runtime.execute.assembly_tools.glob as GLOB
import gtkml.gtkml.tag_frame_objects as OBJ

from gtkml.gtkml.tag import Tag
import gtkml.gtkml.static.names as NAMES

class LayoutAssembler():
    def __init__(self, assembler):
        self.assembler = assembler

    def get_window(self, tag):
        title = GLOB.get_attribute(tag, "title")
        visible = GLOB.get_str_bool_attribute(tag, "show")
        width = GLOB.get_attribute(tag, "width")
        height = GLOB.get_attribute(tag, "height")

        tagID = GLOB.get_attribute(tag, "id")

        window = OBJ.Window()
        win = Gtk.Window()
        win.connect("delete-event", Gtk.main_quit)

        window.body = OBJ.Body()
        window.body.children = []
        window.body.value = Gtk.VBox()

        window.value = win

        children = []
        for component in tag.children:
            if isinstance(component, Tag):
                if component.name not in NAMES.WINDOW_CHILDREN:
                    raise GtkmlException("Invalid child: {} cannot be embedded into {}".format(
                        component.name, tag.name
                    ))
                elif component.name == "body":
                    window.body = self.assembler._get_body(component)
                    window.value.add(window.body.value)
                elif component.name == "appmenu":
                    window.value.add(self.assembler.get_object(component).value)

        if title is not None:
            win.set_title(title)
        else:
            win.set_title("")

        if height is not None and width is not None:
            win.set_size_request(int(width), int(height))

        if visible:
            window.show()
        else:
            window.hide()

        OBJECT_POOL.set_object(tagID, window, [])
        return window

    def get_body(self, tag):
        body = OBJ.Body()
        body.value = Gtk.VBox()
        body.children = []

        tagID = GLOB.get_attribute(tag, "id")

        for widget_tag in tag.children:
            if isinstance(widget_tag, Tag):
                obj = self.assembler.get_object(widget_tag)
                if widget_tag.name in NAMES.WIDGETS:
                    expand = GLOB.get_str_bool_attribute(widget_tag, Sizes.EXPAND)
                    fill = GLOB.get_str_bool_attribute(widget_tag, Sizes.FILL)
                    margin = GLOB.get_str_num_attribute(widget_tag, Sizes.MARGIN)
                    body.value.pack_start(obj.value, expand=expand, fill=fill, padding=margin)
                elif widget_tag.name in NAMES.UNIVERSAL:
                    body.append(obj)
                elif widget_tag.name == "appmenu":
                    expand = GLOB.get_str_bool_attribute(widget_tag, Sizes.EXPAND)
                    body.value.pack_start(obj.value, expand=expand, fill=True, padding=0)
        OBJECT_POOL.set_object(tagID, body, [])
        return body

    def get_hbox(self, tag):
        hbox = OBJ.HBox()
        hbox.value = Gtk.HBox()
        hbox.children = []

        tagID = GLOB.get_attribute(tag, "id")

        for widget_tag in tag.children:
            if isinstance(widget_tag, Tag):
                obj = self.assembler.get_object(widget_tag)
                if widget_tag.name in NAMES.WIDGETS:
                    expand = GLOB.get_str_bool_attribute(widget_tag, Sizes.EXPAND)
                    fill = GLOB.get_str_bool_attribute(widget_tag, Sizes.FILL)
                    margin = GLOB.get_str_num_attribute(widget_tag, Sizes.MARGIN)
                    hbox.value.pack_start(obj.value, expand=expand, fill=fill, padding=margin)
                elif widget_tag.name in NAMES.UNIVERSAL:
                    hbox.append(obj)
        OBJECT_POOL.set_object(tagID, hbox, "")
        return hbox

    def get_vbox(self, tag):
        vbox = OBJ.VBox()
        vbox.value = Gtk.VBox()
        vbox.children = []

        tagID = GLOB.get_attribute(tag, "id")

        for widget_tag in tag.children:
            if isinstance(widget_tag, Tag):
                obj = self.assembler.get_object(widget_tag)
                if widget_tag.name in NAMES.WIDGETS:
                    expand = GLOB.get_str_bool_attribute(widget_tag, Sizes.EXPAND)
                    fill = GLOB.get_str_bool_attribute(widget_tag, Sizes.FILL)
                    margin = GLOB.get_str_num_attribute(widget_tag, Sizes.MARGIN)
                    vbox.value.pack_start(obj.value, expand=expand, fill=fill, padding=margin)
                elif widget_tag.name in NAMES.UNIVERSAL:
                    vbox.append(obj)
        OBJECT_POOL.set_object(tagID, vbox, "")
        return vbox

    def get_grid(self, tag):
        grid = OBJ.Grid()
        grid.value = Gtk.Grid()
        grid.children = []

        tagID = GLOB.get_attribute(tag, "id")

        i = 0
        for component in tag.children:
            if isinstance(component, Tag):
                obj = self.assembler.get_object(component)
                if component.name in NAMES.WIDGETS:
                    if i == 0:
                        grid.value.add(obj.value)
                    else:
                        left = GLOB.get_str_num_attribute(component, "left")
                        top = GLOB.get_str_num_attribute(component, "top")
                        right = GLOB.get_str_num_attribute(component, "right")
                        bottom = GLOB.get_str_num_attribute(component, "bottom")
                        width = right - left
                        height = bottom - top
                        if GLOB.numbers_are_0(left, top, width, height, right, bottom):
                            grid.value.add(obj.value)
                        else:
                            print("{}, {}, {}, {}".format(left, top, width, height))
                            grid.value.attach(child=obj.value, left=left, top=top,
                                              width=width, height=height)
                elif component.name in NAMES.UNIVERSAL:
                    grid.append(obj)
            i += 1
        OBJECT_POOL.set_object(tagID, grid, [])
        return grid