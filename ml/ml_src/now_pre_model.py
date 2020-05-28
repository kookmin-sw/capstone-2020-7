from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Embedding, Conv1D, GlobalAveragePooling1D, Input, Activation, \
    BatchNormalization, concatenate
import tensorflow as tf



def now_pre_RedDNN(max_len=1600, embedding_size=8):
    now_pay_input_layer = Input((max_len,), name='now_pay')
    embedding_layer = Embedding(257, embedding_size)(now_pay_input_layer)
    x = Conv1D(32, 3)(embedding_layer)
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    x = Dense(16)(x)
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    gap = GlobalAveragePooling1D()(x)
    x1 = Dense(16, activation='relu')(gap)

    pre_pay_input_layer = Input((max_len,), name='pre_pay')
    embedding_layer = Embedding(257, embedding_size)(pre_pay_input_layer)
    x = Conv1D(32, 3)(embedding_layer)
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    x = Dense(16)(x)
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    gap2 = GlobalAveragePooling1D()(x)
    x2 = Dense(16, activation='relu')(gap2)

    concatennated = concatenate([x1, x2], axis=-1)

    output_layer = Dense(1, activation='sigmoid')(concatennated)
    return Model(inputs=[now_pay_input_layer, pre_pay_input_layer], outputs=output_layer)


def preprocessing_payload(payloads, max_len=1600):
    from tensorflow.keras.preprocessing.sequence import pad_sequences
    import numpy as np
    tmp = []
    for payload in payloads:
        byte_payload = []
        for i in range(0, len(payload), 2):
            byte_payload.append(int(payload[i:i + 2], 16))
        tmp.append(byte_payload)
    tmp = pad_sequences(tmp, maxlen=max_len, padding='post', truncating='post', value=256)
    pre = []
    now = []
    pre.append(np.array([256] * max_len))
    now.append(tmp[0])
    for i in range(1, len(tmp)):
        pre.append(tmp[i-1])
        now.append(tmp[i])
    return np.array(pre), np.array(now)
