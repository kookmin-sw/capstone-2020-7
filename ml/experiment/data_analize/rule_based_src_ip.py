#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from tqdm.notebook import tqdm
import pandas as pd

def shift_8bit(train_df, test_df):
    for i in tqdm(range(len(train_df['sourceIP']))):
        train_df['sourceIP'][i] = train_df['sourceIP'][i] >> 8

    for i in tqdm(range(len(test_df['sourceIP']))):
        test_df['sourceIP'][i] = test_df['sourceIP'][i] >> 8
        
    return train_df, test_df

def ip_anal(train_df, test_df):

    # 학습 데이터(_train), 테스트 데이터(_test)
    x_train = train_df[['sourceIP']]
    y_train = 2 - train_df['analyResult']
    x_test = test_df[['sourceIP']]
    y_test = 2 - test_df['analyResult']

    # 학습 진행
    forest = RandomForestClassifier(n_estimators = 100, verbose = 1)
    forest.fit(x_train, y_train)

    # 예측
    y_pred = forest.predict(x_test)

    # 정확도 확인
    accuracy = metrics.accuracy_score(y_test, y_pred)
    
    return accuracy

def ip8_anal(train_df, test_df):

    # 학습 데이터(_train), 테스트 데이터(_test)
    x_train, x_test = shift_8bit(train_df, test_df)
    y_train = 2 - df_train['analyResult']
    y_test = 2 - df_test['analyResult']

    # 학습 진행
    forest = RandomForestClassifier(n_estimators = 100, verbose = 1)
    forest.fit(x_train, y_train)

    # 예측
    y_pred = forest.predict(x_test)

    # 정확도 확인
    accuracy = metrics.accuracy_score(y_test, y_pred)
    
    return accuracy

if __name__=="__main__":
    train_PATH = "TRAIN_PATH"
    test_PATH = "TEST_PATH"
    train_df = pd.read_csv(train_PATH, encoding='UTF-8', low_memory=False)
    test_df = pd.read_csv(test_PATH, encoding='UTF-8', low_memory=False)
    
    ip_anal = ip_anal(train_df, test_df)
    ip8_anal = ip8_anal(train_df, test_df)
    
    print(ip_anal, ip8_anal)


# In[ ]:




