import gtkml.gtkml.abstractions as abstr
import gtkml.runtime.runtime_variables as VAR
from gtkml.tools.reference import REF

import gtkml.gtkml.stdlib.gtk_query as Q
_ = Q._

class GtkmlObject:
    pass

class AbsWidget(GtkmlObject, abstr.Sizeable, abstr.SelfSizeable):
    def __init__(self):
        abstr.Sizeable.__init__(self)
        abstr.SelfSizeable.__init__(self)
        self.__value = None
        self.__visible = True

    def destroy(self):
        pass

    @property
    def value(self):
        return REF(self.__dict__, "_AbsWidget__value")

    @value.setter
    def value(self, val):
        self.__value = val

    @property
    def visible(self):
        return REF(self.__dict__, "_AbsWidget__visible")

    def show(self):
        self.__visible = True

    def hide(self):
        self.__visible = False

class AbsApplication(GtkmlObject):
    def __init__(self, name):
        super()
        self.__name = name
        self.__components = []

    @property
    def name(self):
        return REF(self.__dict__, "_AbsApplication__name")

    @name.setter
    def name(self, val):
        self.__name = val

    @property
    def components(self):
        return REF(self.__dict__, "_AbsApplication__components")

    @components.setter
    def components(self, val):
        self.__components = val

    def add_component(self, comp):
        self.__components.append(comp)

    def run(self):
        pass

    def exit(self):
        pass

class AbsLayoutWidget(AbsWidget):
    def __init__(self):
        super()
        self.__content = []

    @property
    def children(self):
        return REF(self.__dict__, "_AbsLayoutWidget__content")

    @children.setter
    def children(self, val):
        self.__content = val

    def append(self, child):
        self.__content.append(child)

class AbsWindow(AbsWidget):
    def __init__(self):
        super()
        self.__header = None
        self.__body = None
        self.__title = None
        self.__menu = None

    @property
    def title(self):
        return REF(self.__dict__, "_AbsWindow__title")

    @title.setter
    def title(self, val):
        self.__title = val

    @property
    def menu(self):
        return REF(self.__dict__, "_AbsWindow__menu")

    @menu.setter
    def menu(self, val):
        self.__menu = val

    @property
    def body(self):
        return REF(self.__dict__, "_AbsWindow__body")

    @body.setter
    def body(self, val):
        self.__body = val


class AbsHeader(AbsLayoutWidget):
    def __init__(self):
        super()
        self.__title = ""


class AbsPython(GtkmlObject):
    def __init__(self):
        super()
        self.__src = None
        self.__pysrc = ""

    def get_src(self):
        return self.__src

    src = property(get_src)

    @src.setter
    def src(self, val):
        self.__src = val

    def execute(self):
        exec(self.__pysrc)

    def load(self):
        homedir = VAR.START_DIR
        python_src = ""
        with open(str(homedir) + "/" + str(self.__src)) as pyfile:
            for line in pyfile:
                python_src += line
        self.__pysrc = python_src


class AbsImport(GtkmlObject):
    def __init__(self):
        super()
        self.__from = None
        self.__import = None

    def execute(self):
        #TODO: Handle both python and GTKML imports!!!
        pass

#LAYOUT WIDGETS

#BOX
class AbsBox(AbsLayoutWidget):
    def __init__(self):
        super()


class AbsVBox(AbsBox):
    pass

class AbsHBox(AbsBox):
    pass

#!BODY!
class AbsBody(AbsHBox):
    def __init__(self):
        super()



class AbsGrid(AbsLayoutWidget):
    def __init__(self):
        super()

class AbsListBox(AbsLayoutWidget):
    pass

class AbsFlowBox(AbsLayoutWidget):
    pass

class AbsActionBar(AbsLayoutWidget):
    pass

class AbsFixed(AbsLayoutWidget):
    pass

class AbsLayout(AbsLayoutWidget):
    pass





class AbsDisplayWidget(AbsWidget):
    pass


#DISPLAY WIDGETS

class AbsLabel(AbsDisplayWidget, abstr.TextedWidget):
    def __init__(self):
        pass

class AbsImage(AbsDisplayWidget):
    pass

class AbsSpinner(AbsDisplayWidget):
    pass

class AbsProgressBar(AbsDisplayWidget):
    pass




class AbsButtonWidget(AbsWidget, abstr.TextedWidget):
    def __init__(self):
        super()
        self.__onclick = None

    @property
    def onclick(self):
        return REF(self.__dict__, "_AbsButtonWidget__onclick")

    @onclick.setter
    def onclick(self, val):
        self.__onclick = val


#BUTTONS

class AbsButton(AbsButtonWidget):
    def __init__(self):
        super()

class AbsCheck(AbsButtonWidget):
    def __init__(self):
        self.__checked = False

class AbsRadio(AbsButtonWidget):
    def __init__(self):
        self.__checked = False
        self.__group = None

class AbsToggle(AbsButtonWidget):
    def __init__(self):
        self.__pressed = None

class AbsLinkButton(AbsButtonWidget):
    pass




class AbsInputWidget(AbsWidget, abstr.TextedWidget):
    def __init__(self):
        super()


#INPUT

#abs
class AbsEntry(AbsInputWidget):
    pass


class AbsSimpleEntry(AbsEntry):
    pass

#abs
class AbsTextEditor(AbsInputWidget):
    pass

class AbsSimpleTextEditor(AbsTextEditor):
    pass



class AbsTreeView(AbsWidget):
    pass

class AbsListView(AbsWidget):
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


#TREES & LIST

class AbsSimpleTreeView(AbsTreeView):
    pass

class AbsSimpleListView(AbsListView):
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
class AbsMenu(AbsWidget):
    def __init__(self):
        pass


class AbsAppmenu(AbsWidget):
    pass

class AbsAppSubmenu(AbsWidget):
    pass

class AbsAppmenuItem(AbsWidget):
    pass


#################
##CONTROL

class AbsControlNode:
    def __init__(self):
        self.__condition = None

    @property
    def condition(self):
        return REF(self.__dict__, "_AbsControlNode__condition")

    @condition.setter
    def condition(self, val):
        self.__condition = val

    def operate(self):
        pass

class AbsIF(AbsControlNode):
    pass

class AbsFOR(AbsControlNode):
    pass




##MISCELLANOUS & HIGH LEVEL

class AbsTable(AbsWidget):
    def __init__(self):
        self.__head = []
        self.__body = []
