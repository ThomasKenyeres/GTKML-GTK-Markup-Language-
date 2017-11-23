import sys

from gtkml.runtime.runtime import RUNTIME

def cli():
    pass

def run(start_file):
    RUNTIME.run(start_file)

def build(start_file, build_path):
    pass

def help():
    print("HELP PAGE")

def main(cmds = sys.argv[1::]):
    print(cmds)
    length = len(cmds)
    if length == 0:
        help()
    elif length == 1:
        run(cmds[0])

if __name__ == '__main__':
    def simulate():
        main(["/home/thomas/Asztal/gtkml_examples/realgtk1.xml"])

    #simulate()
    main()
