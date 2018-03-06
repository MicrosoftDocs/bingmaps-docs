---
title: "KmlScreenOverlay Class | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: ae512318-735b-4bb3-9f7a-940c8baf43e1
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# KmlScreenOverlay Class
Overlays HTML elements within the map container that are above the map.

## Constructor

> KmlScreenOverlay(htmlElement?: string *or* HTMLElement, options?: [KmlScreenOverlayOptions](../v8-web-control/kmlscreenoverlayoptions-object.md))

## Properties

| Name     | Type   | Description                                                          |
|----------|--------|----------------------------------------------------------------------|
| `metadata` | object | Optional property to store any additional metadata for this overlay. |

## Methods

| Name                                                | Return Type | Description                                                                                     |
|-----------------------------------------------------|-------------|-------------------------------------------------------------------------------------------------|
| `clear()`                                             |             | Removes all the data in the layer.                                                              |
| `getBelowNavigationBar()`                             | boolean     | Gets a boolean indicating if the screen overlay is displayed above or below the navigation bar. |
| `getHtmlElement()`                                    | HTMLElement | Returns the data source used by the layer.                                                      |
| `getMap()`                                            | [Map](../v8-web-control/map-class.md)         | Returns the map that this overlay is attached to.                                               |
| `getVisible()`                                        | boolean     | Gets a boolean indicating if the screen overlay is visible or not.                              |
| `setHtmlElement(htmlElement: string *or* HTMLElement)` |             | Updates the html element of this screen overlay.                                                |
| setOptions(options: [KmlScreenOverlayOptions](../v8-web-control/kmlscreenoverlayoptions-object.md))        |             | Sets the options to customize the screen overlay.                                               |
| `setVisible(value: boolean)`                          |             | Sets whether the layer is visible or not.                                                       |
