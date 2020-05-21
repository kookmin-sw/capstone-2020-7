def data_loader(LOG_DATA_PATH = "./20181201000000.pkl"):
    import pandas as pd
    data = pd.DataFrame(pd.read_pickle(LOG_DATA_PATH))
    return data


def grouped_data(
    data, GROUPED_KEY = 'orgIDX', SORT_KEY = "atdate", 
    UNIQUE_ID = '_id'
):    # data type is pandas' DataFrame
    """
    input : data type of input is pandas's DataFrame
    output : data type of output is dict
    params : 
    - GROUPED_KEY : organize index, type is str, int
    - SORT_KEY    : datetime
    - UNIQUE_ID   : unique_value of logs
    """
    import pandas as pd
    g = data.groupby(GROUPED_KEY)
    g_keys = list(data[GROUPED_KEY].unique())
    output = {"payload":[], "id":[]}
    for key in g_keys:
        temp = g.get_group(key)
        temp = temp.sort_values(SORT_KEY)
        output['payload'].append(list(temp['payload']))
        output['id'].append(list(temp[UNIQUE_ID]))
    return output



def get_model(WEIGHT_PATH="./model_weight.h5"):
    from now_pre_model import now_pre_RedDNN
    model = now_pre_RedDNN()
    model.load_weights(WEIGHT_PATH)
    model.compile(loss='binary_crossentropy', optimizer='adam')
    return model


def preprocessing(data):
    from now_pre_model import preprocessing_payload
    output = {'pre':[], 'now':[], 'id':[]}
    for payloads, ids in zip(data['payload'], data['id']):
        pre, now = preprocessing_payload(payloads)
        output['pre'].extend(pre)
        output['now'].extend(now)
        output['id'].extend(ids)
    return output
