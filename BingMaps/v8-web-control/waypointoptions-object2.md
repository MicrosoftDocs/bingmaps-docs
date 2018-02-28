---
title: "WaypointOptions Object2 | Microsoft Docs"
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
---
# WaypointOptions Object
The following is a list of properties that are available in the WaypointOptions object.

| Name         | Type     | Description  |
|--------------|----------|--------------|
| `address`    | string   | The address string of the waypoint. For example, the following strings are valid for this parameter: "Seattle", "1 Microsoft Way, Redmond, WA". Either the address or location property must be specified. |
| `isViaPoint` | boolean  | A boolean indicating whether the waypoint is a via point. A via point is a point along the route that is not a stop point. Set this property to true if you just want the route to pass through this location. Default: **false**     |
| `location`   | [Location](Location%20Class.md) | The location of the waypoint. Either the `address` or `location` property must be specified.          |
