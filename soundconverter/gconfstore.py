#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# SoundConverter - GNOME application for converting between audio formats.
# Copyright 2004 Lars Wirzenius
# Copyright 2005-2012 Gautier Portet
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 3 of the License.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307
# USA

from gi.repository import GConf
from gi.repository import GLib
import json
import os

class GConfStore(object):

    def __init__(self, root, defaults):
        self.config_file = os.path.join(GLib.get_user_config_dir(), "soundconverter.json")
        self.root = root
        self.defaults = defaults
        self.config = self._load()

    def get_with_default(self, key):
        root = self.config[self.root]
        return root.get(key, self.defaults[key])

    def get_int(self, key):
        return self.get_with_default(key)

    def set_int(self, key, value):
        self._save(key, value)

    def get_float(self, key):
        return self.get_with_default(key)

    def set_float(self, key, value):
        self._save(key, value)

    def get_string(self, key):
        return self.get_with_default(key)

    def set_string(self, key, value):
        self._save(key, value)

    def path(self, key):
        assert key in self.defaults, 'missing gconf default:%s' % key
        return '%s/%s' % (self.root, key)
    
    def _load(self):
        config = {}
        if os.path.isfile(self.config_file):
            with open(self.config_file, "r") as f:
                config = json.load(f)
        if not self.root in config:
            config[self.root] = {}
        return config
    
    def _save(self, key, value):
        if not self.root in self.config:
            self.config[root] = {}
        root = self.config[self.root]
        root[key] = value
        self.config[self.root] = root
        with open(self.config_file, "w") as f:
            json.dump(self.config, f)

