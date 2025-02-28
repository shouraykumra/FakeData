# -*- coding: utf-8 -*-
"""farsante.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RKLZEInPtj3JZK8nW-wEMZvZU2Cf4J8Q
"""

# Commented out IPython magic to ensure Python compatibility.
# %%capture
# !pip install farsante

!pip install faker

!pip install --upgrade dask

import farsante

df = farsante.quick_pandas_df(['first_name', 'last_name'], 3)
print(df)

help(farsante.pandas_df)

# Commented out IPython magic to ensure Python compatibility.
# %%time
# 
# import farsante
# from mimesis import Person, Address, Datetime
# 
# person = Person()
# address = Address()
# datetime = Datetime()
# # Generate a pandas DataFrame with Farsante
# df = farsante.pandas_df([person.full_name, person.email, address.city, address.state, datetime.datetime, datetime.week_date], 5010)
# df.to_csv('./fake_data.csv', index=False)
# 
# # Print generated DataFrame
# display(df)
#

# Commented out IPython magic to ensure Python compatibility.
# %%time
# 
# import pandas as pd
# from faker import Faker
# import random
# from datetime import datetime, timedelta
# 
# # Create an instance of Faker
# fake = Faker()
# 
# # Generate data for the DataFrame using Faker
# data = {
#     "full_name": [fake.name() for _ in range(3)],
#     "email": [fake.email() for _ in range(3)],
#     "city": [fake.city() for _ in range(3)],
#     "state": [fake.state_abbr() for _ in range(3)],
#     "datetime": [datetime.now() - timedelta(days=random.randint(0, 10)) for _ in range(3)],
# }
# 
# # Convert to DataFrame
# df_faker = pd.DataFrame(data)
# df_faker.to_csv('./fake_data_faker.csv', index=False)
# 
# # Print generated DataFrame
# print(df_faker)
#

