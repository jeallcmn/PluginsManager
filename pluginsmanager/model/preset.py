# Copyright 2017 SrMouraSilva
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from abc import ABCMeta, abstractmethod

from unittest.mock import MagicMock


class PresetError(Exception):

    def __init__(self, message):
        super(PresetError, self).__init__(message)
        self.message = message


class Preset(metaclass=ABCMeta):
    """
    :class:`.Patch` represents an Audio Plugin Patch::

    :param Effect effect: Effect in which this parameter belongs
    """

    def __init__(self, effect, label, uri):
        self._uri = uri
        self._label = label
        self._effect = effect

    @property
    def label(self):
        return self._label

    @property
    def effect(self):
        """
        :return: Effect in which this parameter belongs
        """
        return self._effect
    
    @property
    def uri(self):
        """
        Parameter uri

        :getter: Current uri
        :setter: Set the current uri
        """
        return self._uri
    
    def __repr__(self, *args, **kwargs):
        return "<{} object as uri={}, value={} at 0x{:x}>".format(
            self.__class__.__name__,
            self._uri,
            self._label,
            id(self)
        )

    @property
    def __dict__(self):
        return {
            'label': self._label,
            'uri': self._uri
        }
