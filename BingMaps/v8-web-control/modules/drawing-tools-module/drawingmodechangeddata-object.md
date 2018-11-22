---
title: "DrawingModeChangedData Object | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 7b82e48a-a19f-443a-89f5-8f84985ea6c9
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# DrawingModeChangedData Object
An object that contains the event arguments for when the drawing mode changes in the drawing tools.

| Name  | Type        | Description                                    |
|-------|-------------|------------------------------------------------|
| shape | [IPrimitive](../../map-control-api/iprimitive-class.md)  | The shape being modified by the drawing tools. |
| mode  | [DrawingMode](drawingmode-enumeration.md) | The new drawing mode.                          |
