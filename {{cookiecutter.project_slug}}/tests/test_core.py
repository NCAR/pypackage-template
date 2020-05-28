import pytest
import xarray
import {{cookiecutter.project_slug}}

def test_foo():
    assert 'foo' == 'foo'


@pytest.mark.parametrize('dataset_name', ['rasm', 'air_temperature'])
def test_mean_func(dataset_name):
    ds = xr.tutorial.open_dataset(dataset_name)
    results = {{cookiecutter.project_slug}}.core.mean_func(ds)
    assert isinstance(results, xr.Dataset)
