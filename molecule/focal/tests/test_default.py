import os
from pytest import fixture

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(os.environ["MOLECULE_INVENTORY_FILE"]).get_hosts("all")


@fixture
def get_vars(host):
    defaults_files = "file=../../defaults/main.yml name=role_defaults"
    vars_files = "file=../../vars/main.yml name=role_vars"
    ansible_vars = host.ansible("include_vars", defaults_files)["ansible_facts"]["role_defaults"]
    ansible_vars.update(host.ansible("include_vars", vars_files)["ansible_facts"]["role_vars"])
    return ansible_vars


def test_exiftool(host):
    exiftool_command = host.file("/usr/local/bin/exiftool")

    assert exiftool_command.is_file
    assert exiftool_command.user == "root"
    assert exiftool_command.group == "root"
    assert exiftool_command.mode == 0o555


def test_correct_exiftool_version(get_vars, host):
    ver = host.run("exiftool -Ver")
    assert ver.stdout.strip() == get_vars["exiftool_version"]
