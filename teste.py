#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#-*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import xml.etree.cElementTree as ET

html = requests.get("http://www.perverted-justice.com/?con=full")

soup = BeautifulSoup(html.text, "html.parser")
div_main = soup("div", {"id":"mainbox"})[0]

for li in div_main("a", {"id":"pedoLink"}):
    pedoopen = li["href"]
    
    original = pedoopen
    pedoopen1 = original.replace(".", "")
    novaUrl = "http://www.perverted-justice.com" + pedoopen1
    html2 = requests.get(novaUrl)
    
    soup2 = BeautifulSoup(html2.text, "html.parser")
    div_main2 = soup2("div", {"class":"chatLog"})

    root = ET.Element("root")
    doc = ET.SubElement(root, "doc")

    ET.SubElement(doc, "field1", name="blah").text = "some value1"
    ET.SubElement(doc, "field2", name="asdfasd").text = "some vlaue2"

    tree = ET.ElementTree(root)
tree.write("Hacka.xml")            
 



