import folium
import pandas 
import branca

data1 = pandas.read_csv("primaryschoolsg.csv")
Lat1 = list(data1["Latitude"])
Lon1 = list(data1["Longitude"])
Zone = list(data1["Zone"])
Name = list(data1["Name"])

map = folium.Map([1.393680,103.879010], zoom_start=100, tiles="Stamen Terrain")

fgS = folium.FeatureGroup(name="Primary Schools")

for Lt1,Ln1,Nm,Zn, in zip(Lat1,Lon1,Name,Zone):
    fgS.add_child(folium.Marker(location=[Lt1, Ln1], popup=Nm, color="White"))

fgP = folium.FeatureGroup(name="World Population")

fgP.add_child(folium.GeoJson(data=open("world.json",
 "r", encoding="utf-8-sig").read(), style_function=lambda x: {"fillColor":"Yellow" if x["properties"]["POP2005"]<10000000 
 else "orange" if 10000000<= x["properties"]["POP2005"] <50000000 else "red"}))

#accessing value [properties] of features key
#accessing value [POP2005] of properties key 
#style_function expects lambda function

colormap = branca.colormap.linear.YlOrRd_09.scale(0, 8500)
colormap = colormap.to_step(index=[0, 1000, 3000, 5000, 8500])
colormap.caption = 'World Population)'
colormap.add_to(map)

fgM = folium.FeatureGroup(name="MRT Stations")

data2 = pandas.read_csv("mrtsg.csv")
Lat2 = list(data2["Latitude"])
Lon2 = list(data2["Longitude"])
Stn_Name = list(data2["STN_NAME"])
Stn_No = list(data2["STN_NO"])
Color = list(data2["COLOR"])
New_Color = [c if c != "OTHERS" else "grey" for c in Color]

for Lt2,Ln2,Sna,Co,Sno in zip(Lat2,Lon2,Stn_Name,New_Color,Stn_No):
    fgM.add_child(folium.CircleMarker(location=[Lt2, Ln2], popup=Sna, radius = 10, 
    fill_color=Co, color= "black", fill_opacity = 1))

map.add_child(fgS)
map.add_child(fgP)
map.add_child(fgM)
map.add_child(folium.LayerControl())

map.save("Map1.html")
