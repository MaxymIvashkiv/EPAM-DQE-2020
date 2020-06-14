import xml.etree.ElementTree as ET

mytree = ET.parse('mondial-3.0.xml')

myroot = mytree.getroot()

gov = list()

for i in myroot.findall('country'):
    # вибираю лише теги country з розпарсеного xml
    # у тезі country перевіряю чи є пробіл у значенні атрибуту name
    # якщо так вибираю значення атрибуту government і додаю в список
    if ' ' in i.attrib['name'].strip():
        gov.append(i.attrib['government'].strip())

# переводжу список в множину щоб вибрати лише унікальні значення
print('Кількість типів уряду: ' + str(len(set(gov))))

# виводжу у вигляді списку через кому
print(list(set(gov)))
