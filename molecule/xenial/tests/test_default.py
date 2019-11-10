import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(os.environ["MOLECULE_INVENTORY_FILE"]).get_hosts("all")


def test_exiftool(host):
    exiftool_command = host.file("/usr/local/bin/exiftool")

    assert exiftool_command.is_file
    assert exiftool_command.user == "root"
    assert exiftool_command.group == "root"
    assert exiftool_command.mode == 0o555
