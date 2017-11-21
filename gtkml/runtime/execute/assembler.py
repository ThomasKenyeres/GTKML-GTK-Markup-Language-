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

        components = []
        for component in tag.children:
            if isinstance(component, Tag):
                if component.name not in NAMES.APPLICATION_CHILDREN:
                    raise GtkmlException("Invalid child")
            components.append(self.get_object(component))

        app = OBJ.Application()
        app.name = name
        app.components = components
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

        return window

    def _get_header(self, tag):
        pass

    def _get_body(self, tag):
        body = OBJ.Body()
        body.value = Gtk.VBox()
        body.children = []

        for widget_tag in tag.children:
            if isinstance(widget_tag, Tag):
                obj = self.get_object(widget_tag)
                if widget_tag.name in NAMES.WIDGETS:
                    #print(">>>" + str(widget_tag.name))
                    expand = GLOB.get_str_bool_attribute(widget_tag, Sizes.EXPAND)
                    fill = GLOB.get_str_bool_attribute(widget_tag, Sizes.FILL)
                    padding = GLOB.get_str_num_attribute(widget_tag, "padding")
                    body.value.pack_start(obj.value, expand=expand, fill=fill, padding=padding)
                elif widget_tag.name in NAMES.UNIVERSAL:
                    body.append(obj)
                elif widget_tag.name == "appmenu":
                    expand = GLOB.get_str_bool_attribute(widget_tag, Sizes.EXPAND)
                    body.value.pack_start(obj.value, expand=expand, fill=True, padding=0)
        return body

    def _get_hbox(self, tag):
        hbox = OBJ.HBox()
        hbox.value = Gtk.HBox()
        hbox.children = []

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
        return hbox

    def _get_vbox(self, tag):
        vbox = OBJ.VBox()
        vbox.value = Gtk.VBox()
        vbox.children = []

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
        return vbox

    def _get_label(self, tag):
        label = OBJ.Label()
        label.value = Gtk.Label()

        text = tag.text
        if isinstance(label.value, Gtk.Label):
            label.value.set_text(text)

        for tag in tag.children:
            if isinstance(tag, Tag):
                if tag.name in NAMES.UNIVERSAL:
                    pass
                else:
                    raise GtkmlException("Invalid child!")
        return label

    def _get_button(self, tag):
        button = OBJ.Button()
        button.value = Gtk.Button()

        onclick_str = GLOB.get_attribute(tag, "onclick")

        text = tag.text
        if isinstance(button.value, Gtk.Button):
            button.value.set_label(text)

        if onclick_str is not None:
            button.onclick = globals()[onclick_str]

        for tag in tag.children:
            if isinstance(tag, Tag):
                print(tag.name)
                if tag.name in NAMES.UNIVERSAL:
                    pass
                else:
                    raise GtkmlException("Invalid child!")
        return button

    def _get_entry(self, tag):
        entry = OBJ.Entry()
        entry.value = Gtk.Entry()

        text = tag.text
        if isinstance(entry.value, Gtk.Entry):
            entry.value.set_text(text)

        for tag in tag.children:
            if isinstance(tag, Tag):
                if tag.name in NAMES.UNIVERSAL:
                    pass
                else:
                    raise GtkmlException("Invalid child!")
        return entry

    def _get_appmenu(self, tag):
        appmenu = OBJ.AppMenu()
        menubar_gtk = Gtk.MenuBar()

        appmenu.value = menubar_gtk

        if isinstance(menubar_gtk, Gtk.MenuBar):
            print("ASD")
            for item in tag.children:
                obj = self.get_object(item)
                name = item.name
                if name == "submenu":
                    appmenu.value.append(obj.value)
        return appmenu

    def _get_submenu(self, tag):
        submenu = OBJ.AppSubMenu()
        menuitem_gtk = Gtk.MenuItem(GLOB.get_attribute(tag, "title"))
        menu = Gtk.Menu()
        has_child = False

        if isinstance(menuitem_gtk, Gtk.MenuItem):
            for menuitem in tag.children:
                has_child = True
                obj = self.get_object(menuitem)
                if menuitem.name == "menu-item":
                    menu.add(obj.value)

        if has_child:
            menuitem_gtk.set_submenu(menu)
        submenu.value = menuitem_gtk

        return submenu

    def _get_menu_item(self, tag):
        menuitem = OBJ.AppMenuItem()
        menuitem_gtk = Gtk.MenuItem(GLOB.get_attribute(tag, "title"))
        menuitem.value = menuitem_gtk
        return menuitem

