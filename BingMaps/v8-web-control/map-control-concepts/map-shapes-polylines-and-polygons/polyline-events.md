---
title: "Polyline Events | Microsoft Docs"
description: Provides a code example that attaches mouse events to a polyline, which will be highlighted by labels as the events fire.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 2f628ba9-56c2-44ff-b1f2-63118960d205
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Polyline Events

[!INCLUDE [bing-maps-web-control-sdk-retirement](../../includes/bing-maps-web-control-sdk-retirement.md)]s

This example attaches several mouse events to a polyline. When these events fire they highlight a label to indicate which event fired. 

```html
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <meta charset="utf-8" />
	<script type='text/javascript'>
    var map;

    function GetMap() {
        map = new Microsoft.Maps.Map('#myMap', {});

        //Create a random polyline.
        var polyline = Microsoft.Maps.TestDataGenerator.getPolylines(1, map.getBounds());

        //Add the polyline to map
        map.entities.push(polyline);

        //Add mouse events to the polyline.
        Microsoft.Maps.Events.addHandler(polyline, 'click', function () { highlight('polylineClick'); });
        Microsoft.Maps.Events.addHandler(polyline, 'mousedown', function () { highlight('polylineMousedown'); });
        Microsoft.Maps.Events.addHandler(polyline, 'mouseout', function () { highlight('polylineMouseout'); });
        Microsoft.Maps.Events.addHandler(polyline, 'mouseover', function () { highlight('polylineMouseover'); });
        Microsoft.Maps.Events.addHandler(polyline, 'mouseup', function () { highlight('polylineMouseup'); });
    }

    function highlight(id) {
        //Highlight the mouse event div to indicate that the event has fired.
        document.getElementById(id).style.background = 'LightGreen';

        //Remove the highlighting after a second.
        setTimeout(function () { document.getElementById(id).style.background = 'white'; }, 1000);
    }
    </script>
    <script type='text/javascript' src='http://www.bing.com/api/maps/mapcontrol?callback=GetMap&key=[YOUR_BING_MAPS_KEY]' async defer></script>
</head>
<body>
    <div id="myMap" style="position:relative;width:600px;height:400px;"></div>

    <div id="polylineClick">click</div>
    <div id="polylineMousedown">mousedown</div>
    <div id="polylineMouseout">mouseout</div>
    <div id="polylineMouseover">mouseover</div>
    <div id="polylineMouseup">mouseup</div>
</body>
</html>
```

If you run this code and hover and click the polyline you will see all these different events fire.

![Screenshot of a Bing map showing a polyline with a list of events below the map that are highlighted in green as they fire.](../../media/bmv8-polylineevents.png)

[Try it now](https://www.bing.com/api/maps/sdk/mapcontrol/isdk#polylineAllEvents+JS)