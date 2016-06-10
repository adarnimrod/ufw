def test_ufw(Command):
    assert 'Status: active' in Command('ufw status').stdout
