# -*- coding: utf-8 -*-
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from mmd_uuunyaa_tools import auto_load

bl_info = {
    "name": "mmd_uuunyaa_tools",
    "author": "UuuNyaa",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
    "description": "Utility tools for MMD model & scene editing by Uuu(/>ω<)/Nyaa!.",
    "location": "View3D > Tool Shelf > MMD Tools Panel",
    "warning": "",
    "category": "Generic"
}

auto_load.init()

def register():
    auto_load.register()

def unregister():
    auto_load.unregister()
