---
title: "Basic Contour Layer | Microsoft Docs"
description: "Describes the basic contour layer and provides the layer's example and a link that lets you try creating a basic contour layer yourself."
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 0f576d65-320b-467a-85fd-529504fee27a
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Basic Contour Layer

This example takes contour line data that represents elevations around Mount Rainer. Each contour line has an elevation assigned to it in meters. The colour of the contour areas will be based on the elevation where a value of 4000 or more will be green, 3500 to 4000 will be light green, 3000 to 3500 more will be yellow, and 2000 to 3000 will be orange.

```html
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <meta charset="utf-8" />

    <script type='text/javascript'
            src='https://www.bing.com/api/maps/mapcontrol?callback=GetMap'
            async defer></script>

    <script type='text/javascript'>
    var map;

    function GetMap()
    {
        map = new Microsoft.Maps.Map('#myMap', {
            credentials: 'Your Bing Maps Key',
            center: new Microsoft.Maps.Location(46.854048, -121.768712),
            zoom: 11
        });

        //Load the Contour module.
        Microsoft.Maps.loadModule('Microsoft.Maps.Contour', function () {
            //Create some contour lines.
            var contourLine1 = new Microsoft.Maps.ContourLine([new Microsoft.Maps.Location(46.842308, -121.770771), new Microsoft.Maps.Location(46.847944, -121.752232), new Microsoft.Maps.Location(46.854048, -121.752232), new Microsoft.Maps.Location(46.860622, -121.761845), new Microsoft.Maps.Location(46.864378, -121.763905), new Microsoft.Maps.Location(46.864378, -121.770085), new Microsoft.Maps.Location(46.866256, -121.780385), new Microsoft.Maps.Location(46.864378, -121.787251), new Microsoft.Maps.Location(46.856866, -121.775578), new Microsoft.Maps.Location(46.847474, -121.776265), new Microsoft.Maps.Location(46.845126, -121.775578)], 4000);
            var contourLine2 = new Microsoft.Maps.ContourLine([new Microsoft.Maps.Location(46.837141, -121.776265), new Microsoft.Maps.Location(46.838081, -121.757039), new Microsoft.Maps.Location(46.842308, -121.749485), new Microsoft.Maps.Location(46.848883, -121.740559), new Microsoft.Maps.Location(46.856396, -121.741932), new Microsoft.Maps.Location(46.863909, -121.750859), new Microsoft.Maps.Location(46.863909, -121.756352), new Microsoft.Maps.Location(46.868134, -121.761845), new Microsoft.Maps.Location(46.868134, -121.768025), new Microsoft.Maps.Location(46.870950, -121.774205), new Microsoft.Maps.Location(46.870950, -121.781071), new Microsoft.Maps.Location(46.872828, -121.787251), new Microsoft.Maps.Location(46.861561, -121.794117), new Microsoft.Maps.Location(46.854518, -121.787938), new Microsoft.Maps.Location(46.853109, -121.783131), new Microsoft.Maps.Location(46.846065, -121.783818)], 3500);
            var contourLine3 = new Microsoft.Maps.ContourLine([new Microsoft.Maps.Location(46.830565, -121.774891), new Microsoft.Maps.Location(46.830565, -121.756352), new Microsoft.Maps.Location(46.830565, -121.756352), new Microsoft.Maps.Location(46.832914, -121.746052), new Microsoft.Maps.Location(46.833383, -121.733693), new Microsoft.Maps.Location(46.839020, -121.730946), new Microsoft.Maps.Location(46.839490, -121.726826), new Microsoft.Maps.Location(46.848413, -121.724080), new Microsoft.Maps.Location(46.857335, -121.730946), new Microsoft.Maps.Location(46.861092, -121.734379), new Microsoft.Maps.Location(46.865317, -121.735066), new Microsoft.Maps.Location(46.868134, -121.743306), new Microsoft.Maps.Location(46.871420, -121.748112), new Microsoft.Maps.Location(46.871889, -121.754292), new Microsoft.Maps.Location(46.877991, -121.754979), new Microsoft.Maps.Location(46.872359, -121.767338), new Microsoft.Maps.Location(46.876114, -121.774205), new Microsoft.Maps.Location(46.876114, -121.779698), new Microsoft.Maps.Location(46.882215, -121.787251), new Microsoft.Maps.Location(46.876583, -121.790684), new Microsoft.Maps.Location(46.875175, -121.794804), new Microsoft.Maps.Location(46.870011, -121.800297), new Microsoft.Maps.Location(46.863439, -121.806477), new Microsoft.Maps.Location(46.857335, -121.807850), new Microsoft.Maps.Location(46.854988, -121.801671), new Microsoft.Maps.Location(46.849822, -121.803730), new Microsoft.Maps.Location(46.846535, -121.798924), new Microsoft.Maps.Location(46.841369, -121.795491), new Microsoft.Maps.Location(46.836672, -121.796864), new Microsoft.Maps.Location(46.836672, -121.788624)], 3000);
            var contourLine4 = new Microsoft.Maps.ContourLine([new Microsoft.Maps.Location(46.851231, -121.714467), new Microsoft.Maps.Location(46.847474, -121.712407), new Microsoft.Maps.Location(46.847944, -121.707600), new Microsoft.Maps.Location(46.851231, -121.709660), new Microsoft.Maps.Location(46.851231, -121.713780)], 3000);
            var contourLine5 = new Microsoft.Maps.ContourLine([new Microsoft.Maps.Location(46.813180, -121.783818), new Microsoft.Maps.Location(46.803311, -121.763905), new Microsoft.Maps.Location(46.806131, -121.757725), new Microsoft.Maps.Location(46.806131, -121.752232), new Microsoft.Maps.Location(46.812241, -121.749485), new Microsoft.Maps.Location(46.812711, -121.740559), new Microsoft.Maps.Location(46.809421, -121.734379), new Microsoft.Maps.Location(46.802841, -121.734379), new Microsoft.Maps.Location(46.802841, -121.724766), new Microsoft.Maps.Location(46.809421, -121.721333), new Microsoft.Maps.Location(46.808481, -121.715153), new Microsoft.Maps.Location(46.806601, -121.715840), new Microsoft.Maps.Location(46.806131, -121.710347), new Microsoft.Maps.Location(46.806601, -121.706227), new Microsoft.Maps.Location(46.809421, -121.700734), new Microsoft.Maps.Location(46.822578, -121.707600), new Microsoft.Maps.Location(46.827746, -121.703480), new Microsoft.Maps.Location(46.825397, -121.696614), new Microsoft.Maps.Location(46.827276, -121.691807), new Microsoft.Maps.Location(46.821169, -121.685627), new Microsoft.Maps.Location(46.818819, -121.667775), new Microsoft.Maps.Location(46.823048, -121.666401), new Microsoft.Maps.Location(46.825397, -121.660222), new Microsoft.Maps.Location(46.832914, -121.665028), new Microsoft.Maps.Location(46.839020, -121.669835), new Microsoft.Maps.Location(46.839490, -121.660908), new Microsoft.Maps.Location(46.845126, -121.656102), new Microsoft.Maps.Location(46.852170, -121.650609), new Microsoft.Maps.Location(46.852640, -121.640309), new Microsoft.Maps.Location(46.847944, -121.634129), new Microsoft.Maps.Location(46.846535, -121.619023), new Microsoft.Maps.Location(46.841369, -121.613530), new Microsoft.Maps.Location(46.847474, -121.609410), new Microsoft.Maps.Location(46.853109, -121.612843), new Microsoft.Maps.Location(46.854048, -121.618336), new Microsoft.Maps.Location(46.853579, -121.625203), new Microsoft.Maps.Location(46.857805, -121.625889), new Microsoft.Maps.Location(46.856866, -121.631382), new Microsoft.Maps.Location(46.860622, -121.633442), new Microsoft.Maps.Location(46.857335, -121.636189), new Microsoft.Maps.Location(46.856396, -121.644429), new Microsoft.Maps.Location(46.860153, -121.645802), new Microsoft.Maps.Location(46.859683, -121.650609), new Microsoft.Maps.Location(46.856396, -121.651982), new Microsoft.Maps.Location(46.854048, -121.661595), new Microsoft.Maps.Location(46.859683, -121.662968), new Microsoft.Maps.Location(46.862500, -121.673268), new Microsoft.Maps.Location(46.862031, -121.679448), new Microsoft.Maps.Location(46.862500, -121.687001), new Microsoft.Maps.Location(46.866725, -121.689061), new Microsoft.Maps.Location(46.870011, -121.698674), new Microsoft.Maps.Location(46.878461, -121.704167), new Microsoft.Maps.Location(46.885500, -121.694554), new Microsoft.Maps.Location(46.883154, -121.707600), new Microsoft.Maps.Location(46.887378, -121.717900), new Microsoft.Maps.Location(46.891132, -121.708973), new Microsoft.Maps.Location(46.898170, -121.706227), new Microsoft.Maps.Location(46.903800, -121.684254), new Microsoft.Maps.Location(46.905676, -121.678074), new Microsoft.Maps.Location(46.907553, -121.668461), new Microsoft.Maps.Location(46.912713, -121.670521), new Microsoft.Maps.Location(46.917872, -121.663655), new Microsoft.Maps.Location(46.915058, -121.651982), new Microsoft.Maps.Location(46.915996, -121.620396), new Microsoft.Maps.Location(46.914589, -121.610783), new Microsoft.Maps.Location(46.919279, -121.614216), new Microsoft.Maps.Location(46.918341, -121.620396), new Microsoft.Maps.Location(46.919748, -121.626576), new Microsoft.Maps.Location(46.918341, -121.632069), new Microsoft.Maps.Location(46.920217, -121.637562), new Microsoft.Maps.Location(46.920217, -121.643055), new Microsoft.Maps.Location(46.918341, -121.651295), new Microsoft.Maps.Location(46.920217, -121.659535), new Microsoft.Maps.Location(46.920686, -121.665715), new Microsoft.Maps.Location(46.925844, -121.666401), new Microsoft.Maps.Location(46.927720, -121.672581), new Microsoft.Maps.Location(46.931471, -121.665028), new Microsoft.Maps.Location(46.934754, -121.667088), new Microsoft.Maps.Location(46.932409, -121.673268), new Microsoft.Maps.Location(46.935222, -121.679448), new Microsoft.Maps.Location(46.932409, -121.682881), new Microsoft.Maps.Location(46.925376, -121.681508), new Microsoft.Maps.Location(46.924438, -121.686314), new Microsoft.Maps.Location(46.920217, -121.681508), new Microsoft.Maps.Location(46.915058, -121.680134), new Microsoft.Maps.Location(46.911305, -121.692494), new Microsoft.Maps.Location(46.916465, -121.697987), new Microsoft.Maps.Location(46.922093, -121.698674), new Microsoft.Maps.Location(46.923500, -121.701420), new Microsoft.Maps.Location(46.926782, -121.697987), new Microsoft.Maps.Location(46.928189, -121.702107), new Microsoft.Maps.Location(46.924907, -121.706227), new Microsoft.Maps.Location(46.912243, -121.700734), new Microsoft.Maps.Location(46.910367, -121.706913), new Microsoft.Maps.Location(46.911305, -121.715153), new Microsoft.Maps.Location(46.904738, -121.723393), new Microsoft.Maps.Location(46.895824, -121.723393), new Microsoft.Maps.Location(46.894885, -121.732319), new Microsoft.Maps.Location(46.897231, -121.737812), new Microsoft.Maps.Location(46.904269, -121.770085), new Microsoft.Maps.Location(46.901454, -121.774205), new Microsoft.Maps.Location(46.902861, -121.783818), new Microsoft.Maps.Location(46.911774, -121.785878), new Microsoft.Maps.Location(46.912713, -121.792744), new Microsoft.Maps.Location(46.915527, -121.795491), new Microsoft.Maps.Location(46.918810, -121.808537), new Microsoft.Maps.Location(46.915996, -121.818837), new Microsoft.Maps.Location(46.910836, -121.818150), new Microsoft.Maps.Location(46.905676, -121.826390), new Microsoft.Maps.Location(46.905676, -121.833256), new Microsoft.Maps.Location(46.890193, -121.816090), new Microsoft.Maps.Location(46.887378, -121.820210), new Microsoft.Maps.Location(46.886439, -121.829136), new Microsoft.Maps.Location(46.883623, -121.836003), new Microsoft.Maps.Location(46.885031, -121.842869), new Microsoft.Maps.Location(46.882685, -121.845616), new Microsoft.Maps.Location(46.879869, -121.839436), new Microsoft.Maps.Location(46.875644, -121.836689), new Microsoft.Maps.Location(46.871889, -121.831196), new Microsoft.Maps.Location(46.862500, -121.834630), new Microsoft.Maps.Location(46.859213, -121.842869), new Microsoft.Maps.Location(46.862970, -121.853169), new Microsoft.Maps.Location(46.860622, -121.859349), new Microsoft.Maps.Location(46.861561, -121.866902), new Microsoft.Maps.Location(46.858744, -121.866215), new Microsoft.Maps.Location(46.859213, -121.857975), new Microsoft.Maps.Location(46.857335, -121.852482), new Microsoft.Maps.Location(46.856866, -121.849049), new Microsoft.Maps.Location(46.850761, -121.843556), new Microsoft.Maps.Location(46.845126, -121.846302), new Microsoft.Maps.Location(46.841369, -121.848362), new Microsoft.Maps.Location(46.838081, -121.851109), new Microsoft.Maps.Location(46.833853, -121.849736), new Microsoft.Maps.Location(46.831504, -121.855916), new Microsoft.Maps.Location(46.829156, -121.855229), new Microsoft.Maps.Location(46.832444, -121.839436), new Microsoft.Maps.Location(46.830095, -121.831196), new Microsoft.Maps.Location(46.820699, -121.822957), new Microsoft.Maps.Location(46.816000, -121.826390), new Microsoft.Maps.Location(46.816000, -121.820897), new Microsoft.Maps.Location(46.816940, -121.814717), new Microsoft.Maps.Location(46.812711, -121.811970), new Microsoft.Maps.Location(46.810831, -121.797551), new Microsoft.Maps.Location(46.808951, -121.793431)], 2000);
            var contourLine6 = new Microsoft.Maps.ContourLine([new Microsoft.Maps.Location(46.872359, -121.673954), new Microsoft.Maps.Location(46.883623, -121.640995), new Microsoft.Maps.Location(46.885500, -121.645802), new Microsoft.Maps.Location(46.887378, -121.648549), new Microsoft.Maps.Location(46.886908, -121.655415), new Microsoft.Maps.Location(46.883154, -121.656788), new Microsoft.Maps.Location(46.882215, -121.661595), new Microsoft.Maps.Location(46.883623, -121.665715), new Microsoft.Maps.Location(46.886439, -121.665715), new Microsoft.Maps.Location(46.884092, -121.669835), new Microsoft.Maps.Location(46.880807, -121.669148), new Microsoft.Maps.Location(46.873767, -121.674641)], 2000);

            //Add the contour lines to a contour layer.
            var layer = new Microsoft.Maps.ContourLayer([contourLine1, contourLine2, contourLine3, contourLine4, contourLine5, contourLine6], {
                colorCallback: assignContourColor,
                polygonOptions: {
                    //Make the outlines of the contour area transparent.
                    strokeColor: 'rgba(0, 0, 0, 0)'
                }
            });

            //Add the contour layer to the map.
            map.layers.insert(layer);
        });
    }

    //A function that contains business logic that specifies which color to make a contour area based on it's value.
    function assignContourColor(value) {
        var color = 'rgba(235, 140, 14, 0.5)';

        if (value >= 4000) {
            color = 'rgba(25, 150, 65, 0.5)';
        }
        else if (value >= 3500) {
            color = 'rgba(140, 202, 32, 0.5)';
        }
        else if (value >= 3000) {
            color = 'rgba(255, 255, 0, 0.5)';
        }

        return color;
    }
    </script>
    <style>
        .contourLegend {
            margin-left: 10px;
            float: left;
            text-align: center;
            width: 100px;
        }
    </style>
</head>
<body>
    <div id="myMap" style="position:relative;width:600px;height:400px;float:left;"></div>

    <div class="contourLegend">
        <div style="background-color: rgba(25, 150, 65, 0.5)">4000m</div>
        <div style="background-color: rgba(140, 202, 32, 0.5)">3500m</div>
        <div style="background-color: rgba(255, 255, 0, 0.5)">3000m</div>
        <div style="background-color: rgba(235, 140, 14, 0.5)">2000m</div>
    </div>
</body>
</html>
```

Running this code in a browser will display colored contour areas representing the elevation of the land around Mount Rainer.

![BMV8_BasicContourLayer](../../media/bmv8-basiccontourlayer.PNG)

[Try it now](https://www.bing.com/api/maps/sdk/mapcontrol/isdk#basicContourLayer+JS)