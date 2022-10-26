#Maya Tabbah
#maya.tabbah40@myhunter.cuny.edu
#March 29, 2022

import pandas as pd
import folium

in1 = input("Enter a csv file: ")
out1 = input("Enter the output file") 
file = pd.read_csv(in1)

mapCUNY = folium.Map(location=[40.75, -74.125], zoom_start=10)

for index,row in file.iterrows():
    lat = row["LATITUDE"]
    lon = row["LONGITUDE"]
    name = row["TIME"]
    newMarker = folium.Marker([lat, lon], popup=name, tiles="Cartodb Positron")
    newMarker.add_to(mapCUNY)


mapCUNY.save(outfile = out1)

