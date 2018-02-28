---
title: "Infobox with Options | Microsoft Docs"
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
---
# Infobox with Options
This example shows how to create and infobox with the options that hide the pointer and close button, and additional has two action links.

```
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <meta charset="utf-8" />
    <script type='text/javascript' 
            src='http://www.bing.com/api/maps/mapcontrol?callback=GetMap' 
            async defer></script>
    <script type='text/javascript'>
    var map, infobox;

    function GetMap() {
        map = new Microsoft.Maps.Map('#myMap', {
            credentials: 'Your Bing Maps Key'
        });

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
</head>
<body>
    <div id="myMap" style="position:relative;width:600px;height:400px;"></div>
</body>
</html>
```

This code displays an infobox that doesn’t have a pointer or close button but does have two link buttons. 

![BMV8_InfoboxOptionsExample](../v8-web-control/media/bmv8-infoboxoptionsexample2.png)