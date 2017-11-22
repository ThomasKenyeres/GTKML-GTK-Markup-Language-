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
        return REF(self.__dict__, "_pool")

    def get(self, selector, val):
        if selector is "id":
            return REF(REF(self._pool, val), "obj")

    def classes_of(self, id):
        return self._pool[id]["class"]

OBJECT_POOL = ObjectPool()

#TESTS
if __name__ == '__main__':
    from gtkml.gtkml.tag_frame_objects import Window
    OBJECT_POOL.set_object("window1", Window(), ["cls1", "cls2"])
    a = OBJECT_POOL.get("id", "window1")
    print(a)