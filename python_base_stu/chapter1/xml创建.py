'''
Created on 2018年5月3日

@author: zhang
'''
import xml.etree.ElementTree as ET
 
 
new_xml = ET.Element("namelist")
personinfo = ET.SubElement(new_xml,"personinfo",attrib={"enrolled":"yes"})
name = ET.SubElement(personinfo,'name')
name.text = 'Alex'
age = ET.SubElement(personinfo,"age",attrib={"checked":"no"})
sex = ET.SubElement(personinfo,"sex")
sex.text = '33'
personinfo2 = ET.SubElement(new_xml,"personinfo2",attrib={"enrolled":"no"})
name = ET.SubElement(personinfo2,'name')
name.text = 'OldBoy'
age = ET.SubElement(personinfo2,"age")
age.text = '19'
 
et = ET.ElementTree(new_xml) #生成文档对象
et.write("xml_创建格式.xml", encoding="utf-8",xml_declaration=True)
 
ET.dump(new_xml) #打印生成的格式