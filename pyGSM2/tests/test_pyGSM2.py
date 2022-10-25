"""
Unit and regression test for the pyGSM2 package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import pyGSM2


def test_pyGSM2_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "pyGSM2" in sys.modules
