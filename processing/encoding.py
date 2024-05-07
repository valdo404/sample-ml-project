from category_encoders import (
    BinaryEncoder, OrdinalEncoder, OneHotEncoder, HashingEncoder
)
from sklearn.compose import ColumnTransformer

import numpy as np
import pandas as pd
from processing import detection

# Here the idea is to encode categorical variables and list variables for a correlation analysis job
# Hence the choosed encoders are not depending on any target variable.

encoder_list = [
    ('test', HashingEncoder(), ['test']),

]

multi_labelled_encoder_list = [
    ('test', HashingEncoder(n_components=4), ['test']),
   ]

def encode_categorical(df, category_like_columns):
    preprocessor = ColumnTransformer(transformers=encoder_list, remainder='drop')
    transformed_data = preprocessor.fit_transform(df)

    if hasattr(preprocessor, 'get_feature_names_out'):
        transformed_columns = preprocessor.get_feature_names_out()
    else:
        # Fallback or manual naming strategy for older versions
        transformed_columns = ['column_' + str(i) for i in range(transformed_data.shape[1])]

    return pd.DataFrame(transformed_data, columns=transformed_columns, index=df.index)

def encode_list_like(only_lists_df, list_like_columns):

    for column in list_like_columns:
        transform_list_column(only_lists_df, only_lists_df, column)
        only_lists_df.drop(columns=[column], inplace=True)

    only_lists_preprocessor = ColumnTransformer(transformers=multi_labelled_encoder_list, remainder='drop')
    only_lists_transformed_data = only_lists_preprocessor.fit_transform(only_lists_df)

    if hasattr(only_lists_preprocessor, 'get_feature_names_out'):
        only_lists_transformed_columns = only_lists_preprocessor.get_feature_names_out()
    else:
        only_lists_transformed_columns = ['column_' + str(i) for i in range(only_lists_transformed_data.shape[1])]

    return pd.DataFrame(only_lists_transformed_data, columns=only_lists_transformed_columns, index=only_lists_df.index)


def one_hot_encode_list_column(df, column_name):
    new_columns_data = {}
    unique_tags = set(tag for sublist in df[column_name].dropna() for tag in sublist if sublist is not None)

    for tag in unique_tags:
        new_column_name = f'{column_name}_{tag}'
        new_columns_data[new_column_name] = df[column_name].apply(lambda x: 1 if isinstance(x, list) and tag in x else 0)

    return pd.DataFrame(new_columns_data, index=df.index)

def transform_list_column(transformed_df, df, column_name):
    string_column_name = f'{column_name}_joined'
    transformed_df.loc[:, string_column_name] = df[column_name].apply(lambda x: ':'.join(x) if detection.is_list(x) else '')
