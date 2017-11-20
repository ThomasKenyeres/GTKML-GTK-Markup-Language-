from gtkml.gtkml.static.names import BUILTIN_NAMES, USER_NAMES
from gtkml.gtkml.tag import Tag
from gtkml.runtime.execute.assembler import ObjectAssembler
#from gtkml.runtime.runtime import RUNTIME
from gtkml.runtime.object_pool import OBJECT_POOL

from gtkml.runtime.execute.assembler import VAR


class ObjectBuilder:
    def __init__(self):
        self.assembler = ObjectAssembler()

    def _get(self, tag):
        obj = self.assembler.get_object(tag)
        if hasattr(tag, "id"):
            OBJECT_POOL.set_object(id, obj, [])
        return obj

    def build(self, tag):
        name = tag.name
        if name in BUILTIN_NAMES or name in USER_NAMES:
            return self._get(tag)
        print(str(name))
        return None
