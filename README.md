# ansible-role-chrony-aws #

[![GitHub Build Status](https://github.com/cisagov/ansible-role-chrony-aws/workflows/build/badge.svg)](https://github.com/cisagov/ansible-role-chrony-aws/actions)
[![CodeQL](https://github.com/cisagov/ansible-role-chrony-aws/workflows/CodeQL/badge.svg)](https://github.com/cisagov/ansible-role-chrony-aws/actions/workflows/codeql-analysis.yml)

An Ansible role for installing
[chrony](https://en.wikipedia.org/wiki/Chrony) and configuring it to
use [the Amazon Time Sync
Service](https://aws.amazon.com/blogs/aws/keeping-time-with-amazon-time-sync-service/).
Note that the Amazon Time Sync Service is available at the
`169.254.169.123` IP address for any instance running in a VPC, and
therefore does not require internet access or any changes to security
group or network ACL rules.

## Requirements ##

None.

## Role Variables ##

None.

<!--
| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| optional_variable | Describe its purpose. | `default_value` | No |
| required_variable | Describe its purpose. | n/a | Yes |
-->

## Dependencies ##

None.

## Example Playbook ##

Here's how to use it in a playbook:

```yaml
- hosts: all
  become: yes
  become_method: sudo
  tasks:
    - name: Install and configure chrony for AWS
      ansible.builtin.include_role:
        name: chrony_aws
```

## Contributing ##

We welcome contributions!  Please see [`CONTRIBUTING.md`](CONTRIBUTING.md) for
details.

## License ##

This project is in the worldwide [public domain](LICENSE).

This project is in the public domain within the United States, and
copyright and related rights in the work worldwide are waived through
the [CC0 1.0 Universal public domain
dedication](https://creativecommons.org/publicdomain/zero/1.0/).

All contributions to this project will be released under the CC0
dedication. By submitting a pull request, you are agreeing to comply
with this waiver of copyright interest.

## Author Information ##

Shane Frasier - <jeremy.frasier@trio.dhs.gov>
