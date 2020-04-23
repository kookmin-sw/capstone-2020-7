#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from tqdm.notebook import tqdm

def shift_8bit(train_df, test_df):
    for i in tqdm(range(len(train_df['sourceIP']))):
        train_df['sourceIP'][i] = train_df['sourceIP'][i] >> 8

    for i in tqdm(range(len(test_df['sourceIP']))):
        test_df['sourceIP'][i] = test_df['sourceIP'][i] >> 8
        
    return train_df, test_df
    

def rule_based(train_x, train_y, test_x, test_y, train_z, test_z):
    
    test_sets = []
    for x, y in zip(test_x, test_y):
        test_sets.append((x, y))

    test_sets = set(test_sets)

    db = {}
    for x, y, res in tqdm(zip(train_x, train_y, train_z)):
        temp = (x, y)
        if temp in test_sets:
            if temp not in db:
                db[temp] = [0,0]
            db[temp][res] += 1


    rule = {}
    for key in db:
        a2, a1 = db[key]
        if a2 > a1:
            rule[key] = 0
        else:
            rule[key] = 1

    answer = test_z
    wrong = 0
    correct = 0
    not_in = 0
    i = 0
    for ip, port in zip(test_x, test_y):
        temp = (ip, port)
        if temp in rule:
            if answer[i] == rule[temp]:
                correct += 1
            else:
                wrong += 1
        else:
            not_in += 1
        i+=1

    accuracy = correct/(wrong+correct)
    coverage = (wrong+correct)/(wrong+correct+not_in)
    
    return accuracy, coverage



if __name__=="__main__":
    train_PATH = "TRAIN_PATH"
    test_PATH = "TEST_PATH"
    train_df = pd.read_csv(train_PATH, encoding='UTF-8', low_memory=False)
    test_df = pd.read_csv(test_PATH, encoding='UTF-8', low_memory=False)
    
    train_src_ip8, test_src_ip8 = list(shift_8bit(train_df, test_df))
    train_src_ip = list(train_df['sourceIP'])
    test_src_ip = list(test_df['sourceIP'])
    train_src_port = list(train_df['sourcePort'])
    test_src_port = list(test_df['sourcePort'])
    train_src_packetSize = list(train_df['packetSize'])
    test_src_packetSize = list(test_df['packetSize'])
    train_anal = list(2-train_df['analyResult'])
    test_anal = list(2-train_df['analyResult'])

    rb_ip_port = rule_based(train_src_ip, train_src_port, test_src_ip, test_src_port, train_anal, test_anal)
    rb_ip8_port = rule_based(train_src_ip8, train_src_port, test_src_ip8, test_src_port, train_anal, test_anal)
    rb_ip_packetSize = rule_based(train_src_ip, train_src_packetSize, test_src_ip, test_src_packetSize, train_anal, test_anal)
    rb_ip8_packetSize = rule_based(train_src_ip8, train_src_packetSize, test_src_ip8, test_src_packetSize, train_anal, test_anal)
    
    print(rb_ip_port, rb_ip8_port, rb_ip_packetSize, rb_ip8_packetSize)


# In[ ]:




