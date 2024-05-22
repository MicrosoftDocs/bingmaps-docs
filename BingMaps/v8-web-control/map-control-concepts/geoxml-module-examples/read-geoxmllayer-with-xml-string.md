---
title: "Read GeoXmlLayer with XML String | Microsoft Docs"
description: Provides a code sample that shows how to pass in a string of GeoRSS data into a GeoXmlLayer and overlay it on the map.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 8c482056-9413-4b2b-af9e-c845a195131a
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Read GeoXmlLayer with XML String

[!INCLUDE [bing-maps-web-control-sdk-retirement](../../../includes/bing-maps-web-control-sdk-retirement.md)]

Raw XML data that is stored as a string can be passed into the GeoXml read functions and GeoXmlLayer class. This sample shows how to easily pass in a string of GeoRSS data into a GeoXmlLayer and overlay it on the map.

```html
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <meta charset="utf-8" />
    <script type='text/javascript'>
    var map;
    var georss = '<feed xmlns="http://www.w3.org/2005/Atom" xmlns:georss="http://www.georss.org/georss"><entry><title>Sample Polygon</title><georss:polygon>46.31409 -122.22616 46.31113 -122.22968 46.31083 -122.23320</georss:polygon></entry></feed>';

    function GetMap() {
        map = new Microsoft.Maps.Map('#myMap', {
            credentials: 'Your Bing Maps Key',
            zoom: 1
        });

        //Load the GeoXml module.
        Microsoft.Maps.loadModule('Microsoft.Maps.GeoXml', function () {
            //Create an instance of the GeoXmlLayer.
            layer = new Microsoft.Maps.GeoXmlLayer(georss);

            //Add the layer to the map.
            map.layers.insert(layer);
        });
    }
    </script>
    <script type='text/javascript' src='https://www.bing.com/api/maps/mapcontrol?callback=GetMap' async defer></script>
</head>
<body>
    <div id="myMap" style="position:relative;width:800px;height:600px;"></div>
</body>
</html>
```

Here is what this GeoRSS data looks like on the map. 

![Screenshot of a Bing map showing a triangle over a landmass.](../../media/bmv8-basicgeoxml.PNG)
 
[Try it now](https://bingmapsv8samples.azurewebsites.net/#GeoXmlLayer%20-%20Basic)
