---
title: "Venue label JSON class | Microsoft Docs"
ms.custom: ""
ms.date: "05/26/2020"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: DAD91BE8-234E-4509-8EC1-6EF6D52A2DFF
caps.latest.revision: 3
author: "dbuerer"
ms.author: ""
manager: ""
ms.service: "bing-maps"
---
# Venue label JSON class

Encapsulates information on how to label a polygon geometry.

## Properties

| Property | Type           | Req? | Description |
|----------|----------------|------|-------------|
| text     | string         |  ✔   | Text to display in the label. |
| rects    | [rectangle] [] |  ✔   | Rectangles to try to place the text of the label in. |

## Example

```json
{
  "text": "My Label", 
  "rect": {"angle":-10,"xy":[20, 30],"width":5.01E-05,"height":2.1E-05}
}
```

[rectangle]: rectangle.md
