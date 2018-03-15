---
title: "TimeTypes Enumeration | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 5d6bc366-0511-4c2e-889c-1d00249cf9f3
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms:service: "bing-maps"
---
# TimeTypes Enumeration
Defines the transit time type. The `Microsoft.Maps.Directions.TimeTypes` enumeration has the following options.

| Name             | Description                                                                                |
|------------------|--------------------------------------------------------------------------------------------|
| `arrival`        | The dateTime parameter contains the desired arrival time for a transit request.            |
| `departure`      | The dateTime parameter contains the desired departure time for a transit request.          |
| `firstAvailable` | The dateTime parameter should be ignored and the first available transit taken.            |
| `lastAvailable`  | The dateTime parameter contains the latest departure time available for a transit request. |

