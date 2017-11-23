import gi

from gtkml.exception.gtmkl_exception import GtkmlException
from gtkml.gtkml.enums import Sizes
from gtkml.tools.frame_object_tools import is_layout_widget

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import gtkml.gtkml.tag_frame_objects as OBJ
from gtkml.gtkml.tag import Tag

import gtkml.runtime.execute.assembly_tools.glob as GLOB
import gtkml.gtkml.static.names as NAMES

import gtkml.runtime.runtime_variables as VAR

_ = OBJ._

from gtkml.runtime.object_pool import OBJECT_POOL

from gtkml.gtkml.tag_frame_objects import ENVIRONMENT


class ObjectAssembler:
    def __init__(self):
        pass

    def get_object(self, tag):
        name = tag.name
        if name == "application": return self._get_application(tag)
        if name == "python": return self._get_python(tag)
        if name == "window": return self._get_window(tag)
        if name == "header": return self._get_header(tag)
        if name == "body": return self._get_body(tag)
        if name == "title": return self._get_title(tag)

        if name == "hbox": return self._get_hbox(tag)
        if name == "vbox": return self._get_vbox(tag)

        if name == "label": return self._get_label(tag)
        if name == "button": return self._get_button(tag)
        if name == "entry": return self._get_entry(tag)

        if name == "appmenu": return self._get_appmenu(tag)
        if name == "submenu": return self._get_submenu(tag)
        if name == "menu-item": return self._get_menu_item(tag)

    def _get_application(self, tag):
        name = GLOB.get_attribute(tag, "name")
        tagID = GLOB.get_attribute(tag, "id")

        components = []
        for component in tag.children:
            if isinstance(component, Tag):
                if component.name not in NAMES.APPLICATION_CHILDREN:
                    raise GtkmlException("Invalid child")
            components.append(self.get_object(component))

        app = OBJ.Application()
        app.name = name
        app.components = components
        OBJECT_POOL.set_object(tagID, app, [])
        return app

    def _get_python(self, tag):
        python = OBJ.Python()
        src = GLOB.get_attribute(tag, "src")
        python.src = str(src)
        print(src)
        print(python.src)
        g = python.src
        #print(g)
        python.load()
        python.execute()

    def _get_window(self, tag):
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
                    raise GtkmlException("Invalid child")
                elif component.name == "body":
                    window.body = self._get_body(component)
                    window.value.add(window.body.value)
                elif component.name == "appmenu":
                    window.value.add(self.get_object(component).value)

        if title is not None: win.set_title(title)
        else: win.set_title("")

        if height is not None and width is not None:
            win.set_size_request(int(width), int(height))

        if visible: window.show()
        else: window.hide()

        OBJECT_POOL.set_object(tagID, window, [])
        return window

    def _get_header(self, tag):
        pass

    def _get_body(self, tag):
        body = OBJ.Body()
        body.value = Gtk.VBox()
        body.children = []

        tagID = GLOB.get_attribute(tag, "id")

        for widget_tag in tag.children:
            if isinstance(widget_tag, Tag):
                obj = self.get_object(widget_tag)
                if widget_tag.name in NAMES.WIDGETS:
                    expand = GLOB.get_str_bool_attribute(widget_tag, Sizes.EXPAND)
                    fill = GLOB.get_str_bool_attribute(widget_tag, Sizes.FILL)
                    padding = GLOB.get_str_num_attribute(widget_tag, "padding")
                    body.value.pack_start(obj.value, expand=expand, fill=fill, padding=padding)
                elif widget_tag.name in NAMES.UNIVERSAL:
                    body.append(obj)
                elif widget_tag.name == "appmenu":
                    expand = GLOB.get_str_bool_attribute(widget_tag, Sizes.EXPAND)
                    body.value.pack_start(obj.value, expand=expand, fill=True, padding=0)
        OBJECT_POOL.set_object(tagID, body, [])
        return body

    def _get_hbox(self, tag):
        hbox = OBJ.HBox()
        hbox.value = Gtk.HBox()
        hbox.children = []

        tagID = GLOB.get_attribute(tag, "id")

        for widget_tag in tag.children:
            if isinstance(widget_tag, Tag):
                obj = self.get_object(widget_tag)
                if widget_tag.name in NAMES.WIDGETS:
                    expand = GLOB.get_str_bool_attribute(widget_tag, Sizes.EXPAND)
                    fill = GLOB.get_str_bool_attribute(widget_tag, Sizes.FILL)
                    padding = GLOB.get_str_num_attribute(widget_tag, "padding")
                    hbox.value.pack_start(obj.value, expand=expand, fill=fill, padding=padding)
                elif widget_tag.name in NAMES.UNIVERSAL:
                    hbox.append(obj)
        OBJECT_POOL.set_object(tagID, hbox, "")
        return hbox

    def _get_vbox(self, tag):
        vbox = OBJ.VBox()
        vbox.value = Gtk.VBox()
        vbox.children = []

        tagID = GLOB.get_attribute(tag, "id")

        for widget_tag in tag.children:
            if isinstance(widget_tag, Tag):
                obj = self.get_object(widget_tag)
                if widget_tag.name in NAMES.WIDGETS:
                    expand = GLOB.get_str_bool_attribute(widget_tag, Sizes.EXPAND)
                    fill = GLOB.get_str_bool_attribute(widget_tag, Sizes.FILL)
                    padding = GLOB.get_str_num_attribute(widget_tag, "padding")
                    vbox.value.pack_start(obj.value, expand=expand, fill=fill, padding=padding)
                elif widget_tag.name in NAMES.UNIVERSAL:
                    vbox.append(obj)
        OBJECT_POOL.set_object(tagID, vbox, "")
        return vbox

    def _get_label(self, tag):
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

    def _get_button(self, tag):
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

    def _get_entry(self, tag):
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

    def _get_appmenu(self, tag):
        appmenu = OBJ.AppMenu()
        menubar_gtk = Gtk.MenuBar()

        appmenu.value = menubar_gtk

        tagID = GLOB.get_attribute(tag, "id")

        if isinstance(menubar_gtk, Gtk.MenuBar):
            print("ASD")
            for item in tag.children:
                obj = self.get_object(item)
                name = item.name
                if name == "submenu":
                    appmenu.value.append(obj.value)
        OBJECT_POOL.set_object(tagID, appmenu, [])
        return appmenu

    def _get_submenu(self, tag):
        submenu = OBJ.AppSubMenu()
        menuitem_gtk = Gtk.MenuItem(GLOB.get_attribute(tag, "title"))
        menu = Gtk.Menu()
        has_child = False

        tagID = GLOB.get_attribute(tag, "id")

        if isinstance(menuitem_gtk, Gtk.MenuItem):
            for menuitem in tag.children:
                has_child = True
                obj = self.get_object(menuitem)
                if menuitem.name == "menu-item":
                    menu.add(obj.value)

        if has_child:
            menuitem_gtk.set_submenu(menu)
        submenu.value = menuitem_gtk

        OBJECT_POOL.set_object(tagID, submenu, [])
        return submenu

    def _get_menu_item(self, tag):
        menuitem = OBJ.AppMenuItem()
        menuitem_gtk = Gtk.MenuItem(GLOB.get_attribute(tag, "title"))
        menuitem.value = menuitem_gtk

        tagID = GLOB.get_attribute(tag, "id")
        OBJECT_POOL.set_object(tagID, menuitem, [])

        return menuitem

