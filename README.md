# ExifTool

[![Ansible Role](https://img.shields.io/ansible/role/11829.svg?maxAge=2592000)](https://galaxy.ansible.com/tlehoux/exiftool/)

This is an Ansible role to install ExifTool (http://www.sno.phy.queensu.ca/~phil/exiftool/)

# Requirements

Ansible 2.x

# Role Variables

|            Variable            | Description | Default |
| ------------------------------ | ----------- | ------- |
| ```exiftool_version```         |             | 10.25   |
| ```exiftool_verify_checksum``` |             | true    |

# Dependencies

None.

# Example Playbook

    - hosts: servers
      roles:
         - { role: tlehoux.exiftool }

# License

BSD

# Authors

- Thomas Lehoux
- Daniel Hoherd

# Links

- Exiftool homepage: <http://www.sno.phy.queensu.ca/~phil/exiftool/>
- Exiftool release notes: <https://www.sno.phy.queensu.ca/~phil/exiftool/history.html>
