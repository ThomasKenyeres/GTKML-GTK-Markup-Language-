import xml.etree.ElementTree as ET

class Tag:
    def __init__(self, name, attributes={}, content=[], encoding="utf-8", text=None):
        self.name = name
        self.attributes = attributes
        self.children = content
        self.encoding = encoding
        self.text = text

    def get_gtkml(self):
        elem = ET.Element(self.name)
        for attr in self.attributes:
            elem.attrib[attr] = self.attributes[attr]
        for child in self.children:
            xml = child.get_gtkml()
            elem.append(ET.fromstring(xml))
        if self.text is not None:
            elem.text = self.text
        xmltostr = ET.tostring(elem, encoding=self.encoding, method="xml")
        return xmltostr.decode(self.encoding)

    def parse(self, xml):
        element = ET.fromstring(xml)

        self.name = element.tag
        self.attributes = element.attrib

        self.children = []
        for child in element:
            cur_xml = ET.tostring(child).decode(self.encoding)
            text = str(child.text)
            child_name = child.tag
            child_attributes = child.attrib
            tag = Tag(child_name, child.attrib)
            tag.parse(cur_xml)
            self.children.append(tag)
            if text is not None:
                tag.text = text

    def __str__(self):
        return "<'" + str(self.name) + "' tag object: " + ">"


if __name__ == '__main__':
    win = Tag("window", {"show": "True"})
    tag1 = Tag("application", {"id": "app1"}, [win])
    print(tag1.get_gtkml())
    print("------------------")
    tag1.parse("<kaka attr1=\"3\"><asd at=\"k\"><e u=\"yu\" e=\"ee\">kiki</e></asd></kaka>")
    print(tag1.get_gtkml())
    print("------------------")
