---
title: "Paged Search Results Example | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: c3542e7e-8b9f-429a-9b0e-063c6b0cf0f9
caps.latest.revision: 5
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Paged Search Results Example

This code example takes a data source and performs an initial radial search of 10 kilometers. It then displays the first 10 results on the map and also creates a list of the results below the map. Clicking on any item in the list below the map triggers an event that looks up the associated pushpin, then zooms and centers the map over it. Because there are more than 10 results for the initial query, this code sample lets you page through the results (10 at a time.) The Forth Coffee Cup data source is used in this example and contains a set of fictitious coffee shop locations. 

```html
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <meta charset="utf-8" />
	<script type='text/javascript'>
    var sdsDataSourceUrl = 'http://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops';

    var map, pageIdx = 0, queryOptions, numResults;

    function GetMap() {
        map = new Microsoft.Maps.Map('#myMap', {
            credentials: 'Your Bing Maps Key',
            center: new Microsoft.Maps.Location(47.678, -122.133),
            zoom: 13
        });

        //Load the Bing Spatial Data Services module.
        Microsoft.Maps.loadModule('Microsoft.Maps.SpatialDataService', function () {
            //Create a query to get nearby data.
            queryOptions = {
                queryUrl: sdsDataSourceUrl,
                top: 10,
                inlineCount: true,
                spatialFilter: {
                    spatialFilterType: 'nearby',
                    location: map.getCenter(),
                    radius: 10
                }
            };

            //Trigger an initial search.
            getNearByLocations();
        });
    }

    function getNearByLocations() {
        //Remove any existing data from the map.
        map.entities.clear();

        //Update the query options to skip results based on the page index.
        queryOptions.skip = pageIdx * 10,

        Microsoft.Maps.SpatialDataService.QueryAPIManager.search(queryOptions, map,
        function (data, inlineCount) {
            //Store the number of results available.
            numResults = inlineCount;

            if (data.length > 0) {
                //Calculate the start and end result index.
                var start = pageIdx * 10 + 1;
                var end = start + data.length - 1;

                document.getElementById('pageInfo').innerText = 'Results: ' + start + ' - '
                    + end + ' of ' + inlineCount + ' results';

                //Create a list of the results.
                var listHTML = ['<table>'],
                    locations = [];

                for (var i = 0; i < data.length; i++) {
                    //Create HTML for each line item in the list. 

                    //Add a column of index numbers.
                    listHTML.push('<tr><td>', (start + i), ') </td>');

                    //Create a link that calls a function, pass in the EntityID of a result.
                    listHTML.push('<td><a href="javascript:void(0);" ',
                        'onclick="listItemClicked(\'', data[i].metadata.EntityID, '\');">',
                        data[i].metadata.DisplayName, '</a></td>');

                    //Create a column to display the distance to the location.
                    listHTML.push('<td>', data[i].metadata.__Distance.toFixed(2),
                        ' km(s)</td></tr>');

                    //Add the result number to the pushpin.
                    data[i].setOptions({ text: start + i + '' });

                    locations.push(data[i].getLocation());
                }

                listHTML.push('</table>');

                document.getElementById('resultList').innerHTML = listHTML.join('');

                //Add results to the map.
                map.entities.push(data);

                //Set the map view to show all the locations. 
                //Add padding to account for the pushpins pixel size.
                map.setView({
                    bounds: Microsoft.Maps.LocationRect.fromLocations(locations),
                    padding: 30
                });
            }
        });
    }

    function listItemClicked(entityId) {
        //When an item in the list is clicked, look up its pushpin by entitiyId.
        var shape, len = map.entities.getLength();

        for (var i = 0; i < len; i++) {
            shape = map.entities.get(i);
        
            if (shape.metadata.EntityID == entityId) {
                //Center the map over the pushpin and zoom in.
                map.setView({ center: shape.getLocation(), zoom: 15 });
                break;
            }
        }
    }

    function pageBackwards() {
        if (pageIdx > 0) {
            pageIdx--;
            getNearByLocations();
        }
    }

    function pageForward() {
        //Ensure that paging does not exceed the number of results.
        if ((pageIdx + 1) * 10 < numResults) {
            pageIdx++;
            getNearByLocations();
        }
    }
    </script>
    <script type='text/javascript' src='http://www.bing.com/api/maps/mapcontrol?callback=GetMap' async defer></script>
</head>
<body>
    <div id="myMap" style="position:relative;width:600px;height:400px;"></div>
    <div style="margin-top:10px;">
        <input type="button" value="<" onclick="pageBackwards();" />
        <input type="button" value=">" onclick="pageForward();" /><br /><br />
        <div id="pageInfo"></div><br />
        <div id="resultList"></div>
    </div>
</body>
</html>
```

Running this code will load a map that display up to 10 Forth Coffee Cup locations at a time that are within 10 kilometers of Bellevue, WA. Pressing the forward or backwards button will trigger a new request that pages through the results of the initial query. Additionally, each result is displayed in a list, clicking on an item will result in the map zooming and centering over that location. This is a very common set of functionalities used in store locators.

![Paged Search Results on a Map](../../../media/bmv8-pagednearbyresultsexample.png)

[Try it now](https://www.bing.com/api/maps/sdk/mapcontrol/isdk?sdsNearbySearch+JS#sdsPageResults+JS)