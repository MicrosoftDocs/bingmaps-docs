---
title: "Directions Input Panel | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 1ce05044-4f7b-44c2-805f-d2a4f7c39498
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# Directions Input Panel
The following examples shows how to display the built in input panel for calculating directions. This is useful if you don’t want to create a custom input panel. 

```
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <meta charset="utf-8" />
	<script type='text/javascript'>
        var map;
        var directionsManager;

        function GetMap()
        {
            map = new Microsoft.Maps.Map('#myMap', {});

            //Load the directions module.
            Microsoft.Maps.loadModule('Microsoft.Maps.Directions', function () {
                //Create an instance of the directions manager.
                directionsManager = new Microsoft.Maps.Directions.DirectionsManager(map);

                //Specify where to display the route instructions.
                directionsManager.setRenderOptions({ itineraryContainer: '#directionsItinerary' });

                //Specify the where to display the input panel
                directionsManager.showInputPanel('directionsPanel');
            });
        }
    </script>
    <style>
        html, body{
            padding:0;
            margin:0;
            height:100%;
        }

        .directionsContainer{
            width:380px;
            height:100%;
            overflow-y:auto;
            float:left;
        }

        #myMap{
            position:relative;
            width:calc(100% - 380px);
            height:100%;
            float:left;
        }
    </style>
    <script type='text/javascript' src='http://www.bing.com/api/maps/mapcontrol?callback=GetMap&key=[YOUR_BING_MAPS_KEY]' async defer></script>
</head>
<body>
    <div class="directionsContainer">
        <div id="directionsPanel"></div>
        <div id="directionsItinerary"></div>
    </div>
    <div id="myMap"></div>
</body>
</html>
```

Running this code will display the directions input panel in the top left corner of the page with the map to the right of it. As you type in locations the suggested will be displayed. When directions are calculated, the turn by turn instructions will be displayed in below the input panel. Here is what this looks like while typing in “New York” as the starting location. 

![BMV8_DirectionsInputPanelExample](../v8-web-control/media/bmv8-directionsinputpanelexample.PNG)