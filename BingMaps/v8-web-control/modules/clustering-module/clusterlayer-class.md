---
title: "ClusterLayer Class | Microsoft Docs"
description: Describes the ClusterLayer class, which controls clustering functionality, and provides a description for its constructor, methods, and events.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 219249aa-4e2e-45cf-b8fe-e4af9530369f
caps.latest.revision: 7
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# ClusterLayer Class

[!INCLUDE [bing-maps-web-control-sdk-retirement](../../../includes/bing-maps-web-control-sdk-retirement.md)]

This is the main class that provides the clustering functionality.

## Constructor

> `ClusterLayer(pushpins: Pushpin[], options?: ClusterLayerOptions)`

## Methods

Name                                          | Return Type          | Description
--------------------------------------------- | -------------------- | --------------------------------
`clear()`                                     |                      | Clears all the data in the cluster layer.
`getDisplayedPushpins()`                      | [Pushpin](../../map-control-api/pushpin-class.md)[]            | Gets the pushpins that are in the current map view. If clustering is disabled, all pushpins in the clustering layer are returned.
`getOptions()`                                  | [ClusterLayerOptions](clusterlayeroptions-object.md)  | Gets the current options used by the cluster layer.
`getPushpins()`                               | [Pushpin](../../map-control-api/pushpin-class.md)[]            | Gets all pushpins that are in the layers.
`getClusterPushpinByGridKey(gridKey:number)`  | [ClusterPushpin](clusterpushpin-class.md) _or_ [Pushpin](../../map-control-api/pushpin-class.md) | Gets the pushpin in the specified cluster grid cell which can be either a ClusterPushpin if there are multiple pushpins in a cell or a single Pushpin.
`getVisible()` | boolean | Returns a boolean indicating if the cluster layer is visible or not. 
`setOptions(options: ClusterLayerOptions)`    |                      | Sets the clustering options to use in the layer.
`setPushpins(pushpins: Pushpin[])`            |                      | Sets the array of pushpins that are used in the clustering layer.
`setVisible(visible: boolean)` |  | Sets the visibility of the cluster layer.

## Events


| Name   | Arguments    | Description   |
|--------|--------------|---------------|
| `click`      | [MouseEventArgs](../../map-control-api/mouseeventargs-object.md) | Occurs when the mouse is used to click the map or when a touch end event occurs on a pushpin or cluster in the layer.               |
| `dblclick` | [MouseEventArgs](../../map-control-api/mouseeventargs-object.md)| Occurs when the mouse is used to double click the map or when a touch end event occurs on a pushpin or cluster in the layer. |
| `mousedown`  | [MouseEventArgs](../../map-control-api/mouseeventargs-object.md) | Occurs when the left mouse button is pressed or a touch start event occurs on a pushpin or cluster in the layer.                    |
| `mouseover`  | [MouseEventArgs](../../map-control-api/mouseeventargs-object.md) | Occurs when the mouse cursor moves over top of the area covered by a pushpin or cluster in the layer.                               |
| `mouseout`   | [MouseEventArgs](../../map-control-api/mouseeventargs-object.md) | Occurs when the mouse cursor moves out of the area covered by a pushpin or cluster in the layer.                                    |
| `mouseup`    | [MouseEventArgs](../../map-control-api/mouseeventargs-object.md) | Occurs when the left mouse button is lifted up or when the touch end event occurs on a pushpin or cluster  in the layer.             |
| `rightclick` | [MouseEventArgs](../../map-control-api/mouseeventargs-object.md) | Occurs when the right mouse button is used to click the map or when a long touch press occurs on a pushpin or cluster in the layer. |
