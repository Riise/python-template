# Development Environment Setup on Windows

The tools installed are:

- Windows Subsystem for Linux v2 (WSL2)
- Docker Desktop
- VS Code
- Git for Windows

## Prerequisites

- Windows 10 version 2004 and higher (Build 19041 and higher) or Windows 11.

## Steps

### 1. Install WSL2

1. Open PowerShell as Administrator.
2. Enable the WSL feature:

    ```powershell
    wsl --install
    ```

3. Set WSL2 as the default version:

    ```powershell
    wsl --set-default-version 2
    ```

4. Install a Linux distribution from the Microsoft Store (e.g., Ubuntu).

### 2. Install Docker Desktop

1. Download Docker Desktop from [Docker's official website](https://www.docker.com/products/docker-desktop).
2. Run the installer and follow the on-screen instructions.
3. During installation, ensure the option "Use the WSL 2 based engine" is selected.
4. After installation, start Docker Desktop and enable integration with your WSL2 distribution.

### 3. Install Visual Studio Code

1. Download VS Code from [Visual Studio Code's official website](https://code.visualstudio.com/).
2. Run the installer and follow the on-screen instructions.
3. Install the "Remote - WSL" extension for VS Code:
    1. Open VS Code.
    2. Go to the Extensions view by clicking the Extensions icon in the Activity Bar on the side of the window.
    3. Search for "Remote - WSL" and install it.

### 4. Install Git for Windows

1. Download Git for Windows from [Git's official website](https://git-scm.com/).
2. Run the installer and follow the on-screen instructions.
3. During installation, ensure the option "Git from the command line and also from 3rd-party software" is selected.

### 5. Verify Installation

Open PowerShell and verify:

```powershell
wsl --list --verbose
docker --version
code --version
git --version
```

You have now set up your development environment on Windows.
