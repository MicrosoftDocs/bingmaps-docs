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
ms.service: "bing-maps"
---
# Pushpin Class
Pushpins, sometimes also referred to as markers or MapIcons on other mapping platforms, are one of the primary ways of marking a location on a map. The Pushpin class derives from the `IPrimitive` interface.

**Note:** When an array of pushpins are added to the map or a layer, the first pushpin is rendered last. The idea being that if the array contained search results, the first/most relevant result would be rendered on top rather than being covered by other nearby pushpins. This is a fundamental change made to improve the user experience from how previous versions of Bing Maps rendered pushpins.

## Constructor

> Pushpin(location: [Location](location-class.md), options?: [PushpinOptions](pushpinoptions-object.md))

## Methods

The Pushpin class has the following methods.

| Name                            | Return Type     | Description                                                                                                                                                           | 
|---------------------------------|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `getAnchor()`                     | [Point](point-class.md) | Returns the point on the pushpin icon which is anchored to the pushpin location. An anchor of (0,0) is the top left corner of the icon.                   |
| `getClickedStyleEnabled()`        | boolean         | Returns whether the pushpin clicked style is enabled.                                                                                                               |
| `getColor()`                      | string or [Color](color-class.md) | Returns the color option of the pushpin.                                                                                                        |
| `getCursor()`                     | string          | Gets the css cursor value when the pushpin has mouse events on it.                                                                                                            |
| `getDraggable()`                    | boolean         | Returns a boolean indicating if the pushpin is draggable or not.                                                                                                  |
| `getHoverStyleEnabled()`          | boolean         | Returns whether the default pushpin hover style is enabled.                                                                                                         |
| `getIcon()`                       | string          | Returns the pushpin icon path.                                                                                                                                      |  
| `getLocation()`                   | [Location](location-class.md)  | Returns the location of the pushpin.                                                                                                               |
| `getRoundClickableArea()`         | boolean         | Returns whether the clickable area of the pushpin is an ellipse.                                                                                                    |
| `getText()`                       | string          | Returns the text associated with the pushpin.                                                                                                                       |
| `getTextOffset()`                 | [Point](point-class.md) | Returns the amount the text is shifted from the pushpin icon.                                                                                             |
| `getTitle()`                      | string          | Returns the title label of the Pushpin.                                                                                                                             |
| `getSubTitle()`                   | string          | Returns the subtitle label of the Pushpin.                                                                                                                          |
| `getVisible()`                    | boolean         | Returns a boolean indicating whether the pushpin is visible or not. A value of false indicates that the pushpin is hidden, although it is still an entity on the map. |
| setLocation(loc: [Location](location-class.md))      |                 | Sets the location of the pushpin.                                                                                                              |
| setOptions(opt: [PushpinOptions](pushpinoptions-object.md)) |                 | Sets options for the pushpin.                                                                                                           |
 
## Properties

Name          | Type        | Description
------------- | ----------- | -----------------------------
`metadata`    | object      | Information that is linked to the pushpin. Some modules such as the GeoJSON, and Spatial Data Service modules will also often add information to this property.

## Events

Name            | Arguments | Description
--------------- | --------- | ----------------------------------
`changed`       | [IPrimitiveChangedEventArgs](iprimitivechangedeventargs-object.md) | Occurs when the location or options of the pushpin has changed. 
`click`         | [MouseEventArgs](mouseeventargs-object.md) | Occurs when the mouse is used to click the pushpin.
`dblclick` | [MouseEventArgs](mouseeventargs-object.md) | Occurs when the mouse is used to double click the pushpin.
`drag`          | [MouseEventArgs](mouseeventargs-object.md) | Occurs when the pushpin is being dragged.
`dragend`       | [MouseEventArgs](mouseeventargs-object.md) | Occurs when the pushpin stops being dragged.
`dragstart`     | [MouseEventArgs](mouseeventargs-object.md) | Occurs when the pushpin starts being dragged.
`mousedown`     | [MouseEventArgs](mouseeventargs-object.md) | Occurs when the left mouse button is pressed when the mouse is over the pushpin.
`mouseout`      | [MouseEventArgs](mouseeventargs-object.md) | Occurs when the mouse cursor moves out of the area covered by the pushpin.
`mouseover`     | [MouseEventArgs](mouseeventargs-object.md) | Occurs when the mouse is over the pushpin.
`mouseup`       | [MouseEventArgs](mouseeventargs-object.md) | Occurs when the left mouse button is lifted up when the mouse is over the pushpin.

## Examples
  
  * [Default Pushpin with Text](../map-control-concepts/pushpins/default-pushpin-with-text-example.md)
  * [Changing the color of the default Pushpin](../map-control-concepts/pushpins/changing-the-color-of-the-default-pushpin.md)
  * [Custom Image Pushpin](../map-control-concepts/pushpins/custom-image-pushpin-example.md)
  * [Custom SVG File Pushpin](../map-control-concepts/pushpins/custom-svg-file-pushpin-example.md)
  * [Custom Inline SVG Pushpin](../map-control-concepts/pushpins/custom-inline-svg-pushpin-example.md)
  * [Dynamically create SVG Pushpin](../map-control-concepts/pushpins/dynamically-create-svg-pushpin-example.md)
  * [Custom Base64 Image Pushpin](../map-control-concepts/pushpins/custom-base64-image-pushpin-example.md)
  * [Custom Canvas Pushpin](../map-control-concepts/pushpins/custom-canvas-pushpin-example.md)
  * [Font based Pushpins](../map-control-concepts/pushpins/font-based-pushpins.md)
  * [HTML Pushpin Overlay](../map-control-concepts/custom-overlays/html-pushpin-overlay.md)
  * [Image and Canvas Pushpin](../map-control-concepts/pushpins/image-and-canvas-pushpin-example.md)
  * [Pushpin Events](../v8-web-control/pushpin-events-example.md)
  * [Pushpin Hover Style](../map-control-concepts/pushpins/pushpin-hover-style.md) 
  * [Anchoring Pushpins](../map-control-concepts/pushpins/anchoring-pushpins.md) 
  
  ## See Also

  * [PushpinOptions Object](pushpinoptions-object.md)
  * [Pushpin Examples](../map-control-concepts/pushpins/index.md)
  