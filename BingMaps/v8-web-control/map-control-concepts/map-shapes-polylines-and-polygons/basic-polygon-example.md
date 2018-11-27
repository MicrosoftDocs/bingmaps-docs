---
title: "Basic Polygon Example | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 54f25066-0add-43dc-a13b-284b01f364db
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Basic Polygon Example
The following code creates a simple polygon that has a red outline and a semi-transparent green fill color, and has a stroke thickness of 2 pixels. 

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

        //Create a polygon
        var polygon = new Microsoft.Maps.Polygon(exteriorRing, {
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

Here is what this polygon would look like when zoomed out.

![Polygon on a Map](..//media/bmv8-basicpushpinexample.png)