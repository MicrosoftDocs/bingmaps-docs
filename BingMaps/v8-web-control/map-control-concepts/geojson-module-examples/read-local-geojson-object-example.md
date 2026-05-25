---
title: "Read Local GeoJSON Object Example | Microsoft Docs"
description: Provides a code example that shows how to parse a locally defined GeoJSON object into a map shape using the GeoJSON module, then adds it to the map.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 057e8e6c-a1a9-407f-86d2-abf3876361ee
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Read Local GeoJSON Object Example

[!INCLUDE [bing-maps-web-control-sdk-retirement](../../../includes/bing-maps-web-control-sdk-retirement.md)]

The following code example takes a locally defined GeoJSON object and parses it into a Bing Maps shape using the GeoJSON module, then adds it to the map. When parsing the GeoJSON object, the options for polygons is set such that they will have a semi-transparent red fill color, a stroke thickness of 5 pixels, and a stroke color of white.

```html
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <meta charset="utf-8" />
	<script type='text/javascript'>
    function GetMap() {
        var map = new Microsoft.Maps.Map('#myMap', {
            credentials: ‘Your Bing Maps Key’,
            mapTypeId: Microsoft.Maps.MapTypeId.aerial,
            center: new Microsoft.Maps.Location(47.642, -122.128),
            zoom: 18
        });

        var myGeoJson = {
            "type": "Polygon",
            "coordinates": [[
                    [-122.12901, 47.64178],
                    [-122.12901, 47.64226],
                    [-122.12771, 47.64226],
                    [-122.12771, 47.64178],
                    [-122.12901, 47.64178]
            ]]
        };

        //Load the GeoJson Module.
        Microsoft.Maps.loadModule('Microsoft.Maps.GeoJson', function () {

            //Parse the GeoJson object into a Bing Maps shape.
            var shape = Microsoft.Maps.GeoJson.read(myGeoJson, {
                polygonOptions: {
                    fillColor: 'rgba(255,0,0,0.5)',
                    strokeColor: 'white',
                    strokeThickness: 5
                }
            });

            //Add the shape to the map.
            map.entities.push(shape);
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

Here is what this GeoJSON object looks like on the map. It is a polygon that outlines a soccer field on the Microsoft campus.

![Screenshot of a Bing map showing a rectangle polygon shape on top of a soccer field on the Microsoft campus.](../../media/bmv8-readlocalgeojsonobjectexample-map.png)