---
title: "DataBinInfo Object | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 99e2a706-667f-4521-9d6a-53dd86eb9572
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# DataBinInfo Object
The result of a calculated data bin.

| Name              | Type           | Description                                                                                                                     |
|-------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------|
| containedPushpins | [Pushpin](../v8-web-control/pushpin-class.md)\[\]    | An array of all the pushpins that are in the data bin.                                                                          |
| metrics           | [DataBinMetrics](../v8-web-control/databinmetrics-object.md) | A set of calculated metric values determined using the aggregationProperty value of all the pushpins contained in the data bin. |