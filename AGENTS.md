# Agents

## Workspace layout

The project root at `/workspaces/torchmil/` is a plain directory containing two sibling Git repositories:

- `/workspaces/torchmil/torchmil/` is the Torchmil repository. Run Torchmil Git commands, inspect its diffs, and make source changes there.
- `/workspaces/torchmil/workspace/` is the workspace repository. It owns the devcontainer and editor configuration, scripts, notes, and experiments.
- Experiment directories live directly under `/workspaces/torchmil/workspace/`. They are not part of the Torchmil repository unless a task explicitly says to move a change from an experiment into Torchmil.

`setup.sh` links configuration from the workspace repository into the project root. The script defines which links are managed.

Keep the two repositories as siblings; do not turn the Torchmil checkout into a submodule or nest it inside the workspace repository.
