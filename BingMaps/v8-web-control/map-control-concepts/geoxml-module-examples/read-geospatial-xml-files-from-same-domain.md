---
title: "Read Geospatial XML Files from Same Domain | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 29e1ac9c-3e2c-4015-95dc-6cab557ce226
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Read Geospatial XML Files from Same Domain

This sample shows how to load a geospatial XML file that is hosted on the same domain as the application using a relative URL into a GeoXmlLayer. This sample will read in a sample GeoRSS file and render it on the map. 

```html
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <meta charset="utf-8" />
    <script type='text/javascript'>
    var map, layer;
    var xmlUrl = 'SampleGeoRSS.xml';

    function GetMap() {
        map = new Microsoft.Maps.Map('#myMap', {
            credentials: 'Your Bing Maps Key',
            zoom: 1
        });

        //Load the GeoXml module.
        Microsoft.Maps.loadModule('Microsoft.Maps.GeoXml', function () {
            //Create an instance of the GeoXmlLayer and pass in the URL to the GeoRSS file that is hosted on the same domain.
            layer = new Microsoft.Maps.GeoXmlLayer(xmlUrl, true);

            //Add the layer to the map.
            map.layers.insert(layer);
        });
    }
    </script>
    <script type='text/javascript' src='https://www.bing.com/api/maps/mapcontrol?callback=GetMap' async defer></script>
</head>
<body>
    <div id="myMap" style="position:relative;width:800px;height:600px;"></div>
</body>
</html>
```

Running this sample (when you have the sample GeoRSS file) will load a map that looks like this.
 
![BMV8_GeoRssSample](../../media/bmv8-georsssample.PNG)
 
[Try it now](https://bingmapsv8samples.azurewebsites.net/#GeoXmlLayer%20-%20Same%20Domain)

**Note:** Not all file and mime types are enabled in all servers. If using .NET, it is recommended to add the following to the web.config file:

```xml
<configuration>
  <system.webServer>
    <staticContent>
      <remove fileExtension=".json"/>
      <mimeMap fileExtension=".json" mimeType="application/json" />
      <mimeMap fileExtension=".geojson" mimeType="application/json" />
      <mimeMap fileExtension=".gpx" mimeType="application/xml" />
      <mimeMap fileExtension=".georss" mimeType="application/xml" />
      <mimeMap fileExtension=".kml" mimeType="application/vnd.google-earth.kml+xml" />
      <mimeMap fileExtension=".kmz" mimeType="application/vnd.google-earth.kmz" />
    </staticContent>
</configuration>
```
