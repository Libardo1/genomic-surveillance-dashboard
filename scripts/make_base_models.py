"""
Makes all the models!

Trains a Random Forest Regressor on the protease data. Provides a baseline
model that's pickled to disk that all other models can be compared to.
"""

from sklearn.ensemble import RandomForestRegressor
from sklearn.externals import joblib
import custom_funcs as cf

drugs = ['FPV', 'ATV', 'IDV', 'LPV', 'NFV', 'SQV', 'TPV', 'DRV',]
protein = 'protease'

for drug in drugs:
    data, feat_cols = cf.get_cleaned_data(protein, drug)

    # Just checking:
    cf.test_data_integrity(data)

    ## Now, let's do data transformations.
    data_numeric = cf.to_numeric_rep(data, feat_cols, rep='mw')

    # Finally, split the data into a training set, and test set.
    X, Y, X_train, X_test, Y_train, Y_test = cf.to_train_test_split(data_numeric, feat_cols, drug, test_size=0.3)

    mdl = RandomForestRegressor(n_estimators=100)
    mdl.fit(X, Y)

    joblib.dump(mdl, '../models/base/{drug}/{drug}.pkl'.format(drug=drug))