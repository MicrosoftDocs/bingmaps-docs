---
title: "Vector Map Labels | Microsoft Docs"
description: "This article describes vector map labels and lists common issues that can be resolved by utilizing them."
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: e655830f-95f7-49e1-9e08-e5db52f1a5cc
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Vector Map Labels

[!INCLUDE [bing-maps-web-control-sdk-retirement](../../includes/bing-maps-web-control-sdk-retirement.md)]

Vector map labels are new in the Bing Maps V8 web control. Map labels are the names of roads, cities and other entities that are displayed on the map. Traditionally online maps have embedded these labels into the base map image. Vector map labels essentially removes the labels from the base map image and instead overlays them above the map just like a pushpin. By doing this, a number of common issues can be solved. For example:

   *	When adding a tile layer to a map, such as a weather radar overlay, in the past the map labels would be covered and not clearly visible. Vector labels now render above tile layers and as such are clearly visible. 
   *	When drawing a route line on a road, in the past the line itself would cover the road names. With vector labels, the road names now appear above the line and are easy to see.
   *	When pushpins are displayed on the map, they can often overlap map labels. If this happens a lot, the map can look cluttered with partially visible map labels which don’t add a lot of value. If the pushpin has text on it, this can be even worse. Vector labels have collision detection which checks to see if individual labels are colliding with pushpins. When a collision happens the map will try and move the label to a logical alternative position. If the label represents an area like a city, the map will try moving it up/down/left/right to see if it can find a place that is still above the area but not overlapped by a pushpin. If the label is for a road, the map will try moving the label down the road to a place where it isn’t overlapped by the pushpin and doesn’t collide with other map labels. If the map is unable is unable to find a reasonable place to move the label to, it will simply hide it. Additionally, pushpins now have two new label options; title and subTitle, which allow you to assign text to a pushpin that is displayed on the map but uses the same collision detection logic as the map labels. This is also a good way to create custom map labels as well.

One of the main benefits of vector labels is that it prioritizes the data that is overlaid on the map while rendering the labels in a way that makes sense depending on the type of data that is being displayed. This makes it easier to gain value from the data that is overlaid on the map, as the map itself sites in the background and acts as visual reference.

This feature does add some performance overhead as additional network calls are made to retrieve the vector label data, there is also a decent number of calculations involved in the collision detection logic used for rendering. In most apps this won’t be an issue. However, a new “lite” map mode option has been added, which disables vector labels and reverts back to rendering map labels on the map tile images on the server. This is a good option to enable when rendering large data sets. Additionally, in case where performance issues are known, the map will automatically use “lite” mode to improve the overall performance. This can happen when using the map on a less powerful device or browser, or when accessing the map from a location that is known to have slow network speeds. 

> [!NOTE]
> Vector map labels are not supported in China, Japan or South Korea. 
 