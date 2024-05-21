---
title: "Calculate Transit Directions | Microsoft Docs"
description: Provides a code example that shows how to calculate transit directions using a route from Redmond, WA to Seattle, WA.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 179eb252-6f53-44ef-8d77-5b7733b71466
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Calculate Transit Directions

[!INCLUDE [bing-maps-web-control-sdk-retirement](../../includes/bing-maps-web-control-sdk-retirement.md)]

The following example shows how to calculate transit directions from “Redmond, WA” to “Seattle, WA” leaving an hour from the current time. The directions are displayed on the map and instructions are rendered in a div element with an id of `directionsItinerary`.

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
                var directionsManager = new Microsoft.Maps.Directions.DirectionsManager(map);
                
                //Calculate a date time that is 1 hour from now.
                var departureTime  = new Date();
                departureTime.setMinutes(departureTime.getHours() + 1);

                //Set Route Mode to transit.
                directionsManager.setRequestOptions({
                    routeMode: Microsoft.Maps.Directions.RouteMode.transit,
                    time: departureTime,
                    timeType: Microsoft.Maps.Directions.TimeTypes.departure
                });

                //Add waypoints.
                var waypoint1 = new Microsoft.Maps.Directions.Waypoint({ address: 'Redmond, WA' });
                directionsManager.addWaypoint(waypoint1);

                var waypoint2 = new Microsoft.Maps.Directions.Waypoint({ address: 'Seattle, WA' });                
                directionsManager.addWaypoint(waypoint2);

                //Set the element in which the itinerary will be rendered.
                directionsManager.setRenderOptions({ itineraryContainer: document.getElementById('directionsItinerary') });

                //Calculate directions.
                directionsManager.calculateDirections();
            });
        }
    </script>
    <script type='text/javascript' src='http://www.bing.com/api/maps/mapcontrol?callback=GetMap&key=[YOUR_BING_MAPS_KEY]' async defer></script>
</head>
<body>
    <div id="myMap" style="position:relative;width:800px;height:600px;"></div>
    <div id='directionsItinerary'></div>
</body>
</html>
```

Running this code will display a transit route from “Redmond, WA” to “Seattle, WA” with a departure time that is an hour from now, instructions are displayed below the map. 

![Screenshot o a Bing map showing a route from Redmond, Washington to Seattle, Washington, with transit directions listed below the map.](../../media/bmv8-transitdirectionsexample2.PNG)

[Try it now](https://www.bing.com/api/maps/sdk/mapcontrol/isdk#directionsCreateTransitRoute+JS)