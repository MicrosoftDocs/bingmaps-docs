---
title: "TrafficManager Class | Microsoft Docs"
description: Describes the TrafficManager class, which controls the show of traffic flow and incident data, and details the class's constructor and methods.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: ff06d899-5c8e-468c-b405-cb3fe8cea5d6
caps.latest.revision: 5
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# TrafficManager Class

[!INCLUDE [bing-maps-web-control-sdk-retirement](../../../includes/bing-maps-web-control-sdk-retirement.md)]

The **TrafficManager** class provides the ability to show traffic flow and incident data on top of the map. When creating an instance of the **TrafficManager** class the map must be passed as an argument to the constructor. 

## Constructor

> TrafficManager(map: [Map](../../map-control-api/map-class.md))

## Methods

Name                   | Type                | Description
-----------------------|---------------------|---------------------------------------------------------- 
`hide()`               |                     | Hides all traffic data.
`hideFlow()`           |                     | Hides the traffic flow layer.
`hideIncidents()`      |                     | Hides all traffic incidents.
`hideLegend()`         |                     | Hides the traffic legend.
setOptions(options: [TrafficOptions](trafficoptions-object.md)) | | Sets the options for the traffic manager.  
`show()`               |                     | Displays all traffic data.
`showFlow()`           |                     | Displays the traffic flow layer.
`showIncidents()`      |                     | Displays all traffic incidents.
`showLegend()`         |                     | Displays the traffic legend.

> [!NOTE]
> The individual functions for hiding and showing traffic information has been added for backwards compatibility with V7. In V8 a `setOptions` function has been added which is a single function that can be used to hide/show multiple traffic features.