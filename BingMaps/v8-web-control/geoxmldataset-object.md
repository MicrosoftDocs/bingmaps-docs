---
title: "GeoXmlDataSet Object | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 48872248-322b-4677-9513-c80dcd5e64bd
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms:service: "bing-maps"
---
# GeoXmlDataSet Object
A GeoXML result data set that is returned when reading a spatial XML file.

| Name           | Type                        | Description             |
|----------------|-----------------------------|-------------------------|
| `layers`         | ([Layer](../v8-web-control/layer-class.md) _or_ [GroundOverlay](../v8-web-control/groundoverlay-class.md))\[\] | An array of layers that are in the XML document. In shapes in KML that are in a child documents and folders of the main document or folder are grouped together in a data Layer. KML also supports GroundOverlay. |
| `screenOverlays` | [KmlScreenOverlay](../v8-web-control/kmlscreenoverlay-class.md)\[\]        | An array of screen overlays that have been parsed from a KML file.              |
| `shapes`         | [IPrimitive](../v8-web-control/iprimitive-class.md)\[\]              | An array of shapes that are in the XML document.                                |
| `stats`          | [GeoXmlStats](../v8-web-control/geoxmlstats-object.md)                 | Statistics about the content and processing time of a XML feed.                 |
| `summary`        | [GeoXmlSummaryMetadata](../v8-web-control/geoxmlsummarymetadata-object.md)       | Summary metadata provided at the document level of the XML feed data set.       |