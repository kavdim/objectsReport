# -*- coding: utf-8 -*-

import postgresql
import xml.etree.ElementTree as ET
import addFiles

from os.path import isfile

if isfile('listGroup.xml'):
    pass
else:
    addFiles.addFiles()