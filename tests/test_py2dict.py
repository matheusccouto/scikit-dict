"""Test creating dict files from python objects."""

import sklearn.linear_model

import skdict


def test_simple_object():
    """Test if it dumps a simple object."""
    out = skdict.dump(sklearn.linear_model.LinearRegression())
    ref = {"LinearRegression": None}
    assert out == ref


def test_pipeline():
    """Test dumping a complex pipeline."""
    ref = skdict.dump(
        sklearn.pipeline.Pipeline(
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
                        learning_rate=0.01,
                        loss="poisson",
                    ),
                ],
            ]
        )
    )
    out = {
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
                            "learning_rate": 0.01,
                            "loss": "poisson",
                        }
                    },
                ],
            ]
        }
    }
    assert out == ref
