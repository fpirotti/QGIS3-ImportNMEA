# -*- coding: utf-8 -*-

"""
/***************************************************************************
 ImportNMEA
                                 A QGIS plugin
 Lets you read NMEA ASCII files and import points and attributes
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2021-07-17
        copyright            : (C) 2021 by Francesco Pirotti University of Padova
        email                : francesco.pirotti@unipd.it
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

__author__ = 'Francesco Pirotti University of Padova'
__date__ = '2021-07-17'
__copyright__ = '(C) 2021 by Francesco Pirotti University of Padova'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

import os
import sys
import inspect


from qgis.PyQt.QtWidgets import QAction
from qgis.PyQt.QtGui import QIcon
 

from qgis.core import QgsProcessingAlgorithm, QgsApplication
import processing
from .import_nmea_provider import ImportNMEAProvider

cmd_folder = os.path.split(inspect.getfile(inspect.currentframe()))[0]

if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)


class ImportNMEAPlugin(object):

    def __init__(self, iface):
        self.provider = None
        self.iface = iface

    def initProcessing(self):
        """Init Processing provider for QGIS >= 3.8."""
        self.provider = ImportNMEAProvider()
        QgsApplication.processingRegistry().addProvider(self.provider)

    def initGui(self):
        self.initProcessing()
        icon = os.path.join(os.path.join(cmd_folder, 'logo.png'))
        self.action = QAction(
          QIcon(icon),
          u"Import NMEA files", self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addPluginToMenu(u"&ImportNMEA", self.action)
        self.iface.addToolBarIcon(self.action)



    def unload(self):  
        if self.provider is not None:
            QgsApplication.processingRegistry().removeProvider(self.provider)

        self.iface.removePluginMenu(u"&ImportNMEA", self.action)
        self.iface.removeToolBarIcon(self.action)
        #Spass

    def run(self):
        processing.execAlgorithmDialog("ImportNMEA:Import NMEA")
 