---
title: Venue inner JSON class | Microsoft Docs
titleSuffix: Microsoft Bing Maps
description: Venue inner JSON class encapsulates a hole within a polygon geometry. This class is part of the venue JSON class structure.
ms.custom: 
ms.date: 05/26/2020
ms.reviewer: 
ms.suite: 
ms.tgt_pltfrm: 
ms.topic: article
ms.assetid: 788C378D-A997-4B2A-AD0A-8B690DFB229F
caps.latest.revision: 3
author: DavidBuerer
ms.author: dbuerer
manager: 
ms.service: bing-maps
---

# Venue inner JSON class

[!INCLUDE [bing-maps-web-control-sdk-retirement](../../../includes/bing-maps-web-control-sdk-retirement.md)]

Encapsulates a hole within a polygon [geometry].

This class is part of the [venue] JSON class structure.

## Properties

| Property | Type       | Req? | Description |
|----------|------------|------|-------------|
| x        | number[]   |  ✔   | When combined with y, forms a series of coordinates that make up the inner geometry. |
| y        | number[]   |  ✔   | When combined with x, forms a series of coordinates that make up the inner geometry. |

## Example

```json
{
  "x": [0.25,0.25,0.75,0.75],
  "y": [0.75,0.25,0.25,0.75]
}
```

[geometry]: geometry.md
[venue]: venue.md
