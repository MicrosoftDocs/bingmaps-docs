---
title: "DirectionsErrorEventArgs Object | Microsoft Docs"
description: Describes the DirectionsErrorEventArgs object, which contains direction event errors, and provides a list of related properties.
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

The following is a list of properties that are available in the DirectionsErrorEventArgs object.

| Name           | Type              | Description                                        |
|----------------|-------------------|----------------------------------------------------|
| `responseCode` | [RouteResponseCode](routeresponsecode-enumeration.md) | The code which identifies the error that occurred. |
| `message`      | string            | The error message.                                 |