---
title: "Write Bing Maps Shape as GeoJSON Example | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 83d5e440-7ec9-4ea6-a963-62ca1d13c5fe
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# Write Bing Maps Shape as GeoJSON Example
This example takes a Bing Maps shape and uses the GeoJSON module to generate a GeoJSON object out of it. The code then turns this GeoJSON object into a string and displays it in a new window. The shape is added to the map so that you can see what it looks like, but this isn’t required to generate the GeoJSON object. 

```
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <meta charset="utf-8" />
    <script type='text/javascript'
            src='http://www.bing.com/api/maps/mapcontrol?callback=GetMap'
            async defer></script>
    <script type='text/javascript'>
    function GetMap() {
        var map = new Microsoft.Maps.Map('#myMap', {
            credentials: ‘Your Bing Maps Key’,
            center: new Microsoft.Maps.Location(43, -107.55),
            zoom: 5
        });

        //Create some shapes to convert into GeoJSON.
        var polygon = new Microsoft.Maps.Polygon([
            [new Microsoft.Maps.Location(41, -104.05),
            new Microsoft.Maps.Location(45, -104.05),
            new Microsoft.Maps.Location(45, -111.05),
            new Microsoft.Maps.Location(41, -111.05),
            new Microsoft.Maps.Location(41, -104.05)]]);

        var pin = new Microsoft.Maps.Pushpin(new Microsoft.Maps.Location(43, -107.55));

        //Create an array of shapes.
        var shapes = [polygon, pin];

        //Add the shapes to the map so we can see them (optional).
        map.entities.push(shapes);

        Microsoft.Maps.loadModule('Microsoft.Maps.GeoJson', function () {
            //Convert the array of shapes into a GeoJSON object.
            var geoJson = Microsoft.Maps.GeoJson.write(shapes);

            //Display the GeoJson in a new Window.
            var myWindow = window.open('', '_blank', 'scrollbars=yes, resizable=yes, width=400, height=100');
            myWindow.document.write(JSON.stringify(geoJson));
        });
    }
    </script>
</head>
<body>
    <div id="myMap" style="position:relative;width:600px;height:400px;"></div>
</body>
</html>
```

When you run this code you should see the map center over top of Wyoming with its boundaries drawn out with a polygon, and an alert message displayed showing the GeoJSON equivalent of this polygon.

![GeoJSON Markup from a Bing Maps Shape](../v8-web-control/media/bmv8-geojson-write.png)