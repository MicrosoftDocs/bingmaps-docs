---
title: "Load Multiple Boundaries GeoData Example | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 4173ee75-9a85-4ab5-9cdb-116871187565
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# Load Multiple Boundaries GeoData Example
Displaying the boundary of a single location is useful, but sometimes you need to display the boundaries of several locations at once. This code sample shows how to request the boundaries for 5 zip codes and render them on the map.

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
            center: new Microsoft.Maps.Location(47.614, -122.165),
            zoom: 11
        });

        //Create an array of locations to get the boundaries of.
        var zipCodes = ['98004', '98005', '98007', '98008', '98039'];

        //Create the request options.
        var geoDataRequestOptions = {
            entityType: 'Postcode1'
        };

        //Load the Bing Spatial Data Services module.
        Microsoft.Maps.loadModule('Microsoft.Maps.SpatialDataService', function () {

            //Use the GeoData API manager to get the boundaries of the zip codes.
            Microsoft.Maps.SpatialDataService.GeoDataAPIManager.getBoundary(
                zipCodes,
                geoDataRequestOptions,
                map,
                function (data) {
                    //This callback function will be called once for each zip code.
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

Running this code will load a map that displays the boundaries of 5 zip codes that are in the city of Bellevue, WA.

![Multiple Boundaries on a Map](../v8-web-control/media/bmv8-geodatamultipleboundaries.png)

[Try it now](http://www.bing.com/api/maps/sdk/mapcontrol/isdk#sdsLoadMultipleBoundaries+JS)