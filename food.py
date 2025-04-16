import pandas as pd
import streamlit as st

#loaded file from desktop
df = pd.read_csv('/Users/mariolaczajkowska/Desktop/BakedFoodNutritions.csv')

df.info() #data type
df.describe() # data statistic
df.isna().sum() # sum missing values in each column

st.tictle("Food analyzer")

df = df.dropna(subset=['Food', 'ProductType'])

food_types = df['Food'].unique()
selected_food = st.selectbox("Please select food type", sorted(food_types))

filtered_df = df[df['Food'] == selected_food]

product_types = filtered_df['ProductType'].unique()
selected_product_types = st.selectbox("Please select product type", sorted(product_types))

final_filtered_df = filtered_df[filtered_df['ProductType'] == selected_product_types]

columns_to_show = ['Food', 'ProductType', 'FlavorVariant', 'Calories-kcl', 'Protein-g', 'MQCalories100gm-kcl']
st.dataframe(filtered_df[columns_to_show])