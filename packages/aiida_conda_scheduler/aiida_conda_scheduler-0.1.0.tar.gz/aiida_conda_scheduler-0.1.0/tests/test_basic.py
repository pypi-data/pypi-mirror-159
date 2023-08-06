"""Some simple tests"""
from aiida.common import CodeInfo, CodeRunMode
from aiida.plugins import SchedulerFactory

from aiida_conda_scheduler.schedulers import (
    CondaDirectScheduler,
    CondaSlurmScheduler,
    append_conda_run,
)


def test_init_direct():
    CondaDirectScheduler()


def test_init_slurm():
    CondaSlurmScheduler()


def test_load_direct():
    assert issubclass(SchedulerFactory("conda.direct"), CondaDirectScheduler)


def test_load_slurm():
    assert issubclass(SchedulerFactory("conda.slurm"), CondaSlurmScheduler)


class DummyCode:
    def __init__(self, description: str):
        self.description = description


def _load_code(*args, **kwargs):
    assert kwargs["uuid"] == "uuid"
    return DummyCode("env=myenv")


def test_append_conda_run():
    code_info = CodeInfo({"code_uuid": "uuid"})
    string = append_conda_run(
        "cmd", [code_info], CodeRunMode.SERIAL, _load_code=_load_code
    )
    assert string == "conda run -n myenv cmd"
