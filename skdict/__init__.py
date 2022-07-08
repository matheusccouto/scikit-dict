"""Define Scikit-Learn objects using YAML"""

from __future__ import annotations

import json
import importlib
import inspect
import pkgutil
from types import ModuleType, FunctionType

import sklearn
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.utils._pprint import _changed_params


MODULES = [
    "sklearn.base",
    "sklearn.calibration",
    "sklearn.cluster",
    "sklearn.compose",
    "sklearn.covariance",
    "sklearn.cross_decomposition",
    "sklearn.datasets",
    "sklearn.decomposition",
    "sklearn.discriminant_analysis",
    "sklearn.dummy",
    "sklearn.ensemble",
    "sklearn.exceptions",
    "sklearn.experimental",
    "sklearn.feature_extraction",
    "sklearn.feature_selection",
    "sklearn.gaussian_process",
    "sklearn.impute",
    "sklearn.inspection",
    "sklearn.isotonic",
    "sklearn.kernel_approximation",
    "sklearn.kernel_ridge",
    "sklearn.linear_model",
    "sklearn.manifold",
    "sklearn.metrics",
    "sklearn.mixture",
    "sklearn.model_selection",
    "sklearn.multiclass",
    "sklearn.multioutput",
    "sklearn.naive_bayes",
    "sklearn.neighbors",
    "sklearn.neural_network",
    "sklearn.pipeline",
    "sklearn.preprocessing",
    "sklearn.random_projection",
    "sklearn.semi_supervised",
    "sklearn.svm",
    "sklearn.tree",
    "sklearn.utils",
]
for mod in MODULES:
    importlib.import_module(mod)


def _get_submodules(module):
    """Get all submodules of a module."""
    if hasattr(module, "__path__"):
        return [name for _, name, _ in pkgutil.iter_modules(module.__path__)]
    return []


def get_all_sklearn_objects(module: ModuleType) -> FunctionType | BaseEstimator | TransformerMixin:
    """Get all objects from a module."""
    objs = {}
    submodules = _get_submodules(module)
    for name in dir(module):
        if not name.startswith("_"):
            obj = getattr(module, name)
            if name in submodules:
                objs.update(get_all_sklearn_objects(obj))
            elif inspect.isclass(obj) or inspect.isfunction(obj):
                objs[name] = obj

    return objs


def load(dict_: dict, /) -> BaseEstimator | TransformerMixin:
    """Create a python instance from dict structure."""
    objs = get_all_sklearn_objects(sklearn)

    if isinstance(dict_, list):
        for i, item in enumerate(dict_):
            dict_[i] = load(item)
        return dict_

    if isinstance(dict_, dict):
        for key in dict_.keys():
            dict_[key] = load(dict_[key])
            kwargs = dict_[key] if dict_[key] is not None else {}
            try:
                return objs[key](**kwargs)
            except KeyError:
                pass
        return dict_

    return dict_


class SKLearnEncoder(json.JSONEncoder):
    """Encode SKLearn objects to JSON."""

    def default(self, o):
        """Default encoding."""
        if isinstance(o, (sklearn.base.BaseEstimator, sklearn.base.TransformerMixin)):
            name = o.__class__.__name__
            params = _changed_params(o)
            if params == {}:
                params = None
            return {name: params}
        return json.JSONEncoder.default(self, o)


def dump(obj: BaseEstimator | TransformerMixin, /) -> dict:
    """Create a dict from a python object."""
    return json.loads(json.dumps(obj, cls=SKLearnEncoder))
