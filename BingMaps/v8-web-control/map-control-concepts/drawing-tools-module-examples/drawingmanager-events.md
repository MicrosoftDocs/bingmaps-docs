---
title: "DrawingManager Events | Microsoft Docs"
description: Provides a code example that shows how to add events to the drawing manager that is created by the drawing tools module.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 1a2cb0cf-d2b9-452b-963a-2d7a734991e7
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# DrawingManager Events

The example adds a bunch of events to the drawing manager that is created by the drawing tools module. As the different events first a label will be highlighted in green to indicate which event(s) have fired.

```html
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <meta charset="utf-8" />
	<script type='text/javascript'>
    var map, drawingManager;

    function GetMap() {
        map = new Microsoft.Maps.Map('#myMap', {});

        //Load the DrawingTools module
        Microsoft.Maps.loadModule('Microsoft.Maps.DrawingTools', function () {
            //Create an instance of the DrawingTools class and bind it to the map.
            var tools = new Microsoft.Maps.DrawingTools(map);

            //Show the drawing toolbar and enable editting on the map.
            tools.showDrawingManager(function (manager) {

                //Add events to the drawing manager.
                Microsoft.Maps.Events.addHandler(manager, 'drawingChanged', function () { highlight('drawingChanged'); });
                Microsoft.Maps.Events.addHandler(manager, 'drawingChanging', function () { highlight('drawingChanging'); });
                Microsoft.Maps.Events.addHandler(manager, 'drawingEnded', function () { highlight('drawingEnded'); });
                Microsoft.Maps.Events.addHandler(manager, 'drawingErased', function () { highlight('drawingErased'); });
                Microsoft.Maps.Events.addHandler(manager, 'drawingModeChanged', function () { highlight('drawingModeChanged'); });
                Microsoft.Maps.Events.addHandler(manager, 'drawingStarted', function () { highlight('drawingStarted'); });
            })
        });
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

    <div id="drawingChanged">drawingChanged</div>
    <div id="drawingChanging">drawingChanging</div>
    <div id="drawingEnded">drawingEnded</div>
    <div id="drawingErased">drawingErased</div>
    <div id="drawingModeChanged">drawingModeChanged</div>
    <div id="drawingStarted">drawingStarted</div>
</body>
</html>
```

Running this code in a browser you will see the different events highlighted in green as you draw a shape on the map.

![Screenshot of a Bing map showing a polygon shape overlaid on top of Redmond, Washington, and a list of events below the map.](../../media/bmv8-drawingtoolseventsexample.png)