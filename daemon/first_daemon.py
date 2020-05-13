#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import csv
import re

with open('Full_data.csv', 'r') as fr:
  read_file = csv.reader(fr)

  for line in read_file:
    line = ''.join(line)
    line = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', line)

    with open('Realtime.csv', 'a') as fw:
      write_file = csv.writer(fw)
      write_file.writerow([str(line)])
      time.sleep(0.25)

