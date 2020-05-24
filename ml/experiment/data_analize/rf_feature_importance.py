#!/usr/bin/env python
# coding: utf-8

# In[4]:


from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import pandas as pd

def rf_feature(train_df, test_df):

    # 학습 데이터(_train), 테스트 데이터(_test)
    x_train = train_df[['sourceIP','sourcePort','destinationIP','destinationPort','packetSize']]
    y_train = 2 - train_df['analyResult']
    x_test = test_df[['sourceIP','sourcePort','destinationIP','destinationPort','packetSize']]
    y_test = 2 - test_df['analyResult']

    # 학습 진행
    forest = RandomForestClassifier(n_estimators = 100, verbose = 1)
    forest.fit(x_train, y_train)

    # 예측
    y_pred = forest.predict(x_test)

    # 정확도 확인
    accuracy = metrics.accuracy_score(y_test, y_pred)
    feature_imp = forest.feature_importances_
    
    return accuracy, feature_imp

if __name__=="__main__":
    train_PATH="TRAIN_PATH"
    test_PATH="TEST_PATH"
    train_df = pd.read_csv(train_PATH, encoding='UTF-8', low_memory=False)
    test_df = pd.read_csv(test_PATH, encoding='UTF-8', low_memory=False)
    
    acc_imp = rf_feature(train_df, test_df)
    print(acc_imp)


# In[ ]:




