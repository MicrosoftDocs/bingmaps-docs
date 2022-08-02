---
title: Venue label JSON class | Microsoft Docs
titleSuffix: Microsoft Bing Maps
description: Venue label JSON class encapsulates the position and contents of a text label to try to apply to an entity.
ms.custom: 
ms.date: 05/26/2020
ms.reviewer: 
ms.suite: 
ms.tgt_pltfrm: 
ms.topic: article
ms.assetid: DAD91BE8-234E-4509-8EC1-6EF6D52A2DFF
caps.latest.revision: 3
author: DavidBuerer
ms.author: dbuerer
manager: 
ms.service: bing-maps
---

# Venue label JSON class

Encapsulates the position and contents of a text label to try to apply to an entity.

This class is part of the [venue] JSON class structure.

## Properties

| Property | Type         | Req? | Description                                          |
|----------|--------------|------|------------------------------------------------------|
| text     | string       |  ✔   | Text to display in the label.                        |
| rects    | [rectangle]  |      | Rectangles to try to place the text of the label in. |

### Rectangles

Each rectangle should be tested in order and only drawn if the text fits in the rectangle and it does not overlap another label.
For polygons, the current ordering is that the first rectangle is horizontal and fits within the polygon, and the second is not
constrained by being horizontal but is the largest oriented rectangle that fits in the polygon.

## Example

```json
{
  "text": "My Label", 
  "rect": {"angle":-10,"xy":[20, 30],"width":5.01E-05,"height":2.1E-05}
}
```

[rectangle]: rectangle.md
[venue]: venue.md
