---
title: "Animated Weather Radar Map | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: ed0d6a6f-3ddf-460d-a578-08cba9e7f492
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms:service: "bing-maps"
---
# Animated Weather Radar Map
This example uses the [AnimatedTileLayer](../v8-web-control/animatedtilelayer-class.md) to animate through an array of tile layers. For this example the weather radar tile service from the [Iowa Environmental Mesonet of Iowa State University](http://www.mesonet.agron.iastate.edu/ogc/) and animates it. This service provides radar images for the last 50 minutes over the USA broken up into 5 minute increments.

```
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <meta charset="utf-8" />
	<script type='text/javascript'>
    var map, animatedLayer;

    //Weather tile url from Iowa Environmental Mesonet (IEM): http://mesonet.agron.iastate.edu/ogc/
    var urlTemplate = 'http://mesonet.agron.iastate.edu/cache/tile.py/1.0.0/nexrad-n0q-{timestamp}/{zoom}/{x}/{y}.png';

    //The time stamps values for the IEM service for the last 50 minutes broken up into 5 minute increments.
    var timestamps = ['900913-m50m', '900913-m45m', '900913-m40m', '900913-m35m', '900913-m30m', '900913-m25m', '900913-m20m', '900913-m15m', '900913-m10m', '900913-m05m', '900913'];

    function GetMap()
    {
        map = new Microsoft.Maps.Map('#myMap', {
            credentials: 'Your Bing Maps Key',
            center: new Microsoft.Maps.Location(39, -92),
            zoom: 5
        });
        
        var tileSources = [];

        //Create a tile source for each time stamp.
        for (var i = 0; i < timestamps.length; i++) {
            var tileSource = new Microsoft.Maps.TileSource({
                uriConstructor: urlTemplate.replace('{timestamp}', timestamps[i])
            });
            tileSources.push(tileSource);
        }

        //Create the animated tile layer and add it to the map.
        animatedLayer = new Microsoft.Maps.AnimatedTileLayer({
            mercator: tileSources,
            frameRate: 500
        });
        map.layers.insert(animatedLayer);
    }
    </script>
    <script type='text/javascript' src='http://www.bing.com/api/maps/mapcontrol?callback=GetMap' async defer></script>
</head>
<body>
    <div id="myMap" style="position:relative;width:600px;height:400px;"></div>
</body>
</html>
```

If you run this code you will briefly see a loading message on the map which is pre-loading the map tiles in the current map view for the animation. Once this message disappears the animation will begin and smoothly transition between each tile layer. If you pan or zoom the map the loading screen will appear again as new map tiles are preloaded for the new map view.

![BMV8_AnimatedWeatherRadar](../v8-web-control/media/bmv8-animatedweatherradar.PNG)

[Try it now](http://www.bing.com/api/maps/mapcontrol/isdk#weatherRadarMap+JS)