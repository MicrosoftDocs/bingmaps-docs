---
title: "IPrimitive Class | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 4f881622-efc2-4e6b-a6c7-4765e94a2b76
caps.latest.revision: 4
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms:service: "bing-maps"
---
# IPrimitive Class
All shapes __Pushpins, Polylines__ and __Polygons__ derive from the IPrimitive interface. This means that they can be passed into any function that takes in an IPrimitive object. Also, any function that returns an IPrimitive is capable of returning any of these shapes.

All IPrimitive objects have a `metadata` property which can be used to link data to a shape object. Some modules such as the GeoJSON module also use this property.
