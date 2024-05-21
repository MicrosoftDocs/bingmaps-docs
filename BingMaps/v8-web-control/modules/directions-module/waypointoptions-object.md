---
title: "WaypointOptions Object | Microsoft Docs"
description: Describes the properties available in the WaypointOptions object.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 283af52e-e0a2-4032-8640-0953dbe12363
caps.latest.revision: 4
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# WaypointOptions Object

[!INCLUDE [bing-maps-web-control-sdk-retirement](../../includes/bing-maps-web-control-sdk-retirement.md)]

The following is a list of properties that are available in the WaypointOptions object.

| Name         | Type     | Description  |
|--------------|----------|--------------|
| `address`    | string   | The address string of the waypoint. For example, the following strings are valid for this parameter: "Seattle", "1 Microsoft Way, Redmond, WA". Either the address or location property must be specified. |
| `isViaPoint` | boolean  | A boolean indicating whether the waypoint is a via point. A via point is a point along the route that is not a stop point. Set this property to true if you just want the route to pass through this location. Default: **false**     |
| `location`   | [Location](../../map-control-api/location-class.md) | The location of the waypoint. Either the `address` or `location` property must be specified.          |
