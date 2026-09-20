# Development Guide

This document provides a reference for development practices and tools used in this project.

## Assumption & Pre-requisites

- The project is developed using Visual Studio Code and the development container.
- The development container is configured to use Python 3.14.
- Windows was used as the development environment, but development can happen on other operating systems.
- Linux was used as the development container.
- Production environment is assumed to be Linux-based.

### Windows Pre-requisites

For development on Windows, the following pre-requisites are required:

- [Windows Subsystem for Linux (WSL) 2](https://docs.microsoft.com/en-us/windows/wsl/install)
- [Docker Desktop](https://www.docker.com/products/docker-desktop)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Git for Windows](https://git-scm.com/download/win)

See local Windows installation guide here: [docs/dev-env-setup.md](./dev-env-setup.md).

## Getting Started

To get started with the project, follow these steps:

1. Clone the repository.
2. Open the repository in VS Code.
3. Reopen the repository in the development container ([on Windows](https://code.visualstudio.com/docs/devcontainers/containers#_open-a-wsl-2-folder-in-a-container-on-windows)).
4. Start coding!

## Development Container

The project uses a development container to ensure a consistent development environment across all developers. The development container is defined in `.devcontainer/devcontainer.json` and uses the following configuration:

- It is from a Python 3.14 base image.
- Recommended VS Code extensions will be installed.
- [uv](https://docs.astral.sh/uv/) will be installed and the project's `dev` dependency group will be synced into a `.venv` via `uv sync --group dev`.

## Project Structure

The project structure is as follows:

```bash
.
├── .vscode/                   # Shared VS Code workspace configuration
├── .devcontainer/             # Development container configuration
├── scripts/                   # CLI scripts
│   └── devcontainer-setup.sh  # Development container setup (ref. in devcontainer.json)
├── src/                       # Source code
├── tests/                     # Unit tests
├── docs/                      # Main documentation
├── pyproject.toml             # Project metadata and dependency declarations (PEP 735 groups)
├── uv.lock                    # Locked, exact dependency versions (committed, do not edit by hand)
├── .python-version            # Pinned Python version for uv
└── ...
```

## Python Dependency Management

This project uses [uv](https://docs.astral.sh/uv/) for Python packaging and dependency management. Dependencies are declared in `pyproject.toml` and pinned to exact resolved versions in `uv.lock` (which is committed to version control for reproducibility).

- Add an application/production dependency: `uv add <package>`
- Add a development tool dependency (linters, test tools, etc.): `uv add --group dev <package>`
- Add a dependency needed only in CI: `uv add --group ci <package>` — the `ci` group starts as an extension of `dev` (`{include-group = "dev"}` in `pyproject.toml`), so it only needs entries once it needs to diverge from `dev`.
- Install/refresh your local environment: `uv sync --group dev`
- Install the environment the way CI will: `uv sync --group ci`
- Run a command inside the managed environment without activating it: `uv run <command>` (e.g. `uv run pytest`)
- Upgrade dependencies within their declared version bounds and update the lockfile: `uv lock --upgrade`

## Linting, Code Security Scanning, and Dependency Vulnerability Scanning

The project uses [Bandit](https://github.com/PyCQA/bandit) and [Pylint Secure Coding Standard](https://github.com/Takishima/pylint-secure-coding-standard) to scan for security vulnerabilities and code quality issues. Bandit is a dedicated, comprehensive security scanner, while Pylint Secure Coding Standard is a lightweight plugin that surfaces a small subset of the same concerns directly in the linter, giving faster in-editor feedback.

Both tools have VS Code extensions installed for real-time scanning, but they can also be run from the command line.

The project uses [pip-audit](https://pypi.org/project/pip-audit/) to scan for Python dependencies with known security vulnerabilities. It is fully open source and requires no account or commercial license.

The configuration files are located in the root of the project:

- [`.pylintrc`](../.pylintrc): Pylint configuration.
- [`bandit.yml`](../bandit.yml): Bandit configuration.

### Running Linters and Scanners from the Command Line

To run Pylint with Secure Coding Standard:

```bash
uv run pylint src
```

To run Bandit security scanner:

```bash
uv run bandit -r src               # only source code folder
uv run bandit -c bandit.yml -r .   # entire project and using a Bandit config file
```

To run pip-audit dependency vulnerability scanner:

```bash
uv run pip-audit
```

## The use of FIXME and TODO

The project uses the [TODO Highlight](https://marketplace.visualstudio.com/items?itemName=wayou.vscode-todo-highlight) extension to highlight `TODO`, and `FIXME` comments and a CI check should be setup to fail if any FIXMEs are present in a `main` branch merge request. Pylint checks for "fixme" comments.

The convention is to use `FIXME` for tasks that need to be fixed before the PR can be approved and merged. See it as notes to yourself about incomplete code or security issues that need to be addressed.

`TODO` is for tasks that need to be done sometime in the future. It can be used for improvements, refactoring, or other tasks that are not blocking the PR.

Note! It should be a comment line starting with TODO or FIXME followed by a colon and a space.

Example:
<pre># FIXME&colon; Add input validation.</pre>
