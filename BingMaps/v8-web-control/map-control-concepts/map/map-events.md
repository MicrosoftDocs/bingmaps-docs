---
title: "Map Events | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 534c434d-bce0-4137-909e-c017ff18db4e
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Map Events
This example shows how all the different events for the map work by highlight a label to indicate which event fired as you use the map. 

```
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <meta charset="utf-8" />
	<script type='text/javascript'>
    var map;

    function GetMap() {
        map = new Microsoft.Maps.Map('#myMap', {});

        //Add view change events to the map.
        Microsoft.Maps.Events.addHandler(map, 'viewchangestart', function () { highlight('mapViewChangeStart'); });
        Microsoft.Maps.Events.addHandler(map, 'viewchange', function () { highlight('mapViewChange'); });
        Microsoft.Maps.Events.addHandler(map, 'viewchangeend', function () { highlight('mapViewChangEnd'); });

        //Add mouse events to the map.
        Microsoft.Maps.Events.addHandler(map, 'click', function () { highlight('mapClick'); });
        Microsoft.Maps.Events.addHandler(map, 'dblclick', function () { highlight('mapDblClick'); });
        Microsoft.Maps.Events.addHandler(map, 'rightclick', function () { highlight('mapRightClick'); });
        Microsoft.Maps.Events.addHandler(map, 'mousedown', function () { highlight('mapMousedown'); });
        Microsoft.Maps.Events.addHandler(map, 'mouseout', function () { highlight('mapMouseout'); });
        Microsoft.Maps.Events.addHandler(map, 'mouseover', function () { highlight('mapMouseover'); });
        Microsoft.Maps.Events.addHandler(map, 'mouseup', function () { highlight('mapMouseup'); });
        Microsoft.Maps.Events.addHandler(map, 'mousewheel', function () { highlight('mapMousewheel'); });

        //Add addition map event handlers
        Microsoft.Maps.Events.addHandler(map, 'maptypechanged', function () { highlight('maptypechanged'); });
    }

    function highlight(id) {
        //Highlight the div to indicate that the event has fired.
        document.getElementById(id).style.background = 'LightGreen';

        //Remove the highlighting after a second.
        setTimeout(function () { document.getElementById(id).style.background = 'white'; }, 1000);
    }
    </script>
    <script type='text/javascript' src='http://www.bing.com/api/maps/mapcontrol?callback=GetMap&key=[YOUR_BING_MAPS_KEY]' async defer></script>
</head>
<body>
    <div id="myMap" style="position:relative;width:600px;height:400px;"></div>

    <div id="mapViewChangeStart">viewchangestart</div>
    <div id="mapViewChange">viewchange</div>
    <div id="mapViewChangEnd">viewchangeend</div>

    <div id="mapClick">click</div>
    <div id="mapDblClick">dblclick</div>
    <div id="mapRightClick">rightclick</div>
    <div id="mapMousedown">mousedown</div>
    <div id="mapMouseout">mouseout</div>
    <div id="mapMouseover">mouseover</div>
    <div id="mapMouseup">mouseup</div>
    <div id="mapMousewheel">mousewheel</div>

    <div id="maptypechanged">maptypechanged</div>
</body>
</html>
```
This code loads a map. As you interactive with it using a mouse or touch you will see the different map events highlighted as they are fired.

![BMV8_MapEvents](../../media/bmv8-mapevents.png)

[Try it now](https://www.bing.com/api/maps/sdk/mapcontrol/isdk#mapMouseEvents+JS)