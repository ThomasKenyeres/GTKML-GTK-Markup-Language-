from gtkml.exception.gtmkl_exception import UnsetPropertyError
from gtkml.gtkml.enums import Sizes
from gtkml.tools.reference import REF


class TextedWidget:
    def __init__(self):
        self.__text = None

    @property
    def text(self):
        #return REF(self.__dict__, "_" + str(self.__class__.__name__) + "__text")
        return REF(self.__dict__, "_TextedWidget__text")

    @text.setter
    def text(self, val):
        self._on_set_text(val)
        self.__text = val

    def _on_set_text(self, val):
        pass


class LabeledWidget:
    def __init__(self):
        self.__label = None

    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, val):
        self._on_set_label(val)
        self.__label = val

    def _on_set_label(self, val):
        pass


class Checkable:
    def __init__(self):
        self.__checked = False

    @property
    def checked(self):
        return REF(self.__dict__, "_Checkable__checked")

    @checked.setter
    def checked(self, val):
        self._on_set_checked(val)
        self.__checked = bool(val)

    def _on_set_checked(self, val):
        pass


class Sizeable:
    def __init__(self):
        self.__width = 0
        self.__height = 0

    @property
    def width(self):
        try:
            return REF(self.__dict__, "_Sizeable__width")
        except KeyError:
            raise UnsetPropertyError("Set 'width' before accessing it")

    @width.setter
    def width(self, val):
        self._on_set_width(val)
        self.__width = val

    @property
    def height(self):
        try:
            return REF(self.__dict__, "_Sizeable__height")
        except KeyError:
            raise UnsetPropertyError("Set 'height' before accessing it")

    @height.setter
    def height(self, val):
        self._on_set_height(val)
        self.__height = val

    def _on_set_width(self, val):
        pass

    def _on_set_height(self, val):
        pass


class SelfSizeable:
    def __init__(self):
        self.__data = Sizes

    @property
    def data(self):
        return REF(self.__dict__, "_SelfSizeable__data")

    @data.setter
    def data(self, val):
        self._on_set_data(val)
        self.__data = val

    def _on_set_data(self, val):
        pass