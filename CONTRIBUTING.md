# Contributing to Comet

Thanks for your interest in contributing to Comet. Bug reports, questions, and pull requests are all welcome.

## Reporting bugs / requesting features

Please open an [issue](https://github.com/mibur1/comet/issues) with:

- A short description of the problem or the feature you'd like.
- For bugs: a minimal reproducible example, the comet version, your OS, and any relevant error output.
- For features: what you'd use it for. A concrete use case helps us decide scope.

## Development setup

```bash
conda create -n comet python==3.13
conda activate comet

git clone https://github.com/mibur1/comet.git
cd comet
pip install -e ".[test,doc,gui,build]"
```

## Running the tests

```bash
pytest tests/
```

The CIFTI tests need [Connectome Workbench](https://www.humanconnectome.org/software/connectome-workbench) on your `PATH`; they'll skip if `wb_command` isn't available.

## Submitting a pull request

Before you spend time on a larger changes, **please open an issue first** so we can align on scope.

- Keep the change focused; one topic per PR.
- Add or update a test if you're changing behaviour.
- Update the relevant tutorial or docstring if you're changing a public API.
- Commits that only touch docs / tutorials can include `[skip ci]` in the message to avoid re-running the test workflow.

## Questions

For anything that isn't a bug or feature request, feel free to email the maintainer (address in [`pyproject.toml`](pyproject.toml)) or open a discussion issue.

By contributing, you agree that your contributions are licensed under the same MIT License as the rest of the project.
