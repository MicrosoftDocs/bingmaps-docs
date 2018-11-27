---
title: "Custom Base64 Image Pushpin Example | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 523f7f36-cf29-4ea9-bd95-8f3af0ca86c1
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Custom Base64 Image Pushpin Example
In addition to being able to create custom pushpins using images and SVG, you can also use base64 image strings as well. This is useful in two scenarios. The first is to save on separate HTTP requests that you may incur if you have a lot of different icons; rather than request multiple different icons, you can include resources directly in your page and include them in a single HTTP request. In some circumstances, this will be much quicker than using separate HTTP requests for individual images. The second is to allow you to create a custom image using a HTML5 Canvas and then export it as a data URL. This example takes the following base64 string of an image and uses it to create a custom pushpin in the center of the map.

```
data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABkAAAAcCAYAAACUJBTQAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH3wQbECUudScMXAAAAB1pVFh0Q29tbWVudAAAAAAAQ3JlYXRlZCB3aXRoIEdJTVBkLmUHAAACGUlEQVRIx+3Wy2sTURTH8e/NTDIzaZMxadMWhyBUSheiiyo+QPpHuHIhdOfSP8GlbkXEhTv/gNau3LgRurEIUqlWU2ubh7evPEg6NjOZJHNdlIgLo11YRcj5A84Hfpx7zxFKKcUJlw7gOM6JAVLKIwTg4avbfxy4c/UJABH+Qg2QAfKfI98f48vc/CCuATJA/iEilFKq3/q98XTk2I0W5qp916/41SHhOM6xoIW5KlLK/t/K6oNbwlAdknELYSZpxTMkxrO4XoCUUv0O6gHlYkjHWxF+yyWTsKit57CGbbTMGSJWepTh05PIRof3mxLNjNP0Pdp+i9ziIyGl7BtFD1hdOqRdei5ijW2shkSvS8LAJTM2gh4JiWzvFNksFdAsA3s0Ram4TrtZJxnXCLwKWSF+CvWAt89czmffiEQ0gGYZzSuTX3tNx60Q1Pcxwyb67JUL7Jb38VsdojETz2ux8W6JqG6iJaOoGLTr98WP0fWAsZgQ849v8mnZYeriLNinwAup722RsW12cysYiRT62voGwymbbsQgMZREcMD1yzN4nkctrNEV4HbrTKeFKNeOJlFKiXtwV2ganJvKkF8rsvxiEd8P0FSTiXQa2wxJxEz2yl/QA2Mc2Qihq7NdqdE5rJAc2ufsZBbTiIIGXWXTVeCIa0glMQwh8vl7hMDHD5+Zmb7E16ZPtVrFilnsFLY42CngTDhEohbfALpF/s+4JwbyAAAAAElFTkSuQmCC
```

This base64 image string generates an image that looks like this: &nbsp;
![Bubble Icon](..//media/bmv8-custompushpinusingbase64imageexample-icon.png)
 
To create a custom pushpin out of this base64 image string, simply pass it into the `icon` property of the pushpin, like so:

```
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <meta charset="utf-8" />
	<script type='text/javascript'>
    function GetMap() {
        var map = new Microsoft.Maps.Map('#myMap', {});

        var center = map.getCenter();

        var base64Image = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABkAAAAcCAYAAACUJBTQAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH3wQbECUudScMXAAAAB1pVFh0Q29tbWVudAAAAAAAQ3JlYXRlZCB3aXRoIEdJTVBkLmUHAAACGUlEQVRIx+3Wy2sTURTH8e/NTDIzaZMxadMWhyBUSheiiyo+QPpHuHIhdOfSP8GlbkXEhTv/gNau3LgRurEIUqlWU2ubh7evPEg6NjOZJHNdlIgLo11YRcj5A84Hfpx7zxFKKcUJlw7gOM6JAVLKIwTg4avbfxy4c/UJABH+Qg2QAfKfI98f48vc/CCuATJA/iEilFKq3/q98XTk2I0W5qp916/41SHhOM6xoIW5KlLK/t/K6oNbwlAdknELYSZpxTMkxrO4XoCUUv0O6gHlYkjHWxF+yyWTsKit57CGbbTMGSJWepTh05PIRof3mxLNjNP0Pdp+i9ziIyGl7BtFD1hdOqRdei5ijW2shkSvS8LAJTM2gh4JiWzvFNksFdAsA3s0Ram4TrtZJxnXCLwKWSF+CvWAt89czmffiEQ0gGYZzSuTX3tNx60Q1Pcxwyb67JUL7Jb38VsdojETz2ux8W6JqG6iJaOoGLTr98WP0fWAsZgQ849v8mnZYeriLNinwAup722RsW12cysYiRT62voGwymbbsQgMZREcMD1yzN4nkctrNEV4HbrTKeFKNeOJlFKiXtwV2ganJvKkF8rsvxiEd8P0FSTiXQa2wxJxEz2yl/QA2Mc2Qihq7NdqdE5rJAc2ufsZBbTiIIGXWXTVeCIa0glMQwh8vl7hMDHD5+Zmb7E16ZPtVrFilnsFLY42CngTDhEohbfALpF/s+4JwbyAAAAAElFTkSuQmCC';

        //Create custom Pushpin using a base64 image string.
        var pin = new Microsoft.Maps.Pushpin(center, {
            icon: base64Image,
            anchor: new Microsoft.Maps.Point(12, 28)
        });

        //Add the pushpin to the map
        map.entities.push(pin);
    }
    </script>
    <script type='text/javascript' src='http://www.bing.com/api/maps/mapcontrol?callback=GetMap&key=[YOUR_BING_MAPS_KEY]' async defer></script>
</head>
<body>
    <div id="myMap" style="position:relative;width:600px;height:400px;"></div>
</body>
</html>
```

Here is what this pushpin looks like on the map.

![BMV8_Base64PushpinExample](..//media/bmv8-base64pushpinexample.png) 