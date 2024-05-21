---
title: "Pushpin Hover Style | Microsoft Docs"
description: Provides a code example that show how to use mouse events to update the pushpin options when a user interacts with the pushpin.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: f0745a32-0bf8-443c-8b7e-4e58e156bbc5
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Pushpin Hover Style

[!INCLUDE [bing-maps-web-control-sdk-retirement](../../includes/bing-maps-web-control-sdk-retirement.md)]

Creating a custom pushpin is great, but having the style change when users interact with the pushpin can make the user experience a bit more engaging. This example uses mouse events to update the pushpin options when a user mouses over, press down and mouses out of the pushpin. For simplicity the color of the pushpin will be change depending on how the user interacts with the pushpin, however you could just as easy change any of the other pushpin options if desired. 

```html
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <meta charset="utf-8" />
	<script type='text/javascript'>
    var map;

    var defaultColor = 'blue';
    var hoverColor = 'red';
    var mouseDownColor = 'purple';

    function GetMap()
    {
        map = new Microsoft.Maps.Map('#myMap', {});

        var pin = new Microsoft.Maps.Pushpin(map.getCenter(), {
            color: defaultColor
        });

        map.entities.push(pin);

        Microsoft.Maps.Events.addHandler(pin, 'mouseover', function (e) {
            e.target.setOptions({ color: hoverColor });
        });

        Microsoft.Maps.Events.addHandler(pin, 'mousedown', function (e) {
            e.target.setOptions({ color: mouseDownColor });
        });

        Microsoft.Maps.Events.addHandler(pin, 'mouseout', function (e) {
            e.target.setOptions({ color: defaultColor });
        });
    }
    </script>
    <script type='text/javascript' src='http://www.bing.com/api/maps/mapcontrol?callback=GetMap&key=[YOUR_BING_MAPS_KEY]' async defer></script>
</head>
<body>
    <div id="myMap" style="position:relative;width:800px;height:600px;"></div>
</body>
</html>
```

If you run this code, you will see a blue pushpin in the center of the map. If you drag the mouse over the pushpin it will change to red and if you press down purple. 

> [!Note]
> This is unrelated to Pushpin enableHoverStyle option which only effects the default pushpin style. However you could use the pushpin's getOptions function inside the event handlers to determine if the pushpins style should be changed or not when hovered.  
