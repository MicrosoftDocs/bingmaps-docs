---
title: "Find By Property Example | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 6d497c56-74e3-482f-92bb-869ea1c0a571
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Find By Property Example
One of the simpliest ways to query a data source is to do a property based search. This can easily be achieved with the Spatial Data Services module by specifying a data source and a filter.

```
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <meta charset="utf-8" />
	<script type='text/javascript'>
    var map;

    //Query URL to the NAVTEQ POI data source
    var sdsDataSourceUrl = 'http://spatial.virtualearth.net/REST/v1/data/f22876ec257b474b82fe2ffcb8393150/NavteqNA/NavteqPOIs';

    function GetMap() {
        map = new Microsoft.Maps.Map('#myMap', {
            credentials: 'Your Bing Maps Key',
            zoom: 2
        });

        //Load the Bing Spatial Data Services module.
        Microsoft.Maps.loadModule('Microsoft.Maps.SpatialDataService', function () {
            findByPropperty();
        });
    }

    function findByPropperty() {
        //Remove any existing data from the map.
        map.entities.clear();

        //Create a query to get nearby data.
        var queryOptions = {
            queryUrl: sdsDataSourceUrl,
            filter: new Microsoft.Maps.SpatialDataService.Filter('EntityTypeID', 'eq', 5540) //Filter to retrieve Gas Stations.
        };

        //Process the query.
        Microsoft.Maps.SpatialDataService.QueryAPIManager.search(queryOptions, map, function (data) {
            //Add results to the map.
            map.entities.push(data);
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

Running this code will search for the first 25 gas stations in the [NavteqNA data source](../spatial-data-services/navteqna.md).

![BMV8_FindByPropertyExample](../../media/bmv8-findbypropertyexample.PNG)