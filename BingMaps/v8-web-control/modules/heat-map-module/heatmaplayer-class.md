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
ms.service: "bing-maps"
---

# HeatMapLayer Class

This is the main class that provides that heat map functionality.

## Constructor

> HeatMapLayer(locations: ([Location](../../map-control-api/location-class.md) | [Pushpin](../../map-control-api/pushpin-class.md))[], options?: [HeatMapLayerOptions](heatmaplayeroptions-object.md))

## Methods

Name                                      | Return Type            | Description
----------------------------------------- | ---------------------- | --------------------------------------------
`clear()`                                 |                        | Clears all data in the heat map layer.
`dispose()`                               |                        | Disposes the heat map layer.
`getVisible()` | boolean | Returns a boolean indicating if the heat map layer is visible or not. 
setLocations(loc: ([Location](../../map-control-api/location-class.md) _or_ [Pushpin](../../map-control-api/pushpin-class.md))[])  |                        | Specifies the locations to use when generating the heat map.
setOptions(opt: [HeatMapLayerOptions](heatmaplayeroptions-object.md))   |                        | Sets the options to use with the heat map layer.
`setVisible(visible: boolean)`  | | Sets the visibility of the heat map layer.
