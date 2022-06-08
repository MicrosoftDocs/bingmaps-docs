---
title: Venue geometry JSON class | Microsoft Docs
description: Venue geometry JSON class encapsulates a polyline or polygon geometry within a venue entity.
ms.custom: 
ms.date: 05/26/2020
ms.reviewer: 
ms.suite: 
ms.tgt_pltfrm: 
ms.topic: article
ms.assetid: 7B7C56D5-2E4B-4CAC-9068-A43B0E807E84
caps.latest.revision: 3
author: DavidBuerer
ms.author: dbuerer
manager: 
ms.service: bing-maps
---
# Venue geometry JSON class

Encapsulates a polyline or polygon geometry within a venue [entity].

## Properties

| Property | Type       | Req? | Description |
|----------|------------|------|-------------|
| x        | number[]   |  ✔   | When combined with y, forms a series of coordinates that make up the geometry. |
| y        | number[]   |  ✔   | When combined with x, forms a series of coordinates that make up the geometry. |
| closed   | boolean    |      | Differentiates between a closed polygon and an open line. |
| inner    | [inner] [] |      | Holes within a polygon geometry. |

## Example

```json
{
  "x": [0, 1, 1, 0],
  "y": [1, 1, 0, 0],
  "closed": true,
  "inner": [ {"x": [0.25,0.25,0.75,0.75], "y": [0.75,0.25,0.25,0.75]} ]
}
```

[inner]: inner.md
[entity]: entity.md
