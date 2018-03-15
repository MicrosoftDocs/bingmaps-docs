---
title: "Basic Reverse Geocode Example | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 0e128463-8c86-4284-93ab-0d7abc73b439
caps.latest.revision: 4
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Basic Reverse Geocode Example
The following code sample shows how to make a reverse geocode request using the Search module. This code loads the search module if it isn’t already loaded. It then reverse geocodes the center of the map and, if successful, it will show a message on the screen with the display name (often an address) of the reverse geocoded location.

```
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <meta charset="utf-8" />
    <script type='text/javascript'>
    var map, searchManager;

    function GetMap() {
        map = new Microsoft.Maps.Map('#myMap', {
            credentials: 'Your Bing Maps Key',
            center: new Microsoft.Maps.Location(47.678, -122.133),
            zoom: 11
        });

        //Make a request to reverse geocode the center of the map.
        reverseGeocode();
    }

    function reverseGeocode() {
        //If search manager is not defined, load the search module.
        if (!searchManager) {
            //Create an instance of the search manager and call the reverseGeocode function again.
            Microsoft.Maps.loadModule('Microsoft.Maps.Search', function () {
                searchManager = new Microsoft.Maps.Search.SearchManager(map);
                reverseGeocode();
            });
        } else {
            var searchRequest = {
                location: map.getCenter(),
                callback: function (r) {
                    //Tell the user the name of the result.
                    alert(r.name);
                },
                errorCallback: function (e) {
                    //If there is an error, alert the user about it.
                    alert("Unable to reverse geocode location.");
                }
            };

            //Make the reverse geocode request.
            searchManager.reverseGeocode(searchRequest);
        }
    }
    </script>    
    <script type='text/javascript' src='http://www.bing.com/api/maps/mapcontrol?callback=GetMap' async defer></script>
</head>
<body>
    <div id="myMap" style="position:relative;width:600px;height:400px;"></div>
</body>
</html>
```

Here is what the result looks like when centered over a location in Redmond, WA.

![Reverse Geocode Exapmle Map](../v8-web-control/media/bmv8-reversegeocodeexample.png)

[Try it now](https://bingmapsv8samples.azurewebsites.net/#Reverse%20Geocode)