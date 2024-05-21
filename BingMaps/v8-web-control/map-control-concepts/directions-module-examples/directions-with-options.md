---
title: "Directions with Options | Microsoft Docs"
description: Provides a code example that shows how to use render options to modify how a route is calculated and displayed on a map.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 0c624a59-fb89-4e86-a7a4-f338b2f217d9
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Directions with Options

[!INCLUDE [bing-maps-web-control-sdk-retirement](../../includes/bing-maps-web-control-sdk-retirement.md)]

When calculating directions request options can be used to modify how the route is calculated. Render options can be used to customize how the route is displayed on the map. In this example driving directions are calculated in kilometers and set to avoid highways. The route line is rendered green and thick, while the title of all waypoints are replaced with an empty string to hide the default behaviour.

```html
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <meta charset="utf-8" />
    <script type='text/javascript'>
    var map, directionsManager;

    function GetMap()
    {
        map = new Microsoft.Maps.Map('#myMap', {
            credentials: 'Your Bing Maps Key'
        });

        //Load the directions module.
        Microsoft.Maps.loadModule('Microsoft.Maps.Directions', function () {
            //Create an instance of the directions manager.
            directionsManager = new Microsoft.Maps.Directions.DirectionsManager(map);

            //Create waypoints to route between.
            directionsManager.addWaypoint(new Microsoft.Maps.Directions.Waypoint({ address: 'London, UK' }));
            directionsManager.addWaypoint(new Microsoft.Maps.Directions.Waypoint({ address: 'Paris, FR' }));
            directionsManager.addWaypoint(new Microsoft.Maps.Directions.Waypoint({ address: 'Madrid, ES' }));

            //Set the request options that avoid highways and uses kilometers.
            directionsManager.setRequestOptions({
                distanceUnit: Microsoft.Maps.Directions.DistanceUnit.km,
                routeAvoidance: [Microsoft.Maps.Directions.RouteAvoidance.avoidLimitedAccessHighway]
            });

            //Make the route line thick and green. Replace the title of waypoints with an empty string to hide the default text that appears.
            directionsManager.setRenderOptions({
                drivingPolylineOptions: {
                    strokeColor: 'green',
                    strokeThickness: 6
                },
                waypointPushpinOptions: {
                    title: ''
                }
            });

            //Calculate directions.
            directionsManager.calculateDirections();
        });
    }
    </script>
    <script type='text/javascript' src='https://www.bing.com/api/maps/mapcontrol?callback=GetMap' async defer></script>
</head>
<body>
    <div id="myMap" style="position:relative;width:800px;height:600px;"></div>
</body>
</html>
```

Running this code will display a map with a route from London, UK to Madrid, Spain, going through Paris, France which looks like this.

![Screenshot of a Bing map showing a route from London, UK to Madrid, Spain with a stop in Paris, France.](../../media/bmv8-directionswithoptions.PNG)

[Try it now](https://bingmapsv8samples.azurewebsites.net/#Directions_WithOptions)

See also this sample on [Fully Custom Waypoint Pushpins](https://bingmapsv8samples.azurewebsites.net/#Fully%20Custom%20Waypoint%20Pushpinshttps://bingmapsv8samples.azurewebsites.net/)
