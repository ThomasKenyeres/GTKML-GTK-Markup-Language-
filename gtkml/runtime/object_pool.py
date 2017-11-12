class ObjectPool:
    def __init__(self):
        self.pool = {}

    def set_object(self, id, obj, classes):
        self.pool[id] = {"obj": obj, "class": classes}

    def null_object(self, id):
        self.pool[id] = None

    def __getitem__(self, id):
        return self.pool[id]["obj"]

    def classes_of(self, id):
        return self.pool[id]["class"]