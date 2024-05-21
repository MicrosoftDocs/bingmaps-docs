---
title: "GeoXmlSummaryMetadata Object | Microsoft Docs"
description: Describes the GeoXmlSummaryMetadata object and its properties.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: d4507edf-74ba-46ec-ab44-62ef52a689e5
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# GeoXmlSummaryMetadata Object

[!INCLUDE [bing-maps-web-control-sdk-retirement](../../../includes/bing-maps-web-control-sdk-retirement.md)]

Summary metadata provided at the document level of the XML feed data set.

| Name          | Type         | Description                                                              |
|---------------|--------------|--------------------------------------------------------------------------|
| `bounds`      | LocationRect | The bounds of all the shapes and layers in the XML document.             |
| `description` | string       | The description of the content of the XML document.                      |
| `metadata`    | object       | Any additional metadata that the XML document may have. i.e. `atom:author` |
| `title`       | string       | The title or name of the content of the XML document.                    |
