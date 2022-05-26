---
title: "Module Loading Methods2 | Microsoft Docs"
description: Describes module loading methods, which allow registering and loading custom modules for map control, and provides the list of methods.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 95e0a746-764c-49ed-a3ba-01bcc611accb
caps.latest.revision: 6
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Module Loading Methods

The following methods allow you to register and load your own modules for use by the map control. Al of these static methods are under the `Microsoft.Maps` namespace.

Name                                                                            | Description
------------------------------------------------------------------------------- | -----------------------------------
loadModule(moduleKey: string _or_ string[], options?: [ModuleOptions](../../map-control-api/moduleoptions-object.md) _or_ function())   | Loads the specified registered module, making its functionality available. You can provide the name of a single module or an array of names in. Options or a callback function that is called when the module is loaded can be specified.<br/><br/> To register a custom module, use the `registerModule` method before calling the `loadModule` method.
`moduleLoaded(moduleKey: string)`                                                          | Signals that the specified module has been loaded and if specified, calls the callback function in `loadModule`. Call this method at the end of your custom module script.
`registerModule(moduleKey:string, scriptURL:string, options:{styleURLs:string[]})`        | Registers a module with the map control. The name of the module is specified in **moduleKey**, the module script is defined in **scriptURL**, and the options provides the location of a *.css file to load with the module.

**_Tip_**: To minimize possible conflicts with other custom modules, choose a unique module name (defined in moduleKey). For example, you can use your company name in the name of the module.

Once you have registered a module, you can make its functionality available by loading it using `loadModule`.
