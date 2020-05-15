import os
from os import path as op

import click
from .classifier import gen_workflow, run_workflow


@click.option("--csv", help="CSV file to use")
def main():
    clfs = [('sklearn.ensemble', 'ExtraTreesClassifier',
             {"n_estimators":100, "class_weight":'balanced'}),
            #('sklearn.svm', 'SVC', {"probability": True},
            # [{'kernel': ['rbf', 'linear'], 'C': [1, 10, 100, 1000]}]),
            #('sklearn.linear_model', 'LogisticRegressionCV',
            # {"solver":'liblinear', "penalty":'l1'}),
            ('sklearn.neural_network', 'MLPClassifier',
             {"alpha":1, "max_iter":1000}),
            #('sklearn.neighbors', 'KNeighborsClassifier', {},
            # [{'n_neighbors': [3, 5, 7, 9, 11, 13, 15, 17, 19],
            #   'weights': ['uniform','distance']}]),
            #('sklearn.tree', 'DecisionTreeClassifier', {"max_depth":5}),
            #('sklearn.ensemble', 'RandomForestClassifier', {"n_estimators": 100})),
            #('sklearn.ensemble', 'AdaBoostClassifier', {}),
            #('sklearn.naive_bayes', 'GaussianNB', {}})
            ]
    inputs = {"filename": os.path.abspath('breast_cancer.csv'),
              "x_indices": range(30), "target_vars": ('target',),
              "n_splits": 2, "test_size": 0.2,
              "clf_info": clfs,
              "permute": [True, False][-1:],
              "noshap": False,
              "nsamples": 100,
              "l1_reg": "aic"
              }
    n_procs = 1
    cache_dir = os.path.join(os.getcwd(), 'cache-wf')
    wf = gen_workflow(inputs, cache_dir=cache_dir)
    run_workflow(wf, n_procs)