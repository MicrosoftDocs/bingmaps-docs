---
title: "Polygons with Holes Example | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 02a8995d-3df2-4b5d-b150-d27314d64b99
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Polygons with Holes Example
The following code is an example that creates a complex polygon that has a hole cut out of it. 

``` 
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <meta charset="utf-8" />
	<script type='text/javascript'>
    function GetMap() {
        var map = new Microsoft.Maps.Map('#myMap', {});

        var center = map.getCenter();

        //Create array of locations to form a ring.
        var exteriorRing = [
            center,
            new Microsoft.Maps.Location(center.latitude - 0.5, center.longitude - 1),
            new Microsoft.Maps.Location(center.latitude - 0.5, center.longitude + 1),
            center
        ];

        //Create an array of locations that form a ring inside the exterior ring.
        var interiorRing = [
            new Microsoft.Maps.Location(center.latitude - 0.2, center.longitude),
            new Microsoft.Maps.Location(center.latitude - 0.4, center.longitude + 0.5),
            new Microsoft.Maps.Location(center.latitude - 0.4, center.longitude - 0.5),
            new Microsoft.Maps.Location(center.latitude - 0.2, center.longitude)
        ];

        //Create an array of rings.
        var rings = [exteriorRing, interiorRing];

        //Create a polygon
        var polygon = new Microsoft.Maps.Polygon(rings, {
            fillColor: 'rgba(0, 255, 0, 0.5)',
            strokeColor: 'red',
            strokeThickness: 2
        });

        //Add the polygon to map
        map.entities.push(polygon);
    }
    </script>
    <script type='text/javascript' src='http://www.bing.com/api/maps/mapcontrol?callback=GetMap&key=[YOUR_BING_MAPS_KEY]' async defer></script>
</head>
<body>
    <div id="myMap" style="position:relative;width:600px;height:400px;"></div>
</body>
</html>
```

Here is what this complex polygon would look like when zoomed out.

![Polygon with a Hole on a Map](..//media/bmv8-polygonwithholeexample.png)