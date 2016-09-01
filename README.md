Role Name
=========

This is an Ansible role to install ExifTool (http://www.sno.phy.queensu.ca/~phil/exiftool/)

Requirements
------------

Ansible 2.x

Role Variables
--------------

|Variable|Description|Default|
|---|---|---|
|```exiftool_version```||10.25|
|```exiftool_verify_checksum```||true|

Dependencies
------------

None.

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: tlehoux.exiftool }

License
-------

BSD

Author Information
------------------

Thomas Lehoux
