import pandas as pd
import streamlit as st
import plotly.express as px

#loaded file from desktop
df = pd.read_csv('/Users/mariolaczajkowska/Desktop/BakedFoodNutritions.csv')


st.title("Food analyzer")

df = df.dropna(subset=['Food', 'ProductType'])

food_types = df['Food'].unique()
selected_FOOD = st.selectbox("Please select food type", sorted(food_types))

filtered_df = df[df['Food'] == selected_FOOD]

product_types = filtered_df['ProductType'].unique()
selected_product_types = st.selectbox("Please select product type", sorted(product_types))

final_filtered_df = filtered_df[filtered_df['ProductType'] == selected_product_types]

columns_to_show = ['Food', 'ProductType', 'FlavorVariant', 'Calories-kcl', 'Sugar-g', 'Protein-g']
st.dataframe(final_filtered_df[columns_to_show])

st.subheader("Calories Chart")

final_filtered_df['Calories-kcl'] = pd.to_numeric(final_filtered_df['Calories-kcl'], errors='coerce')

st.write("Final filtered data:", final_filtered_df[['FlavorVariant', 'Calories-kcl']])

if not final_filtered_df.empty:
    fig = px.bar(
        final_filtered_df.sort_values(by='Calories (kcal)', ascending=False),
        x='FlavorVariant',
        y='Calories-kcl',
        color='FlavorVariant',
        title='Calories per Flavor Variant',
        labels={'Calories (kcal)': 'Calories (kcal)', 'FlavorVariant': 'FlavorVariant'}
    )
    fig.update_layout(xaxis_tickangle=-45, height=500)
    st.plotly_chart(fig)
else:
    st.warning("No data available for the selected options.")
