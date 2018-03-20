# -*- coding: utf-8 -*-

import postgresql
import xml.etree.ElementTree as ET
import addFiles

from os.path import isfile

if isfile('listGroup.xml') != True:#создаем файл с группами и определяем какие будут участвовать в отчете
    addFiles.addFiles()

if isfile('listObjects.xml') != True:#создаем файл с объектами которые принадлежат соответствующим группам
    addFiles.initListObjects()