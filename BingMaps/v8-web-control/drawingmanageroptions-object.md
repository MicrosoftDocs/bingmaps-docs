---
title: "DrawingManagerOptions Object | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: b67388be-8b6f-42bd-9c9f-034d74cfe425
caps.latest.revision: 4
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# DrawingManagerOptions Object
An object that contains options to change the settings of the drawing manager.

| Name   | Type            | Description                                       |
|--------|-----------------|---------------------------------------------------|
| drawingBarActions | [DrawingBarAction](../v8-web-control/drawingbaraction-enumeration.md) | Set of buttons to show in the drawing bar.<br/><br/> **Example:**<br/><br/>var da = Microsoft.Maps.DrawingTools.DrawingBarAction;<br/>manager.setOptions({ drawingBarActions: da.polyline &#124; da.polygon &#124; da.erase  }); |
| fillColor   | string or [Color](../v8-web-control/color-class.md) | The fill color used for pushpins and polygons.    |
| strokeColor | string or [Color](../v8-web-control/color-class.md) | The stroke color used for polylines and polygons. |
