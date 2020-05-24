from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

MAX_LEN = 1600

def preprocessing_payload(payloads, max_len=MAX_LEN):
    tmp = []
    for payload in payloads:
        byte_payload = []
        for i in range(0, len(payload), 2):
            byte_payload.append(int(payload[i:i + 2], 16))
        tmp.append(byte_payload)
    tmp = pad_sequences(tmp, maxlen=max_len, padding='post', truncating='post', value=256)
    tmp2 = []
    for data in tmp:
        tmp2.append(data/256)

    return np.array(tmp2)


def extract(data):
    temp_payload = []
    temp_y = []
    for value in data.values():
        for j in range(len(value)):
            temp_payload.append(value[j][0])
            temp_y.append(2 - value[j][3])
    return temp_payload, temp_y