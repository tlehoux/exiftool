# ExifTool

<https://galaxy.ansible.com/danielhoherd/ansible-role-exiftool/>

This is an Ansible role to install ExifTool (http://www.sno.phy.queensu.ca/~phil/exiftool/)

# Requirements

Ansible 2.x

# Role Variables

|            Variable        | Description | Default |
| -------------------------- | ----------- | ------- |
| `exiftool_version`         |             | 10.25   |
| `exiftool_verify_checksum` |             | true    |

# Dependencies

None.

# Example Playbook

```yml
- hosts: servers
  roles:
    - { role: danielhoherd.ansible-role-exiftool }
```

# Example requirements.yml

```yml
---
- name: exiftool
  scm: git
  src: git@github.com:danielhoherd/ansible-role-exiftool.git
  version: 43f5f894d42cbaf722299a7fb85b57f64181eb69
```

# License

BSD

# Authors

- Thomas Lehoux
- Daniel Hoherd

# Links

- Exiftool homepage: <http://www.sno.phy.queensu.ca/~phil/exiftool/>
- Exiftool release notes: <https://www.sno.phy.queensu.ca/~phil/exiftool/history.html>
