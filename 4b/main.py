import numpy as np
import pandas as pd
from time import time
from IPython.display import display
import matplotlib.pyplot as plt
import time
import xgboost as xgb
from sklearn.model_selection import train_test_split
from xgboost.sklearn import XGBRegressor


def fill_missing(store):
    store = store.fillna({'Promo2SinceWeek': 0, 'Promo2SinceYear': 0, 'CompetitionDistance': 0, 'PromoInterval': 0})
    store['CompetitionOpenSinceMonth'] = store['CompetitionOpenSinceMonth'].fillna(
        store['CompetitionOpenSinceMonth'].median())
    store['CompetitionOpenSinceYear'] = store['CompetitionOpenSinceYear'].fillna(
        store['CompetitionOpenSinceYear'].median())
    return store


def trans_date(test_new):
    test_new['Year'] = test_new.Date.apply(lambda x: x.split('-')[0])
    test_new['Year'] = test_new['Year'].astype(float)
    test_new['Month'] = test_new.Date.apply(lambda x: x.split('-')[1])
    test_new['Month'] = test_new['Month'].astype(float)
    test_new['Day'] = test_new.Date.apply(lambda x: x.split('-')[2])
    test_new['Day'] = test_new['Day'].astype(float)
    return test_new


def trans_str(test_new):
    mappings = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    test_new.StoreType.replace(mappings, inplace=True)
    test_new.Assortment.replace(mappings, inplace=True)
    test_new.StateHoliday.replace(mappings, inplace=True)
    return test_new


def new_f(test_new):
    # 构建字典
    month2str = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sept', 10: 'Oct',
                 11: 'Nov', 12: 'Dec'}
    test_new['monthStr'] = test_new.Month.map(month2str)  # 将数字映射为月份
    test_new.loc[test_new.PromoInterval == 0, 'PromoInterval'] = ''  # 缺失值的字符串转换
    test_new['IsPromoMonth'] = 0  # 创建一新列
    for interval in test_new.PromoInterval.unique():
        if interval != '':
            for month in interval.split(','):
                test_new.loc[(test_new.monthStr == month) & (test_new.PromoInterval == interval), 'IsPromoMonth'] = 1

    test_new['CompetitionOpen'] = 12 * (test_new.Year - test_new.CompetitionOpenSinceYear) + (
            test_new.Month - test_new.CompetitionOpenSinceMonth)
    test_new['CompetitionOpen'] = test_new.CompetitionOpen.apply(lambda x: x if x > 0 else 0)
    return test_new


def drop_f(test_new):
    test_new_final = test_new.drop(
        ['Id', 'IsPromoMonth', 'Date', 'Promo2', 'Promo2SinceWeek', 'Promo2SinceYear', 'PromoInterval', 'monthStr',
         'CompetitionOpenSinceMonth', 'CompetitionOpenSinceYear', 'Open'], axis=1)
    return test_new_final


def turn_to_float(test_new_final):
    test_new_final = test_new_final.astype(float)


def preprocess(df, merge_df):
    df = fill_missing(df)
    merge_df = trans_date(merge_df)
    merge_df = trans_str(merge_df)
    merge_df = new_f(merge_df)
    merge_df_final = drop_f(merge_df)
    test_new_final = merge_df_final.astype(float)
    merge_df_final = turn_to_float(merge_df)
    return merge_df, merge_df_final


def split_data(df):
    features = df.drop(['Sales'], axis=1)
    Sales = df['Sales']

    from sklearn.model_selection import train_test_split
    # 将数据切分成训练集和测试集
    x_train, x_test, y_train, y_test = train_test_split(features, Sales, test_size=0.2, random_state=0)
    return x_train, x_test, y_train, y_test


def rmspe(y, yhat):
    return np.sqrt(np.mean((yhat / y - 1) ** 2))


def train(x_train, x_test, y_train, y_test, test_new, test_new_final):
    Model_1 = XGBRegressor(learning_rate=0.1, n_estimators=400, max_depth=8)
    start = time.clock()
    Model_1.fit(x_train.values, y_train.values, eval_set=[(x_test.values, y_test.values)])
    # eval_set 是验证集
    end = time.clock()
    print('Model_1 Running time: %s Seconds' % (end - start))

    y_pred = Model_1.predict(x_test.values)
    error = rmspe(y_test, y_pred)
    print("accuarcy: %.2f%%" % (error * 100.0))

    print("Make predictions on the test set")
    Test_Pred = Model_1.predict(test_new_final.values)

    result = pd.DataFrame({"Id": test_new['Id'], 'Sales': np.expm1(Test_Pred)})
    # 由于之前我们对Sales数据进行了log（x+1）运算，所以这里要进行反运算
    result.to_csv("Rossmann_submission_Model_1.csv", index=False)


def main():
    store = pd.read_csv("./rossmann-store-sales/store.csv")
    sample = pd.read_csv("./rossmann-store-sales/sample_submission.csv")
    test = pd.read_csv("./rossmann-store-sales/test.csv")
    train = pd.read_csv("./rossmann-store-sales/train.csv")
    test_new, test_new_final = pd.merge(test, store, on='Store')
    train_new, train_new_final = pd.merge(train, store, on='Store')
    x_train, x_test, y_train, y_test = split_data(train_new_final)
    train(x_train, x_test, y_train, y_test, test_new, test_new_final)


if __name__ == "__main__":
    main()
