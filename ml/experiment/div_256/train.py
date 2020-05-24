import pandas as pd
from div_preprocessing import *
from RedDNN import RedDNN
import numpy as np

from tensorflow.keras.metrics import Precision
from tensorflow.keras.metrics import Recall
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint


CKPT_SAVE_PATH = ""        # File_format : *.h5
TEMP_INPUT_DATA_PATH = ""


def run(ckpt, temp_path):
    CKPT_SAVE_PATH = ckpt
    TEMP_INPUT_DATA_PATH = temp_path

    print("Data Load")
    data = pd.read_pickle(TEMP_INPUT_DATA_PATH)
    print("Data Extract")
    X, y = extract(data)
    y = np.asarray(y, dtype=np.float32)
    print("Data PreProcessing")
    X = preprocessing_payload(X)
    X = np.reshape(X, (X.shape[0], X.shape[1], 1))
    print("Load Model")
    model = RedDNN()
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc', Precision(), Recall()])
    ear = EarlyStopping(monitor='loss', patience=4)
    ckpt = ModelCheckpoint(filepath=CKPT_SAVE_PATH, monitor='loss',
                           verbose=1, save_best_only=True)

    model.fit(
        {
            'now_pay': X,
        }, y,
        epochs=16, batch_size=256,
        verbose=1, callbacks=[ear, ckpt],
    )
    model.layers[-2].save_weights(CKPT_SAVE_PATH, save_format='h5')



if __name__=="__init__":
    ckpt_path = "SAVE_PATH"
    path = "DATA_PATH_TYPE_IS_PKL"
    run(ckpt=ckpt_path, temp_path=path)