# -*- coding: utf-8 -*-
#
#    Gedit Custom Indentation
#    Copyright (C) 2011  Leandro Vaz
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import gtk
import gedit
import settings
import utils


class GciPluginHelper(object):

    def __init__(self, window):
        self._window = window
        self._window.connect('tab-added', self.on_tab_added)

    def activate(self):
        utils.apply_settings_to_documents(window)

    def on_tab_added(self, window, tab):
        doc = tab.get_document()
        doc.connect('loaded', self.on_document_loaded)

    def on_document_loaded(self, doc, error):
        utils.apply_settings_to_document(doc)
