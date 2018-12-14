---
title: "Get Shapes from DrawingManager | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 46fec141-d79c-428a-ab71-9e441f42de59
caps.latest.revision: 4
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Get Shapes from DrawingManager

This example shows how to get all the shapes that are in the drawing manager at any time. 

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

        Microsoft.Maps.loadModule('Microsoft.Maps.DrawingTools', function () {
            var tools = new Microsoft.Maps.DrawingTools(map);

            tools.showDrawingManager(function (manager) {
                drawingManager = manager;
            })
        });
    }

    function getShapes() {
        var shapes = drawingManager.getPrimitives();

        if (shapes && shapes.length > 0) {
            alert('Retrieved ' + shapes.length + ' from the drawing manager.');
        } else {
            alert('No shapes in the drawing manager.');
        }
    }
    </script>
    <script type='text/javascript' src='http://www.bing.com/api/maps/mapcontrol?callback=GetMap&key=[YOUR_BING_MAPS_KEY]' async defer></script>
</head>
<body>
    <div id="myMap" style="position:relative;width:600px;height:400px;"></div><br/>
    <input type="button" value="Get Shapes" onclick="getShapes()"/>
</body>
</html>
```

> [!TIP]
> If you want to get a shape right after it was drawn, use the `drawingEnded` event on the [DrawingManager](../../modules/drawing-tools-module/drawingmanager-class.md).