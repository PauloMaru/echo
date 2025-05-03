# Echo as a Service

This document outlines the task of building and deploying a simple TCP-based
echo service ([RFC 862](https://tools.ietf.org/html/rfc862)) as part of the
[Protohackers "Smoke Test" challenge](https://protohackers.com/problem/0).
It specifies key requirements and constraints, guiding you through the application
setup with modern DevOps tools like AWS CloudFormation, Ansible, and Git.

### Scope

- **Application Implementation**:
  Build a TCP-based echo service based on RFC 862.
- **Infrastructure Provisioning**: Provision a minimal EC2 instance and
  necessary resources via CloudFormation.
- **Configuration and Deployment**: Automate setup and deployment of the
  service using Ansible.
- **Version Control**: Manage both application code and infrastructure
  configuration using Git.

This document assumes you have basic familiarity with Linux and IT practices.
We'll focus on applying modern DevOps tools, so expect to get hands-on with
CloudFormation, Ansible, and Git.

## System Requirements Specification

### Functional Requirements

- The functional requirements are met when the application passes the
  Protohackers "Smoke Test" challenge. Your application should implement the
  Echo Protocol (RFC 862), but the choice of programming language and tools
  is entirely up to you.

### Non-Functional Requirements

- The application code and system configuration must be hosted in a Git
  repository (e.g., GitHub) to maintain version control and support
  collaboration.
- The TCP service must allow the listening port to be configured without
  changing the code, making deployment easier and more flexible.
- The EC2 instance must be provisioned using AWS CloudFormation, ensuring
  infrastructure is defined as code for repeatability.
- Instance configuration must be automated with Ansible, including package
  installation, user setup, and system configuration. This automation ensures
  consistency and reduces the risk of manual errors.
- The echo service must be deployed using Ansible, maintaining automation and
  repeatability across different environments.

### Constraints

- Use CloudFormation to provision the EC2 instance and all required
  resources, and manage the CloudFormation stacks with the AWS CLI to ensure
  consistency.
- Use the AWS CLI to start and stop EC2 instances and retrieve system
  information (e.g., instance IP address). This helps keep the process
  automated and avoids reliance on the AWS Management Console.
- All configuration tasks on the EC2 instance must be automated with Ansible.
  Direct SSH access for configuration is not allowed, ensuring the process is
  fully automated and repeatable.

## Guidance

- **Get comfortable with your shell**: A lot of DevOps work involves using the
  terminal, so make sure you're comfortable with your shell and terminal
  application. You'll be using them extensively during this task.
- **Save useful shell commands**: You'll be executing a lot of shell commands,
  some of which may be complex. Save these commands as shell scripts for quick
  reuse and to avoid retyping.
- **Document your process**: While this is a hands-on task, documenting your
  process - especially for repetitive steps—can save you time later. Commenting
  on configuration files or scripts is a good practice.
- **Focus on automation**: Automation is at the heart of DevOps. Always think
  about automating any manual steps, no matter how simple. This mindset will
  be invaluable for more complex tasks in the future.
- **If using Python, stick to the standard library**: While Python is popular in
  DevOps, packaging and distributing Python applications can be tricky when
  third-party libraries are involved. For this task, stick with Python's standard
  library - it's sufficient for the job and keeps things simple.
