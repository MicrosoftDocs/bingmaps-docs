---
title: "DirectionsStepWarning | Microsoft Docs"
description: Describes DirectionsStepWarning, which represents a route direction warning, and provides descriptions for each of its properties.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 02fbce04-7451-457a-ba14-1aa467a4f28b
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# DirectionsStepWarning

[!INCLUDE [bing-maps-web-control-sdk-retirement](../../../includes/bing-maps-web-control-sdk-retirement.md)]

Represents a route direction warning, such as a traffic congestion warning.

| Name        | Type   | Description  |
|-------------|--------|--------------|
| `origin`      | string | Where the warning starts.  |
| `severity`    | string | The severity of the warning. Values can be: Low Impact, Minor, Moderate, Serious or None. |
| `text`        | string | The warning text. |
| `to`          | string | Where the warning ends. |
| `warningType` | string | The type of warning. See the list of [Warning Type values](../../../rest-services/routes/warning-types.md) |