---
title: "CustomOverlay Class | Microsoft Docs"
description: "This article shares methods and tips for the CustomOverlay Class, which lets you create custom overlays on top of the map."
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 83ae557f-40b5-4908-94f8-21be12a24923
caps.latest.revision: 5
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# CustomOverlay Class

[!INCLUDE [bing-maps-web-control-sdk-retirement](../../includes/bing-maps-web-control-sdk-retirement.md)]

You can use this class to create custom overlays on top of the map. These can be static overlays such as custom navigation bars, or dynamic overlays such as custom visualization layers. Custom overlays can be added to the map just like any other layer using the `map.layers` property.

## Constructor

> CustomOverlay(options?: [CustomOverlayOptions](customoverlayoptions-object.md))

## Methods

| Name        | Return Type | Description                                                                                     |
|-------------|-------------|-------------------------------------------------------------------------------------------------|
| `getHtmlElement()`  | `HTMLElement` | Gets the HTML element of this custom overlay.                                             |
| `getMap()` | [Map](map-class.md) | Gets the map object that the overlay is has been added to. This will be null until the onLoad function is called. |
| `setHTMLElement(elm: HTMLElement)` |             | Updates the HTML element of this custom overlay.                           |
| `onAdd()`                          |             | Implement this method to perform any task that should be done when the overlay is added to the map.               |
| `onLoad()`                         |             | Implement this method to perform any task that should be done after the overlay has been added to the map.         |
| `onRemove()`                       |             | Implement this method to perform any tasks that should be done when the overlay is removed from the map.           |

To implement, inherit this class through the prototype property of your custom class. This class can implement three methods: `onAdd()`, `onLoad()`, `onRemove()`.

 * The `onAdd()` function is triggered when the overlay has been added to a map instance. This is a good place to create any required DOM element and pass it into the `setHTMLElement` function.
 * The `onLoad()` function is triggered after the overlay is added to a map instance.
 * The `onRemove()` function is triggered when the overlay is removed from the map instance.

For example:

```javascript
//Define a custom overlay class that inherits from the CustomOverlay class.
MyCustomOverlay.prototype = new Microsoft.Maps.CustomOverlay();

//Define a constructor for the custom overlay class.
function MyCustomOverlay() {
}

MyCustomOverlay.prototype.onAdd = function () {
    //Logic to perform when adding overlay to map.
};

MyCustomOverlay.prototype.onLoad = function () {
    //Logic to perform after overlay has been added to the map.
};

MyCustomOverlay.prototype.onAdd = function () {
    //Logic to perform when overlay has been removed from the map.
};

//Implement the new custom overlay class.
var overlay = new MyCustomOverlay();

//Add the custom overlay to the map.
map.layers.insert(overlay);
```

**Tips:**

 * Turn your custom overlay class into a custom module to make it easier to reuse it in additional applications.
 * If you want to overlay elements above the map but don’t need to update their position, you can also float a DOM element above the map using absolute positioning.
 * If you want to create a new visualization, insert a canvas element that is the same dimensions as the map and use the view change events to redraw your data.
 
 ## See Also
 
* [Simple Static Overlay](../map-control-concepts/custom-overlays/simple-static-overlay.md)
* [Topography Overlay](../map-control-concepts/custom-overlays/topography-overlay.md)
* [HTML Pushpin Overlay](../map-control-concepts/custom-overlays/html-pushpin-overlay.md)
* [Dynamic Canvas Overlay](../map-control-concepts/custom-overlays/dynamic-canvas-overlay.md)
