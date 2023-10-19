# This file is part of imagecraft.
#
# Copyright 2023 Canonical Ltd.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 3, as published
# by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranties of MERCHANTABILITY,
# SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

from typing import TYPE_CHECKING, List, Optional, cast
from pydantic import conlist
from craft_parts import plugins

from imagecraft.ubuntu_image import generate_ubuntu_image_calls_rootfs
from imagecraft.utils import craft_base_to_ubuntu_series

# A workaround for mypy false positives
# see https://github.com/samuelcolvin/pydantic/issues/975#issuecomment-551147305
# fmt: off
if TYPE_CHECKING:
    UniqueStrList = List[str]
else:
    UniqueStrList = conlist(str, unique_items=True, min_items=1)


class GerminatePluginProperties(plugins.PluginProperties):
    germinate_sources: UniqueStrList
    germinate_source_branch: Optional[str]
    germinate_seeds: UniqueStrList
    germinate_components: UniqueStrList
    germinate_pocket: Optional[str] = "updates"

    @classmethod
    def unmarshal(cls, data):
        plugin_data = plugins.base.extract_plugin_properties(
            data, plugin_name="germinate"
        )
        return cls(**plugin_data)


class GerminatePlugin(plugins.Plugin):
    properties_class = GerminatePluginProperties

    def get_build_snaps(self):
        return ["ubuntu-image"]

    def get_build_packages(self):
        return []

    def get_build_environment(self):
        return {}

    def get_build_commands(self):
        options = cast(GerminatePluginProperties, self._options)

        germinate_arch = self._part_info.target_arch
        germinate_series = craft_base_to_ubuntu_series(
            self._part_info.project_info.base)
        germinate_source_branch = options.germinate_source_branch
        if not germinate_source_branch:
            germinate_source_branch = germinate_series

        return generate_ubuntu_image_calls_rootfs(
            germinate_series,
            germinate_arch,
            options.germinate_sources,
            germinate_source_branch,
            options.germinate_seeds,
            options.germinate_components,
            options.germinate_pocket,
        )