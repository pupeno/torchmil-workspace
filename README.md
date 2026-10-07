# Pablo's Torchmil Contributing Workspace

This repository is Pablo's development workspace for contributing to [torchmil](https://github.com/Franblueee/torchmil).

It keeps the devcontainer configuration, experiments, useful scripts, documentation, and useful links together.

## Open Tickets

## Closed Tickets

## Open Pull Requests

## Actioned Pull Requests

## Setup

Set up the host NVIDIA driver and
[NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)
so Docker can expose the GPU.

Clone the workspace and run its setup script:

```bash
mkdir torchmil
git clone https://github.com/pupeno/torchmil-workspace.git torchmil/workspace
torchmil/workspace/setup.sh
```

Open the outer `torchmil/` directory in an editor with devcontainer support, then reopen it in its devcontainer.

## Common Commands

Run tests inside the devcontainer:

```bash
cd /workspaces/torchmil/torchmil
pytest
```

Sync dependencies:

```bash
uv sync --project /workspaces/torchmil/workspace --locked
```
