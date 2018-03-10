---
title: "PolygonOptions Object1 | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: f17573ea-22bc-40c9-92cd-8df55f6bc709
caps.latest.revision: 7
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# PolygonOptions Object
The following polygon option properties can be used to create customized polygons. 

Name               | Type                        | Description
------------------ | --------------------------- | ----------------------------------------------
`cursor` | string | The css cursor to show when the polygon has mouse events on it. Default value is **pointer** (hand).
`generalizable` | boolean | Automatically generate and draw generalized polygon based on the zoom level to improve rendering performance. Default **true**
`fillColor`          | string _or_ [Color](../v8-web-control/color-class.md)  | The color of the inside of the polygon.
`strokeColor`       | string _or_ [Color](../v8-web-control/color-class.md) | The color of the polygon rings.
`strokeDashArray`    | string _or_ number[]        | A string representing the stroke/gap sequence to use to draw the polygon rings. The string must be in the format S, G, S*, G*, where S represents the stroke length and G represents gap length. Stroke lengths and gap lengths can be separated by commas or spaces. For example, a stroke dash string of "1 4 2 1" would draw the polygon with a dash, four spaces, two dashes, one space, and then repeated.
`strokeThickness`    | number                 | The thickness of the polygon rings.
`visible`            | boolean                | A boolean indicating whether to show or hide the polyline. A value of false indicates that the polygon is hidden, although it is still an entity on the map.
