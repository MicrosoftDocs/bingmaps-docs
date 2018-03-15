---
title: "HeatMapLayerOptions Object | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: e815a92d-7237-4bcb-9336-074baf52f095
caps.latest.revision: 6
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms:service: "bing-maps"
---
# HeatMapLayerOptions Object
The following is a list of properties that are available in the **HeatMapLayerOptions** object.

Name                 | Type                    | Description
-------------------- | ----------------------- | -----------------------------------------------
`colorGradient`      | IDictionary of string     | The temperature gradient that is used to colorize the map. Default gradient:<br/><br/>`{`<br/>&nbsp;&nbsp;&nbsp;&nbsp;`   '0.00': 'rgb(255,0,255)',  // Magenta`<br/>&nbsp;&nbsp;&nbsp;&nbsp;`    '0.25': 'rgb(0,0,255)',    // Blue`<br/>&nbsp;&nbsp;&nbsp;&nbsp;`    '0.50': 'rgb(0,255,0)',    // Green`<br/>&nbsp;&nbsp;&nbsp;&nbsp;`    '0.75': 'rgb(255,255,0)', // Yellow`<br/>&nbsp;&nbsp;&nbsp;&nbsp;`    '1.00': 'rgb(255,0,0)'    // Red`<br/>`}`
`intensity`          | number                  | The intensity of each heat point. This is a decimal value between 0 and 1. This is used to specify how "hot" a single data point should be. Default: **0.5**
`opacity`            | number                  | The opacity of the HeatMapLayer canvas. Value should be a decimal between 0 and 1. Default: **1**
`radius`             | number                  | The radius to draw each data point on the map. Default: **10** 
`unit`               | string             | The distance units of the radius. Possible values are:<br/><br/>&nbsp; • `pixels`<br/>&nbsp; • `meters`<br/><br/>When set to pixels the size of each data point will always be the same radius, regardless of zoom level. When set to meters, the size of the data points will scale based on zoom level so as to ensure that the radius is spatially accurate. Default: **pixels**  
`visible` | boolean | A boolean indicating if the heat map layer is visible or not.