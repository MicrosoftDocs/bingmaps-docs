---
title: "Render GeoJSON as Heat Map | Microsoft Docs"
description: Provides a code example that loads earthquake data from the United States geological survey and displays the data as a heatmap layer.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: bd171a06-3473-4621-be3f-4bfec1e6d9dd
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Render GeoJSON as Heat Map

[!INCLUDE [bing-maps-web-control-sdk-retirement](../../../includes/bing-maps-web-control-sdk-retirement.md)]

This code sample loads in earthquake data for the last 30 days from the United States Geological Survey (USGS) and displays them as a heatmap layer. The USGS data makes a number of earthquake data feeds available in GeoJSON format on their website [here](https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php). 

```html
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <meta charset="utf-8" />
	<script type='text/javascript'>
    var usgsEarthquakeUrl = ' http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson';

    function GetMap() {
        var map = new Microsoft.Maps.Map('#myMap', {
            credentials: ‘Your Bing Maps Key’,
            center: new Microsoft.Maps.Location(40, -120),
            zoom: 2
        });

        //Load the GeoJSON and HeatMap modules.
        Microsoft.Maps.loadModule(['Microsoft.Maps.GeoJson', 'Microsoft.Maps.HeatMap'], function () {
            Microsoft.Maps.GeoJson.readFromUrl(usgsEarthquakeUrl, function (shapes) {
                var heatmap = new Microsoft.Maps.HeatMapLayer(shapes, { radius: 5 });
                map.layers.insert(heatmap);
            });
        });
    }
    </script>
    <script type='text/javascript' src='https://www.bing.com/api/maps/mapcontrol?callback=GetMap' async defer></script>
</head>
<body>
    <div id="myMap" style="position:relative;width:600px;height:400px;"></div>
</body>
</html>
```

Here is what this heat map looks like over the Pacific Ocean which is surrounded by the [Ring of Fire](https://en.wikipedia.org/wiki/Ring_of_Fire), an area where a large number of earthquakes and volcanic eruptions occur. 

![Screenshot of a Bing Map showing the Pacific Ocean with the earthquake data loaded as a heat map over it.](../../media/bmv8-ringoffireexample-map.png)

[Try it now](https://www.bing.com/api/maps/sdk/mapcontrol/isdk#heatMapFromGeoJson+JS)