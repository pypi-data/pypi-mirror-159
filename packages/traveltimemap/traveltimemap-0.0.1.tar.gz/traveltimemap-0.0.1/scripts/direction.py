from folium import plugins
import folium
import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
from geopy.distance import geodesic
from math import atan
import math
from tasks import *
from timestamp import *
from map import *

def map_arrow(df):
    """
    Get the dataframe with timestamps and return a map with permanent timestamps
    """
    # change data path here
    data = read_data(df)

    lat = list(data["LATITUDE"])
    long = list(data["LONGITUDE"])
    speed = list(data["Speed (MPH)"])
    date = list(data['LOCAL TIME'])
    date2 = list(data['LOCAL DATE'])

    feature = folium.FeatureGroup(name="Travel Time Map with Permanent Stamps")

    # change map center with the avg of the data
    map = folium.Map([data.Lat.mean(), data.Long.mean()], zoom_start=12)

    # #add arrow
    # la1 = lat[0]
    # lo1 = long[0]
    # la2 = lat[200]
    # lat2 = lat[-1]
    # lo2 = long[200]
    # lon2 = long[-1]
    # coordinates=[((la1), (lo1)),((la2), (lo2))]
    # latitude_difference = lat2-la1
    # longitude_difference=lon2-lo1

    # map = folium.Map([data.Lat.mean(), data.Long.mean()], zoom_start=12)
    # aline=folium.PolyLine(locations=coordinates,weight=2,color = 'blue')
    # map.add_child(aline)

    # folium.RegularPolygonMarker(location=(la2, lo2), fill_color='blue', number_of_sides=3, radius=10, rotation= math.degrees((latitude_difference/longitude_difference))).add_to(map)

    # add a marker for each point
    for lt, ln, s, t, dt in zip(lat, long, speed, date, date2):
        feature.add_child(
            folium.CircleMarker(location=[lt, ln], radius=.7, tooltip=folium.Tooltip(text=dt + ' ' + t),
                                fill_color=coloring(s), color=coloring(s), fill_opacity=0.7))

    # add arrow
    create_arrow(map)
    plugins.ScrollZoomToggler().add_to(map)

    # call for legend
    map = create_legend(map, 'Speed - MPH',
                        colors=['red', 'orange', 'yellow', '#60f250'],
                        labels=['0-20', '21-40', '41-55', '55+'])

    # time stats
    time_list = list(data['LOCAL TIME'])
    date_list = list(data['LOCAL DATE'])
    date_1 = date_list[0]
    time_1 = time_list[0]
    date_2 = date_list[-1]
    time_2 = time_list[-1]

    # str time
    tistr1 = str(date_1 + ' ' + time_1)
    tistr2 = str(date_2 + ' ' + time_2)

    # #time differences
    # if date_2 == date_1:
    #   timediff = time_2 - time_1
    # elif date_2 >= date_1:
    #   daydiff = date_2 - date_1
    #   timediff = (daydiff * 24) + (time_2 - time_1)
    # timediff = dt.datetime.strptime(str(time_1), '%H:%M:%S')

    t1 = datetime.strptime(str(tistr1), "%m/%d/%y %H:%M:%S")
    t2 = datetime.strptime(str(tistr2), "%m/%d/%y %H:%M:%S")
    timediff = t2 - t1
    difti = datetime.strptime(str(timediff), "%H:%M:%S")

    # print time
    stati1 = datetime.strptime(time_1, '%H:%M:%S').strftime('%I:%M %p')
    stati2 = datetime.strptime(time_2, '%H:%M:%S').strftime('%I:%M %p')
    str1 = 'Start: ' + date_1 + ' ' + stati1
    str2 = 'Stop: ' + date_2 + ' ' + stati2
    dur = 'Duration: ' + str(difti.minute) + ' min ' + str(difti.second) + ' sec'
    str3 = str1 + '<br/>' + str2 + '<br/>' + dur

    # mean speed
    speed = list(data['Speed (MPH)'])
    mean = round(sum(speed) / len(speed))
    finm = str(mean)
    mean = 'Average Speed: ' + finm + ' mph'

    # distance
    lat1 = lat[0]
    lon1 = long[0]
    lat2 = lat[-1]
    lon2 = long[-1]

    orig = (lat1, lon1)
    dis = (lat2, lon2)

    distance = 'Distance: ' + str(round(geodesic(orig, dis).miles)) + ' miles'

    m1 = mean + '<br/>' + distance

    # call for textbox
    map = create_textbox(map, 'Statistics', str3, m1)

    # display data points on the map and export
    map.add_child(feature)
    folium.LayerControl().add_to(map)

    return map