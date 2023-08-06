

Banking Project
===============
This is the banking project contains models on customer chrun, revenue prediction, and more. For queries contact apurv@shorthillstech.com.

Installing
============

.. code-block:: bash

    pip install pybanking

Usage
=====

.. code-block:: bash

    >>> from pybanking.example import custom_sklearn
    >>> custom_sklearn.get_sklearn_version()
    '0.24.2'

.. code-block:: bash

    >>> from pybanking.churn_prediction import model_churn
    >>> df = model_churn.get_data()
    >>> model = model_churn.pretrained("Logistic_Regression")
    >>> X, y = model_churn.preprocess_inputs(df)
    >>> model_churn.predict(X, model)