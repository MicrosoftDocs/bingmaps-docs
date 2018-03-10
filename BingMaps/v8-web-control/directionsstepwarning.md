---
title: "DirectionsStepWarning | Microsoft Docs"
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
---
# DirectionsStepWarning
Represents a route direction warning, such as a traffic congestion warning.

| Name        | Type   | Description  |
|-------------|--------|--------------|
| `origin`      | string | Where the warning starts.  |
| `severity`    | string | The severity of the warning. Values can be: Low Impact, Minor, Moderate, Serious or None. |
| `text`        | string | The warning text. |
| `to`          | string | Where the warning ends. |
| `warningType` | string | The type of warning. A list of Warning type values can be found [here](../rest-services/warning-types.md). |