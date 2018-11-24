import os

import pytest

from minimizer.core import Minimizer

fp = os.path.abspath(os.path.join("tests", os.pardir)) + "/static"
filename = "placeholder-min.jpg"
size = (125, 125)
_format = "png"


def test_minimizer_fails_with_bad_directory():
    with pytest.raises(AssertionError) as exc:
        m = Minimizer("/s/t/c")
    assert "does not exist" in str(exc)


def test_minimizer_fails_with_unsupported_image_format():
    with pytest.raises(AssertionError) as exc:
        m = Minimizer(fp, format="JPG")
    assert "not supported" in str(exc)


def test_minimizer_fails_with_bad_filename():
    with pytest.raises(AssertionError) as exc:
        m = Minimizer(fp, name="placeholder")
    assert "does not exist" in str(exc)


def test_minimizer_runs_and_creates_new_image():
    m = Minimizer(fp, size=size)
    m()
    assert os.path.isfile(f"{fp}/{filename}") == True
    os.remove(f"{fp}/{filename}")


def test_minimizer_converts_image_format():
    m = Minimizer(fp, size=size, format=_format)
    m()
    name = filename.replace("jpg", "png")
    assert os.path.isfile(f"{fp}/{name}") == True
    os.remove(f"{fp}/{name}")
