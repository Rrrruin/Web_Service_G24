import main
import pandas as pd
import numpy as np
from IPython.display import display



def test_fill_missing():
    df = pd.read_csv("./rossmann-store-sales/store.csv")
    df = main.fill_missing(df)
    column_list = df.columns.values.tolist()
    count = 0
    for i in column_list:
        count += df[i].isna().sum()
    assert count == 0


def test_trans_date():
    store = pd.read_csv("./rossmann-store-sales/store.csv")
    test = pd.read_csv("./rossmann-store-sales/test.csv")
    test_new = pd.merge(test, store, on='Store')
    print(test_new.columns)
    test_new = main.trans_date(test_new)
    Y_lenth = len(test_new['Year'])
    M_lenth = len(test_new['Month'])
    D_lenth = len(test_new['Day'])
    assert Y_lenth == M_lenth == D_lenth == len(test_new)

def test_trans_str():
    store = pd.read_csv("./rossmann-store-sales/store.csv")
    test = pd.read_csv("./rossmann-store-sales/test.csv")
    test_new = pd.merge(test, store, on='Store')
    test_new = main.trans_str(test_new)
    assert isinstance(test_new['StoreType'][1],np.int64) == True


def test_new_f():
    store = pd.read_csv("./rossmann-store-sales/store.csv")
    test = pd.read_csv("./rossmann-store-sales/test.csv")
    store = main.fill_missing(store)
    test_new = pd.merge(test, store, on='Store')
    test_new = main.trans_date(test_new)
    test_new = main.trans_str(test_new)
    test_new = main.new_f(test_new)
    assert 'CompetitionOpen' in test_new.columns