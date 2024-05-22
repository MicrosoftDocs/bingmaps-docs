---
title: "BufferEndCap Enumeration | Microsoft Docs"
description: Describes the BufferEndCap enumeration, which defines end of line buffering, and provides a list of line end types and a diagram demonstrating the different end cap types.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 7810466f-2b26-44cb-a96f-517a62f3f413
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# BufferEndCap Enumeration

[!INCLUDE [bing-maps-web-control-sdk-retirement](../../../includes/bing-maps-web-control-sdk-retirement.md)]

This enumeration defines how the end of a line should be buffered. You can access this enumeration with the `Microsoft.Maps.SpatialMath.Geometry.BufferEndCap` namespace.

| Name | Description |
|------|-------------|
| Round | Adds a rounded end to a buffered line. |
| Flat | Adds a flat end to a buffered line that touches the end of the line. |
| Square | Adds a square end to a buffered line that has a buffer area at the end of the line |

The following diagram shows the different between these different end caps.

![BMV8_BufferEndCaps](../../media/bmv8-bufferendcaps.png)