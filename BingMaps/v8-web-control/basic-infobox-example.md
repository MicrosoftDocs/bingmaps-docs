---
title: "Basic Infobox Example | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 5763d013-e555-49bf-8e8f-65dfaae1b9b6
caps.latest.revision: 4
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms:service: "bing-maps"
---
# Basic Infobox Example
The following code shows how to add an infobox with a title and description to the center of the map. 

```
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <meta charset="utf-8" />
	<script type='text/javascript'>
    var map;

    function GetMap() {
        map = new Microsoft.Maps.Map('#myMap', {
            credentials: 'Your Bing Maps Key',
            center: new Microsoft.Maps.Location(47.60357, -122.32945)
        }); 
        var center = map.getCenter();

        //Create an infobox that will render in the center of the map.
        var infobox = new Microsoft.Maps.Infobox(center, {
            title: 'Map Center',
            description: 'Seattle'
        });

        //Assign the infobox to a map instance.
        infobox.setMap(map);
    }
    </script>
    <script type='text/javascript' src='http://www.bing.com/api/maps/mapcontrol?callback=GetMap' async defer></script>
</head>
<body>
    <div id="myMap" style="position:relative;width:600px;height:400px;"></div>
</body>
</html> 
```

This code will add an infobox to the center of the map like this.

![Basic Infobox on a Map](../v8-web-control/media/bmv8-basicinfoboxexample2.png)

[Try it now](http://www.bing.com/api/maps/sdk/mapcontrol/isdk#addDefaultInfobox+JS)