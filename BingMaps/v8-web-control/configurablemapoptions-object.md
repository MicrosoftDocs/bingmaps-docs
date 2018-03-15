---
title: "ConfigurableMapOptions Object | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 11184204-3ccb-4e45-b6d2-8ba18e881db1
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# ConfigurableMapOptions Object
This is the root object which defines a configurable map.

## Properties

| Name       | Type                      | Description                            |
|------------|---------------------------|----------------------------------------|
| mapOptions | [MapOptions](../v8-web-control/mapoptions-object.md)                | **Required**. Initial map options.     |
| modules    | [ConfigurableMapModule](../v8-web-control/configurablemapmodule-object.md)\[\] | List of configuration modules to load. |
