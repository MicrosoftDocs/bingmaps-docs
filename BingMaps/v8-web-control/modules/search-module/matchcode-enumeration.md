---
title: "MatchCode Enumeration | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 67734540-ac51-4ac4-9a36-f96f2a7f822a
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# MatchCode Enumeration

Defines the geocoding level of the location match found by the geocoder.

| Name | Description |
|-------------|-----------------------------------------------------------|
| `none`        | No match was found.                                       |
| `good`        | The match was good.                                       |
| `ambiguous`   | The match was ambiguous. Multiple results were returned.  |
| `upHierarchy` | The match was found by a broader search.                  |
| `modified`    | The match was found, but possibly using a modified query. |

Additional details are defined in the [Bing Maps REST Location API](../../../rest-services/locations/index.md)
