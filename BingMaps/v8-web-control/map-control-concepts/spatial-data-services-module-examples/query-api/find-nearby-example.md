---
title: "Find Nearby Example | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: b0d06ab0-6748-439c-b68b-fb393182ba95
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Find Nearby Example

One of the most common types of searches done with a map is a nearby search, also known as a radial search. In the example an event handler is added to the maps **viewchangeend** event. When the map is panned or zoomed this event will trigger a query to the [NAVTEQ Point of Interest data source](../../../../spatial-data-services/public-data-sources/navteqna.md) in Bing Spatial Data Services and will retrieve up to 25 gas stations that are within 25 kilometers of the center of the map. A filter will be used to limit the results to those that have an **EntityTypeID** value of **5540**, which is the ID used for Gas Stations in this data source.

```html
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <meta charset="utf-8" />
	<script type='text/javascript'>
    var map;

    //Query URL to the NAVTEQ POI data source
    var sdsDataSourceUrl = 'https://spatial.virtualearth.net/REST/v1/data/f22876ec257b474b82fe2ffcb8393150/NavteqNA/NavteqPOIs';

    function GetMap() {
        map = new Microsoft.Maps.Map('#map', {});

        //Load the Bing Spatial Data Services module.
        Microsoft.Maps.loadModule('Microsoft.Maps.SpatialDataService', function () {
            //Add an event handler for when the map moves.
            Microsoft.Maps.Events.addHandler(map, 'viewchangeend', getNearByLocations);

            //Trigger an initial search.
            getNearByLocations();
        });
    }

    function getNearByLocations() {
        //Remove any existing data from the map.
        map.entities.clear();

        //Create a query to get nearby data.
        var queryOptions = {
            queryUrl: sdsDataSourceUrl,
            spatialFilter: {
                spatialFilterType: 'nearby',
                location: map.getCenter(),
                radius: 25
            },
            //Filter to retrieve Gas Stations.
            filter: new Microsoft.Maps.SpatialDataService.Filter('EntityTypeID','eq',5540) 
        };

        //Process the query.
        Microsoft.Maps.SpatialDataService.QueryAPIManager.search(queryOptions, map, function (data) {
            //Add results to the map.
            map.entities.push(data);
        });
    }
    </script>
    <script type='text/javascript' src='http://www.bing.com/api/maps/mapcontrol?callback=GetMap&key=[YOUR_BING_MAPS_KEY]' async defer></script>
</head>
<body>
    <div id="map" style="position:relative;width:600px;height:400px;"></div>
</body>
</html>
```

Running this code will load a map that displays the locations of gas stations. As you pan and zoom the map new data will be pulled in. Here is a screenshot of gas stations in Bellevue, WA.

![Search Results on a Map](../../../media/bmv8-basicfindnearbyexample.png)

[Try it now](https://www.bing.com/api/maps/sdk/mapcontrol/isdk?sdsNearbySearch+JS#sdsNearbySearch+JS)
