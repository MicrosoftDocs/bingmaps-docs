---
title: "GeoXmlWriteOptions Object | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 4c0b2393-070c-4abc-b4a4-65dcc64493fc
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# GeoXmlWriteOptions Object
Options that are used to customize how the GeoXml writes XML.

| Name             | Type         | Description  |
|------------------|--------------|--------------|
| `indentChars`    | string       | The characters to use to create an indent in the XML data. Default: **\\t** |
| `newLineChars`   | string       | The characters to use to create a new line in the XML data. Default: **\\r\\n** |
| `prettyPrint`    | boolean      | A boolean indicating if the generated XML should be use new lines and indents to make the generated nicely formatted. Default: **true** |
| `roundLocations` | boolean      | A boolean indicating if Location and LocationRect values should be rounded off to 6 decimals. Default: **false** |
| `validate`       | boolean      | A boolean indicating if the shapes should be made valid before writing. If set to true, will use the Geometry.makeValid function of the SpatialMath module. Default: **false** |
| `xmlFormat`      | [GeoXmlFormat](geoxmlformat-enumeration.md) | The XML format to write the shapes to. Default: **Kml**   |
