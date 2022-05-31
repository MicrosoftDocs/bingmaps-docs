---
title: "ConfigurableMapModule Object | Microsoft Docs"
description: "This article describes properties of the ConfigurableMapModule Object, which defines what module should be loaded and the data sets that should be loaded with it.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 10e599a9-221e-4e69-9f72-76305a986f2d
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# ConfigurableMapModule Object

Defines which module should be loaded, and the data sets that should be loaded with it. Currently supports the "Microsoft.Maps.GeoXml" and "Microsoft.Maps.GeoJson" modules. Additional modules can be specified and will be loaded, but will not do anything other than load those modules into the web app, which is useful when loading the configuration file via the [ConfigurableMap class](configurablemap-class.md).

## Properties

| Name          | Type                                    | Description                                         |
|---------------|-----------------------------------------|-----------------------------------------------------|
| moduleName    | string                                  | **Required**. Initial map options.                      |
| moduleOptions | [PostModuleAction](postmoduleaction-object.md) _or_ [PostModuleAction](postmoduleaction-object.md)\[\] | A set of steps to execute after a module is loaded. |
