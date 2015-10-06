#!/usr/bin/python3

import sys
import lxml

from lxml import etree
def main():
    doc = etree.parse('ciudadreal.osm')
    #print(etree.tostring(doc,pretty_print=True ,xml_declaration=True, encoding="utf-8"))
    raiz=doc.getroot()
    ways=raiz.findall("way")
    tipos = ["residential"]
    for way in ways:
        if(not way.find('tag') is None):
            if(way.find('tag').attrib["k"] == "highway"  and way.find('tag').attrib["v"] in tipos):
                for n in way.findall("nd"):
                    print(n.attrib["ref"])



main()
