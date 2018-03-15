---
title: "PolylineOptions Object | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 54fb429b-2eb0-4512-a529-feb74438900d
caps.latest.revision: 6
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms:service: "bing-maps"
---
# PolylineOptions Object
The following polyline option properties can be used to create customized polylines.

Name             | Type                   | Description
---------------- | ---------------------- | -------------------------------------------
`cursor` | string | The css cursor to show when the polyline has mouse events on it. Default value is **pointer** (hand).
`generalizable` | boolean | Automatically generate and draw generalized polyline based on the zoom level to improve rendering performance. Default **true**
`strokeColor`      | string _or_ [Color](../v8-web-control/color-class.md)   | The color of the polyline.
`strokeDashArray`  | string _or_ number[]	  | A string representing the stroke/gap sequence to use to draw the polyline. The string must be in the format S, G, S*, G*, where S represents the stroke length and G represents gap length. Stroke lengths and gap lengths can be separated by commas or spaces. For example, a stroke dash string of "1 4 2 1" would draw the polyline with a dash, four spaces, two dashes, one space, and then repeated.
`strokeThickness`  | number                 | The thickness of the polyline.
`visible`          | boolean                | A boolean indicating whether to show or hide the polyline. A value of false indicates that the polyline is hidden, although it is still an entity on the map.
