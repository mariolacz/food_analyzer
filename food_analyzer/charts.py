import plotly.express as px
import streamlit as st

def plot_calories_chart(df):
    fig = px.bar(
        df.sort_values(by='Calories-kcl', ascending=False),
        x='FlavorVariant',
        y='Calories-kcl',
        color='FlavorVariant',
        title='Calories per Flavor Variant',
        labels={'Calories-kcl': 'Calories-kcl', 'FlavorVariant': 'FlavorVariant'}
    )
    fig.update_layout(xaxis_tickangle=-45, height=500)
    st.plotly_chart(fig)

def plot_sugar_chart(df):
    fig = px.bar(
        df.sort_values(by='Sugar-g', ascending=False),
        x='FlavorVariant',
        y='Sugar-g',
        color='FlavorVariant',
        title='Sugar per Flavor Variant',
        labels={'Sugar-g': 'Sugar-g', 'FlavorVariant': 'FlavorVariant'}
    )
    fig.update_layout(xaxis_tickangle=-45, height=500)
    st.plotly_chart(fig)

def plot_nutrient_comparison(df):
    nutrients = ['Protein-g', 'Fiber-g', 'SaturatedFat-g', 'MonounsaturatedFat-g', 'PolyunsaturatedFat-g']
    fig = px.bar(df, x='FlavorVariant', y=nutrients, barmode='group', title="Nutrient Comparison per Flavor Variant")
    st.plotly_chart(fig)

def plot_calories_per_100g(df):
    fig = px.bar(df, x='FlavorVariant', y='MQCalories100gm-kcl', color='FlavorVariant', title="Calories per 100g")
    st.plotly_chart(fig)
