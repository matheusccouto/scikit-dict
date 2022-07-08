"""Test creating YAML files from python objects."""

import sklearn.linear_model

import skdict


def test_linear_model():
    """Test get linear model."""
    ref = {"LinearRegression": None}
    out = skdict.dump(sklearn.linear_model.LinearRegression())
    assert ref == out
