---
title: "Modular Framework | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: f72c11f1-e9e7-43bc-9764-c7dc5cbe3a80
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Modular Framework

The Bing Maps V8 SDK uses a modular framework as a way to minimize loading of features and functionalities that may not be needed. The base map control consists of a number of core features such as support for pushpins, polylines, polygons, and tile layers. Modules allow users to load only the features and functionalities they need, rather than loading everything up when the application starts. 

You can also save a lot of development time by using the modular framework in Bing Maps V8 for your own custom modules, as well. 

### References

  * [Out-of-the-Box Modules you can use](../../modules/index.md)
  * [Module Loading Methods](module-loading-methods.md)
  * [Implementing Modules](implementing-modules.md)
  * [Creating Custom Modules](creating-custom-modules.md)