"""Test creating python objects from dict objects."""

import sklearn.linear_model

import skdict


def test_imported_module():
    """Test if it loads an object from a model that has been imported."""
    out = skdict.load({"LinearRegression": None})
    ref = sklearn.linear_model.LinearRegression()
    assert str(out) == str(ref)


def test_not_imported_module():
    """Test if it loads an object from a model that has not been imported."""
    out = skdict.load({"KMeans": {"n_clusters": 10}})
    assert str(out) == "KMeans(n_clusters=10)"


def test_pipeline():
    """Test a complex pipeline."""
    out = skdict.load(
        {
            "Pipeline": {
                "steps": [
                    [
                        "transformer",
                        {
                            "ColumnTransformer": {
                                "remainder": {"PowerTransformer": None},
                                "transformers": [
                                    "encoder",
                                    {
                                        "OneHotEncoder": {
                                            "handle_unknown": "ignore",
                                            "sparse": False,
                                        }
                                    },
                                    [0],
                                ],
                            }
                        },
                    ],
                    [
                        "regressor",
                        {
                            "HistGradientBoostingRegressor": {
                                "learning_rate": 0.1,
                                "loss": "poisson",
                            }
                        },
                    ],
                ]
            }
        }
    )
    ref = sklearn.pipeline.Pipeline(
        [
            [
                "transformer",
                sklearn.compose.ColumnTransformer(
                    transformers=[
                        "encoder",
                        sklearn.preprocessing.OneHotEncoder(
                            handle_unknown="ignore",
                            sparse=False,
                        ),
                        [0],
                    ],
                    remainder=sklearn.preprocessing.PowerTransformer(),
                ),
            ],
            [
                "regressor",
                sklearn.ensemble.HistGradientBoostingRegressor(
                    learning_rate=0.1,
                    loss="poisson",
                ),
            ],
        ]
    )
    assert str(out) == str(ref)
