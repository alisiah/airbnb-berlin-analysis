from sklearn.model_selection import train_test_split, cross_validate
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import root_mean_squared_error, mean_absolute_error, r2_score
from xgboost import XGBRegressor
import numpy as np


def train_models(X, y, feature_names=None):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    models = {
        'LinearRegression': LinearRegression(),
        'RandomForest': RandomForestRegressor(random_state=42),
        'GradientBoosting': GradientBoostingRegressor(random_state=42),
        'XGBoost': XGBRegressor(n_estimators=300
                                , max_depth=6
                                , learning_rate=0.1
                                , subsample=0.8
                                , colsample_bytree=0.8
                                , objective='reg:squarederror'
                                , random_state=42)
    }

    results = {}

    for name, model in models.items():
        model.fit(X_train, y_train)
        preds = model.predict(X_test)

        rmse = root_mean_squared_error(y_test, preds)   # Root Mean Squared Error (Standardabweichung)
        mae = mean_absolute_error(y_test, preds)        # Mean Absolute Error (Mittlere Absolute Fehler)
        r2 = r2_score(y_test, preds)                    # Coefficient of determination (Bestimmtheitsmaß)

        # Performs cross-validation:
        cv_results = cross_validate(model, X, y, scoring=['neg_root_mean_squared_error', 'neg_mean_absolute_error', 'r2'], cv=5)

        results[name] = {
            'model': model
            , 'RMSE': rmse
            , 'MAE': mae
            , 'R2': r2
            # Average RMSE across all cross-validation folds:
            , 'CV_RMSE': -np.mean(cv_results['test_neg_root_mean_squared_error'])
            , 'CV_MAE': -np.mean(cv_results['test_neg_mean_absolute_error'])
            , 'CV_R2': np.mean(cv_results['test_r2'])
        }

    return results

