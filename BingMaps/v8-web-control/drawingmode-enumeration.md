---
title: "DrawingMode Enumeration | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 8b4d5be2-4887-4f39-bea0-8269dc601c91
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms:service: "bing-maps"
---
# DrawingMode Enumeration
The different drawing modes that the drawing manager can be set to. This can be accessed by **Microsoft.Maps.DrawingTools.DrawingMode.[mode_name]**.

| Name       | Description                                                  |
|------------|--------------------------------------------------------------|
| `edit`     | Edit an existing shape. Click on a shape to edit it.         |
| `erase`    | Erase and existing shape. Click on the shapes to erase them. |
| `none`     | Sets the drawing manager into an idle mode.                  |
| `polygon`  | Allow the user to draw a polygon.                            |
| `polyline` | Allow the user to draw a polyline.                           |
| `pushpin`  | Allow the user to draw a pushpin.                            |