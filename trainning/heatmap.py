import pandas as pd
import folium
from folium import plugins

data_frame = pd.read_csv('train.csv')
# print(data_frame.head())

positions = data_frame[['Y', 'X']].values

m = folium.Map(location=[positions[0][0], positions[0][1]], zoom_start=15)
m.add_child(plugins.HeatMap(positions[:60000], radius=15))
m.save('map.html')
