---
title: "DirectionsEventArgs Object | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 105f6d10-96d4-4e07-b0f8-e3ffb00e13ac
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# DirectionsEventArgs Object

The following is a list of properties that are available in the DirectionsEventArgs object.

| Name         | Type             | Description                                                                     |
|--------------|------------------|---------------------------------------------------------------------------------|
| routeSummary | [RouteSummary](routesummary-object.md)\[\] | The route summary (or summaries) of the route(s) defined in the route property. |
| route        | [Route](route-object.md)\[\]        | The calculated route (or routes, if the route mode is transit).                 |