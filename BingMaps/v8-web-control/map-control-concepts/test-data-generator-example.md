---
title: "Test Data Generator Example | Microsoft Docs"
description: Provides a code example that creates two random polygons with a scaleFactor of 0.5 random polygon options, and a hole.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 8f216851-55a1-433b-9792-222501bc03b4
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Test Data Generator Example
## Related Topics

* [TestDataGenerator Class](../map-control-api/testdatagenerator-class.md)

## Basic Example

The following code sample shows how to create two random polygons that have a scaleFactor of 0.5, random polygon options and a hole. 

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

        var polygons = Microsoft.Maps.TestDataGenerator.getPolygons(3, map.getBounds(), 5, null, null, true);
        map.entities.push(polygons);
    }
    </script>
    <script type='text/javascript' src='http://www.bing.com/api/maps/mapcontrol?callback=GetMap' async defer></script>
</head>
<body>
    <div id="myMap" style="position:relative;width:600px;height:400px;"></div>
</body>
</html>
```

Here is what these polygons look like when running this code. Note that since the polygons are random, the polygons that will be generated when you run this code will look different. 

![Test Data Generator](../media/bmv8-testdatageneratorexample.png)

[Try it now](https://www.bing.com/api/maps/sdk/mapcontrol/isdk#createPolygonsWithHoles+JS)