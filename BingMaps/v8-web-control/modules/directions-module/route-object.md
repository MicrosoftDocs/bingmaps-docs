---
title: "Route Object | Microsoft Docs"
description: Describes the Route object, which represents a route, and provides descriptions for each of its properties.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 06302eac-0542-47cb-b208-91ff26f9b92f
caps.latest.revision: 4
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Route Object

Represents a route.

| Name	      | Type        | Description                                                                             |
|-------------|-------------|-----------------------------------------------------------------------------------------|
| `routeLegs` |	[RouteLeg](routeleg-object.md)[]	|The legs of the route. Each route leg represents the route between two waypoints. |
| `routePath` | [Location\[\]](../../map-control-api/location-class.md) | An array of locations that makes up the path of the route.