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

from pluginsmanager.model.preset import Preset


class Lv2Preset(Preset):
    """
    Representation of a Lv2 Preset.

    For general input use, see :class:`.Preset` class documentation.

    :param Lv2Effect effect: Effect that contains the Presety
    :param str symbol: symbol for the effect

    .. _Preset: http://lv2plug.in/ns/ext/Preset#
    """

    def __init__(self, effect, label, uri):
        super(Lv2Preset, self).__init__(effect, label, uri)

    @property
    def __dict__(self):
        dictionary = super(Lv2Preset, self).__dict__
        return dictionary
