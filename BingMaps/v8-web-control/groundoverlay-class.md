---
title: "GroundOverlay Class | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: a0f34a05-3cb8-4ac2-8126-d3c9f5064ec4
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# GroundOverlay Class
A map overlay that binds an image to a bounding box area on the map.

## Constructor

GroundOverlay(options: [GroundOverlayOptions](../v8-web-control/groundoverlayoptions-object.md))

## Properties

| Name     | Type   | Description                                                                 |
|----------|--------|-----------------------------------------------------------------------------|
| metadata | object | Optional property to store any additional metadata for this ground overlay. |

## Methods

| Name                                      | Return Type       | Description                                                        |
|-------------------------------------------|-------------------|--------------------------------------------------------------------|
| `getBackgroundColor()`                      | string _or_ [Color](../v8-web-control/color-class.md) | Gets the background color of the ground overlay.                   |
| `getBounds()`                               | [LocationRect](../v8-web-control/locationrect-class.md)      | Gets the bounding box that the ground overlay is bounded to.       |
| `getImageUrl()`                             | string            | Gets the url to the gorund overlay image.                          |
| `getOpacity()`                              | number            | Gets the opacity of the ground overlay.                            |
| `getMap()`                                  | [Map](../v8-web-control/map-class.md)               | Gets the map that this overlay is attached to.                     |
| `getRotation()`                             | number            | Gets the rotation of the ground overlay.                           |
| `getVisible()`                              | boolean           | Gets a boolean indicating if the ground overlay is visible or not. |
| setOptions(options: [GroundOverlayOptions](../v8-web-control/groundoverlayoptions-object.md)) |                   | Sets the options used to render the ground overlay.                |
| `setVisible(visible: boolean)`              |                   | Sets the visibility of the Ground Overlay.                         |

## GroundOverlay Samples:

-   [Simply Ground Overlay](https://www.bing.com/api/maps/mapcontrol/isdk?autoRedirect=false#simpleGroundOverlay+JS)
-   [Basic Ground Overlay](http://bingmapsv8samples.azurewebsites.net/#Basic%20Ground%20Overlay)
-   [Ground Overlay with Options](http://bingmapsv8samples.azurewebsites.net/#Ground%20Overlay%20Options)
-   [SVG Ground Overlay](http://bingmapsv8samples.azurewebsites.net/#SVG%20Ground%20Overlay)
