---
title: "Read Same Domain GeoJSON Example | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: c013fb23-533f-4098-b40c-6c57a869e5de
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Read Same Domain GeoJSON Example
The following code example takes a URL to a GeoJSON file that is hosted on the same domain as the application or has CORS enabled on the hosting server and parses it into a Bing Maps shape using the GeoJSON module, then adds it to the map. 

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
            zoom: 1
        });

        //Load GeoJSON module.
        Microsoft.Maps.loadModule('Microsoft.Maps.GeoJson', function () {

            //Read the GeoJSON file that is hosted on the same domain.
            Microsoft.Maps.GeoJson.readFromUrl('data/Countries.js',
                function (shapes) {
                    //Add the shape(s) to the map.
                    map.entities.push(shapes);
                });
        });
    }
    </script>
    <script type='text/javascript' src='http://www.bing.com/api/maps/mapcontrol?callback=GetMap' async defer></script>
</head>
<body>
    <div id="myMap" style="position:relative;width:1000px;height:800px;"></div>
</body>
</html>
```

Here is what this GeoJSON file looks like on the map. All the country boundaries displayed as polygons.

![Read GeoJSON on a Map](../../media/bmv8-readsamedomaingeojsonexample-map.png)
