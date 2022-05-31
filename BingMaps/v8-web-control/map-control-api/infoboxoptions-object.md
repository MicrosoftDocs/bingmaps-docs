---
title: "InfoboxOptions Object | Microsoft Docs"
description: "This article provides infobox option properties can be used to create customized infoboxes."
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 50c1f792-e4dd-4836-8a5e-5b33e6faef9a
caps.latest.revision: 8
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# InfoboxOptions Object

The following infobox option properties can be used to create customized infoboxes.

| Name            | Type               | Description                                                                                     |
|-----------------|--------------------|-------------------------------------------------------------------------------------------------|
| `actions`         | [InfoboxActions](infoboxactions-object.md)\[\] | A list of the infobox actions, where each item is a `label` (the link text) or *icon* (the URL of the image to use as the icon link) and `eventHandler` (name of the function handling a click of the action link). Note that this is not supported when using `htmlContent`, use HTML anchors instead. <br/><br/>**Note**: InfoboxActions have been included in Bing Maps V8 primarily for backwards compatibility with V7. Instead it is recommended to use standard HTML buttons and links in the infobox description.  |
| `closeDelayTime` | number | The number of milliseconds to wait before closing an infobox when the visible option is changed from true to false. Default: 0 | 
| `description`     | string             | The string displayed inside the infobox.   |
| `htmlContent`     | string             | The HTML that represents the infobox. Note that some infobox options are ignored if custom HTML is set (title, description, maxHeight, maxWidth, actions, showCloseButton, showPoint). Also, if custom HTML is used to represent the infobox, the infobox is anchored at the top-left corner.|
| `location`        | [Location](location-class.md) | The location on the map where the infobox’s anchor is attached.   |
| `maxHeight` | number | The maximium size that the infobox height can expand to based on it’s content. Default: **126** |
| `maxWidth` | number | The maximium size that the infobox width can expand to based on it’s content. Default: **256** |
| `offset`          | [Point](point-class.md) | The amount the infobox pointer is shifted from the location of the infobox, or if `showPointer` is false, then it is the amount the info box bottom left edge is shifted from the location of the infobox. If custom HTML is set, it is the amount the top-left corner of the infobox is shifted from its location. The default offset value is (0,0), which means there is no offset.  |
| `showCloseButton` | boolean            | A boolean indicating whether to show the close dialog button on the infobox. The default value is true. By default, the close button is displayed as an X in the top right corner of the infobox. This property is ignored if custom HTML is used to represent the infobox.     |
| `showPointer`     | boolean            | A boolean indicating whether to display the infobox with a pointer. The default value is true. In this case the infobox is anchored at the bottom point of the pointer. If this property is set to false, the infobox is anchored at the bottom left corner. This property is ignored if custom HTML is used to represent the infobox.                                            |
| `title`           | string             | The title of the infobox. |
| `visible`         | boolean            | A boolean indicating whether to show or hide the infobox. The default value is true. A value of false indicates that the infobox is hidden, although it is still an entity on the map.    |
| `zIndex`          | number             | The z-index of the infobox with respect to other items on the map.     |
