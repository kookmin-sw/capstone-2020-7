import csv
import time

with open('test_data.csv', 'a', encoding='utf-8') as f:
        wr = csv.writer(f)
        wr.writerow(["first", "second", "third"])
for i in range(50, 100):
        with open('test_data.csv', 'a', encoding='utf-8') as f:
                wr = csv.writer(f)
                wr.writerow([i, i*3, i*10])
        time.sleep(3)
