---
title: "HeatMapLayer Class | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: e99b0b3e-b8ae-4f4c-8ad5-4fa2b2234445
caps.latest.revision: 8
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# HeatMapLayer Class
This is the main class thate provides that heat map functionality.

## Constructor

> HeatMapLayer(locations: ([Location](Location%20Class.md) | [Pushpin](Pushpin%20Class.md))[], options?: [HeatMapLayerOptions](../v8-web-control/heatmaplayeroptions-object.md))

## Methods

Name                                      | Return Type            | Description
----------------------------------------- | ---------------------- | --------------------------------------------
`clear()`                                 |                        | Clears all data in the heat map layer.
`dispose()`                               |                        | Disposes the heat map layer.
`getVisible()` | boolean | Returns a boolean indicating if the heat map layer is visible or not. 
setLocations(loc: ([Location](Location%20Class.md) _or_ [Pushpin](Pushpin%20Class.md))[])  |                        | Specifies the locations to use when generating the heat map.
setOptions(opt: [HeatMapLayerOptions](../v8-web-control/heatmaplayeroptions-object.md))   |                        | Sets the options to use with the heat map layer.
`setVisible(visible: boolean)`  | | Sets the visibility of the heat map layer.
