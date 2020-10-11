# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GravityTools
                                 A QGIS plugin
 This plugin processes gravity data and calculates topo reductions
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-10-07
        copyright            : (C) 2020 by Stavros Kampourakis
        email                : stavkamp@outlook.com
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
    """Load GravityTools class from file GravityTools.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .grav_tools import GravityTools
    return GravityTools(iface)
