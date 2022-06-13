---
title: "RouteOptimization Enumeration | Microsoft Docs"
description: Describes the RouteOptimization enumerators that define the optimization options for calculating directions such as shortestTime, timeWithTraffic, minimizeTransfers and minimizeWalking.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 5c92edf7-5de4-40f9-b5af-51a027174bd2
caps.latest.revision: 4
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# RouteOptimization Enumeration

Defines optimization options for calculating directions. The `Microsoft.Maps.Directions.RouteOptimization` enumeration has the following options.

| Name             | Description                                                                                           |
|------------------|-------------------------------------------------------------------------------------------------------|
| `shortestTime`     | The route is calculated to minimize the time. Traffic information is not used.                      |
| `shortestDistance` | The route is calculated to minimize the distance. Traffic information is not used.                  |
| `timeWithTraffic`  | The route is calculated to minimize the time and uses current traffic information.                  |
| `timeAvoidClosure` | The route is calculated to minimize the time and avoid road closures. Traffic information is not used in the calculation. |
| `minimizeMoney` | Minimize the cost when calculating directions. This option only affects transit routes that have the culture set to *ja-jp*. |
| `minimizeTransfers` | Minimize transit transfers when calculating directions. This option only affects transit routes that have the culture set to *ja-jp*. |
| `minimizeWalking` | Minimize the amount of walking when calculating directions. This option only affects transit routes that have the culture set to *ja-jp*. |