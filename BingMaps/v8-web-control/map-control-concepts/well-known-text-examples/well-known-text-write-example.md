---
title: "Well Known Text Write Example | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 935b9bb6-f0f1-4455-9cc3-e643226b473a
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Well Known Text Write Example

This code example shows how to convert a Bing Maps shape into a Well Known Text string value and display it using an alert.

```html
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <meta charset="utf-8" />
	<script type='text/javascript'>
    function GetMap() {
        var map = new Microsoft.Maps.Map('#myMap', {
            credentials: 'Your Bing Maps Key',
            center: new Microsoft.Maps.Location(47.655, -122.10)
        });

        //Create polyline.
        var polyline = new Microsoft.Maps.Polyline([
                new Microsoft.Maps.Location(47.66852, -122.10025),
                new Microsoft.Maps.Location(47.65118, -122.13218),
                new Microsoft.Maps.Location(47.65164, -122.0903),
                new Microsoft.Maps.Location(47.6676, -122.12463),
                new Microsoft.Maps.Location(47.64494, -122.11193),
                new Microsoft.Maps.Location(47.66737, -122.10094)],
            {
                strokeColor: 'Magenta',
                strokeThickness: 4
            });

        //Add it to the map.
        map.entities.push(polyline);

        //Load the Well Known Text module.
        Microsoft.Maps.loadModule('Microsoft.Maps.WellKnownText',
            function () {
                //Convert polyline into a Well Known Text.
                var wkt = Microsoft.Maps.WellKnownText.write(polyline);

                //Display the Well Known Text in a new Window.
                var myWindow = window.open('', '_blank', 'scrollbars=yes, resizable=yes, width=400, height=100');
                myWindow.document.write(wkt);
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

Running this code will display a map with a polyline in the shape of a star drawn on it. An alert will be displayed that contains the Well Known Text value of the polyline.

![Well Known Text from Shapes on a Map](../../media/bmv8-writewkt.png)

[Try it now](https://www.bing.com/api/maps/sdk/mapcontrol/isdk#wktWriteToWkt+JS)