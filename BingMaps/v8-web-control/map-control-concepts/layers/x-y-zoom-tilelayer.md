---
title: "X, Y, Zoom TileLayer | Microsoft Docs"
description: Provides a code example that shows how to display a tile layer that uses an X, Y, and Zoom tile URL schema.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: caea8f62-54e3-4509-a448-e63c3aec35e2
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# X, Y, Zoom TileLayer

[!INCLUDE [bing-maps-web-control-sdk-retirement](../../includes/bing-maps-web-control-sdk-retirement.md)]

This example shows how to display a tile layer that uses an X, Y and Zoom tile URL schema. The source of this tile layer is a weather radar overlay from the [Iowa Environmental Mesonet of Iowa State University](https://mesonet.agron.iastate.edu/ogc/).

```html
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <meta charset="utf-8" />
    <script type='text/javascript'
            src='https://www.bing.com/api/maps/mapcontrol?callback=GetMap'
            async defer></script>

    <script type='text/javascript'>
    var map;

    function GetMap() {
        map = new Microsoft.Maps.Map('#myMap', {
            credentials: 'You Bing Maps Key',
            center: new Microsoft.Maps.Location(40.75, -99.47),
            zoom: 4
        });

        //Weather radar tiles from Iowa Environmental Mesonet of Iowa State University
        var weatherTileLayer = new Microsoft.Maps.TileLayer({
            mercator: new Microsoft.Maps.TileSource({
                uriConstructor: 'https://mesonet.agron.iastate.edu/cache/tile.py/1.0.0/nexrad-n0q-900913/{zoom}/{x}/{y}.png'
            })
        });
        map.layers.insert(weatherTileLayer);
    }
    </script>
</head>
<body>
    <div id="myMap" style="position:relative;width:600px;height:400px;"></div>
</body>
</html>
```

Running this code in a browser will display a weather radar tile layer over top of the USA. 
 
![Screenshot of a Bing map that shows a weather radar over the physical map of the United States of America.](../../media/bmv8-tilelayerxyzoom.PNG)

[Try it now](https://www.bing.com/api/maps/sdk/mapcontrol/isdk#tileLayerPublicXYZoom+JS)
