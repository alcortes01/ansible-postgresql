import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_postgresql_is_installed(host):
    postgresql = host.package("postgresql-server")
    assert postgresql.is_installed


def test_postgresql_running_and_enabled(host):
    postgresql = host.service("postgresql")
    assert postgresql.is_running
    assert postgresql.is_enabled


def test_port_5432_is_listening(host):
    socket = host.socket("tcp://5432")
    assert(socket.is_listening)
