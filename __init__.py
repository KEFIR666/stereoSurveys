# -*- coding: utf-8 -*-
"""
/***************************************************************************
 stereoSurveys
                                 A QGIS plugin
 Streetview stereo surveys
                             -------------------
        begin                : 2015-05-25
        copyright            : (C) 2015 by Enrico Ferreguti
        email                : enricofer@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load stereoSurveys class from file stereoSurveys.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .stereoSurveysModule import stereoSurveys
    return stereoSurveys(iface)
