# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zoish', 'zoish.feature_selectors', 'zoish.notebooks', 'zoish.utils']

package_data = \
{'': ['*']}

install_requires = \
['catboost>=1.0.6,<2.0.0',
 'click>=8.1.3,<9.0.0',
 'fasttreeshap>=0.1.2,<0.2.0',
 'feature-engine>=1.4.1,<2.0.0',
 'imblearn>=0.0,<0.1',
 'lightgbm>=3.3.2,<4.0.0',
 'matplotlib>=3.5.2,<4.0.0',
 'numba>=0.55.2,<0.56.0',
 'numpy<1.55.0',
 'optuna>=2.10.1,<3.0.0',
 'pandas>=1.4.3,<2.0.0',
 'pip-licenses>=3.5.4,<4.0.0',
 'scikit-learn>=1.1.1,<2.0.0',
 'scipy>=1.8.1,<2.0.0',
 'shap>=0.41.0,<0.42.0',
 'xgboost>=1.6.1,<2.0.0']

setup_kwargs = {
    'name': 'zoish',
    'version': '1.55.0',
    'description': 'This project uses shapely values for selecting Top n features compatible with scikit learn pipeline',
    'long_description': '# Zoish\n\nZoish is a package built to use [SHAP](https://arxiv.org/abs/1705.07874) (SHapley Additive exPlanation)  for a \nbetter feature selection. It is compatible with [scikit-learn](https://scikit-learn.org) pipeline . This package  uses [FastTreeSHAP](https://arxiv.org/abs/2109.09847) while calcualtion shap values. \n\n\n## Introduction\n\nZoish has a class named ScallyShapFeatureSelector that can receive various parameters. From a tree-based estimator class to its tunning parameters and from Grid search, Random Search, or Optuna to their parameters. X, y, will be split to train and validation set, and then optimization will estimate optimal related parameters.\n\n After that, the best subset of features  with higher shap values will be returned. This subset can be used as the next steps of the Sklearn pipeline. \n\n\n## Installation\n\nZoish package is available on PyPI and can be installed with pip:\n\n```sh\npip install zoish\n```\n\n\n## Supported estimators\n\n- XGBRegressor  [XGBoost](https://github.com/dmlc/xgboost)\n- XGBClassifier [XGBoost](https://github.com/dmlc/xgboost)\n- RandomForestClassifier \n- RandomForestRegressor \n- CatBoostClassifier \n- CatBoostRegressor \n- BalancedRandomForestClassifier \n- LGBMClassifier [LightGBM](https://github.com/microsoft/LightGBM)\n- LGBMRegressor [LightGBM](https://github.com/microsoft/LightGBM)\n\n## Usage\n\n- Find features using specific tree-based models with the highest shap values after hyper-parameter optimization\n- Plot the shap summary plot for selected features\n- Return a sorted two-column Pandas data frame with a list of features in one column and shap values in another. \n\n\n## Notebooks\n\n\n\n## License\nLicensed under the [BSD 2-Clause](https://opensource.org/licenses/BSD-2-Clause) License.',
    'author': 'drhosseinjavedani',
    'author_email': 'h.javedani@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/drhosseinjavedani/zoish',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
