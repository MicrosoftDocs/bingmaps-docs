---
title: "DataBinType Enumeration | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 3a7c787f-9697-4b7d-92e0-15e18363bd02
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# DataBinType Enumeration
This enumeration is used to specify the shape of data bin rendered in the layer. This enumeration is specified as `Microsoft.Maps.DataBinType.[Name]` where Name can be any of the following values.

| Name          | Description                                             | Example |
|---------------|---------------------------------------------------------|---------|
| `circle`        | Renders data bins as circles in a square grid.          | ![BMV8_CircleDataBin](../v8-web-control/media/bmv8-circledatabin.PNG) |
| `hexagon`       | Renders data bins as hexagons with a flat top edge.     | ![BMV8_HexDataBin](../v8-web-control/media/bmv8-hexdatabin.PNG)
| `hexCircle`     | Renders data bins as circles in a hexagonal grid.       | ![BMV8_HexCircleDataBin](../v8-web-control/media/bmv8-hexcircledatabin.PNG) |
| `pointyHexagon` | Renders data bins as hexagons with a pointy top corner. | ![BMV8_PointyHexDataBin](../v8-web-control/media/bmv8-pointyhexdatabin.PNG) |
| `square`        | Renders data bins as a square grid.                     | ![BMV8_SquareDataBin](../v8-web-control/media/bmv8-squaredatabin.PNG) |