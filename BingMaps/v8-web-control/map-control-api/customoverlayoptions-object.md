---
title: "CustomOverlayOptions Object | Microsoft Docs"
description: "This article describes properties of the CustomOverlayOptions Object that can be used when initializing a CustomOverlay."
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: d0c59ed0-916e-4714-b378-c6bd9d7c2c1a
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# CustomOverlayOptions Object

The following is a list of option properties that can be used when initializing a [CustomOverlay](customoverlay-class.md).

## Properties

| Name          | Type    | Description                  |
|---------------|---------|------------------------------|
| beneathLabels | boolean | Specifies if the custom overlay should be rendered above or below the label layer of the map. When above, elements in the overlay can be clickable. Default: **true** |
| drawOrder | number | In case of multiple overlay, draw order defines the order of overlay in relation to labels/Poi's. drawOrder can be between -100 to -1 to display the overlay below the Labels/Pois or 1 to 100 to display the overlay above it. If this option is set, then beneathLabels is ignored. Default: **-1** |