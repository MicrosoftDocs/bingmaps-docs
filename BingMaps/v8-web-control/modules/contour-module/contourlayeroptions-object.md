---
title: "ContourLayerOptions Object | Microsoft Docs"
description: Describes the ContourLayerOptions object, which is used with the ContourLayer class, and provides its options.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: a216a093-385c-4ca0-81fe-f4e7e27e1343
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# ContourLayerOptions Object

These options can be used to with the [ContourLayer](contourlayer-class.md) class.

| Name           | Type                                    | Description                                                                                                                                   |
|----------------|-----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| `colorCallback`  | function(contourValue: number _or_ string) | A callback function which defines the color of the contour line fill. The callback function must return a CSS color string or a Color object. |
| `polygonOptions` | [PolygonOptions](../../map-control-api/polygonoptions-object.md)                          | The polygon options that apply to all contour lines in this layer.                                                                            |
| `visible`        | boolean                                 | A boolean indicating if the layer is visible or not.                                                                                          |
| `zIndex`         | number                                  | The z-index of the layer.                                                                                                                     |
