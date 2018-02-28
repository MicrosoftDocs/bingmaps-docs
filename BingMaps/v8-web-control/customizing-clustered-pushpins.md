---
title: "Customizing Clustered Pushpins | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 5091ce5a-25b3-436a-819b-0707b04124b7
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# Customizing Clustered Pushpins
By default, the clustering layer uses the default pushpin and sets the text option to the number of pushpins that are in the cluster. Customizing the clustered pushpins can be done by passing a callback function into the `clusteredPinCallback` option of the cluster layer. This callback will receive a reference to a [ClusterPushpin](../v8-web-control/clusterpushpin-class.md) object which is special pushpin that has a couple of extra properties on it. You can customize the ClusterPushpin the same way you would a standard pushpin, using the `setOptions` function. For example:

```
var clusterLayer = new Microsoft.Maps.ClusterLayer(pins, {
    clusteredPinCallback: function (cluster) {
        //Customize clustered pushpin.
        cluster.setOptions({
            icon: '[custom pushpin info]'
        });
    }
});
```

There are many different ways to customize a pushpin in Bing Maps such as using a URL to an image or SVG file, using inline SVG or a Base64 image string. Documentation on how to create these different types of custom pushpins [here](../v8-web-control/pushpins.md).

In this code example, instead of simply using a custom image to represent a clustered pushpin, we will see how to dynamically create an inline SVG icon based on the number of pushpins that are in the cluster. Clusters will be represented using a circle. The more pushpins in the cluster the larger the circle will become, using a logarithmic scale. Since the size of the circles will grow, we will increase the grid size used by the clustering layer to accommodate this. Additionally, if a cluster has less than 10 pushpins, the circle will be green, less than 100 pushpins, yellow, more than 100, red. 

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
                clusteredPinCallback: createCustomClusteredPin,
                gridSize: 80
            });
            map.layers.insert(clusterLayer);
        });
	}

	function createCustomClusteredPin(cluster) {
	    //Define variables for minimum cluster radius, and how wide the outline area of the circle should be.
	    var minRadius = 12;
	    var outlineWidth = 7;

        //Get the number of pushpins in the cluster
	    var clusterSize = cluster.containedPushpins.length;

        //Calculate the radius of the cluster based on the number of pushpins in the cluster, using a logarithmic scale.
	    var radius = Math.log(clusterSize) / Math.log(10) * 5 + minRadius;

        //Default cluster color is red.
	    var fillColor = 'rgba(255, 40, 40, 0.5)';

	    if (clusterSize < 10) {
	        //Make the cluster green if there are less than 10 pushpins in it.
	        fillColor = 'rgba(20, 180, 20, 0.5)';            
	    } else if (clusterSize < 100) {
	        //Make the cluster yellow if there are 10 to 99 pushpins in it.
	        fillColor = 'rgba(255, 210, 40, 0.5)';
	    }

	    //Create an SVG string of two circles, one on top of the other, with the specified radius and color.
	    var svg = ['<svg xmlns="http://www.w3.org/2000/svg" width="', (radius * 2), '" height="', (radius * 2), '">',
            '<circle cx="', radius, '" cy="', radius, '" r="', radius, '" fill="', fillColor, '"/>',
            '<circle cx="', radius, '" cy="', radius, '" r="', radius - outlineWidth, '" fill="', fillColor, '"/>',
            '</svg>'];

	    //Customize the clustered pushpin using the generated SVG and anchor on its center.
	    cluster.setOptions({
	        icon: svg.join(''),
	        anchor: new Microsoft.Maps.Point(radius, radius),
	        textOffset: new Microsoft.Maps.Point(0, radius - 8) //Subtract 8 to compensate for height of text.
	    });
	}
    </script>
</head>
<body>
    <div id="myMap" style="position:relative;width:600px;height:400px;"></div>
</body>
</html>
```

Running this code in a browser will cluster 3,000 random pushpins and display them as scaled and colored circles. 

![BMV8_CustomClusteredPushpinsExample](../v8-web-control/media/bmv8-customclusteredpushpinsexample.png)

[Try it now](http://www.bing.com/api/maps/sdk/mapcontrol/isdk#customizeClusteredPushpins+JS)