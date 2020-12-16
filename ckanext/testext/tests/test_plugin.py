"""
Tests for plugin.py.

To write tests for your extension you should install the pytest-ckan package:

    pip install pytest-ckan

This

"""
import pytest

import ckanext.testext.plugin as plugin

@pytest.mark.usefixtures('clean_db')
def test_plugin():

    pass
