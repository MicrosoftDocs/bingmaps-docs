---
title: "DirectionsErrorEventArgs Object | Microsoft Docs"
description: Describes the DirectionsErrorEventArgs object, which contains direction event errors, and provides descriptions for each of its properties.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: ec487ff0-8618-45ca-a188-764247d3b734
caps.latest.revision: 4
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# DirectionsErrorEventArgs Object

[!INCLUDE [bing-maps-web-control-sdk-retirement](../../../includes/bing-maps-web-control-sdk-retirement.md)]

The following is a list of properties that are available in the DirectionsErrorEventArgs object.

| Name           | Type              | Description                                        |
|----------------|-------------------|----------------------------------------------------|
| `responseCode` | [RouteResponseCode](routeresponsecode-enumeration.md) | The code which identifies the error that occurred. |
| `message`      | string            | The error message.                                 |