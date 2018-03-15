---
title: "GeoXmlStats Object | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 6fc69b54-592f-496e-83e8-2bee170b753a
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms:service: "bing-maps"
---
# GeoXmlStats Object
Statistics about the content and processing time of a XML feed.

| Name                | Type   | Description                                                              |
|---------------------|--------|--------------------------------------------------------------------------|
| `fileSize`          | number | The number of characters in the XML feed.                                |
| `numGroundOverlays` | number | Number of Ground Overlays in the XML feed.                               |
| `numLocations`      | number | Number of Location objects in the XML feed.                              |
| `numNetworkLinks`   | number | The number of network links in the XML feed.                             |
| `numPolygons`       | number | Number of Polygons objects in the XML feed.                              |
| `numPolylines`      | number | Number of Polylines objects in the XML feed.                             |
| `numPushpins`       | number | Number of Pushpins objects in the XML feed.                              |
| `numScreenOverlays` | number | Number of Screen Overlays in the XML feed.                               |
| `processingTime`    | number | The amount of time in milliseconds (ms) it took to process the XML feed. |
