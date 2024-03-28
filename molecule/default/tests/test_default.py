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
    svc = None
    if host.system_info.distribution in ["debian", "kali", "ubuntu"]:
        svc = "chrony"
    elif host.system_info.distribution in ["amzn", "redhat"]:
        svc = "chronyd"
    else:
        # Should never get here
        assert False, f"Unknown distribution {host.system_info.distribution}"

    assert host.service(svc).is_enabled


def check_config(host):
    """Ensure that chrony is configured as expected."""
    filename = None
    if host.system_info.distribution in ["amzn", "debian", "kali", "redhat", "ubuntu"]:
        filename = "/etc/chrony/chrony.conf"
    else:
        # Should never get here
        assert False, f"Unknown distribution {host.system_info.distribution}"

    f = host.file(filename)
    assert f.exists
    assert f.is_file
    assert f.contains("server 169.254.169.123 prefer iburst")
