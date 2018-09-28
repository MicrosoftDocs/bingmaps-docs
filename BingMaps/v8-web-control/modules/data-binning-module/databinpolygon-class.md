---
title: "DataBinPolygon Class | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 1dd760a3-d1f2-434a-bc21-4b8cfd33bf0a
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# DataBinPolygon Class
This class is an extension of the Polygon class and has all the same methods, events and properties of that class. In addition to this, the DataBinPolygon also exposes additional details about the data bin through its `dataBinInfo` property.

## Properties

| Name        | Type        | Description                                                                    |
|-------------|-------------|--------------------------------------------------------------------------------|
| `dataBinInfo` | [DataBinInfo](../v8-web-control/databininfo-object.md) | Information about the data bin; the contained pushpins and calculated metrics. |