---
title: "Geometry Binary Operations | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: bdb63aac-b70b-470f-8ce8-5465b4939d6b
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Geometry Binary Operations
Binary operations are logical processes such as addition, subtraction or not. Take for example the following operations:

* `difference(A, B)` – This calculation takes the shape A and subtracts the area of shape B.
* `intersection(A, B)` – This calculates the area where A and B overlap. 
* `symDifference(A, B)` – This calculates the area where A and B do not overlap. One way to look at this is the union of A and B minus the intersection of A and B. Another way to look at this is the union of the difference A and B and the difference B and A.
* `union(A, B)` – This calculation takes the area of shape A and B and adds it together.

The Spatial Math module also has a `UnionAggregate` function which can take in an array of shapes of any length and performs an optimized union operation against them.

![BMV8_BinaryOperations](..//media/bmv8-binaryoperations.png)

This example loads a map with two random polygons displayed on it. Below the map 5 buttons are displayed, each triggering a different binary operation to be performed against the polygons.

```
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <meta http-equiv='Content-Type' content='text/html; charset=utf-8' />

    <script type='text/javascript'>
    var map, polygons, result;

    function GetMap() {
        map = new Microsoft.Maps.Map(document.getElementById('myMap'), {
            credentials: 'Your Bing Maps Key',
            center: new Microsoft.Maps.Location(43, -107.55),
            zoom: 15
        });

        //Load the Spatial Math module.
        Microsoft.Maps.loadModule('Microsoft.Maps.SpatialMath', function () {
            //Generate two random polygons to test the geometry calcuations with.
            polygons = Microsoft.Maps.TestDataGenerator.getPolygons(2, map.getBounds(), null, 0.6, null, true);
            map.entities.push(polygons);
        });
    }

    function processOperation(operation) {
        //If a result is already on the map. Clear the map and re-add the test polygons.
        if (result) {
            map.entities.clear();
            map.entities.push(polygons);
        }

        //Apply the requested geometry calculation.
        switch (operation) {
            case 'difference':
                result = Microsoft.Maps.SpatialMath.Geometry.difference(polygons[0], polygons[1]);
                break;
            case 'intersection':
                result = Microsoft.Maps.SpatialMath.Geometry.intersection(polygons[0], polygons[1]);
                break;
            case 'union':
                result = Microsoft.Maps.SpatialMath.Geometry.union(polygons[0], polygons[1]);
                break;
            case 'symDifference':
                result = Microsoft.Maps.SpatialMath.Geometry.symDifference(polygons[0], polygons[1]);
                break;
            case 'unionAggregate':
                result = Microsoft.Maps.SpatialMath.Geometry.unionAggregate(polygons);
                break;
        }

        if (result) {
            //Outline the resulting shape and make the fill area transparent so that the original shapes can still be seen.
            if (result.length !== undefined) {
                for (var i = 0, len = result.length; i < len; i++) {
                    result[i].setOptions({ strokeColor: 'red', fillColor: 'transparent', strokeThickness: 5 });
                }
            }
            else {
                result.setOptions({ strokeColor: 'red', fillColor: 'transparent', strokeThickness: 5 });
            }

            map.entities.push(result);
        }
        else {
            alert('Unable to find a result.');
        }
    }
    </script>
    
    <script type='text/javascript' src='http://www.bing.com/api/maps/mapcontrol?branch=experimental&callback=GetMap' async defer></script>
</head>
<body>
    <div id='myMap' style='position:relative;width:600px;height:400px;'></div>
    <br/>
    <input type="button" value="Difference" onclick="processOperation('difference');" />
    <input type="button" value="Intersection" onclick="processOperation('intersection');" />
    <input type="button" value="Union" onclick="processOperation('union');" />
    <input type="button" value="Union Aggregate" onclick="processOperation('unionAggregate');" />
    <input type="button" value="SymDifference" onclick="processOperation('symDifference');" />
</body>
</html>
```

Running this code, press one of the 5 buttons to perform a binary operation against the displayed polygons. The resulting shape will be outlined in red and while it’s fill color will be made transparent so that the original polygons can still be seen. The following is an example that shows the result when performing the intersection operation.

![BMV8_SpatialMathIntersectionExample](..//media/bmv8-spatialmathintersectionexample.PNG)

[Try it now](http://www.bing.com/api/maps/sdk/mapcontrol/isdk#binaryOperations+JS)