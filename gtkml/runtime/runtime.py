from gtkml.runtime.execute.executor import Executor
from gtkml.runtime.object_pool import ObjectPool
from gtkml.parser.parser import DOMParser

from gtkml.runtime.execute.executor import VAR

class GtkmlRuntime:
    def __init__(self):
        self.object_pool = ObjectPool()
        self.application = None
        #self.assembler = ObjectAssembler()
        self.parser = DOMParser()

    def _parse(self, xml):
        return self.parser.parse(xml)

    def _execute(self, root):
        executor = Executor(root)
        executor.execute()

    def _read(self, path):
        xml = ""
        root = None
        with open(path, "r+") as xmlfile:
            for line in xmlfile.readlines():
                xml += line.strip()
            #print(xml)
            root = self._parse(xml)
            print(root)
        self._execute(root)

    def run(self, start_file):
        if os.path.isfile(start_file):
            directory = os.path.dirname(start_file)
            VAR.START_FILE = start_file
            VAR.START_DIR = directory
            self._read(start_file)



import os
RUNTIME = GtkmlRuntime()


if __name__ == '__main__':
    RUNTIME.run(os.getenv("HOME") + "/Asztal/realgtk1.xml")
    pass