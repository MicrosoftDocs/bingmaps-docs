---
title: "ViewOptions Object | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: df0accb2-08e3-44b0-bd7a-4ca103aa0130
caps.latest.revision: 7
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# ViewOptions Object
The following view options that can be used when loading the map or when using the **setView** function.

Name          | Type            | Description
------------- | --------------- | -----------------------------------
`bounds`        | [LocationRect](../v8-web-control/locationrect-class.md)    | The bounding rectangle of the map view. If both bounds and center are specified, bounds takes precedence over center.
`center`        | [Location](../v8-web-control/location-class.md)        | The location of the center of the map view. If both bounds and center are specified, bounds takes precedence over center.
`centerOffset` | [Point]() | The amount the center is shifted in pixels. This property is ignored if center is not specified.
`heading`       | number          | The directional heading of the map. The heading is represented in geometric degrees with 0 or 360 = North, 90 = East, 180 = South, and 270 = West.
`labelOverlay`  | [LabelOverlay](../v8-web-control/labeloverlay-enumeration.md) | Indicates how the map labels are displayed.
`mapTypeId`     | [MapTypeId](../v8-web-control/maptypeid-enumeration.md)       | The map type of the view. 
`padding`       | number          | The amount of padding in pixels to be added to each side of the bounds of the map view.
`pitch`         | number          | The angle relative to the horizon to tilt a streetside panorama image.
`zoom`          | number          | The zoom level of the map view.
