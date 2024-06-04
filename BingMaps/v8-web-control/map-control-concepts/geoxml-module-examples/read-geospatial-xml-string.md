---
title: "Read Geospatial XML String | Microsoft Docs"
description: Provides a code example that shows how to read geospatial XML data stored in a string and render it on a map.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: ecfbb1d9-0a4f-48f6-a02b-487d85bc54e7
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Read Geospatial XML String

[!INCLUDE [bing-maps-web-control-sdk-retirement](../../../includes/bing-maps-web-control-sdk-retirement.md)]

This sample shows how to read geospatial XML data stored in a string. When reading geospatial XML data using the read and readFromUrl functions you have complete control of the data, you can render it or simply extract information from it. In this sample we will render it on the map. 

```html
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <meta charset="utf-8" />
    <script type='text/javascript'>
    var map;
    var georss = '<feed xmlns="http://www.w3.org/2005/Atom" xmlns:georss="http://www.georss.org/georss"><entry><title>Sample Polygon</title><georss:polygon>46.31409 -122.22616 46.31113 -122.22968 46.31083 -122.23320</georss:polygon></entry></feed>';

    function GetMap()
    {
        map = new Microsoft.Maps.Map('#myMap', {
            credentials: 'Your Bing Maps Key'
        });

        //Load the GeoXml module.
        Microsoft.Maps.loadModule('Microsoft.Maps.GeoXml', function () {
            //Parse the XML data.
            var data = Microsoft.Maps.GeoXml.read(georss);

            //Do something with the parsed XML data, in this case render it.
            renderGeoXmlDataSet(data);
        });
    }

    function renderGeoXmlDataSet(data) {
        //Remove all existing data from the map.
        map.entities.clear();
        map.layers.clear();

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
    <script src='https://www.bing.com/api/maps/mapcontrol?callback=GetMap' async defer></script>
</head>
<body>
    <div id="myMap" style="position:relative;width:800px;height:600px;"></div>
</body>
</html>
```

If you run this sample you will see a simple polygon that was defined in a string in GeoRSS format rendered on the map.

![Screenshot of a Bing map showing a triangle overlaid on top of a landmass.](../../media/bmv8-basicgeoxml.PNG)

[Try it now](https://samples.bingmapsportal.com/?search=Read%20Geospatial%20XML%20String)
