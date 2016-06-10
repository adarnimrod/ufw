UFW
###

Install UFW, set default policy and allow but limit ssh traffic.

Requirements
------------

- `Ansible 2.0 or later <https://www.ansible.com/>`_.
- `Debian Jessie <http://www.debian.org/>`_ (other versions and Debian based
  distros should work but aren't tested).

Role Variables
--------------

.. code:: yaml

    ufw_policy: reject # Default policy, check ufw module for options.

Dependencies
------------

See :code:`meta/main.yml`.

Example Playbook
----------------

See :code:`tests/playbook.yml`.

Testing
-------

To install the dependencies:

.. code:: shell

    ansible-galaxy install git+file://$(pwd),$(git rev-parse --abbrev-ref HEAD)

To run the full test suite:

.. code:: shell

    molecule test

License
-------

This software is licensed under the MIT license (see the :code:`LICENSE.txt`
file).

Author Information
------------------

Nimrod Adar, `contact me <nimrod@shore.co.il>`_ or visit my `website
<https://www.shore.co.il/>`_. Patches are welcome via `git send-email
<http://git-scm.com/book/en/v2/Git-Commands-Email>`_. The repository is located
at: https://www.shore.co.il/git/.
