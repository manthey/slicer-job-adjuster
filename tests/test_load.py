import pytest

from girder.plugin import loadedPlugins


@pytest.mark.plugin('slicer_job_adjuster')
def test_import(server):
    assert 'slicer_job_adjuster' in loadedPlugins()
