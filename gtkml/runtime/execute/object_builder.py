from gtkml.gtkml.static.names import BUILTIN_NAMES, USER_NAMES
from gtkml.gtkml.tag import Tag


class ObjectBuilder:
    def __init__(self):
        pass

    def _get(self, tag):
        pass

    def build(self, tag):
        name = tag.name
        if name in BUILTIN_NAMES or name in USER_NAMES:
            #TODO : see which attributes does it have, the build and set the object with different setter objects
            self._get(tag)
        return tag

if __name__ == '__main__':
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

    tag = Tag("application")
    tag.parse(xml)
    obj = builder.build(tag)
    print(obj)