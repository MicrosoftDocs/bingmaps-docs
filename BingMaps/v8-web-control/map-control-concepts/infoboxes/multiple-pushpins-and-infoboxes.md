---
title: "Multiple Pushpins and Infoboxes | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 9d21f84d-af0c-4f48-b03a-ad0f0a881c06
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Multiple Pushpins and Infoboxes
When you have a lot of pushpins and only want to show one infobox at a time, the best approach is to create one Infobox and to reuse it rather than creating an infobox for each pushpin. By doing this the number of DOM elements created by the application is greatly reduced which can provide better performance. This example creates 5 pushpins at random locations on the map. If you click on any of them, an infobox will be displayed with the content for that pushpin. Note that all `IPrimitive` shapes have a metadata property were you can store data for that shape.

```
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <meta charset="utf-8" />
	<script type='text/javascript'>
    var map, infobox;

    function GetMap() {
        map = new Microsoft.Maps.Map('#myMap', {});

        //Create an infobox at the center of the map but don't show it.
        infobox = new Microsoft.Maps.Infobox(map.getCenter(), {
            visible: false
        });

        //Assign the infobox to a map instance.
        infobox.setMap(map);

        //Create random locations in the map bounds.
        var randomLocations = Microsoft.Maps.TestDataGenerator.getLocations(5, map.getBounds());
        
        for (var i = 0; i < randomLocations.length; i++) {
            var pin = new Microsoft.Maps.Pushpin(randomLocations[i]);

            //Store some metadata with the pushpin.
            pin.metadata = {
                title: 'Pin ' + i,
                description: 'Discription for pin' + i
            };

            //Add a click event handler to the pushpin.
            Microsoft.Maps.Events.addHandler(pin, 'click', pushpinClicked);

            //Add pushpin to the map.
            map.entities.push(pin);
        }
    }

    function pushpinClicked(e) {
        //Make sure the infobox has metadata to display.
        if (e.target.metadata) {
            //Set the infobox options with the metadata of the pushpin.
            infobox.setOptions({
                location: e.target.getLocation(),
                title: e.target.metadata.title,
                description: e.target.metadata.description,
                visible: true
            });
        }
    }
    </script>
    <script type='text/javascript' src='http://www.bing.com/api/maps/mapcontrol?callback=GetMap&key=[YOUR_BING_MAPS_KEY]' async defer></script>
</head>
<body>
    <div id="myMap" style="position:relative;width:600px;height:400px;"></div>
</body>
</html>
```

Running this code will display 5 pushpins on the map. If you click on any of them, you will see an infobox appear with details for that pushpin.

![BMV8_MultiplePushpinsAndInfobox](../../media/bmv8-multiplepushpinsandinfobox2.png)