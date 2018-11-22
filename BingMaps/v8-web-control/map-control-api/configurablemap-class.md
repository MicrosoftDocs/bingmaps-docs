---
title: "ConfigurableMap Class | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: cb96d5dd-0aaf-42d3-89cc-c2fe784f8cb5
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# ConfigurableMap Class
This class allows lets you generate a map using a JSON configuration file using the [Configuration Driven Maps framework](../map-control-concepts/configuration-driven-maps-framework/index.md). This generates a map instance which you can then use just like you would when loading the Map class, however it has the added benefit of loading data layers that have been specified in the configuration file.

**Static Methods**

The ConfigurableMap class has the following static methods available.

| Name       | Return Type | Description         |
|------------|-------------|---------------------|
| createFromConfig(element: string _or_ HTMLElement, configFileUrl: string, withCredentials: boolean, requestHeaders?: IDictionary&lt;string&gt;, callback?: function(map: Map), errorCallback?: function(errorMsg: string)) |             | A static function that loads a map using a JSON configuraiton file.<br/><br/>• `element` - The parent element of the map as a CSS selector string or HTMLElement.<br/>• `configFileUrl` - The Url to download the JSON configuration file from. This should JSON file should contain a IConfigurableMapOptions object.<br/>• `withCredentials` - Creates the config file request with the setwithcredentials property.<br/>• `requestHeaders` - Set of headers that need to be added to config file request.<br/>• `callback` - Callback that is triggered when the map loads successfully.<br/>• `errorCallback` - Callback that is triggered when an error occurs when loading the map.   |
