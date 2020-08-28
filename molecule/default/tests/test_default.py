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


def check_chrony_enabled(host):
    """Ensure that chrony is enabled at boot."""
    if (
        host.system_info.distribution == "debian"
        or host.system_info.distribution == "kali"
        or host.system_info.distribution == "ubuntu"
    ):
        assert host.service("chrony").is_enabled
    elif (
        host.system_info.distribution == "redhat"
        or host.system_info.distribution == "amzn"
    ):
        assert host.service("chronyd").is_enabled
    else:
        # Should never get here
        assert False


def check_config(host):
    """Ensure that chrony is configured as expected."""
    f = host.file("/etc/chrony/chrony.conf")
    assert f.exists
    assert f.is_file
    assert f.contains("server 169.254.169.123 prefer iburst")
