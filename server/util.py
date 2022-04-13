import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None

def predict_rent(localityId,bathroom,floor,parking,property_size,type_bhk,maintenance):
    try:
        loc_index = __data_columns.index(localityId.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0]=bathroom
    x[1]=floor
    x[2]=parking
    x[3]=property_size
    x[4]=type_bhk
    x[5]=maintenance
    if loc_index>=0:
        x[loc_index] = 1

    return round(__model.predict([x])[0])


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __locations

    with open("C:\\Users\\Abhiram\\Desktop\\House_Rent_Prediction\\server\\artifacts\\columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[6:]

    global __model
    if __model is None:
        with open('C:\\Users\\Abhiram\\Desktop\\House_Rent_Prediction\\server\\artifacts\\rent_prediction.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(predict_rent('jubilee_hills',4,2,3,1000,3,1000))