""" The module """

import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """ Convert dict to xml """

    root = ET.Element('root')
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    data = ET.tostring(root)
    with open(filename, 'wb') as xml_file:
        xml_file.write(data)


def deserialize_from_xml(filename):
    """ Convert xml to dict """

    tree = ET.parse(filename)
    root = tree.getroot()
    data = {}
    for el in root:
        data[el.tag] = el.text
    return data