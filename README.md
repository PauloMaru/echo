# Echo Service

This document outlines the task of building and deploying a simple TCP-based
echo service ([RFC 862](https://tools.ietf.org/html/rfc862)) as part of the
[Protohackers "Smoke Test" challenge](https://protohackers.com/problem/0).
It specifies key requirements and constraints, with the goal of leading you
to use modern DevOps environments and tools (including AWS, GitHub, Ansible)
to setup and manage the application.
You're expected to have basic familiarity with Linux and core IT concepts.

The scope of this tutorial includes:

- Application implementation: Build a TCP-based echo service as specified in RFC 862.
- Infrastructure provisioning: Provision a minimal EC2 instance and
  necessary resources via CloudFormation.
- Configuration and deployment: Automate setup and deployment of the
  service using Ansible.
- Version control: Manage application code and infrastructure
  configuration using Git.

## System Requirements Specification

### Functional Requirements

- The functional requirements are met once the application passes the
  Protohackers "Smoke Test" challenge. Your application should implement the
  Echo Protocol (RFC 862), but the choice of programming language and tools
  is entirely up to you.

### Non-Functional Requirements

- The application code and system configuration must be hosted in a GitHub repository.
- The TCP service must support configuration of the listening port without code changes.
- The EC2 instance must be provisioned using AWS CloudFormation.
- Instance configuration must be automated with Ansible, including package
  installation, user setup, and system-level configuration.
- The echo service must be deployed using Ansible.
- The echo service must be managed by the system's execution environment,
  ensuring it starts on boot.

### Constraints

- Use CloudFormation to provision the EC2 instance and all required
  resources. Manage CloudFormation stacks using the AWS CLI.
- Use the AWS CLI to start and stop EC2 instances and to retrieve system
  information (e.g., instance IP address).
- All instance configuration must be automated using Ansible.
  Direct SSH access for configuration tasks is not allowed.

## Guidance

- **Get comfortable with your shell**: Much of DevOps work happens in the terminal.
  Make sure you're comfortable with your shell and terminal application of choice.
- **Save useful shell commands**: You'll run many shell commands, some of which will
  be fairly complex. Save these as scripts
  (or [just](https://just.systems/man/en/) recipes) for quick reuse.
- **Focus on automation**: DevOps is rooted in automation. Look for opportunities
  to eliminate manual steps, even if they seem trivial.
- **If using Python, stick to the standard library**: Python is widely used in DevOps,
  but packaging applications that depend on third-party libraries can be painful.
  For this task, the standard library is more than enough and avoids extra complexity.
  This [RealPython Socket Programming Guide](https://realpython.com/python-sockets/)
  is a good place to start. For modern async applications check out Python's 
  [asyncio module](https://docs.python.org/3/library/asyncio.html).
- **Leverage your systems' service manager**: Use systemd to manage the service. 
  It simplifies startup behvior, logging and monitoring.
  This [RHEL guide to systemd unit files](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/using_systemd_unit_files_to_customize_and_optimize_your_system/assembly_working-with-systemd-unit-files_working-with-systemd)
  is a great resource to get started.
