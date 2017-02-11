#       classes_treeview.py
#
#       Copyright 2015 Florian Maerkl <bokken@florianmaerkl.de>
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

import os

from gi.repository import Gtk
from gi.repository import Pango

class ClassesView(Gtk.ScrolledWindow):

	def __init__(self, uicore, textviews):
		super(ClassesView, self).__init__()

		self.uicore = uicore

		self.strings_tree = ClassesTreeView(self.uicore, textviews)
		self.add(self.strings_tree)
		self.show_all()

	# TODO
	def add_content(self):
		strings = self.uicore.get_strings()
		for string in strings:
			if len(string) == 3:
				self.strings_tree.store.append(string)

	def remove_content(self):
		self.strings_tree.store.clear()


class ClassesTreeView(Gtk.TreeView):
	'''Classes TextView elements'''

	def __init__(self, core, textviews):
		self.uicore = core
		self.textviews = textviews

		self.store = Gtk.ListStore(str, str, str)

		self.create_classes_columns()


	def create_classes_columns(self):
		rendererText = Gtk.CellRendererText()
		column = Gtk.TreeViewColumn("Name", rendererText, text=0)
		column.set_sort_column_id(0)
		self.append_column(column)

