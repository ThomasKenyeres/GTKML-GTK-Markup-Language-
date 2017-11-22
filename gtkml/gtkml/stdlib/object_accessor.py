from gtkml.exception.gtmkl_exception import GtkmlException
from gtkml.runtime.object_pool import OBJECT_POOL
from gtkml.tools.reference import REF


class ObjectAccessor:
    def __init__(self):
        pass

    def get_object(self, selector):
        if isinstance(selector, str):
            if len(selector) > 1:
                first = selector[0]
                if first == "#":
                    return self.__get_by_id(int(selector[1::]))
            else:
                raise GtkmlException("Invalid selector")

    def __get_by_id(self, id):
        pass

    def __get_by_class(self, class_):
        pass

    def __get_by_tag(self, tag_name):
        pass

    def _get_all(self):
        #print(OBJECT_POOL.__dict__)
        return OBJECT_POOL.pool