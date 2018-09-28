---
title: "Continuously Tracking a User Location Example | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 7874d1ba-a150-40b9-abfc-677c9d29f1af
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Continuously Tracking a User Location Example
This example shows how to monitor the user’s location and update the position of a pushpin as the user moves. 

```
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <meta charset="utf-8" />
	<script type='text/javascript'>
    var map, watchId, userPin;

    function GetMap()
    {
        map = new Microsoft.Maps.Map('#myMap', {
            credentials: ‘Your Bing Maps Key’
        });
    }

    function StartTracking() {
        //Add a pushpin to show the user's location.
        userPin = new Microsoft.Maps.Pushpin(map.getCenter(), { visible: false });
        map.entities.push(gpsPin);

        //Watch the users location.
        watchId = navigator.geolocation.watchPosition(UsersLocationUpdated);
    }

    function UsersLocationUpdated(position) {
        var loc = new Microsoft.Maps.Location(
                    position.coords.latitude,
                    position.coords.longitude);

        //Update the user pushpin.
        userPin.setLocation(loc);
        userPin.setOptions({ visible: true });

        //Center the map on the user's location.
        map.setView({ center: loc });
    }

    function StopTracking() {
        // Cancel the geolocation updates.
        navigator.geolocation.clearWatch(watchId);

        //Remove the user pushpin.
        map.entities.clear();
    }
    </script>
    <script type='text/javascript' src='http://www.bing.com/api/maps/mapcontrol?callback=GetMap' async defer></script>
</head>
<body>
    <div id="myMap" style="position:relative;width:600px;height:400px;"></div><br/>
    <input type="button" value="Start Continuous Tracking" onclick="StartTracking()" />
    <input type="button" value="Stop Continuous Tracking" onclick="StopTracking()"/>
</body>
</html>
```
