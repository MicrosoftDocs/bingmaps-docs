---
title: "Zoom into Clusters | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 8b20ab8e-8a6a-40da-afed-5c17fbb74e88
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# Zoom into Clusters
This example adds a click event to the clustered pushpins. When clicked, a bounding box is calculated based on the location of the pushpins in the cluster. This bounding box is then used to zoom into the cluster. A padding is added when setting the map view to provide a buffer to account for the pushpin icon pixel size. If it highly possible that when zooming into a cluster that not all individual pushpins will be displayed as some pushpin may form smaller clusters.

```
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <meta charset="utf-8" />
    <script type='text/javascript'
            src='http://www.bing.com/api/maps/mapcontrol?callback=GetMap' async defer></script>
    <script type="text/javascript">
    var map, clusterLayer;

	function GetMap() {
	    map = new Microsoft.Maps.Map('#myMap',{
	        credentials: 'Your Bing Maps Key',
            zoom: 3
	    });

        Microsoft.Maps.loadModule("Microsoft.Maps.Clustering", function () {
            //Generate 3000 random pushpins in the map view.
            var pins = Microsoft.Maps.TestDataGenerator.getPushpins(3000, map.getBounds());

            //Create a ClusterLayer with options and add it to the map.
            clusterLayer = new Microsoft.Maps.ClusterLayer(pins, {
                clusteredPinCallback: customizeClusteredPin
            });
            map.layers.insert(clusterLayer);
        });
	}

	function customizeClusteredPin(cluster) {
           //Add click event to clustered pushpin
	    Microsoft.Maps.Events.addHandler(cluster, 'click', clusterClicked);
	}

	function clusterClicked(e) {
	    if (e.target.containedPushpins) {
	        var locs = [];
	        for (var i = 0, len = e.target.containedPushpins.length; i < len; i++) {
                //Get the location of each pushpin.
	            locs.push(e.target.containedPushpins[i].getLocation());
	        }

	        //Create a bounding box for the pushpins.
	        var bounds = Microsoft.Maps.LocationRect.fromLocations(locs);

	        //Zoom into the bounding box of the cluster. 
	        //Add a padding to compensate for the pixel area of the pushpins.
	        map.setView({ bounds: bounds, padding: 100 });
	    }
	}
    </script>
</head>
<body>
    <div id="myMap" style="position:relative;width:600px;height:400px;"></div>
</body>
</html>
```