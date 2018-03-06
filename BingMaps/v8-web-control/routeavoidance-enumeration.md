---
title: "RouteAvoidance Enumeration2 | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 2ea74174-8adf-4b71-a8d5-1e57c6c02c8e
caps.latest.revision: 4
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# RouteAvoidance Enumeration
Defines features to avoid when calculating the route. The `Microsoft.Maps.Directions.RouteAvoidance` enumeration has the following options.

| Name               | Description                                                           |
|--------------------|-----------------------------------------------------------------------|
| `none`             | Calculate the best route using any travel option available.           |
| `minimizeHighways` | Reduce the use of limited access highways when calculating the route. |
| `minimizeToll`     | Reduce the use of roads with tolls when calculating the route.        |
| `avoidHighways`    | Avoid using limited access highways when calculating the route.       |
| `avoidToll`        | Avoid using roads with tolls when calculating the route.              |
| `avoidExpressTrain` | Avoid using express trains when calculating the route. This option only affects transit routes that have the culture set to ja-jp. |
| `avoidAirline` | Avoid using airlines when calculating the route. This option only affects transit routes that have the culture set to ja-jp. |
| `avoidBulletTrain` | Avoid using bullet trains when calculating the route. This option only affects transit routes that have the culture set to ja-jp. |
