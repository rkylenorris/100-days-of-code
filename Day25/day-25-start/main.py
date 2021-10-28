import pandas
import pandas as pd

# data = pd.read_csv('weather_data.csv')
# # print(data['temp'])
#
# # data_dict = data.to_dict()
# # print(data_dict)
# #
# # print(data['temp'].to_list())
# #
# # import statistics as st
# #
# # print(st.mean(data['temp'].to_list()))
#
# temps = data['temp']
# #
# max_temp = temps.max()
# #
# # print(max_temp)
#
# # print(data[data.temp == max_temp])
#
# # monday_temp = data[data.day == "Monday"].temp
# #
# # monday_f = (int(monday_temp) * 9/5) + 32
# #
# # print(monday_f)

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
grey_sql = data[data['Primary Fur Color'] == 'Gray']
red_sql = data[data['Primary Fur Color'] == 'Cinnamon']
black_sql = data[data['Primary Fur Color'] == 'Black']

data_dict = {
    "Fur Color": ['Gray', 'Cinnamon', 'Black'],
    "Count": [len(grey_sql), len(red_sql), len(black_sql)]
}

new_df = pandas.DataFrame(data_dict)
print(new_df)