from __future__ import print_function
import xml.etree.ElementTree as ET
import sys

tree = ET.parse('ucd.all.flat.xml')
root = tree.getroot()

for element in root.iter():
    if element.tag.endswith('char'):
        try:
            char = unichr(int(element.get('cp'), base=16))
        except TypeError:
            sys.stderr.write('kaputt: {}\n'.format(str(element)))
            continue
        na = element.get('na')
        if na.startswith('CJK UNIFIED IDEOGRAPH'):
            continue
        print(u'{}  {}'.format(char, na).encode('utf-8'))
