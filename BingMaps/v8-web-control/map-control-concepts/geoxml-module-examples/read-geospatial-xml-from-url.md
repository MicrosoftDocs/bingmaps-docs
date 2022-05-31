---
title: "Read Geospatial XML from URL | Microsoft Docs"
description: Provides a code example that shows how to read a geospatial XML file that is hosted on the same domain as the application using a relative URL.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 7e46115b-6bae-4097-ae26-af28b02127f3
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Read Geospatial XML from URL

This sample shows how to read a geospatial XML file that is hosted on the same domain as the application using a relative URL. This sample will read in a sample GeoRSS file which you can find [here](https://bingmapsv8samples.azurewebsites.net/GeoXml/Data/GeoRSS/SampleGeoRss.xml) and render it on the map. When reading geospatial XML data using the read and readFromUrl functions you have complete control of the data, you can render it or simply extract information from it. In this sample we will render the data on the map. 

```html
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <meta charset="utf-8" />
    <script type='text/javascript'>
    var map;
    var xmlUrl = 'SampleGeoRSS.xml';

    function GetMap()
    {
        map = new Microsoft.Maps.Map('#myMap', {
            credentials: 'Your Bing Maps Key'
        });

        //Load the GeoXml module.
        Microsoft.Maps.loadModule('Microsoft.Maps.GeoXml', function () {
            //Parse the XML data.
            Microsoft.Maps.GeoXml.readFromUrl(xmlUrl, null, function (data) {
                //Do something with the parsed XML data, in this case render it.
                renderGeoXmlDataSet(data);
            });
        });
    }

    function renderGeoXmlDataSet(data) {
        //Add all shapes that are not in layers to the map.
        if (data.shapes) {
            map.entities.push(data.shapes);
        }

        //Add all data layers to the map.
        if (data.layers) {
            for (var i = 0, len = data.layers.length; i < len; i++) {
                map.layers.insert(data.layers[i]);
            }
        }

        //Add all screen overlays to the map.
        if (data.screenOverlays) {
            for (var i = 0, len = data.screenOverlays.length; i < len; i++) {
                map.layers.insert(data.screenOverlays[i]);
            }
        }

        if (data.summary && data.summary.bounds) {
            //Set the map view to focus show the data.
            map.setView({ bounds: data.summary.bounds, padding: 30 });
        }
    }
    </script>
    <script type='text/javascript' src='https://www.bing.com/api/maps/mapcontrol?callback=GetMap' async defer></script>
</head>
<body>
    <div id="myMap" style="position:relative;width:800px;height:600px;"></div>
</body>
</html>
```

If you run this code it will load the specified GeoRSS feed and render it on the map.

![Screenshot of a Bing Map that shows a polygon shape overlaid onto the Coldwater Lake and hiking trail icons on the map.](../../media/bmv8-georsssample.PNG)

[Try it now](https://bingmapsv8samples.azurewebsites.net/#GeoXml%20-%20Read%20from%20Url)

