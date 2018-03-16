from os.path import isfile

import xml.etree.ElementTree as ET
import postgresql

# Проверяем наличие файлов, при отсутствии создаем их

if isfile('delObjects.xml') != True:    # объекты не участвующие в отчетах
    listObjects = ET.Element('listObjects')
    listItems = ET.SubElement(listObjects, 'listItems')

    myList = ET.tostring(listObjects)
    file = open('delObjects.xml', 'w', encoding="utf-8")
    file.write('<?xml version="1.0" encoding="utf-8" standalone="no" ?>\n')
    file.write(str(myList))
    file.close()

if isfile('listGroup.xml') != True: #Управление группами
    db = postgresql.open('pq://root:root@localhost:5432/mgs')
    query = db.query('SELECT objectgroup.group_number, objectgroup.name FROM objectgroup')

    listGroup = ET.Element('listGroup')

    for s in query:
        groupItems = ET.SubElement(listGroup,'groupItems')
        groupItems.set('ID',str(s[0]))
        var = ET.SubElement(groupItems, 'var')
        var.set('name', str(s[0]))
        var.text = str(s[0])
        var = ET.SubElement(groupItems, 'var')
        var.set('name', str(s[1]))
        var.text = str(s[1])
        var = ET.SubElement(groupItems, 'var')
        var.set('name', 'Enabled')
        var.text = 'False'

    myGroup = ET.tostring(listGroup).decode('utf-8')

    file = open('listGroup.xml', 'w', encoding='utf-8')
    file.write('<?xml version="1.0" encoding="utf-8" standalone="no" ?>\n')
    file.write(myGroup)
    file.close()