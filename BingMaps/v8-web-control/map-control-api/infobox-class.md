---
title: "Infobox Class | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 5306a184-8ea4-44ae-bf11-611db93fd827
caps.latest.revision: 12
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Infobox Class
An infobox, also sometimes refer to as an info window or popup, is a simple panel that displays information over top the map. This is often used to display information linked to a location after clicking on a pushpin. 

## Constructor

> Infobox(location: [Location](location-class.md), options?: [InfoboxOptions](infoboxoptions-object.md))

When creating an infobox a location must be passed as an argument to the constructor. Optionally, [infobox options](infoboxoptions-object.md) can also be passed in as an argument.

## Methods

Here is a list of methods available in the Infobox class.

Name                               | Return Type           | Description
---------------------------------- | --------------------- | -----------------------------------
`getActions()`                     | [InfoboxActions](infoboxactions-object.md)\[\]    | Returns a list of the infobox actions, where each item is a `label` (the link text) or icon (the URL of the image to use as the icon link) and `eventHandler` (name of the function handling a click of the action link). Note that this is not supported when using `htmlContent`, use HTML anchors instead.
`getAnchor()`                      | [Point](point-class.md)                 | Returns the point on the infobox which is anchored to the map. An anchor of (0,0) is the top left corner of the infobox.
`getDescription()`                 | string                | Returns the string that is printed inside the infobox.
`getHeight()`                      | number                | Returns the height of the infobox.
`getHtmlContent()`                 | string                | Returns the infobox as HTML.
`getLocation()`                    | [Location](location-class.md)              | Returns the location on the map where the infobox’s anchor is attached.
`getMaxHeight()` | number | Gets the maximium height setting for the infobox.
`getMaxWidth()` | number | Gets the maximium width setting for the infobox.
`getOffset()`                      | [Point](point-class.md)                 | Returns the amount the infobox pointer is shifted from the location of the infobox, or if showPointer is false, then it is the amount the infobox bottom left edge is shifted from the location of the infobox. The default value is (0,0), which means there is no offset.
`getOptions()`                     | [InfoboxOptions](infoboxoptions-object.md)       | Returns the infobox options.
`getShowCloseButton()`             | boolean               | Returns a boolean indicating whether the infobox close button is shown.
`getShowPointer()`                 | boolean               | Returns a boolean indicating whether the infobox is drawn with a pointer.
`getTitle()`                       | string                | Returns a string that is the title of the infobox.
`getVisible()`                     | boolean               | Returns whether the infobox is visible. A value of false indicates that the infobox is hidden, although it is still an entity on the map.
`getWidth()`                       | number                | Returns the width of the infobox.
`getZIndex()`                      | number                | Gets the z-index of the infobox.
`setHtmlContent(content: string)`  |                       | Sets the HTML content of the infobox. You can use this method to change the look of the infobox. Note that infobox options are ignored if custom HTML is set. Also, when custom HTML is used to represent the infobox, the infobox is anchored at the bottom-left corner. 
setLocation(loc: [Location](location-class.md))       |                       | Sets the location on the map where the anchor of the infobox is attached.
setMap(map: [Map](map-class.md))| | Adds the infobox to the map. To remove an Infobox from the map, simply pass null into this function. **Note**: Calling this function removes all event handlers from the infobox. Add your event handlers to the infobox after calling this function. |
setOptions(opt: [InfoboxOptions](infoboxoptions-object.md), ignoreDelay?: boolean)	 |                       | Sets options for the infobox. If the `ignoreDelay` parameter is set to true, the `closeDelayTime` option will be ignored if the visible option is being changed from true to false.

## Events

| Name           | Arguments        | Description                                                            |
|----------------|------------------|------------------------------------------------------------------------|
| `click`          | [InfoboxEventArgs](infoboxeventargs-object.md) | Occurs when the mouse is used to click the infobox.                    |
| `infoboxChanged` | [InfoboxEventArgs](infoboxeventargs-object.md) | Occurs when the locations/rings or options of the polygon has changed. |
| `mouseenter`     | [InfoboxEventArgs](infoboxeventargs-object.md) | Occurs when the mouse cursor enters the infobox area.                  |
| `mouseleave`     | [InfoboxEventArgs](infoboxeventargs-object.md) | Occurs when the mouse cursor moves out of the infobox area.            |

## See Also

  * [Infoboxes Examples](../map-control-concepts/infoboxes/index.md)
  * [InfoboxOptions object](infoboxoptions-object.md) 
