# -*- coding: utf-8 -*-
"""
/***************************************************************************
 stereoSurveysDialog
                                 A QGIS plugin
 Streetview visual surveys
                             -------------------
        begin                : 2015-05-25
        git sha              : $Format:%H$
        copyright            : (C) 2015 by Enrico Ferreguti
        email                : enricofer@gmail.com
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

from PyQt4 import QtCore, QtGui
from stereoSurveysModule_dialog_base import Ui_stereoSurveysDialogBase
# create the dialog for zoom to point

class stereoSurveysDialog(QtGui.QDialog, Ui_stereoSurveysDialogBase):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
