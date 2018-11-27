---
title: "Directions Module Events | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 5beb4103-f409-4709-ab72-0f317f8eabc4
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Directions Module Events

This example shows how to use events with the directions manager. A route from “Seattle, WA” to “Redmond, WA” is calculated and instead of displaying the turn by turn directions, after the route is calculated the route summary information is used instead to display the distance and travel time with traffic.

```html
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <meta charset="utf-8" />
	<script type='text/javascript'>
        var map;
        var directionsManager;

        function GetMap()
        {
            map = new Microsoft.Maps.Map('#myMap', {});

            //Load the directions module.
            Microsoft.Maps.loadModule('Microsoft.Maps.Directions', function () {
                //Create an instance of the directions manager.
                directionsManager = new Microsoft.Maps.Directions.DirectionsManager(map);

                //Create waypoints to route between.
                var seattleWaypoint = new Microsoft.Maps.Directions.Waypoint({ address: 'Seatle, WA' });
                directionsManager.addWaypoint(seattleWaypoint);

                var workWaypoint = new Microsoft.Maps.Directions.Waypoint({ address: 'Redmond, WA' });
                directionsManager.addWaypoint(workWaypoint);

                //Add event handlers to directions manager.
                Microsoft.Maps.Events.addHandler(directionsManager, 'directionsError', directionsError);
                Microsoft.Maps.Events.addHandler(directionsManager, 'directionsUpdated', directionsUpdated);

                //Calculate directions.
                directionsManager.calculateDirections();
            });
        }

        function directionsUpdated(e) {
            //Get the current route index.
            var routeIdx = directionsManager.getRequestOptions().routeIndex;

            //Get the distance of the route, rounded to 2 decimal places.
            var distance = Math.round(e.routeSummary[routeIdx].distance * 100)/100;

            //Get the distance units used to calculate the route.
            var units = directionsManager.getRequestOptions().distanceUnit;
            var distanceUnits = '';

            if (units == Microsoft.Maps.Directions.DistanceUnit.km) {
                distanceUnits = 'km'
            } else {
                //Must be in miles
                distanceUnits = 'miles'
            }

            //Time is in seconds, convert to minutes and round off.
            var time = Math.round(e.routeSummary[routeIdx].timeWithTraffic / 60);

            document.getElementById('routeInfoPanel').innerHTML = 'Distance: ' + distance + ' ' + distanceUnits + '<br/>Time with Traffic: ' + time + ' minutes';
        }

        function directionsError(e) {
            alert('Error: ' + e.message + '\r\nResponse Code: ' + e.responseCode)
        }
    </script>
    <script type='text/javascript' src='http://www.bing.com/api/maps/mapcontrol?callback=GetMap&key=[YOUR_BING_MAPS_KEY]' async defer></script>
</head>
<body>
    <div id="myMap" style="position:relative;width:800px;height:600px;"></div>
    <div id='routeInfoPanel'></div>
</body>
</html>
```

Running this code will display the route from “Seattle, WA” to “Redmond, WA” on the map along with the distance and travel time with traffic below the map.

![Directions Event Example](../../media/bmv8-directionseventexample.PNG)