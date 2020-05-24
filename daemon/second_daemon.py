#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

# 핸들러
def process_line(l):
  print(l)

with open('Realtime.csv', 'r') as fr:
  while True:
    line = fr.readline()
    if not line:
      time.sleep(1)
      continue
    process_line(line)
