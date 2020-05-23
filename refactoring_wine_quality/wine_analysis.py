import pandas as pd

# In [1]
# df = pd.read_csv('winequality-red.csv', sep=';')
# df.head()

# Out[1]
# 	fixed acidity	volatile acidity	citric acid	residual sugar	chlorides	free sulfur dioxide	total sulfur dioxide	density	pH	sulphates	alcohol	quality
# 0	7.4	0.70	0.00	1.9	0.076	11.0	34.0	0.9978	3.51	0.56	9.4	5
# 1	7.8	0.88	0.00	2.6	0.098	25.0	67.0	0.9968	3.20	0.68	9.8	5
# 2	7.8	0.76	0.04	2.3	0.092	15.0	54.0	0.9970	3.26	0.65	9.8	5
# 3	11.2	0.28	0.56	1.9	0.075	17.0	60.0	0.9980	3.16	0.58	9.8	6
# 4	7.4	0.70	0.00	1.9	0.076	11.0	34.0	0.9978	3.51	0.56	9.4

# refactored for modularity
def calculate_columns(data_file):
    df = pd.read_csv(data_file, sep=';')
    return df

calculate_columns('winequality-red.csv').head()

# median_alcohol = df.alcohol.median()
# for i, alcohol in enumerate(df.alcohol):
#     if alcohol >= median_alcohol:
#         df.loc[i, 'alcohol'] = 'high'
#     else:
#         df.loc[i, 'alcohol'] = 'low'
# df.groupby('alcohol').quality.mean()

# median_alcohol = df.alcohol.median()
# median_pH = df.pH.median()
# median_sugar = df.residual_sugar.median()
# median_citric_acid = df.citric_acid.median()
# def calculate_median(column_name, median_category):
#     for i, element in enumerate(df.column_name):
#         if element >= median_category:
#             df.loc[i, column_name] = 'high'
#         else:
#             df.loc[i, column_name] = 'low'
#     df.groupby(column_name).quality.mean()

# calculate_median("alcohol", median_alcohol)
# calculate_median("pH", median_pH)
# calculate_median("sugar", median_sugar)
# calculate_median("citric_acid", median_citric_acid)

def numeric_to_buckets(df, column_name):
    median = df[column_name].median()
    for i, val in enumerate(df[column_name]):
        if val >= median:
            df.loc[i, column_name] = 'high'
        else:
            df.loc[i, column_name] = 'low' 

for feature in df.columns[:-1]:
    numeric_to_buckets(df, feature)
    print(df.groupby(feature).quality.mean(), '\n')