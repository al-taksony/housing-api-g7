import joblib
import numpy as np

model = joblib.load('./model/model.pkl')
sc_x = joblib.load('./model/scaler_x.pkl')
sc_y = joblib.load('./model/scaler_y.pkl')

def predict_price(rooms: int) -> float:
    rooms_sc = sc_x.transform(np.array([[rooms]]))
    prediction_sc = model.predict(rooms_sc)
    prediction = sc_y.inverse_transform(prediction_sc) * 1000
    price = round(float(prediction_sc[0][0]), 2)
    return price