import gtkml.gtkml.abstractions as abstr
from gtkml.tools.reference import REF


class GtkmlObject:
    pass

class AbsWidget(GtkmlObject, abstr.Sizeable, abstr.SelfSizeable):
    def __init__(self):
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

    def append(self, child):
        pass

class AbsWindow(AbsWidget):
    def __init__(self):
        super()
        self.__header = None
        self.__body = None
        self.__title

    @property
    def title(self):
        return REF(self.__dict__, "_AbsWindow__title")

    @title.setter
    def title(self, val):
        self.__title = val


class AbsHeader(AbsLayoutWidget):
    def __init__(self):
        super()
        self.__title = ""

class AbsBody(AbsLayoutWidget):
    def __init__(self):
        super()



class AbsPython(GtkmlObject):
    def __init__(self):
        super()
        self.__src = None

    def execute(self):
        pass

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
