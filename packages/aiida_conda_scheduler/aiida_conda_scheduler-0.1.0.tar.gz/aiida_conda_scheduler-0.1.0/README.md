[![Build Status][ci-badge]][ci-link]
[![Coverage Status][cov-badge]][cov-link]
[![Docs status][docs-badge]][docs-link]
[![PyPI version][pypi-badge]][pypi-link]

# aiida_conda_scheduler

AiiDA scheduler plugins that allow for `conda run`.

Currently, as of aiida-core `v2.0.1`, it is impossible to set up a `Computer` + `Code` which can run, for example:

```shell
conda run --name myenv mpirun -np 4 pw.x -i input.in
```

since, (a) a code can only specify a `remote_abs_path` and (b) only a computer can specify the `mpirun_command`.

This is really the only way to run a code which is not in the Conda `base` environment, since `conda activate myenv`
(which could perhaps be added to `prepend_text`) fails when run in a script.

These scheduler plugins subclass the built-in scheduler subclasses, and overrides the `_get_run_line` method and:

1. Raises a `NotImplementedError` if `len(codes_info) != 1` or `codes_run_mode != CodeRunMode.SERIAL` (i.e. only one code is supported).
2. Loads the code from `codes_info[0].code_uuid` and retrieves its description
3. Uses this description to determine the environment name, by finding `env=myenv`
4. Appends `conda run --name myenv ` to the run line.

## Installation

```shell
pip install aiida_conda_scheduler
reentry scan  # aiida v1.x only
```

Then the plugins should show in:

```shell
verdi plugin list aiida.schedulers
```

## Development

Use [pipx](https://pipx.readthedocs.io) to install the `tox` and `pre-commit` command tools.

```shell
git clone https://github.com/chrisjsewell/aiida-conda-scheduler .
cd aiida-conda-scheduler
pre-commit run --all
tox
```

For aiida-core v1, use e.g.

```shell
tox -e py38-v1
```

## License

MIT

## Contact

chrisj_sewell@hotmail.com

[ci-badge]: https://github.com/chrisjsewell/aiida-conda-scheduler/workflows/ci/badge.svg?branch=master
[ci-link]: https://github.com/chrisjsewell/aiida-conda-scheduler/actions
[cov-badge]: https://coveralls.io/repos/github/chrisjsewell/aiida-conda-scheduler/badge.svg?branch=master
[cov-link]: https://coveralls.io/github/chrisjsewell/aiida-conda-scheduler?branch=master
[docs-badge]: https://readthedocs.org/projects/aiida_conda_scheduler/badge
[docs-link]: http://aiida_conda_scheduler.readthedocs.io/
[pypi-badge]: https://badge.fury.io/py/aiida_conda_scheduler.svg
[pypi-link]: https://badge.fury.io/py/aiida_conda_scheduler
