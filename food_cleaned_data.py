import pandas as pd

#loaded file from desktop
df = pd.read_csv('/Users/mariolaczajkowska/Desktop/BakedFoodNutritions.csv')

#df.info() #data type
#df.describe() # data statistic
#df.isna().sum() # sum missing values in each column

df.rename(columns={
    'Food': 'FOOD',
    'ProductType' : 'PRODUCT_TYPE',
    'Calories-kcl' : 'CALORIES',
    'Protein-g': 'PROTEIN',
    'Sugar-g': 'SUGAR',
    'MeasureType': 'MEASURE_TYPE',
    'MeasureQuantity': 'MEASURE_QUANTITY'

}, inplace = True)

df.to_csv('downloads/Food_data_cleaned', index = False) 



