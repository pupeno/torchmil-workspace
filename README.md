# Pablo's Torchmil Contributing Workspace

This repository is Pablo's development workspace for contributing to [torchmil](https://github.com/Franblueee/torchmil).

It keeps the devcontainer configuration, experiments, useful scripts, documentation, and useful links together.

## Open Tickets

- [#29 - [BUG] MultiheadSelfAttention still uses dropout in eval mode](https://github.com/Franblueee/torchmil/issues/29).
- [#31 - [BUG] ProbSmoothAttentionPool regularization includes padded instances](https://github.com/Franblueee/torchmil/issues/31).

## Closed Tickets

## Open Pull Requests

- [#28 - Fix MultiheadSelfAttention still using dropout in eval mode](https://github.com/Franblueee/torchmil/pull/28): fixes [#29](https://github.com/Franblueee/torchmil/issues/29).
- [#30 - Fix padding in ProbSmoothAttentionPool regularization](https://github.com/Franblueee/torchmil/pull/30): fixes [#31](https://github.com/Franblueee/torchmil/issues/31).

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
