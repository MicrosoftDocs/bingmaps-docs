---
title: "GroundOverlayOptions Object | Microsoft Docs"
description: "This article describes the GroundOverlayOptions Object with each of its properties that are used to specify how to render a ground overlay on the map."
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 43ee2d3d-5b66-469c-a649-cf805b9dced2
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# GroundOverlayOptions Object

[!INCLUDE [bing-maps-web-control-sdk-retirement](../../includes/bing-maps-web-control-sdk-retirement.md)]

The options that specify how to render a ground overlay on the map.

| Name            | Type            | Description    |
|-----------------|-----------------|----------------|
| `backgroundColor` | string _or_ [Color](color-class.md) | A background color that fills the bounding box area beneath the ground overlay. Default: **transparent**   |
| `beneathLabels`   | boolean         | Specifies if the ground overlay should be rendered above or below the label layer of the map. When above, mouse events for elements under the overlay will be blocked. Default: **true** <br/><br/>This can only be set when creating the ground overlay and will not work with the `setOptions` function. |
| `bounds`          | [LocationRect](locationrect-class.md)    | **Required**. The bounding box to anchor the ground overlay to. This is required when creating a ground overlay.       |
| `imageUrl`        | string          | **Required**. The URL to the image to anchor to the map as a ground overlay. <br/><br/>**Tip**: SVG’s can be used as ground overlays. This is required when creating a ground overlay.   |
| `opacity`         | number          | The opacity of the ground overlay image. Decimal values between 0 and 1 are valid. Default: **1**   |
| `rotation`        | number          | An angle in degrees to rotate the overlay in a clockwise direction where 0 = north, 90 = east, 180 = south, 270 = west. Default: **0**  |
| `visible`         | boolean         | A boolean value indicating if the ground overlay is visible or not. Default: **true**   |
