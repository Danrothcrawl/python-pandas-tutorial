# print("Hello World")
# import pandas as pd

# data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
# print(data_frame)
# import pandas as pd
# ages = pd.Series([23,45,7,34,6,63,36,78,54,34])
# print(ages)
# import pandas as pd
# date_series = pd.date_range(start = '2021-05-01', end = '2021-05-12')
# print(date_series)
# import pandas as pd
# my_series = pd.Series([2,4,6,8,10])
# modified_series = my_series.apply(lambda x:x/2)
# print(modified_series)
# import pandas as pd
# data = [["Toyota", "Corolla", "Blue"], ["Ford", "K", "Yellow"], ["Porsche", "Cayenne", "White"]]
# df = pd.DataFrame(data, columns=["Brand", "Model", "Color"])
# print(df)
# import pandas as pd
# data = [
#     {
#         "brand": "Toyota",
#         "model": "Corolla",
#         "color": "Blue"
#     },
#     {
#         "brand": "Ford",
#         "model": "K",
#         "color": "Yellow"
#     },
#     {    
#         "brand": "Porsche",
#         "model": "Cayenne",
#         "color": "White"
#     },
#     {
#         "brand": "Tesla",
#         "model": "Model S",
#         "color": "Red"
#     }
# ]
# df = pd.DataFrame(data)
# print(df)
# import pandas as pd

# data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
# print(data_frame.iloc[133,6])
# import pandas as pd

# data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
# print(data_frame.head(3))
# import pandas as pd

# data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
# print(data_frame.tail(3))
# import pandas as pd

# data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
# print(data_frame[['Name', 'Type 1']][0:10])
# import pandas as pd

# data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
# print(data_frame.loc[data_frame['Attack'] > 80])
# import pandas as pd

# data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
# print(len(data_frame.loc[data_frame['Legendary'] == True]))
# import pandas as pd

# data_frame = pd.read_csv('.learn/assets/us_baby_names_right.csv')
# print(data_frame.head(5))
import pandas as pd

data_frame = pd.read_csv('.learn/assets/us_baby_names_right.csv')
del data_frame[data_frame.columns[0]]
print(data_frame.head(5))