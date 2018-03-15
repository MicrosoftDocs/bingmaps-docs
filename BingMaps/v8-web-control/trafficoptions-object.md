---
title: "TrafficOptions Object | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: ed93a58e-8f87-4b6a-a254-ab42a86a790d
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms:service: "bing-maps"
---
# TrafficOptions Object
The following is a list of properties that are available in the **TrafficOptions** object.

| Name               | Type     | Description                                                               |
|--------------------|----------|---------------------------------------------------------------------------|
| `flowVisible`      | boolean  | Displays the traffic flow layer.                                          |
| `incidentsVisible` | boolean  | Displays all traffic incidents.                                           |
| `legendVisible`    | boolean  | Displays the traffic legend.                                              |
| `opacity`          | number   | Sets the opacity of the traffic flow tile layer. Must be a number between 0 and 1. The default is 1 unless the map mode is set to lite, in which case the default is set to 0.7. |
