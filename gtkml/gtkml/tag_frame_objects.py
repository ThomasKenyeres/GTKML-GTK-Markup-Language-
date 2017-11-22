import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from gtkml.tools.frame_object_tools import is_layout_widget


#from gi.repository import Gdk, Gtk, Gio

import gtkml.gtkml.object as GO
from gtkml.tools.reference import REF

_ = GO._

class Widget(GO.AbsWidget):
    def __init__(self):
        super()

    def show(self):
        self.value.show_all()

    def hide(self):
        self.value.hide()

class Application(GO.AbsApplication):
    def __init__(self):
        super()

    def run(self):
        for component in self.components:
            if isinstance(component, Window):
                component.show()

class LayoutWidget(GO.AbsLayoutWidget):
    def __init__(self):
        super()

    @property
    def children(self):
        super()
        pass

    @children.setter
    def children(self, val):
        super()
        pass

    def append(self, child):
        super()
        pass



class Window(GO.AbsWindow):
    def __init__(self):
        super()
        #self.__title = None
        self.__header = None
        self.__body = None

    def show(self):
        if not "_AbsWidget__visible" in self.__dict__:
            self.value.show_all()

class Header(GO.AbsHeader):
    def __init__(self):
        super()
        self.__title = ""


class Python(GO.AbsPython):
    def __init__(self):
        super()

class Import(GO.AbsImport):
    def __init__(self):
        super()



#LAYOUT WIDGETS

class VBox(GO.AbsVBox):
    pass

class HBox(GO.AbsHBox):
    pass


#!BODY!
class Body(GO.AbsBody):
    def __init__(self):
        super()





class Grid(GO.AbsGrid):
    def __init__(self):
        super()

class ListBox(GO.AbsListBox):
    pass

class FlowBox(GO.AbsFlowBox):
    pass

class ActionBar(GO.AbsActionBar):
    pass

class Fixed(GO.AbsFixed):
    pass

class Layout(GO.AbsLayout):
    pass




class DisplayWidget(GO.AbsDisplayWidget):
    pass


#DISPLAY WIDGETS

class Label(GO.AbsLabel):
    def __init__(self):
        super()
        self.__text = ""

class Image(GO.AbsImage):
    pass

class Spinner(GO.AbsSpinner):
    pass

class ProgressBar(GO.AbsProgressBar):
    pass




class ButtonWidget(GO.AbsButtonWidget):
    pass



#BUTTONS

class Button(GO.AbsButton):
    pass

class Check(GO.AbsCheck):
    pass

class Radio(GO.AbsRadio):
    pass

class Toggle(GO.AbsToggle):
    pass

class LinkButton(GO.AbsLinkButton):
    pass



class InputWidget(GO.AbsInputWidget):
    pass



#INPUT

class Entry(GO.AbsEntry):
    pass

class SimpleEntry(GO.AbsSimpleEntry):
    pass

class TextEditor(GO.AbsTextEditor):
    pass

class SimpleTextEditor(GO.AbsSimpleTextEditor):
    pass



class TreeView(GO.AbsTreeView):
    pass

class ListView(GO.AbsListView):
    pass


#TREES & LIST

class SimpleTreeView(GO.AbsSimpleTreeView):
    pass

class SimpleListView(GO.AbsSimpleListView):
    def __init__(self):
        super()
        self.__columns = []
        self.__rows = []

    def __iadd__(self, other):
        self.__rows.append(other)
        return self

    @property
    def rows(self):
        return REF(self.__dict__, "_" + str(self.__class__.__name__) + "__rows")


#MENUS
class Menu(GO.AbsMenu):
    pass



class AppMenu(GO.AbsAppmenu):
    def __init__(self):
        pass

class AppSubMenu(GO.AbsAppSubmenu):
    pass

class AppMenuItem(GO.AbsAppmenuItem):
    pass



##CONTROL########################

class IF(GO.AbsIF):
    pass

class FOR(GO.AbsFOR):
    pass




##MISCELLANOUS & HIGH LEVEL

class Table(GO.AbsTable):
    pass

###################################TESTING########################################

def test1():
    window = Window()
    window.title = "asd"
    print(window.__dict__)
    #window.show()


def test2():
    widget = Widget()
    from gi.repository import Gtk
    widget.value = Gtk.Window()
    print(widget.__dict__)
    widget.show()
    Gtk.main()


if __name__ == '__main__':
    #test1()
    test2()