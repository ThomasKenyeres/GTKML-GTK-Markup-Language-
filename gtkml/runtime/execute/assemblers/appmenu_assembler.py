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

class AppMenuAssembler():
    def __init__(self, assembler):
        self.assembler = assembler

    def get_appmenu(self, tag):
        appmenu = OBJ.AppMenu()
        menubar_gtk = Gtk.MenuBar()

        appmenu.value = menubar_gtk

        tagID = GLOB.get_attribute(tag, "id")

        if isinstance(menubar_gtk, Gtk.MenuBar):
            print("ASD")
            for item in tag.children:
                obj = self.assembler.get_object(item)
                name = item.name
                if name == "submenu":
                    appmenu.value.append(obj.value)
        OBJECT_POOL.set_object(tagID, appmenu, [])
        return appmenu

    def get_submenu(self, tag):
        submenu = OBJ.AppSubMenu()
        menuitem_gtk = Gtk.MenuItem(GLOB.get_attribute(tag, "title"))
        menu = Gtk.Menu()
        has_child = False

        tagID = GLOB.get_attribute(tag, "id")

        if isinstance(menuitem_gtk, Gtk.MenuItem):
            for menuitem in tag.children:
                has_child = True
                obj = self.assembler.get_object(menuitem)
                if menuitem.name == "menu-item":
                    menu.add(obj.value)

        if has_child:
            menuitem_gtk.set_submenu(menu)
        submenu.value = menuitem_gtk

        OBJECT_POOL.set_object(tagID, submenu, [])
        return submenu

    def get_menu_item(self, tag):
        menuitem = OBJ.AppMenuItem()
        menuitem_gtk = Gtk.MenuItem(GLOB.get_attribute(tag, "title"))
        menuitem.value = menuitem_gtk

        tagID = GLOB.get_attribute(tag, "id")
        OBJECT_POOL.set_object(tagID, menuitem, [])

        return menuitem