# Copyright 2023 Canonical Ltd.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from pathlib import Path

IMAGECRAFT_YAML = """
name: ubuntu-server-amd64
version: "1"
base: ubuntu@22.04
series: jammy
platforms:
  amd64:
    build-for: [amd64]
    build-on: [amd64]
package-repositories:
  - type: apt
    components: [main,restricted]
    url: http://archive.ubuntu.com/ubuntu/
    flavor: ubuntu
    series: jammy
    pocket: proposed
    used-for: build
  - type: apt
    components: [restricted,universe]
    pocket: updates
    used-for: run
parts:
  gadget:
    plugin: gadget
    source: https://github.com/snapcore/pc-gadget.git
    source-branch: classic
  rootfs:
    plugin: ubuntu-bootstrap
    ubuntu-bootstrap-germinate:
      urls:
        - "git://git.launchpad.net/~ubuntu-core-dev/ubuntu-seeds/+git/"
      branch: jammy
      names:
        - server
        - minimal
        - standard
        - cloud-image
    ubuntu-bootstrap-pocket: updates
    ubuntu-bootstrap-extra-snaps: [core20, snapd]
    ubuntu-bootstrap-kernel: linux-generic
    stage:
      - -etc/cloud/cloud.cfg.d/90_dpkg.cfg
"""

IMAGECRAFT_YAML_NO_GADGET = """
name: ubuntu-server-amd64
version: "1"
base: ubuntu@22.04
series: jammy
platforms:
  amd64:
    build-for: [amd64]
    build-on: [amd64]
package-repositories:
  - type: apt
    components: [main,restricted]
    url: http://archive.ubuntu.com/ubuntu/
    flavor: ubuntu
    series: jammy
    pocket: proposed
    used-for: build
parts:
  rootfs:
    plugin: ubuntu-bootstrap
    ubuntu-bootstrap-germinate:
      names:
        - server
        - minimal
        - standard
        - cloud-image
      urls:
        - "git://git.launchpad.net/~ubuntu-core-dev/ubuntu-seeds/+git/"
      branch: jammy
    ubuntu-bootstrap-pocket: updates
    ubuntu-bootstrap-extra-snaps: [core20, snapd]
    ubuntu-bootstrap-kernel: linux-generic
"""


def test_application(new_dir, default_application):
    project_file = Path(new_dir) / "imagecraft.yaml"
    project_file.write_text(IMAGECRAFT_YAML)

    project = default_application.project

    assert (
        project.parts["gadget"].get("source")
        == "https://github.com/snapcore/pc-gadget.git"
    )
    assert project.base == "ubuntu@22.04"


def test_application_no_gadget(new_dir, default_application):
    project_file = Path(new_dir) / "imagecraft.yaml"
    project_file.write_text(IMAGECRAFT_YAML_NO_GADGET)

    project = default_application.project

    assert (
        project.parts["rootfs"].get("ubuntu-bootstrap-germinate").get("branch")
        == "jammy"
    )
