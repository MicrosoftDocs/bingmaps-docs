---
title: "Pushpin Class | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: f472ed7a-b85c-4266-8060-1d0cd4780791
caps.latest.revision: 15
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms:service: "bing-maps"
---
# Pushpin Class
Pushpins, sometimes also referred to as markers or MapIcons on other mapping platforms, are one of the primary ways of marking a location on a map. The Pushpin class derives from the `IPrimitive` interface.

**Note:** When an array of pushpins are added to the map or a layer, the first pushpin is rendered last. The idea being that if the array contained search results, the first/most relevant result would be rendered on top rather than being covered by other nearby pushpins. This is a fundamental change made to improve the user experience from how previous versions of Bing Maps rendered pushpins.

## Constructor

> Pushpin(location: [Location](../v8-web-control/location-class.md), options?: [PushpinOptions](../v8-web-control/pushpinoptions-object.md))

## Methods

The Pushpin class has the following methods.

| Name                            | Return Type     | Description                                                                                                                                                           | 
|---------------------------------|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `getAnchor()`                     | [Point](../v8-web-control/point-class.md) | Returns the point on the pushpin icon which is anchored to the pushpin location. An anchor of (0,0) is the top left corner of the icon.                   |
| `getClickedStyleEnabled()`        | boolean         | Returns whether the pushpin clicked style is enabled.                                                                                                               |
| `getColor()`                      | string or [Color](../v8-web-control/color-class.md) | Returns the color option of the pushpin.                                                                                                        |
| `getCursor()`                     | string          | Gets the css cursor value when the pushpin has mouse events on it.                                                                                                            |
| `getDraggable()`                    | boolean         | Returns a boolean indicating if the pushpin is draggable or not.                                                                                                  |
| `getHoverStyleEnabled()`          | boolean         | Returns whether the default pushpin hover style is enabled.                                                                                                         |
| `getIcon()`                       | string          | Returns the pushpin icon path.                                                                                                                                      |  
| `getLocation()`                   | [Location](../v8-web-control/location-class.md)  | Returns the location of the pushpin.                                                                                                               |
| `getRoundClickableArea()`         | boolean         | Returns whether the clickable area of the pushpin is an ellipse.                                                                                                    |
| `getText()`                       | string          | Returns the text associated with the pushpin.                                                                                                                       |
| `getTextOffset()`                 | [Point](../v8-web-control/point-class.md) | Returns the amount the text is shifted from the pushpin icon.                                                                                             |
| `getTitle()`                      | string          | Returns the title label of the Pushpin.                                                                                                                             |
| `getSubTitle()`                   | string          | Returns the subtitle label of the Pushpin.                                                                                                                          |
| `getVisible()`                    | boolean         | Returns a boolean indicating whether the pushpin is visible or not. A value of false indicates that the pushpin is hidden, although it is still an entity on the map. |
| setLocation(loc: [Location](../v8-web-control/location-class.md))      |                 | Sets the location of the pushpin.                                                                                                              |
| setOptions(opt: [PushpinOptions](../v8-web-control/pushpinoptions-object.md)) |                 | Sets options for the pushpin.                                                                                                           |
 
## Properties

Name          | Type        | Description
------------- | ----------- | -----------------------------
`metadata`    | object      | Information that is linked to the pushpin. Some modules such as the GeoJSON, and Spatial Data Service modules will also often add information to this property.

## Events

Name            | Arguments | Description
--------------- | --------- | ----------------------------------
`changed`       | [IPrimitiveChangedEventArgs](../v8-web-control/iprimitivechangedeventargs-object.md) | Occurs when the location or options of the pushpin has changed. 
`click`         | [MouseEventArgs](../v8-web-control/mouseeventargs-object.md) | Occurs when the mouse is used to click the pushpin.
`dblclick` | [MouseEventArgs](../v8-web-control/mouseeventargs-object.md) | Occurs when the mouse is used to double click the pushpin.
`drag`          | [MouseEventArgs](../v8-web-control/mouseeventargs-object.md) | Occurs when the pushpin is being dragged.
`dragend`       | [MouseEventArgs](../v8-web-control/mouseeventargs-object.md) | Occurs when the pushpin stops being dragged.
`dragstart`     | [MouseEventArgs](../v8-web-control/mouseeventargs-object.md) | Occurs when the pushpin starts being dragged.
`mousedown`     | [MouseEventArgs](../v8-web-control/mouseeventargs-object.md) | Occurs when the left mouse button is pressed when the mouse is over the pushpin.
`mouseout`      | [MouseEventArgs](../v8-web-control/mouseeventargs-object.md) | Occurs when the mouse cursor moves out of the area covered by the pushpin.
`mouseover`     | [MouseEventArgs](../v8-web-control/mouseeventargs-object.md) | Occurs when the mouse is over the pushpin.
`mouseup`       | [MouseEventArgs](../v8-web-control/mouseeventargs-object.md) | Occurs when the left mouse button is lifted up when the mouse is over the pushpin.

## Examples
  
  * [Default Pushpin with Text](../v8-web-control/default-pushpin-with-text-example.md)
  * [Changing the color of the default Pushpin](../v8-web-control/changing-the-color-of-the-default-pushpin.md)
  * [Custom Image Pushpin](../v8-web-control/custom-image-pushpin-example.md)
  * [Custom SVG File Pushpin](../v8-web-control/custom-svg-file-pushpin-example.md)
  * [Custom Inline SVG Pushpin](../v8-web-control/custom-inline-svg-pushpin-example.md)
  * [Dynamically create SVG Pushpin](../v8-web-control/dynamically-create-svg-pushpin-example.md)
  * [Custom Base64 Image Pushpin](../v8-web-control/custom-base64-image-pushpin-example.md)
  * [Custom Canvas Pushpin](../v8-web-control/custom-canvas-pushpin-example.md)
  * [Font based Pushpins](../v8-web-control/font-based-pushpins.md)
  * [HTML Pushpin Overlay](../v8-web-control/html-pushpin-overlay.md)
  * [Image and Canvas Pushpin](../v8-web-control/image-and-canvas-pushpin-example.md)
  * [Pushpin Events](../v8-web-control/pushpin-events-example.md)
  * [Pushpin Hover Style](../v8-web-control/pushpin-hover-style.md) 
  * [Anchoring Pushpins](../v8-web-control/anchoring-pushpins.md) 
  
  ## See Also

  * [PushpinOptions Object](../v8-web-control/pushpinoptions-object.md)
  * [Pushpin Examples](../v8-web-control/pushpins.md)
  