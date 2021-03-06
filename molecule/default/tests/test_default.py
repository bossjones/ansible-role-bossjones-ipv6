import os
# import re

import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


@pytest.mark.parametrize('f',
                         ['net.ipv6.conf.all.disable_ipv6',
                          'net.ipv6.conf.default.disable_ipv6',
                          'net.ipv6.conf.lo.disable_ipv6'])
def test_systcl_settings(host, f):

    cmd = 'sysctl -n {}'.format(f)
    out = host.command.check_output(cmd)

    assert '1' == out

    # assert 3 == len(re.findall(r'member [\d\w]+ is healthy', out))
    # assert 'cluster is healthy' in out

    # - net.ipv6.conf.all.disable_ipv6
    # - net.ipv6.conf.default.disable_ipv6
    # - net.ipv6.conf.lo.disable_ipv6

# def test_consul_is_installed(File):
#     consul = File("/usr/local/bin/consul")
#     assert consul.exists
#     assert not consul.is_directory


# def test_consul_is_running(Service):
#     consul = Service('consul')

#     assert consul.is_running
#     assert consul.is_enabled


# @pytest.mark.parametrize('f',
#                          ['/usr/local/sbin/etcd', '/usr/local/sbin/etcdctl'])
# def test_etcd_installed(host, f):
#     file = host.file(f)

#     assert file.exists


# def test_cluster_configured(host):
#     address = host.interface('eth0').addresses[0]
#     endpoint = 'http://{}:2379'.format(address)
#     cmd = 'etcdctl --endpoints {} cluster-health'.format(endpoint)
#     out = host.command.check_output(cmd)

#     assert 3 == len(re.findall(r'member [\d\w]+ is healthy', out))
#     assert 'cluster is healthy' in out
