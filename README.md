
# Car Price Prediction

This repository contains code for building a machine learning model to predict car prices based on various features. The dataset used for training and testing the model is fetched from a SQL Server database.Attached in this repo is an excel file containing the necessary data that can be uploaded to SQL server data base to execute the same code as indicated in the python notebook file.

## Contents

1. **Introduction**: 
   - This project aims to develop a predictive model for car prices using machine learning techniques.
   
2. **Setup**: 
   - Ensure you have all necessary packages installed, as mentioned in `requirements.txt`.
   - The dataset is fetched from a SQL Server database using PyODBC.
   
3. **Exploratory Data Analysis (EDA)**: 
   - The initial steps involve fetching data from the database and exploring its structure.
   - The Datasist library is used for data description and visualization.

4. **Feature Engineering**: 
   - Features are engineered to handle missing values, create new features, and perform one-hot encoding.
   - The goal is to prepare the data for modeling by selecting the most relevant features.

5. **Modeling**: 
   - Two models are trained: one with the present price feature and one without.
   - Random Forest Regressor is used for modeling car prices.
   - Model performance is evaluated using Root Mean Squared Error (RMSE).
   - The model with the best performance is saved using Joblib.

6. **Model Deployment**: 
   - The best-performing model is deployed to a web application using Streamlit.
   - Instructions for running the web app are provided in the `app/README.md` file.

## Instructions for Use

1. **Clone the Repository**: 
   ```
   git clone https://github.com/your_username/car-price-prediction.git
   ```

2. **Install Dependencies**: 
   ```
   pip install -r requirements.txt
   ```

3. **Run the Notebook**: 
   - Open and run the Jupyter Notebook `car_price_prediction.ipynb`.
   - Follow the step-by-step instructions to fetch data, explore, preprocess, model, and evaluate.

4. **Model Deployment**: 
   - The trained model is saved as `random_forest_carprice_model.pkl`.
   - Load the model for predictions in a production environment.
   - The model is also deployed to a web application using Streamlit. Instructions for running the web app are provided in the `app/README.md` file.

## Contributor
- Victor Emuchay

## Acknowledgments
- Mention any references, datasets, or libraries used.

