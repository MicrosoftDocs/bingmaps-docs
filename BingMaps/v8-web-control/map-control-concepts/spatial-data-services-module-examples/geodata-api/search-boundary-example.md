---
title: "Search Boundary Example | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 4766c274-66b3-4afa-be08-6f781b1060ec
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Search Boundary Example

In common uses of this module, developers will retrieve boundaries when the entity type of the boundary to return is specified. This is useful to get the boundary of a location that has a different entity type than your input data.  

However, what if you want to get the boundary of a location and don't know what it's entity type is? In this code sample, the search module is used to geocode a user's inputted location. If the geocoded result has an entity type value that is supported by the GeoData API, a boundary will then be requested and rendered on the map if available. In this sample, the level of detail of the polygons is set to 1 so that they are more detailed. If a location is passed in that does not have a supported boundary or a boundary can't be found, a pushpin will be displayed on the map instead.

```html
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <meta charset="utf-8" />
	<script type='text/javascript'>
    var map, searchManager;

    function GetMap() {
        map = new Microsoft.Maps.Map('#myMap', {
            credentials: ‘Your Bing Maps Key’
        });
        map = map;

        //Load the Bing Spatial Data Services and Search modules, then create an instance of the search manager.
        Microsoft.Maps.loadModule(['Microsoft.Maps.SpatialDataService',
            'Microsoft.Maps.Search'], function () {
                searchManager = new Microsoft.Maps.Search.SearchManager(map);
            });
    }

    function Search() {
        //Remove all data from the map.
        map.entities.clear();

        //Create the geocode request.
        var geocodeRequest = {
            where: document.getElementById('inputTbx').value,
            callback: getBoundary,
            errorCallback: function (e) {
                //If there is an error, alert the user about it.
                alert("No results found.");
            }
        };

        //Make the geocode request.
        searchManager.geocode(geocodeRequest);
    }

    function getBoundary(geocodeResult){
        //Add the first result to the map and zoom into it.
        if (geocodeResult && geocodeResult.results && geocodeResult.results.length > 0) {
            //Zoom into the location.
            map.setView({ bounds: geocodeResult.results[0].bestView });

            //Create the request options for the GeoData API.
            var geoDataRequestOptions = {
                lod: 1,
                getAllPolygons: true
            };

            //Verify that the geocoded location has a supported entity type.
            switch (geocodeResult.results[0].entityType) {
                case "CountryRegion":
                case "AdminDivision1":
                case "AdminDivision2":
                case "Postcode1":
                case "Postcode2":
                case "Postcode3":
                case "Postcode4":
                case "Neighborhood":
                case "PopulatedPlace":
                    geoDataRequestOptions.entityType = geocodeResult.results[0].entityType;
                    break;
                default:
                    //Display a pushpin if GeoData API does not support EntityType.
                    var pin = new Microsoft.Maps.Pushpin(geocodeResult.results[0].location);
                    map.entities.push(pin);
                    return;
            }

            //Use the GeoData API manager to get the boundaries of the zip codes.
            Microsoft.Maps.SpatialDataService.GeoDataAPIManager.getBoundary(
                geocodeResult.results[0].location,
                geoDataRequestOptions,
                map,
                function (data) {
                    //Add the polygons to the map.
                    if (data.results && data.results.length > 0) {
                        map.entities.push(data.results[0].Polygons);
                    } else {
                        //Display a pushpin if a boundary isn't found.
                        var pin = new Microsoft.Maps.Pushpin(data.location);
                        map.entities.push(pin);
                    }
                });
        }
    }
    </script>
    <script type='text/javascript' src='http://www.bing.com/api/maps/mapcontrol?callback=GetMap' async defer></script>
</head>
<body>
    <input type="text" id="inputTbx"/>
    <input type="button" value="Search" onclick="Search()"/>
    <br/>
    <div id="myMap" style="position:relative;width:600px;height:400px;"></div>
</body>
</html>
```

Running this code will load a textbox, a button and a map. Type in a location into the textbox and press search. If the location has an entity type value that is supported by the GeoData API, a boundary will be requested and if available, displayed on the map. Here is an example when searching for New York City.

![Search Boundary on a Map](../../../media/bmv8-geodataboundarysearch.png)
 
[Try it now](https://www.bing.com/api/maps/sdk/mapcontrol/isdk#sdsLoadBoundaryFromSearch+JS)