---
title: "Displaying a User Location Example | Microsoft Docs"
description: Provides a code example that shows how to request the user's location and display it as a pushpin on the map.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: d3a54ae4-855d-462f-8127-7f72aecc76bb
caps.latest.revision: 4
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Displaying a User Location Example

[!INCLUDE [bing-maps-web-control-sdk-retirement](../../../includes/bing-maps-web-control-sdk-retirement.md)]

This example shows how to request the user’s location and then display it on the map using a pushpin.

```html
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <meta charset="utf-8" />
	<script type='text/javascript'>
    function GetMap() {
        var map = new Microsoft.Maps.Map('#myMap', {
            credentials: ‘Your Bing Maps Key’
        });

        //Request the user's location
        navigator.geolocation.getCurrentPosition(function (position) {
            var loc = new Microsoft.Maps.Location(
                position.coords.latitude,
                position.coords.longitude);

            //Add a pushpin at the user's location.
            var pin = new Microsoft.Maps.Pushpin(loc);
            map.entities.push(pin);

            //Center the map on the user's location.
            map.setView({ center: loc, zoom: 15 });
        });
    }
    </script>
    <script type='text/javascript' src='http://www.bing.com/api/maps/mapcontrol?callback=GetMap' async defer></script>
</head>
<body>
    <div id="myMap" style="position:relative;width:600px;height:400px;"></div>
</body>
</html>
```

If you run this code, a notification will be displayed asking if you want to share your location. If you allow it to use your location the map will center on your location and a pushpin will be displayed. 

## See Also

  * [Geolocation Accuracy Circle Example](../spatial-math-module-examples/geolocation-accuracy-circle-example.md)