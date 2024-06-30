from illyriad.xml_parser import XMLParser

def main():
    with open('../resources/sample_notification.xml', 'r') as input_xml:
        xmlParser = XMLParser()
        print(xmlParser.parse_notifications(input_xml.read()))

if __name__ == '__main__':
    main()