---
title: "Infobox with Options | Microsoft Docs"
description: Provides a code example that shows how to create an infobox with options to hide the pointer and the close button.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 81a01d7f-82fe-4dd9-83f9-a5aa2be80490
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Infobox with Options

This example shows how to create and infobox with the options that hide the pointer and close button, and additionally has two action links.

```html
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <meta charset="utf-8" />
	<script type='text/javascript'>
    var map, infobox;

    function GetMap() {
        map = new Microsoft.Maps.Map('#myMap', {});

        var center = map.getCenter();

        //Create an infobox that doesn't have a pointer or close button.
        infobox = new Microsoft.Maps.Infobox(center, {
            title: 'Map Center',
            description: 'This is the center of the map.',
            showPointer: false, 
            showCloseButton: false,
            actions: [{
                label: 'Handler1',
                eventHandler: function () {
                    alert('Handler1');
                }
            }, {
                label: 'Handler2',
                eventHandler: function () {
                    alert('Handler2');
                }
            }]
        });

        //Assign the infobox to a map instance.
        infobox.setMap(map);
    }
    </script>
    <script type='text/javascript' src='http://www.bing.com/api/maps/mapcontrol?callback=GetMap&key=[YOUR_BING_MAPS_KEY]' async defer></script>
</head>
<body>
    <div id="myMap" style="position:relative;width:600px;height:400px;"></div>
</body>
</html>
```

This code displays an infobox that doesn’t have a pointer or close button but does have two link buttons. 

![Screenshot of a Bing map showing an infobox showing a description and two link buttons.](../../media/bmv8-infoboxoptionsexample2.png)