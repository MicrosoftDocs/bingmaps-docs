---
title: "Check Bird’s eye Coverage Availability | Microsoft Docs"
description: Provides a code example that demonstrates the static function's ability to check if bird's eye imagery is available at a location.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: a443a058-6765-4f9c-a9f1-6e02a3cfd826
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Check Bird’s eye Coverage Availability

The Microsoft.Maps namespace has a static function that can be used to check if Bird’s eye imagery is available in at a specified location.

| **Name**                                                                                                   | **Return Type** | **Description**                                                                     |
|------------------------------------------------------------------------------------------------------------|-----------------|-------------------------------------------------------------------------------------|
| getIsBirdseyeAvailable(loc: [Location](../../map-control-api/location-class.md), heading: [Heading](../../map-control-api/heading-enumeration.md) _or_ number, callback: function(isAvailable: boolean)) |                 | Checks to see if Birdseye imagery is available at a specified location and heading. |

The following code demonstrates how to check if bird’s eye imagery is available for a specified location and then loads the map into bird’s eye or aerial mode accordingly.

```javascript
var map;
var loc = new Microsoft.Maps.Location(45.464210, 9.190396);

Microsoft.Maps.getIsBirdseyeAvailable(loc, Microsoft.Maps.Heading.North, function(isAvailable) {
    map = new Microsoft.Maps.Map(document.getElementById('myMap'), {
        center: mapLocation,
        mapTypeId: isAvailable ? Microsoft.Maps.MapTypeId.birdseye : Microsoft.Maps.MapTypeId.aerial
    });

    //Add your post map load code here.
});
```

[Try it now](https://www.bing.com/mapspreview/mapcontrol/isdk/checkbirdseyev2availability)
