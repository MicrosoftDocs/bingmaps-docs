---
title: "Load Single Boundary GeoData Example | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 437c4081-ce33-441b-a805-bbfd4eb34e5d
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# Load Single Boundary GeoData Example
This examples renders a PopulatedPlace (city, town) boundary for the Location that is in the center of the map view when the map is loaded. The center of the map is set to (43.7, -79.3834) which is a location in Toronto, Ontario, Canada.

```
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <meta charset="utf-8" />
    <script type='text/javascript' 
            src='http://www.bing.com/api/maps/mapcontrol?callback=GetMap' 
            async defer></script>
    <script type='text/javascript'>
    function GetMap() {
        var map = new Microsoft.Maps.Map('#myMap', {
            credentials: ‘Your Bing Maps Key’,
            center: new Microsoft.Maps.Location(43.7, -79.3834),
            zoom: 10
        });

        //Create the request options.
        var geoDataRequestOptions = {
            entityType: 'PopulatedPlace'
        };

        //Load the Bing Spatial Data Services module.
        Microsoft.Maps.loadModule('Microsoft.Maps.SpatialDataService', function () {

            //Use the GeoData API manager to get the boundaries of the zip codes.
            Microsoft.Maps.SpatialDataService.GeoDataAPIManager.getBoundary(
                map.getCenter(),
                geoDataRequestOptions,
                map,
                function (data) {
                    //Add the polygons to the map.
                    if (data.results && data.results.length > 0) {
                        map.entities.push(data.results[0].Polygons);
                    }
                });
        });
    }
    </script>
</head>
<body>
    <div id="myMap" style="position:relative;width:600px;height:400px;"></div>
</body>
</html>
```

Running this code will display a map with the boundaries of Toronto displayed. 

![Single Boundary on a Map](../v8-web-control/media/bmv8-geodatasingleboundary.png)

[Try it now](http://www.bing.com/api/maps/sdk/mapcontrol/isdk#sdsLoadSingleBoundary+JS)