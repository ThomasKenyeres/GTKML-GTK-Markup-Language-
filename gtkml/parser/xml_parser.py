import xml.etree.ElementTree as ET

class XMLParser:
    def __init__(self):
        pass

    def parse(self, xml):
        return ET.fromstring(xml)


if __name__ == '__main__':
    parser = XMLParser()

    xml = """
    <window>
        <meta>metadatas</meta>
        <header id="header1"></header>
    </window>
    """

    a = parser.parse(xml)
    print(a)