---
title: "Basic Core Spatial Math Example | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 5588ed5c-0b25-4e5a-8f51-d2e136850a38
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# Basic Core Spatial Math Example
The following example shows how to use a number of the core Spatial Math functions. It uses north west and south east coordinates of the map to calculate a geodesic line between these points (line that follows the curvature of the earth), the midpoint of this line, a point that is 300 miles from the north west coordinate along the line, the length of the line, the heading between the coordinates, and the also converts the north west coordinate into Degree Minute Second format.

```
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <meta charset="utf-8" />
	<script type='text/javascript'>
    function GetMap() {
        var map = new Microsoft.Maps.Map('#myMap', {
            credentials: 'Your Bing Maps Key',
            zoom: 4
        });

        //Load the Spatial Math module.
        Microsoft.Maps.loadModule("Microsoft.Maps.SpatialMath", function () {
            var bounds = map.getBounds();

            var northWest = bounds.getNorthwest();
            var southEast = bounds.getSoutheast();

            //Calculate a geodesic path between the two points (line the follows curvature of the earth).
            var path = Microsoft.Maps.SpatialMath.getGeodesicPath([northWest, southEast]);
            var poly = new Microsoft.Maps.Polyline(path);
            map.entities.push(poly);

            //Calculate the midpoint of the line.
            var midPoint = Microsoft.Maps.SpatialMath.interpolate(northWest, southEast);
            var pin = new Microsoft.Maps.Pushpin(midPoint, {
                title: 'Midpoint'
            });
            map.entities.push(pin);

            //Calculate a location that is along the path 300 miles from the north west coordinate.
            var point300MilesFromNW = Microsoft.Maps.SpatialMath.getLocationAlongPath(poly, 300, Microsoft.Maps.SpatialMath.DistanceUnits.Miles);
            var pin2 = new Microsoft.Maps.Pushpin(point300MilesFromNW, {
                title: '300 miles from NW'
            });
            map.entities.push(pin2);

            //Calculate the distance from the northWest coordinate to the southEast coordinate.
            var distance = Microsoft.Maps.SpatialMath.getDistanceTo(northWest, southEast, Microsoft.Maps.SpatialMath.DistanceUnits.Miles);

            //Calculate the heading from the northWest coordinate to the southEast coordinate.
            var heading = Microsoft.Maps.SpatialMath.getHeading(northWest, southEast);

            //Convert the northWest coordinate into Degree Minute Second format.
            var northWestDMS = Microsoft.Maps.SpatialMath.toDegMinSec(northWest);

            document.getElementById('outputPanel').innerHTML = 'Distance: ' + distance + ' miles<br/>Heading: ' + heading + ' degrees<br/>North West coordinate in DMS format: ' + northWestDMS;
        });
    }
    </script>
    <script type='text/javascript' src='http://www.bing.com/api/maps/mapcontrol?callback=GetMap' async defer></script>
</head>
<body>
    <div id="myMap" style="position:relative;width:600px;height:400px;"></div><br/>
    <div id="outputPanel"></div>
</body>
</html>
```

Running this code will display a map with a geodesic line, with two pushpins on it. Below the map some calculated values are displayed.

![BMV8_SpatialMathBasics](../v8-web-control/media/bmv8-spatialmathbasics.PNG)