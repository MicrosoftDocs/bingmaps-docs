---
title: "ModuleOptions Object | Microsoft Docs"
description: This article describes the Bing Maps V8 web controls ModuleOptions Object and its callback and errorCallback functions.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: b538feab-de24-4843-b21a-a4637a7f0f62
caps.latest.revision: 4
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# ModuleOptions Object

[!INCLUDE [bing-maps-web-control-sdk-retirement](../../includes/bing-maps-web-control-sdk-retirement.md)]

Name             | Type                           | Description
---------------- | ------------------------------ | -----------------------------------------
`callback`	     | function()                     | A callback function that is fired after the module has loaded.
`credentials`    | string                         | **Deprecated.** A Bing Maps key that is used with the module when the module is loaded without a map.<br/><br/>It is recommended that the Bing Maps key be set as a URL parameter of the Bing Maps script reference as documented in the [Setting Map Control Parameters](../creating-and-hosting-map-controls/setting-map-control-parameters.md) document. This option will continue to work.
`errorCallback`  | function(errorMessage:string)  | A function that is called if there is an error loading the module.
