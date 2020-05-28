#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import csv
import re

import pandas as pd



data = pd.read_csv("./temp.csv")

for i in data.index:
  with open("./Realtime.csv", 'a') as fw:
    write_file = csv.writer(fw)
    write_file.writerow(list(data.loc[i]))
    time.sleep(0.25)


