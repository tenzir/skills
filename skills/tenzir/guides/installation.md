---
title: "Install Tenzir"
description: "Install the tenzir command on macOS or Linux with Homebrew, a Debian or RPM package, a static tarball, Docker, or uv, and run your first pipeline."
canonical: https://tenzir.com/docs/guides/installation
source: https://tenzir.com/docs/guides/installation.md
section: "Docs"
---

# Install Tenzir

> Install the tenzir command on macOS or Linux with Homebrew, a Debian or RPM package, a static tarball, Docker, or uv, and run your first pipeline.

You install one program, the `tenzir` command, and it does everything you need from a terminal: it runs pipelines on your machine with `tenzir run`, runs a deployment on your machine or server with `tenzir up`, and manages your organizations, workspaces, configurations, and deployments on the [platform](../explanations/platform.md). Every method in this guide installs the same command with the pipeline engine built in, so pick the one that fits how you already manage software.

Supported platforms

Tenzir runs on macOS 26 or newer on Apple Silicon, and on Linux for x86\_64 and aarch64. Our Linux builds are statically linked, so they don’t depend on the libraries of your distribution. On Windows, run the Linux build in WSL 2, or use the Docker image.

## Choose an installation method

Each method suits a different situation:

| Situation                                             | Method                                                                                                                                                                            |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| You work on a Mac                                     | [Install the Homebrew cask](installation.md#install-a-system-package)                                                                              |
| You run Debian, Ubuntu, RHEL, or Fedora               | [Install a Debian or RPM package](installation.md#install-a-system-package)                                                                        |
| You have no package manager or no root access         | [Unpack a static tarball](installation.md#unpack-a-static-tarball)                                                                                 |
| You work in containers or on Windows                  | [Run the Docker image](installation.md#run-tenzir-in-docker)                                                                                       |
| A server only runs a deployment in Docker             | [Use the install command from the app](add-a-deployment.md#run-a-deployment-on-a-server)                                                           |
| You want a quick try, a CI job, or an agent’s sandbox | [Install with uv](installation.md#install-with-uv), or [run it with uvx](installation.md#run-it-without-installing) |
| You want to change the engine itself                  | [Build from source](installation.md#build-from-source)                                                                                             |

When in doubt, use the package manager of your system: Homebrew on macOS, and apt or dnf on Linux. It keeps Tenzir up to date with the rest of your software.

## Install a system package

Our packages integrate with the package manager of your system, which suits machines that an administrator maintains. They install the `tenzir` command into `/opt/tenzir/bin`. The download links that follow always point at the newest stable release, and our [GitHub releases page](https://github.com/tenzir/tenzir/releases) lists the packages of every release, for when you want to pin a version.

* macOS

  Install the cask from our [Homebrew](https://brew.sh) tap:

  ```sh
  brew install --cask tenzir/tenzir/tenzir
  ```

  The cask runs our notarized installer package and links the `tenzir` command into Homebrew’s `bin`, so it’s on your `PATH` right away. Upgrade with `brew upgrade --cask tenzir`, and remove Tenzir with `brew uninstall --cask tenzir`.

  Without Homebrew, download the [installer package for macOS](https://storage.googleapis.com/tenzir-dist-public/packages/release/macOS/tenzir-latest-arm64-darwin-static.pkg) and open it, or install it from a terminal:

  ```sh
  curl -fLO https://storage.googleapis.com/tenzir-dist-public/packages/release/macOS/tenzir-latest-arm64-darwin-static.pkg
  sudo installer -pkg tenzir-latest-arm64-darwin-static.pkg -target /
  ```

  The package doesn’t touch your `PATH`, so add `/opt/tenzir/bin` to your shell’s startup file and open a new terminal:

  ```sh
  echo 'export PATH="/opt/tenzir/bin:$PATH"' >> ~/.zshrc
  ```

* Debian and Ubuntu

  Download the package for your architecture and install it with apt, which also installs its dependencies:

  ```sh
  curl -fLO "https://storage.googleapis.com/tenzir-dist-public/packages/release/debian/tenzir_latest_$(dpkg --print-architecture).deb"
  sudo apt-get install "./tenzir_latest_$(dpkg --print-architecture).deb"
  ```

  The package puts `/opt/tenzir/bin` on the `PATH` of login shells, so open a new terminal before you run `tenzir`. Upgrade by installing a newer package the same way, and remove Tenzir with `sudo apt-get remove tenzir`.

* RHEL and Fedora

  Download the package for your architecture and install it with dnf:

  ```sh
  curl -fLO "https://storage.googleapis.com/tenzir-dist-public/packages/release/rpm/tenzir-latest-$(uname -m)-linux-static.rpm"
  sudo dnf install "./tenzir-latest-$(uname -m)-linux-static.rpm"
  ```

  The package puts `/opt/tenzir/bin` on the `PATH` of login shells, so open a new terminal before you run `tenzir`. Upgrade by installing a newer package the same way, and remove Tenzir with `sudo dnf remove tenzir`.

## Unpack a static tarball

A tarball holds the same files as our packages, without a package manager in between. It runs from any directory, which makes it the way to go on machines where you lack root access or can’t install packages.

* macOS

  ```sh
  curl -fLO https://storage.googleapis.com/tenzir-dist-public/packages/release/tarball/tenzir-latest-arm64-darwin-static.tar.gz
  sudo tar xzf tenzir-latest-arm64-darwin-static.tar.gz -C /
  export PATH="/opt/tenzir/bin:$PATH"
  ```

* Linux

  ```sh
  curl -fLO "https://storage.googleapis.com/tenzir-dist-public/packages/release/tarball/tenzir-latest-$(uname -m)-linux-static.tar.gz"
  sudo tar xzf "tenzir-latest-$(uname -m)-linux-static.tar.gz" -C /
  export PATH="/opt/tenzir/bin:$PATH"
  ```

The archive unpacks into `opt/tenzir/` below the directory you pass to `-C`. To install without root, pass a directory you own instead, such as `-C ~/.local` without `sudo`, and put `~/.local/opt/tenzir/bin` on your `PATH`. Add the `export` line to your shell’s startup file to keep the command available in new terminals. To upgrade, unpack a newer tarball over the old one, and to remove Tenzir, delete the `opt/tenzir` directory.

## Run Tenzir in Docker

Our image `tenzir/tenzir` on Docker Hub, also available as `ghcr.io/tenzir/tenzir`, contains the same `tenzir` command as its entry point. Run a pipeline without installing anything on the host:

```sh
docker run --rm tenzir/tenzir run 'from {x: 42}'
```

Add `-i` to pipe data from the host into the pipeline:

```sh
echo '{"x": 1}' | docker run --rm -i tenzir/tenzir run 'x = x + 1'
```

The image comes in these tags:

| Tag      | Contents                                |
| -------- | --------------------------------------- |
| `latest` | The newest stable release.              |
| `v7`     | The newest stable release of Tenzir 7.  |
| `v7.0`   | The newest patch release of Tenzir 7.0. |
| `v7.0.0` | Tenzir 7.0.0 and no other release.      |

Every tag also exists with a `-slim` suffix, such as `v7-slim`, for a smaller image with our statically linked build.

A container forgets your sign-in when it exits. For platform commands, pass an API key from your environment instead, which our guide on [connecting to Tenzir](connect-to-tenzir.md) shows how to create:

```sh
docker run --rm -e TENZIR_API_KEY tenzir/tenzir status
```

To keep a deployment running in a container on a server, use the install command that the app shows, as our guide on [running a deployment on a server](add-a-deployment.md#run-a-deployment-on-a-server) describes.

## Install with uv

For ad-hoc use, such as a quick try, a CI job, or an AI agent’s sandbox, the [uv](https://docs.astral.sh/uv/) package manager installs the `tenzir` command from PyPI into an environment of its own and puts it on your `PATH`, without root access. Our package on PyPI bundles the engine, and uv fetches a Python interpreter when your machine lacks one, so you need nothing else.

If you don’t have uv yet, install it first:

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then install Tenzir:

```sh
uv tool install tenzir
```

If your shell doesn’t find `tenzir` afterwards, run `uv tool update-shell` and open a new terminal. Upgrade to the latest release with `uv tool upgrade tenzir`, and remove the command with `uv tool uninstall tenzir`.

### Run it without installing

The `uvx` command runs Tenzir from uv’s cache without installing it, which suits a first try and CI jobs:

```sh
uvx tenzir run 'from {x: 42}'
```

The cache keeps the version that `uvx` fetched first. Write `uvx tenzir@latest` to check for a newer release on every run, which costs a little startup time.

### Install with pip

When you already work in a Python virtual environment, install the same package with pip, which needs Python 3.10 or newer:

```sh
python3 -m venv .venv
. .venv/bin/activate
pip install tenzir
```

The command is then available while the environment is active.

## Build from source

Building from source gives you the open-source engine, for when you want to change it or contribute to it. The resulting `tenzir` command runs pipelines with `tenzir run`, but it lacks the platform commands, such as `tenzir up` and `tenzir auth login`, and the proprietary plugins of our prebuilt packages. Our guide on [building Tenzir from source](development/build-from-source.md) walks through the build.

## Try a release candidate

Before a release ships, we publish release candidates so that you can test it early. They never replace the stable release that the links and tags in this guide point at, so you opt in explicitly:

* For packages and tarballs, download them from the release that our [GitHub releases page](https://github.com/tenzir/tenzir/releases) marks as **Pre-release**.
* With Docker, use the candidate’s tag, such as `tenzir/tenzir:v7.0.0-rc.1`.
* With uv, run `uv tool install --prerelease allow tenzir`.

Homebrew installs stable releases only.

## Check the installation

Print the version of the command:

```sh
tenzir --version
```

It prints the version you installed, such as `tenzir v7.0.0`. Then run your first pipeline:

```sh
tenzir run 'from {x: 42}'
```

```tql
{
  x: 42,
}
```

The pipeline ran in the `tenzir` process itself, without an account or a deployment. If your shell doesn’t find `tenzir`, check your `PATH`: packages and tarballs install into `/opt/tenzir/bin`, and `uv tool update-shell` adds the directory of uv’s tools.

## Next steps

With the command installed, sign in to the platform as our guide on [connecting to Tenzir](connect-to-tenzir.md) shows, then [add a deployment](add-a-deployment.md) to run your pipelines, or watch live security events flow through Tenzir in our [quickstart](quickstart.md).

* [Connect to Tenzir](connect-to-tenzir.md)
* [Add a deployment](add-a-deployment.md)
* [Quickstart](quickstart.md)
* [CLI](../reference/cli.md)
