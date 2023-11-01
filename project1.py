import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the data for each category
mobile_data = pd.read_csv('mobile_data.csv')
grocery_data = pd.read_csv('grocery_data.csv')
clothing_data = pd.read_csv('cloth_data.csv')

# Initialize the Linear Regression model
lin_reg = LinearRegression()

def main():
    st.title('Price Prediction App')
    cat = st.selectbox("Select the product category", ['Mobile Phone', 'Grocery', 'Clothing'])
   
    if  cat == 'Mobile Phone':
        prod_id = mobile()
    elif cat == 'Grocery':
        prod_id = grocery()
    elif cat == 'Clothing':
        prod_id = clothing()
    
    if st.button('Predict'):
        # Predict for the given product ID
        price = predict_price(prod_id)
        st.write(f"The predicted price for the given product is {price:.2f}")

def predict_price(pro_id):
    # Retrieve the category and product ID
    category, product_id = pro_id.split('_')
    
    # Get the corresponding data for the category
    if category == 'Mobile Phone':
        data = mobile_data
    elif category == 'Grocery':
        data = grocery_data
    elif category == 'Clothing':
        data = clothing_data
    
    # Extract the features and target variable
    X = data.drop('price', axis=1)
    y = data['price']
    
    # Fit the Linear Regression model
    lin_reg.fit(X, y)
    
    # Create a DataFrame for the new product ID
    new_data = pd.DataFrame({data.columns[0]: [product_id]})
    
    # Predict the price for the new product ID
    price = lin_reg.predict(new_data)
    return price[0]

def mobile():
    st.subheader('Mobile Phone Category')
    brand = st.selectbox('Select the brand', mobile_data['brand'].unique())
    series = st.selectbox('Select the series', mobile_data['series'].unique())
    model_number = st.number_input('Enter the model number')
    prod_id = f'Mobile Phone_{brand}_{series}_{model_number}'
    return prod_id

def grocery():
    st.subheader('Grocery Category')
    grocery_type = st.selectbox('Select the type of grocery', grocery_data['type'].unique())
    quantity = st.number_input('Enter the quantity')
    prod_id = f'Grocery_{grocery_type}_{quantity}'
    return prod_id

def clothing():
    st.subheader('Clothing Category')
    category = st.selectbox('Select the category', clothing_data['category'].unique())
    clothing_type = st.selectbox('Select the type of clothing', clothing_data['type'].unique())
    size = st.number_input('Enter the size')
    prod_id = f'Clothing_{category}_{clothing_type}_{size}'
    return prod_id

if __name__ == '__main__':
    main()
