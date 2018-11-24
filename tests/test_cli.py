import os

import pytest
from click.testing import CliRunner

from minimizer.cli import run

fp = os.path.abspath(os.path.join("tests", os.pardir))


@pytest.fixture(scope="module")
def runner():
    return CliRunner()


def test_run_function_completes_without_error(runner):
    result = runner.invoke(run)
    assert result.exception is None
    assert result.exit_code == 0

