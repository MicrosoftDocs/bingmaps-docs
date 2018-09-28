---
title: "GeoJsonReadOptions Object | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: dedc3ac2-6a6d-42bb-a6c0-5e8610d82236
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# GeoJsonReadOptions Object
Options used to customize how a GeoJson file is read and loaded via the [Configuration Driven Maps framework](../v8-web-control/configuration-driven-maps-framework.md).

## Properties

| Name        | Type      | Description                    |
|-----------------|---------------|------------------------|
| jsonpQueryParam | string        | If the GeoJSON file is hosted on a different domain, and [CORS](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing) is not enabled, but does support [JSONP](https://en.wikipedia.org/wiki/JSONP), you will need to specify the name of JSONP URL parameter that can be used to download the file across different domains. |
| layerName       | string        | An optional name to identify the layer by.   |
| style           | [StylesOptions](../v8-web-control/stylesoptions-object.md) | The styles to apply to shapes that don't have a defined style in the XML.  |