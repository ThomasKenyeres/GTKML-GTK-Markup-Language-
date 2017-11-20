import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

BUILTIN_NAMES = {
    "application": "",
    "window": "",
    "title": "",
    "body": "",
    "python": "",

    "box": "",
    "grid": "",
    "listbox": "",
    "flowbox": "",
    "actionbar": "",
    "header": "",
    "fixed": "",
    "layout": "",

    "label": "",
    "img": "",
    "spinner": "",
    "progressbar": "",

    "button": "",
    "check": "",
    "radio": "",
    "toggle": "",
    "linkbutton": "",

    "entry": "",

    "textview": "",
    "editor": "",

    "listview": "",

    #SPECIAL
    "table": "",
    "th": "",
    "tr": "",
    "td": "",
}

USER_NAMES = {}

UNIVERSAL = {
    "python": "",
    "import": "",
    "meta": ""
}

APPLICATION_CHILDREN = {
    "window": "",
}; [APPLICATION_CHILDREN.update(d) for d in [UNIVERSAL]]

WINDOW_CHILDREN = {
    "header": "",
    "appmenu": "",
    "body": ""
}; [WINDOW_CHILDREN.update(d) for d in [UNIVERSAL]]

HEADER_CHILDREN = {

}

LAYOUT_WIDGETS = {
    "vbox": Gtk.VBox,
    "hbox": Gtk.HBox,
    "grid": Gtk.Grid
}

WIDGETS = {
    "label": Gtk.Label,
    "entry": Gtk.Entry,
    "button": Gtk.Button
    #"appmenu": Gtk.MenuBar
}; [WIDGETS.update(d) for d in [LAYOUT_WIDGETS]]

