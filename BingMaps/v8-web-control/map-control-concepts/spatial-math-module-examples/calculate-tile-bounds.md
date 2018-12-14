---
title: "Calculate Tile Bounds | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 70fad55e-3f7d-450b-8270-dfb5d9007953
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Calculate Tile Bounds

This example uses some of the Tile math functions in the Spatial Math library. The Tile math calculations are useful when creating custom visualization (i.e. heat maps). In this example every time the map has moved all the tiles that are in the current map view are calculated. A polygon is then generated for each one to show its area and a pushpin, with its title property set to the quadkey value of the tile, is placed in the center of the polygon.

```html
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <meta charset="utf-8" />
	<script type='text/javascript'>
    var map;

    function GetMap() {
        map = new Microsoft.Maps.Map('#myMap', {
            credentials: 'Your Bing Maps Key',
            zoom: 4
        });

        //Load the Spatial Math module.
        Microsoft.Maps.loadModule("Microsoft.Maps.SpatialMath", function () {
            showMapTileBounds();

            //Recaulte the map tiles bounds everytime the map moves.
            Microsoft.Maps.Events.addHandler(map, 'viewchangeend', showMapTileBounds);
        });
    }

    function showMapTileBounds() {
        map.entities.clear();

        //Get a list of all the tiles in the current map view.
        var tiles = Microsoft.Maps.SpatialMath.Tiles.getTilesInBounds(map.getBounds(), map.getZoom());

        for (var i = 0; i < tiles.length; i++) {
            //Calculate the bounding rectangle of the tile.
            var tileLocRect = Microsoft.Maps.SpatialMath.Tiles.tileToLocationRect(tiles[i]);

            //Create a polygon for the tile and add it to the map.
            var poly = Microsoft.Maps.SpatialMath.locationRectToPolygon(tileLocRect);
            map.entities.push(poly);

            //Add a pushpin with the quadkey value set as the title. 
            var pin = new Microsoft.Maps.Pushpin(tileLocRect.center, {
                title: tiles[i].quadKey
            });
            map.entities.push(pin);
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

Running this code will load the map and display a polygon and pushpin above each map tile in the current map view.

![BMV8_TileBoundsExample](../../media/bmv8-tileboundsexample.PNG)
