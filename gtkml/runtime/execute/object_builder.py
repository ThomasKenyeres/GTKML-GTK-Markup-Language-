from gtkml.gtkml.static.names import BUILTIN_NAMES, USER_NAMES
from gtkml.gtkml.tag import Tag
from gtkml.runtime.execute.assembler import ObjectAssembler
#from gtkml.runtime.runtime import RUNTIME


class ObjectBuilder:
    def __init__(self):
        self.assembler = ObjectAssembler()

    def _get(self, tag):
        return self.assembler.get_object(tag)

    def build(self, tag):
        name = tag.name
        if name in BUILTIN_NAMES or name in USER_NAMES:
            return self._get(tag)
        print(str(name))
        return None

#################################TESTS############################x

def test1():
    builder = ObjectBuilder()
    xml = """
        <application><window show="True"><meta></meta><header><python src="display_content.py"></python>
            <style>
                label {
                    font_size: 23;
                }
            </style><title></title></header><body><box><label id="lbl1" style='color: "red"'>Hi wazzup!</label><!-- Equivalent of '<label>Helloo!</label>' -->
            </box>        
        </body>
    </window>
    </application>
        """
    xml = """
        <application>
            <window></window>
        </application>
        """

    tag = Tag("application")
    tag.parse(xml)

    # obj = builder.build(tag)
    # print(obj)

    def tag_is_layout(tag):
        return tag.name in ["window", "header", "body", "box"]

    def iter_sub(tag):
        print(tag)
        obj = builder.build(tag)
        if tag.children is not None and (tag_is_layout(tag) or tag.name == "application"):
            if tag.name == "application":
                RUNTIME.application = builder.build(tag)
            for subtag in tag.children:
                # obj.children.append()
                # obj.append(iter_sub(subtag))
                # print(subtag)
                s_obj = iter_sub(subtag)
                obj.append(s_obj)
                pass
        return obj

    o = iter_sub(tag)
    print("-----------------------")
    print(o)


def test2():
    from gtkml.parser.parser import DOMParser
    from gi.repository import Gtk
    from gtkml.gtkml.tag_frame_objects import Application

    xml = """
    <application>
        <window title='Hi you crazy!' show='True'>
        </window>
        
        <window title='Wazzup dude?' show='True'>
        </window>
    </application>
    """
    builder = ObjectBuilder()
    parser = DOMParser()
    root_obj = builder.build(parser.parse(xml))


    if isinstance(root_obj, Application):
        root_obj.run()
        Gtk.main()





if __name__ == '__main__':
    test2()