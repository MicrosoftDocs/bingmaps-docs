---
title: "Controlling an AnimatedTileLayer | Microsoft Docs"
description: Provides a code example that shows how to control an AnimatedTileLayer by using the play, pause, and stop functions.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 3d86830a-9e85-4fbe-8394-04c89e2c9e9c
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Controlling an AnimatedTileLayer

[!INCLUDE [bing-maps-web-control-sdk-retirement](../../../includes/bing-maps-web-control-sdk-retirement.md)]

This example shows how to control an [AnimatedTileLayer](../../map-control-api/animatedtilelayer-class.md) by using the `play`, `pause` and `stop` functions. For this example the weather radar tile service from the [Iowa Environmental Mesonet of Iowa State University](https://www.mesonet.agron.iastate.edu/ogc/) and animates it. This service provides radar images for the last 50 minutes over the USA broken up into 5 minute increments.

```html
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <meta charset="utf-8" />
	<script type='text/javascript'>
    var map, animatedLayer;

    //Weather tile url from Iowa Environmental Mesonet (IEM): https://mesonet.agron.iastate.edu/ogc/
    var urlTemplate = 'https://mesonet.agron.iastate.edu/cache/tile.py/1.0.0/nexrad-n0q-{timestamp}/{zoom}/{x}/{y}.png';

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
    <script type='text/javascript' src='https://www.bing.com/api/maps/mapcontrol?callback=GetMap' async defer></script>
</head>
<body>
    <div id="myMap" style="position:relative;width:600px;height:400px;"></div>
    <br/>
    <input type="button" value="Pause" onclick="animatedLayer.pause();"/>
    <input type="button" value="Play" onclick="animatedLayer.play();" />
    <input type="button" value="Stop" onclick="animatedLayer.stop();" />
</body>
</html>
```

Running this code displays a map with an animated weather radar. Below the map are buttons that can be used to play, pause, and stop the animation.

![Screenshot of a Bing map that shows weather radar data over the map with pause, play, and stop buttons below the map.](../../media/bmv8-animatedtilelayer-controls.PNG)