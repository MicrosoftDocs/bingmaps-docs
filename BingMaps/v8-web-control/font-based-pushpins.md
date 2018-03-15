---
title: "Font based Pushpins | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 2ebf5d50-0cff-49e6-af67-f03ad3cf8cb2
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Font based Pushpins
One great source for pushpin icons is font based glyphs. This example shows how to use a custom font to create pushpins icons. For this example, the Font Awesome library is used. In order to create the pushpin icon an off-screen canvas is used to measure the text and create an image from the font. 

```
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <meta charset="utf-8" />
    <link href="http://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.6.3/css/font-awesome.min.css" rel="stylesheet" />

    <script type='text/javascript' src='http://www.bing.com/api/maps/mapcontrol?callback=GetMap' async defer></script>
    
    <script type='text/javascript' charset="utf-8">
    function GetMap() {
        var map = new Microsoft.Maps.Map('#myMap', {
            credentials: 'Your Bing Maps Key'
        });

        //Create a font pushpin of a truck. "&#xf0d1;" => "\uf0d1". List of icon hex values: http://fontawesome.io/3.2.1/cheatsheet/
        var pin = createFontPushpin(map.getCenter(), '\uF0D1', 'FontAwesome', 30, 'red');

        //Add the pushpin to the map
        map.entities.push(pin);
    }

    function createFontPushpin(location, text, fontName, fontSizePx, color) {
        var c = document.createElement('canvas');
        var ctx = c.getContext('2d');

        //Define font style
        var font = fontSizePx + 'px ' + fontName;
        ctx.font = font

        //Resize canvas based on sie of text.
        var size = ctx.measureText(text);
        c.width = size.width;
        c.height = fontSizePx;

        //Reset font as it will be cleared by the resize.
        ctx.font = font;
        ctx.textBaseline = 'top';
        ctx.fillStyle = color;

        ctx.fillText(text, 0, 0);

        return new Microsoft.Maps.Pushpin(location, {
            icon: c.toDataURL(),
            anchor: new Microsoft.Maps.Point(c.width / 2, c.height / 2) //Align center of pushpin with location.
        });
    }
    </script>
</head>
<body>
    <div style="font-family:FontAwesome;position:absolute;color:transparent;">Preload font, otherwise we may end up trying to use it before it is available.</div>
    <div id="myMap" style="position:relative;width:600px;height:400px;"></div>
</body>
</html>
```

Running this code will display a pushpin that looks like a red truck. 

![BMV8_FontBasedPushpins](../v8-web-control/media/bmv8-fontbasedpushpins.PNG)