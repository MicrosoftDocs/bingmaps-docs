---
title: "ConfigurableMapOptions Object | Microsoft Docs"
description: "This article describes properties of the ConfigurableMapOptions Object; the root object which defines a configurable map."
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
| mapOptions | [MapOptions](mapoptions-object.md)                | **Required**. Initial map options.     |
| modules    | [ConfigurableMapModule](configurablemapmodule-object.md)\[\] | List of configuration modules to load. |
