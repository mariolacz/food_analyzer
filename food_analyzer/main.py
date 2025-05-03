import pandas as pd
import streamlit as st
from charts import plot_calories_chart, plot_sugar_chart, plot_nutrient_comparison, plot_calories_per_100g

st.title("Food analyzer")

# Load data
df = pd.read_csv('/Users/mariolaczajkowska/Desktop/BakedFoodNutritions.csv')
df = df.dropna(subset=['Food', 'FlavorVariant'])

# Filter: Only include food types with two and more flavor variants
product_type_counts = df.groupby('Food')['FlavorVariant'].nunique()
valid_foods = product_type_counts[product_type_counts >= 2].index
df = df[df['Food'].isin(valid_foods)]

# Food selection
food_types = df['Food'].unique()
selected_food = st.selectbox("Please select food type", sorted(food_types))

filtered_df = df[df['Food'] == selected_food]

# Product type selection
product_types = filtered_df['ProductType'].unique()
selected_product_types = st.selectbox("Please select product type", sorted(product_types))
final_filtered_df = filtered_df[filtered_df['ProductType'] == selected_product_types]

# Calories filter
min_cal, max_cal = st.slider("Calories range", int(df['Calories-kcl'].min()), int(df['Calories-kcl'].max()), (0, 600))
final_filtered_df = final_filtered_df[(final_filtered_df['Calories-kcl'] >= min_cal) & (final_filtered_df['Calories-kcl'] <= max_cal)]

# Sugar filter
min_sugar, max_sugar = st.slider("Sugar range", int(df['Sugar-g'].min()), int(df['Sugar-g'].max()), (0, 100))
final_filtered_df = final_filtered_df[(final_filtered_df['Sugar-g'] >= min_sugar) & (final_filtered_df['Sugar-g'] <= max_sugar)]

# Display data
columns_to_show = ['Food', 'ProductType', 'FlavorVariant', 'Calories-kcl', 'Sugar-g', 'Protein-g']
st.dataframe(final_filtered_df[columns_to_show])

# Plot charts if data exists
if not final_filtered_df.empty:
    plot_calories_chart(final_filtered_df)
    st.subheader("Sugar Chart")
    plot_sugar_chart(final_filtered_df)
    st.subheader("Nutrient Comparison per Flavor Variant")
    plot_nutrient_comparison(final_filtered_df)
    st.subheader("Calories per 100g")
    plot_calories_per_100g(final_filtered_df)
else:
    st.warning("No data available for the selected options.")
