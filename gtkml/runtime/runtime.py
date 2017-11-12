from gtkml.runtime.object_pool import ObjectPool
from gtkml.parser.parser import DOMParser

class GtkmlRuntime:
    parser = DOMParser()

    def __init__(self, start_file):
        self.start_file = start_file
        self.object_pool = ObjectPool()

    @staticmethod
    def _parse(xml):
        return GtkmlRuntime.parser.parse(xml)

    @staticmethod
    def _read(path):
        with open(path, "r+") as xmlfile:
            xml = ""
            for line in xmlfile.readlines():
                xml += line.strip()
            #print(xml)
            root = GtkmlRuntime._parse(xml)
            print(root)


    def run(self):
        self._read(self.start_file)

if __name__ == '__main__':
    import os
    runtime = GtkmlRuntime(os.getenv("HOME") + "/Asztal/gtkmltry.xml")
    runtime.run()