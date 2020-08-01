import folium
import json
import os


overlay = os.path.join('data', 'overlay.json')

m = folium.Map(
    location=[41.377491, 64.585258],
    zoom_start=6,
    tiles='CartoDB dark_matter'
)

folium.GeoJson(overlay, name='xarita').add_to(m)
m.save('index.html')
