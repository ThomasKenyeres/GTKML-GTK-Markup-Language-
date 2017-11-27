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

import gtkml.runtime.execute.assemblers.layout_assembler as LAY_ASMBLR
import gtkml.runtime.execute.assemblers.misc_assembler as MISC_ASMBLR
import gtkml.runtime.execute.assemblers.std_widget_assembler as WIDGET_ASMBLR
import gtkml.runtime.execute.assemblers.appmenu_assembler as APPMENU_ASMBLR



class ObjectAssembler:
    def __init__(self):
        self.layout_a = LAY_ASMBLR.LayoutAssembler(self)
        self.misc_a = MISC_ASMBLR.MiscellaneousAssembler(self)
        self.widget_a = WIDGET_ASMBLR.StandardWidgetAssembler(self)
        self.menu_a = APPMENU_ASMBLR.AppMenuAssembler(self)

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
        if name == "grid": return self._get_grid(tag)

        if name == "label": return self._get_label(tag)
        if name == "button": return self._get_button(tag)
        if name == "entry": return self._get_entry(tag)

        if name == "appmenu": return self._get_appmenu(tag)
        if name == "submenu": return self._get_submenu(tag)
        if name == "menu-item": return self._get_menu_item(tag)

    def _get_application(self, tag):
        return self.misc_a.get_application(tag)

    def _get_python(self, tag):
        return self.misc_a.get_python(tag)

    def _get_window(self, tag):
        return self.layout_a.get_window(tag)

    def _get_header(self, tag):
        pass

    def _get_body(self, tag):
        return self.layout_a.get_body(tag)

    def _get_hbox(self, tag):
        return self.layout_a.get_hbox(tag)

    def _get_vbox(self, tag):
        return self.layout_a.get_vbox(tag)

    def _get_grid(self, tag):
        return self.layout_a.get_grid(tag)

    def _get_label(self, tag):
        return self.widget_a.get_label(tag)

    def _get_button(self, tag):
        return self.widget_a.get_button(tag)

    def _get_entry(self, tag):
        return self.widget_a.get_entry(tag)

    def _get_appmenu(self, tag):
        return self.menu_a.get_appmenu(tag)

    def _get_submenu(self, tag):
        return self.menu_a.get_submenu(tag)

    def _get_menu_item(self, tag):
        return self.menu_a.get_menu_item(tag)

