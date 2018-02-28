---
title: "RouteSubLeg Object | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 5480d1b8-0d91-461d-b594-c8115a8f8542
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# RouteSubLeg Object
Represents a route sub leg. A route sub leg is the part of the route between a stop point and a via point or between two via points. One or more sub legs make up a route leg.

|   Name             |   Type   |   Description                                                                |
|--------------------|----------|------------------------------------------------------------------------------|
| `actualEnd`        | [Location](Location%20Class.md) | The location of the last waypoint of the sub leg.     |
| `actualStart`      | [Location](Location%20Class.md) | The location of the first waypoint of the sub leg.    |
| `endDescription`   | string   | The description of the last waypoint of the sub leg.                         |
| `startDescription` | string   | The description of the first waypoint of the sub leg.                        |
