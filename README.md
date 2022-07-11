# scikit-dict
Define Scikit-Learn objects from dict

[![PyPi Version](https://img.shields.io/pypi/v/scikit-dict.svg)](https://pypi.python.org/pypi/scikit-dict/)
[![MIT License](https://img.shields.io/github/license/matheusccouto/scikit-dict)](https://github.com/matheusccouto/scikit-dict/blob/master/LICENSE)
[![codecov](https://codecov.io/gh/matheusccouto/scikit-dict/branch/main/graph/badge.svg?token=jvukfL51k7)](https://app.codecov.io/gh/matheusccouto/scikit-dict/branch/main)

## Getting Started
### Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install scikit-dict.
```bash
pip install scikit-dict
```
## Usage
### Create a dict from a Scikit-Learn object.
```python
import skdict
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

obj = Pipeline([("scaler", StandardScaler()), ("svc", sklearn.svm.SVC())])
d = skdict.dump(obj)
```
It will create a dict with this content:
```python
{
    "Pipeline": {
        "steps": [
            [
                "scaler",
                {"StandardScaler": None}
            ],
            [
                "svc",
                {"SVC": None}
            ]
        ]
        }
}
```

### Define a Scikit-Learn object from a dict.
Recreate the original pipeline.
```python
import skdict

skyaml.load(d)
```

## Why should I use this?
This package aims to make it easier to export pipelines to YAML or JSON files.

The goal is to decouple the pipeline from the executing code, so the user can focus only on the pipeline itself.

It also make it easier to quickly switching in between pipelines, and log it as artifacts on experiment tracking tools (e.g. MLFlow). It works better alongside CLI applications.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License.

## Contact

[![Linkedin](https://img.shields.io/badge/-matheusccouto-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/matheusccouto/)](https://www.linkedin.com/in/matheusccouto/)
[![Gmail](https://img.shields.io/badge/-matheusccouto@gmail.com-006bed?style=flat-square&logo=Gmail&logoColor=white&link=mailto:matheusccouto@gmail.com)](mailto:matheusccouto@gmail.com)