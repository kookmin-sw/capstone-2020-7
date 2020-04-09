from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Conv1D, GlobalAveragePooling1D, Input, Activation, \
    BatchNormalization



def RedDNN(max_len=1600):
    now_pay_input_layer = Input((max_len, 1), name='now_pay')
    x = Conv1D(32, 3)(now_pay_input_layer)
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    x = Conv1D(32, 3)(x)
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    x = GlobalAveragePooling1D()(x)
    x = Dense(16)(x)
    x = BatchNormalization()(x)
    x = Activation('relu')(x)

    output_layer = Dense(1, activation='sigmoid')(x)
    return Model(inputs=[now_pay_input_layer], outputs=output_layer)