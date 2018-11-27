---
title: "Expanding Tooltip Infobox | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 741120e9-a946-421b-b50c-268f6d0f0d87
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Expanding Tooltip Infobox
Often infoboxes are displayed when a user clicks or hovers over a pushpin. Another user friendly experience is to show the title when the user hovers over a pushpin like a tooltip, and if they click on the pushpin, then open the full infobox that contains the title and description. The following code shows how to accomplish this by using two infoboxes. One to power the toolitp experience and the other to display the full infobox.

```
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <meta charset="utf-8" />
	<script type='text/javascript'>
    var map, infobox, tooltip;
    var tooltipTemplate = '<div style="background-color:white;height:20px;width:150px;padding:5px;text-align:center"><b>{title}</b></div>';

    function GetMap() {
        map = new Microsoft.Maps.Map('#myMap', {});

        //Create an infobox to use as a tooltip when hovering.
        tooltip = new Microsoft.Maps.Infobox(map.getCenter(), {
            visible: false,
            showPointer: false,
            showCloseButton: false,
            offset: new Microsoft.Maps.Point(-75, 10)
        });

        tooltip.setMap(map);
        
        //Create an infobox for displaying detailed information.
        infobox = new Microsoft.Maps.Infobox(map.getCenter(), {
            visible: false
        });

        infobox.setMap(map);
        
        //Create random locations in the map bounds.
        var randomLocations = Microsoft.Maps.TestDataGenerator.getLocations(5, map.getBounds());

        for (var i = 0; i < randomLocations.length; i++) {
            var pin = new Microsoft.Maps.Pushpin(randomLocations[i]);

            //Store some metadata with the pushpin.
            pin.metadata = {
                title: 'Pushpin ' + i,
                description: 'Discription for pin ' + i
            };

            //Add a mouse events to the pushpin.
            Microsoft.Maps.Events.addHandler(pin, 'click', pushpinClicked);
            Microsoft.Maps.Events.addHandler(pin, 'mouseover', pushpinHovered);
            Microsoft.Maps.Events.addHandler(pin, 'mouseout', closeTooltip);

            //Add pushpin to the map.
            map.entities.push(pin);
        }
    }

    function pushpinClicked(e) {
        //Hide the tooltip
        closeTooltip();

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

    function pushpinHovered(e) {
        //Hide the infobox
        infobox.setOptions({ visible: false });

        //Make sure the infobox has metadata to display.
        if (e.target.metadata) {
            //Set the infobox options with the metadata of the pushpin.
            tooltip.setOptions({
                location: e.target.getLocation(),
                htmlContent: tooltipTemplate.replace('{title}', e.target.metadata.title),
                visible: true
            });
        }
    }

    function closeTooltip() {
        //Close the tooltip.
        tooltip.setOptions({
            visible: false
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

If you run this code and hover over a pushpin you will see a tooltip appear that displays the title property of the pushpin. If you click on the pushpin a detailed infobox will appear that contains the title and description.

![BMV8_InfoboxExpandingTooltipExample](..//media/bmv8-infoboxexpandingtooltipexample.png)