from gtkml.parser.xml_parser import XMLParser
from gtkml.gtkml.tag import Tag

class DOMParser:
    def __init__(self):
        self.parser = XMLParser()

    def parse(self, xml):
        root = self.parser.parse(xml)
        tag = Tag(root.tag)
        tag.parse(xml)
        return tag

if __name__ == '__main__':
    parser = DOMParser()
    xml = """
        <window>
            <meta>metadatas</meta>
            <header id="header1">
                <title>WINDOW</title>
            </header>
        </window>
    """

    p = parser.parse(xml)
    print(p.get_gtkml())