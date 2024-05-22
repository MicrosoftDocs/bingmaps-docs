---
title: "Implementing Modules | Microsoft Docs"
description: Describes how to implement modules and provides steps for registering modules using the Microsoft.Maps.registerModule method.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 22d5b582-7cbf-436e-8783-bc72a119367a
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Implementing Modules

[!INCLUDE [bing-maps-web-control-sdk-retirement](../../../includes/bing-maps-web-control-sdk-retirement.md)]

Implementing modules is fairly easy and consists of the following two steps:

1.	Register the module if it isn’t already registered. This step can be skipped if using any of the built in modules in Bing Maps.
2.	Load the module and run any post load logic 

Before you can load a module, it must first be registered. All modules built into Bing Maps are already registered; however, if you are using a custom module you will need to register it. You can register a custom module using the using the `Microsoft.Maps.registerModule` method. This method takes in the name of the module and a URL to the JavaScript file that contains your module code. Optionally you can also pass in an array of URL’s that point to CSS stylesheets that your module requires. Here is an example of how to register a custom module: 

`Microsoft.Maps.registerModule('MyModule', 'http://example.com/MyModule.js');`

Here is an example of registering a custom module that also has a CSS stylesheet.

`Microsoft.Maps.registerModule('MyModule', 'http://example.com/MyModule.js', { styleURLs: ["http://example.com/MyModule.css"] });`

Now that the module is registered, it can be loaded. The determination of when to load a module really depends on the type of module you are using. For instance, you may want to load the traffic module right after the map is loaded so that you can show traffic data right away. If the map is being loaded as part of the page load process, then this module will also be loaded then. However, as an alternate example, the directions module frequently doesn’t need to be loaded until the user wants to get directions. The loading of this module can be delayed until the user has pressed a button to calculate directions. The benefit of doing this is that the code needed for the Directions module is only loaded if the user wants to calculate directions and is not loaded during the initial page load, which improves initial page load times. Here is the basic way of loading a module:

`Microsoft.Maps.loadModule('MyModule');`

With some modules you may want to run code after the module has loaded. In this case, you can pass in a callback function as an option when loading the module. Doing the following will trigger a function called myModuleLoadedCallback when the module has completed loading.

`Microsoft.Maps.loadModule('MyModule', myModuleLoadedCallback);`

Often more than one module may be desired. An array of module names can be passed into the loadModule function. When all the modules are loaded, the specified callback function will be called. Here is an example of how to do this:

`Microsoft.Maps.loadModule(['MyModule', 'MyModule2'], myModulesLoadedCallback);`

**Note for Bing Maps V7 developers**: In The Bing Maps V7 SDK the `loadModule` function took in an object that had a `callback` property which pointed to a callback function. This added extra code that isn’t needed. In the V8 SDK you can simply pass in the callback function into the `loadModule` function. However, to minimize migration efforts we have added support to handle the older method of loading a module using an object with a `callback` property.
