from gtkml.tools.reference import REF


class ObjectPool:
    def __init__(self):
        self._pool = {}

    def set_object(self, id, obj, classes):
        self._pool[id] = {"obj": obj, "class": classes}

    def null_object(self, id):
        self._pool[id] = None

    def __getitem__(self, id):
        return self._pool[id]["obj"]

    @property
    def pool(self):
        return REF(self.__dict__, "_ObjectPool__pool")

    def get(self, selector, val):
        if selector is "id":
            return REF(self._pool, val)

    def classes_of(self, id):
        return self._pool[id]["class"]

OBJECT_POOL = ObjectPool()