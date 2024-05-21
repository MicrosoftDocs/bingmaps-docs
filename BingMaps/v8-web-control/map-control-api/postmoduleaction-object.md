---
title: "PostModuleAction Object | Microsoft Docs"
description: "Describes the PostModuleAction object and provides a table that outlines the type and description for various properties."
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 80d65157-369f-45c4-b8ff-3d2fac536192
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# PostModuleAction Object

[!INCLUDE [bing-maps-web-control-sdk-retirement](../../includes/bing-maps-web-control-sdk-retirement.md)]

Defines the steps to execute after the module is loaded.

## Properties

| Name            | Type               | Description               |
|-----------------|--------------------|---------------------------|
| addLayerFromUrl | string             | A URL to load the data layer from. Currently supports data in GeoJSON, GeoRSS (with inline GML), GPX, KML, and KMZ formats. Note that your data files must be hosted on a publicly accessible endpoint and have CORS ([Cross-origin Resource Sharing](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing)) enabled to allow cross domain access. |
| geoXmlOption    | [GeoXmlLayerOptions](../modules/geoxml-module/geoxmllayeroptions-object.md) | Options to use when loading data via the GeoXml module.  |
| geoJsonOption   | [GeoJsonReadOptions](../modules/geojson-module/geojsonreadoptions-object.md) | Options to use when loading data via the GeoJson module. |
