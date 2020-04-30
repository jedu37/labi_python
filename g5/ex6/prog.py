from lxml import etree

def print_xml(obj):
    for child in obj:
        print(child.tag, child.attrib, child.text)
        if len(child):
            print_xml(child)

def main():
    xml = etree.parse('g5/ex6/conf.xml')
    root = xml.getroot()
    print(root.tag)
    

    print_xml(root)

if __name__ == "__main__":
    main()