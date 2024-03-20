
import streamlit as st
import joblib

#import pickle
#model =pickle.load(open('C:\\Users\\USER\\Desktop\\Machine_learning_end_to_end\\random_forest_carprice_model.pkl','rb'))  #if you are using pickle not joblib
model_path='C:\\Users\\USER\\Desktop\\Machine_learning_end_to_end\\random_forest_carprice_model1.pkl'
model = joblib.load(model_path)


def main():
    st.title("Car pricing Prediction Solution")
    

    # creating input Variables

    Year = st.number_input('Year', step=1, min_value=1990, max_value=2024)
    Present_Price = st.number_input('Present_Price', step=1)
    Age_of_Car = st.number_input('Age_of_Car', step=1)
    Kms = st.number_input('Kms_Driven', step=1)
    Owner = 1 if st.selectbox('Owner', ('First Owner', 'More Than One Previous Owners')) == 'First Owner' else 0
    Fuel_Type_Diesel = 1 if st.selectbox('Fuel_Type_Diesel', ('Yes', 'No')) == 'Yes' else 0
    Fuel_Type_Petrol = 1 if st.selectbox('Fuel_Type_Petrol', ('Yes', 'No')) == 'Yes' else 0
    Seller_Type_Individual = 1 if st.selectbox('Seller_Type_Individual', ('Yes', 'No')) == 'Yes' else 0
    Transmission_Manual = 1 if st.selectbox('Transmission_Manual', ('Manual', 'Automatic')) == 'Manual' else 0


    # prediction
    if st.button('Predict'):
        makeprediction=model.predict([[Year,Present_Price,Age_of_Car,Kms,Owner,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Manual]])
        output=round(makeprediction[0],2)
        st.success("You can sell your car for ${}".format(output))

if __name__=='__main__':
    
    main()
