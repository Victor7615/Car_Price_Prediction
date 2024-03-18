
from flask import Flask,request,jsonify
import pickle

app=Flask(__name__)
model=pickle.load(open('random_forest_carprice_model.pkl','rb'))

@app.route('/')
def home():
    return 'Welcome to Car pricing Solution API'

@app.route("/predict", methods=["GET"])
def predict():
    Year=request.args.get('Year')
    Age_of_Car=request.args.get('Age_of_Car')
    Kms=request.args.get('Kms_Driven')
    Owner=request.args.get('Owner')
    Fuel_Type_Diesel=request.args.get('Fuel_Type_Diesel')
    Fuel_Type_Petrol=request.args.get('Fuel_Type_Petrol')
    Seller_Type_Individual=request.args.get('Seller_Type_Individual')
    Transmission_Manual=request.args.get('Transmission_Manu')

    makeprediction=model.predict([[Year,Age_of_Car,Kms,Owner,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Manual]])

    return jsonify({'You can sell your car for':makeprediction})

if __name__=="__main__":
    app.run(debug=True)