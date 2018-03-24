from os.path import isfile

import xml.etree.ElementTree as ET
import postgresql

# Проверяем наличие файлов, при отсутствии создаем их
def addFiles():
    if isfile('listGroup.xml') != True: #Управление группами
        db = postgresql.open('pq://root:root@localhost:5432/mgs?client_encoding=utf8')
        query = db.query('SELECT objectgroup.group_number, objectgroup.name FROM objectgroup')

        listGroup = ET.Element('listGroup')
        print("Создание listGroup.xml")
        print("Выберите какие группы будут включены в отчет, нажав - 1 или 0 - для исключения группы из отчета.")
        for s in query:
            groupItems = ET.SubElement(listGroup,'groupItems')
            groupItems.set('ID', str(s[0]))
            var = ET.SubElement(groupItems, 'var')
            var.set('name', str(s[0]))
            var.text = str(s[0])
            var = ET.SubElement(groupItems, 'var')
            var.set('name', str(s[1]))
            var.text = str(s[1])
            var = ET.SubElement(groupItems, 'var')
            var.set('name', 'Enabled')
            print("Включить группу - " + str(s[0]) + " - " + s[1] + "?")
            f = input()
            if f == 0:
                var.text = 'False'
            else:
                if f == 1:
                    var.text = 'True'

        myGroup = ET.tostring(listGroup).decode('utf-8')

        file = open('listGroup.xml', 'w')
        file.write('<?xml version="1.0" encoding="utf-8" standalone="no" ?>\n')
        file.write(myGroup)
        file.close()

def initListObjects():
    if isfile('listGroup.xml') == False:
        print("Невозможно продолжить работу! Отсутствует файл listGroup.xml который необходим для инилиализации объектов.")
        break
    if isfile('listObjects.xml') != True:
        pass