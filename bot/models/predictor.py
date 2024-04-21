
import pmdarima as pm
from pmdarima import model_selection

from db_imp import df

LAST_DATE = df.columns[3].date()


def predict(station: str, df, time_left: int, time_right=0):
    """
    Use this method to predict human flow in one day (put 1 time difference) or in time interval (put 2 time differences)

    :param station: name of station
    :param df: data frame
    :param time_left: difference between today and feature predicted day
    :param time_left: difference between today and last feature predicted day (time left became first date of prediction)
    :return: list of predicted humans flows in interval between time_left and time_right
    """
    if time_right == 0:
        time_right = time_left
    X_train = df.loc[df['Станция'] == station].to_numpy()[0][3:][::-1]
    arima_model = pm.auto_arima(
        X_train,
        start_p=0, start_q=0,
        max_p=5, max_q=5,
        seasonal=True,
        m=7,
        d=None,
        D=1,
        trace=False,
        error_action='ignore',
        suppress_warnings=True,
        stepwise=True
    )
    y_pred = arima_model.predict(n_periods=time_right, alpha=0.05)
    ans = [int(i) for i in y_pred[time_left-1:time_right]]
    return ans


