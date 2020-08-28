"""Module containing the tests for the default scenario."""

# Standard Python Libraries
import os

# Third-Party Libraries
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize("pkg", ["chrony"])
def test_packages(host, pkg):
    """Ensure that all expected packages are installed."""
    assert host.package(pkg).is_installed


@pytest.mark.parametrize("svc", ["chrony"])
def check_services_enabled(host, svc):
    """Ensure that chrony is enabled at boot."""
    assert host.service(svc).is_enabled


def check_config(host):
    """Ensure that chrony is configured as expected."""
    f = host.file("/etc/chrony/chrony.conf")
    assert f.exists
    assert f.is_file
    assert f.contains("server 169.254.169.123 prefer iburst")
