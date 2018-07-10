"""Test the `met` module."""

from hugs.calc import get_wind_dir, get_wind_speed, get_wind_components

from hugs.calc import get_wind_dir, get_wind_speed, get_wind_components

import numpy as np
from numpy.testing import assert_almost_equal, assert_array_almost_equal

import pytest

def test_speed():
    """Test calculating wind speed."""
    u = np.array([4., 2.,0., 0.])
    v = np.array([0.,2., 4., 0.])

    speed = get_wind_speed(u, v)

    s2 = np.sqrt(2.)
    true_speed = np.array([4., 2 * s2, 4., 0.])

    assert_array_almost_equal(true_speed, speed, 4)


def test_scalar_speed():
    """Test wind speed with scalars."""
    s = get_wind_speed(-3., -4.)
    assert_almost_equal(s, 5., 3)


def test_dir():
    """Test calculating wind direction."""
    u = np.array([4., 2., 0., 0.])
    v = np.array([0., 2., 4., 0.])

    direc = get_wind_dir(u, v)

    true_dir = np.array([270., 225., 180., 270.])

    assert_array_almost_equal(true_dir, direc, 4)

# def test_scalar_get_wind_components():
#     """Test calculating wind components for a scalar"""
#     speed = 1.
#     wdir = 0.
#
#     u, v = get_wind_components(speed, wdir)
#
#     true_u, true_v = 0.,-1.
#
#     assert_almost_equal((true_u,true_v), (u,v), 4)
#
# def test_array_get_wind_components():
#     """Test calculating wind components for an array"""
#     speed = np.array((1.,1.))
#     wdir = np.array((0.,90.))
#
#     u, v = get_wind_components(speed, wdir)
#
#     true_u, true_v = np.array([-0., -1.]), np.array([ -1.00000000e+00,  -6.12323400e-17])
#
#     assert_array_almost_equal((true_u,true_v), (u,v), 3)

def test_wind_comps_basic():
  """Test the basic wind component calculation."""
  speed = np.array([4, 4, 4, 4, 25, 25, 25, 25, 10.])
  dirs = np.array([0, 45, 90, 135, 180, 225, 270, 315, 360])
  s2 = np.sqrt(2.)

  u, v = get_wind_components(speed, dirs)

  true_u = np.array([0, -4 / s2, -4, -4 / s2, 0, 25 / s2, 25, 25 / s2, 0])
  true_v = np.array([-4, -4 / s2, 0, 4 / s2, 25, 25 / s2, 0, -25 / s2, -10])

  assert_array_almost_equal(true_u, u, 4)
  assert_array_almost_equal(true_v, v, 4)


def test_wind_comps_scalar():
  """Test wind components calculation with scalars."""
  u, v = get_wind_components(8, 150)
  assert_almost_equal(u, -4, 3)
  assert_almost_equal(v, 6.9282, 3)

def test_warning_direction():
    """Test that warning is raised wind direction > 360."""
    with pytest.warns(UserWarning):
        get_wind_components(3, 480)
