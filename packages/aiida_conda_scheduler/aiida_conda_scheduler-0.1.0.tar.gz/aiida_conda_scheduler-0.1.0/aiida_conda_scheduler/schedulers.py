import re
from typing import List

from aiida.common import CodeInfo, CodeRunMode
from aiida.schedulers.plugins import direct, slurm


def append_conda_run(
    cmd: str, codes_info: List[CodeInfo], codes_run_mode: CodeRunMode, _load_code=None
) -> str:
    """Append conda to the run command."""
    from aiida.orm import load_code

    if codes_run_mode != CodeRunMode.SERIAL:
        raise NotImplementedError(
            f"Conda scheduler only supports serial mode, not {codes_run_mode}"
        )
    if len(codes_info) != 1:
        raise NotImplementedError(
            f"Conda scheduler only supports one code, not {len(codes_info)}"
        )

    code_uuid = codes_info[0].code_uuid
    if _load_code is None:
        _load_code = load_code
    code = _load_code(uuid=code_uuid)

    env_match = re.search(r"env=([^\s]+)", code.description)
    if env_match is None:
        raise ValueError(
            f"Code {code_uuid} has no 'env=name' in its description: {code.description}"
        )
    env_name = env_match.group(1)

    return f"conda run -n {env_name} {cmd}"


class CondaDirectScheduler(direct.DirectScheduler):
    def _get_run_line(
        self, codes_info: List[CodeInfo], codes_run_mode: CodeRunMode
    ) -> str:
        cmd = super()._get_run_line(codes_info, codes_run_mode)
        return append_conda_run(cmd, codes_info, codes_run_mode)


class CondaSlurmScheduler(slurm.SlurmScheduler):
    def _get_run_line(
        self, codes_info: List[CodeInfo], codes_run_mode: CodeRunMode
    ) -> str:
        cmd = super()._get_run_line(codes_info, codes_run_mode)
        return append_conda_run(cmd, codes_info, codes_run_mode)
