from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_ufw(Command):
    assert 'Status: active' in Command('ufw status').stdout
