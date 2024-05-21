---
title: "Infobox when Shape Clicked | Microsoft Docs"
description: Provides a code example that shows how to display an infobox when any IPrimitive shape such as a pushpin, polyline, or polygon is selected.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 8a8c1abe-4547-4694-8622-9ebebe6b6a54
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Infobox when Shape Clicked

[!INCLUDE [bing-maps-web-control-sdk-retirement](../../../includes/bing-maps-web-control-sdk-retirement.md)]

Often it is useful to be able to display an infobox when any `IPrimitive` shape; `Pushpin`, `Polyline`, or `Polygon` is clicked. This example shows how to handle the click events from these shapes and display an infobox on top of them.

```html
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <meta charset="utf-8" />
	<script type='text/javascript'>
    var map, infobox;

    function GetMap() {
        map = new Microsoft.Maps.Map('#myMap', {});

        //Create an infobox at the center of the map but don't show it.
        infobox = new Microsoft.Maps.Infobox( map.getCenter(), {
            visible: false
        });

        //Assign the infobox to a map instance.
        infobox.setMap(map);

        //Create a polygon as our IPrimitive.
        var shape = Microsoft.Maps.TestDataGenerator.getPolygons(1, map.getBounds());

        //Add some metadata to the IPrimitive.
        shape.metadata = {
            title: 'IPrimitive clicked',
            description: 'I am a polygon'
        };

        //Add an click event handler to the IPrimitive.
        Microsoft.Maps.Events.addHandler(shape, 'click', iPrimitiveClicked);

        //Add the IPrimitive to the map.
        map.entities.push(shape);
    }

    function iPrimitiveClicked(e) {
        //Make sure the infobox has metadata to display.
        if (e.target.metadata) {
            //Set the infobox options with the metadata of the pushpin.
            infobox.setOptions({
                //Use the location of where the mouse was clicked to position the infobox.
                location: e.location,
                title: e.target.metadata.title,
                description: e.target.metadata.description,
                visible: true
            });
        }
    }
    </script>
    <script type='text/javascript' src='http://www.bing.com/api/maps/mapcontrol?callback=GetMap&key=[YOUR_BING_MAPS_KEY]' async defer></script>
</head>
<body>
    <div id="myMap" style="position:relative;width:600px;height:400px;"></div>
</body>
</html>
```

Running this code will display a polygon on the map. If you click on it, an infobox will appear filled in with the metadata for that polygon. 

![Screenshot of a Bing map showing an infobox associated with a polygon that has a description stating it is a polygon.](../../media/bmv8-infoboxshapeclicked2.png)