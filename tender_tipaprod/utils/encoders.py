import pandas as pd
from sklearn.preprocessing import LabelEncoder
class CategoricalEncoding:
    def __init__(self, dataframe):
        self.data = dataframe

    def label_encoding(self, target_column):
        le = LabelEncoder()
        self.data[target_column] = le.fit_transform(self.data[target_column])
        return self.data

    def dummy_encoding(self, target_column):
        df_encoded = pd.get_dummies(self.data, columns=[target_column], prefix=[target_column], drop_first=True)
        return df_encoded

    def effect_encoding(self, target_column):
        unique_categories = self.data[target_column].unique()
        effect_encoded_values = {}
        for category in unique_categories:
            category_mean = self.data[self.data[target_column] == category]['target_variable'].mean()
            effect_encoded_values[category] = category_mean

        self.data[f'{target_column}_effect_encoded'] = self.data[target_column].map(effect_encoded_values)
        return self.data
    
    def one_hot(self, target_column):
        one_hot_encoded = pd.get_dummies(self.data[target_column], prefix=target_column)
        dataframe = pd.concat([self.data, one_hot_encoded], axis=1)
        return dataframe
    
    def update_data(self, df):
        self.data = df