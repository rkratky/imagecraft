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

from craft_cli import emit

from imagecraft.lifecycle import ImagecraftLifecycle

from .common import ImagecraftCommand

class CleanCommand(ImagecraftCommand):
    """Prime parts of the image build."""

    name = "clean"
    help_msg = "Clean parts of the image build."
    overview = "TBD"
    execute_step = "clean"

    def run(self, args):
        """Run the command."""
        emit.debug("Running clean command")
        lifecycle = ImagecraftLifecycle(args)
        lifecycle.clean()
        # TBD
