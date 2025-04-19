import pandas as pd
import streamlit as st
import plotly.express as px

#loaded file from desktop
df = pd.read_csv('/Users/mariolaczajkowska/Desktop/BakedFoodNutritions.csv')


st.title("Food analyzer")

df = df.dropna(subset=['Food', 'FlavorVariant'])
product_type_counts = df.groupby('Food')['FlavorVariant'].nunique()
valid_foods = product_type_counts[product_type_counts >= 2].index
df = df[df['Food'].isin(valid_foods)]

food_types = df['Food'].unique()
selected_food = st.selectbox("Please select food type", sorted(food_types))


filtered_df = df[df['Food'] == selected_food]
product_types = filtered_df['ProductType'].unique()
selected_product_types = st.selectbox("Please select product type", sorted(product_types))

final_filtered_df = filtered_df[filtered_df['ProductType'] == selected_product_types]

min_cal, max_cal = st.slider("Calories range", int(df['Calories-kcl'].min()), int(df['Calories-kcl'].max()), (0,600))
final_filtered_df = final_filtered_df[(final_filtered_df['Calories-kcl'] >= min_cal) & (final_filtered_df['Calories-kcl'] <= max_cal)]

min_sugar, max_sugar = st.slider("Calories range", int(df['Sugar-g'].min()), int(df['Sugar-g'].max()), (0,600))

columns_to_show = ['Food', 'ProductType', 'FlavorVariant', 'Calories-kcl', 'Sugar-g', 'Protein-g']
st.dataframe(final_filtered_df[columns_to_show])

if not final_filtered_df.empty:
    fig = px.bar(
        final_filtered_df.sort_values(by='Calories-kcl', ascending=False),
        x='FlavorVariant',
        y='Calories-kcl',
        color='FlavorVariant',
        title='Calories per Flavor Variant',
        labels={'Calories-kcl': 'Calories-kcl', 'FlavorVariant': 'FlavorVariant'}
    )
    fig.update_layout(xaxis_tickangle=-45, height=500)
    st.plotly_chart(fig)
else:
    st.warning("No data available for the selected options.")

st.subheader("Suagr Chart")

if not final_filtered_df.empty:
    fig = px.bar(
        final_filtered_df.sort_values(by='Sugar-g', ascending=False),
        x='FlavorVariant',
        y='Sugar-g',
        color='FlavorVariant',
        title='Sugar per Flavor Variant',
        labels={'Sugar-g': 'Sugar-g', 'FlavorVariant': 'FlavorVariant'}
    )
    fig.update_layout(xaxis_tickangle=-45, height=500)
    st.plotly_chart(fig)
else:
    st.warning("No data available for the selected options.")

nutrients = ['Protein-g', 'Fiber-g', 'SaturatedFat-g', 'MonounsaturatedFat-g', 'PolyunsaturatedFat-g']
st.subheader("Nutrient Comparison per Flavor Variant")
fig = px.bar(final_filtered_df, x='FlavorVariant', y=nutrients, barmode='group')
st.plotly_chart(fig)

st.subheader("Calories per 100g")
fig = px.bar(final_filtered_df, x='FlavorVariant', y='MQCalories100gm-kcl', color='FlavorVariant')
st.plotly_chart(fig)