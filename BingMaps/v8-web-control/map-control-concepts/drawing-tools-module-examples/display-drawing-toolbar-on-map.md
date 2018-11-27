---
title: "Display Drawing Toolbar on Map | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 344617ff-f404-4c18-b681-84be6697224b
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Display Drawing Toolbar on Map
This example shows how to add a drawing toolbar to the map so that the user can draw shapes.

```
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
                //Store a reference to the drawing manager as it will be useful later.
                drawingManager = manager;
            })
        });
    }
    </script>
    <script type='text/javascript' src='http://www.bing.com/api/maps/mapcontrol?callback=GetMap&key=[YOUR_BING_MAPS_KEY]' async defer></script>
</head>
<body>
    <div id="myMap" style="position:relative;width:600px;height:400px;"></div>
</body>
</html>
```

Running this code in a browser will display a map with the drawing toolbar displayed on it. Select a shape and start drawing on the map. When drawing, press the escape button or a button on the toolbar to stop the drawing.

![BMV8_DrawingToolbarExample](..//media/bmv8-drawingtoolbarexample.png)

[Try it now](http://www.bing.com/api/maps/sdk/mapcontrol/isdk#dtDrawThings+JS)