---
title: "Traffic Module Examples | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 3691cdfa-6d19-4f65-b86e-af56e6e35092
caps.latest.revision: 4
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Traffic Module Examples
The Bing Maps SDK provides two types of traffic data through the Traffic module. The first type is a tile layer that shows traffic flow data. This highlights roads with different colors to indicate what the flow of traffic is like compared to the speed limits on those roads. The second type of traffic data is traffic incidents. Traffic incidents are point based data that represent things like road closures, accidents, and construction. Traffic data coverage information can be found [here](../coverage/bing-maps-traffic-coverage.md).

## Example

This examples shows how to display traffic data on top of the map.

```
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <meta charset="utf-8" />
	<script type='text/javascript'>
    var map, trafficManager;

    function GetMap()
    {
        map = new Microsoft.Maps.Map('#myMap', {});

        //Load traffic module.
        Microsoft.Maps.loadModule('Microsoft.Maps.Traffic', function () {
            //Create an instance of the traffic manager and bind to map.
            trafficManager = new Microsoft.Maps.Traffic.TrafficManager(map);

            //Display the traffic data.
            trafficManager.show();
        });
    }
    </script>
    <script type='text/javascript' src='http://www.bing.com/api/maps/mapcontrol?callback=GetMap&key=[YOUR_BING_MAPS_KEY]' async defer></script>
</head>
<body>
    <div id="myMap" style="position:relative;width:600px;height:400px;"></div>
</body>
</html>
```

If you run this code in a browser and zoom into a city that is likely to have a lot of traffic like New York city, you will see color coded roads indicating the flow of traffic and possibly triangle icons indicating traffic incidents on the road. If you hover over and incident a tooltip will appear with some details about the incident.

![BMV8_TrafficModuleExample](../v8-web-control/media/bmv8-trafficmoduleexample.png)

[Try it now](http://www.bing.com/api/maps/sdk/mapcontrol/isdk#trafficHideShowTraffic+JS)

## See Also

* [Traffic Module](../v8-web-control/traffic-module.md)
* [TrafficOptions Object](../v8-web-control/trafficoptions-object.md)