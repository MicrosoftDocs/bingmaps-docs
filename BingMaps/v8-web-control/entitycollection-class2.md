---
title: "EntityCollection Class2 | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 53037c17-0371-47c1-b015-2bcb56fda18d
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# EntityCollection Class
**Deprecated**: This class is deprecated in Bing Maps V8. The new [Layer class](../v8-web-control/layer-class.md) should be used instead. This class is still available in V8, but has been added to provide partial backwards compatibility with V7 apps for simple use cases such as adding individual shapes directly to the map, rather than to a layer or collection.

## Constructor

> EntityCollection()

## Methods

The **EntityCollection** class has the following methods.

| Name                                                        | Return Type | Description    |
|-------------------------------------------------------------|-------------|-----------------------------|
| `clear()`                                                     |             | Removes all shapes from the collection.   |
| `get(index: number)`                                          | [IPrimitive](../v8-web-control/iprimitive-class.md)  | Returns the shape at the specified index in the collection.    |
| `getLength()`                                                 | number      | Returns the number of shapes in the collection.                                                                          |
| indexOf(primitive: [IPrimitive](../v8-web-control/iprimitive-class.md))                              | number      | Returns the index of the specified shape in the collection. If the entity is not found in the collection, -1 is returned. |
| insert(primitive: [IPrimitive](../v8-web-control/iprimitive-class.md) _or_ [IPrimitive](../v8-web-control/iprimitive-class.md)\[\], index: number) |             | Inserts the specified shape(s) into the collection at the given index.                                                       |
| `pop()`                                                       | [IPrimitive](../v8-web-control/iprimitive-class.md)  | Removes the last shape from the collection and returns it.                                                                |
| push(primitive: [IPrimitive](../v8-web-control/iprimitive-class.md) _or_ [IPrimitive](../v8-web-control/iprimitive-class.md)\[\])                  |             | Adds the specified shape(s) to the last position in the collection.                                                          |
| remove(primitive: [IPrimitive](../v8-web-control/iprimitive-class.md))                               | [IPrimitive](../v8-web-control/iprimitive-class.md)  | Removes the specified shape from the collection and returns it.                                                           |
| `removeAt(index: number)`                                     | [IPrimitive](../v8-web-control/iprimitive-class.md)  | Removes the shape at the specified index from the collection and returns it.                                              |

## Events

| Name          | Type                             | Description |
|---------------|----------------------------------|-------------|
| `entityadded`   | [EntityCollectionChangedEventArgs](../v8-web-control/entitycollectionchangedeventargs-object.md) | Occurs when an [IPrimitive](../v8-web-control/iprimitive-class.md) (Pushpin, Polyline, Polygon) is added to the **EntityCollection**.|
| `entityremoved` | [EntityCollectionChangedEventArgs](../v8-web-control/entitycollectionchangedeventargs-object.md) | Occurs when an [IPrimitive](../v8-web-control/iprimitive-class.md) (Pushpin, Polyline, Polygon) is removed from the **EntityCollection**. |

**Note for Bing Maps V7 developers**: In the Bing Maps V7 SDK, the **EntityCollection** class was used to create data layers on the map. This class has been deprecated and replaced with the [Layer class](../v8-web-control/layer-class.md). However, to minimize migration efforts we have added an **EntityCollection** class for backwards compatibility which wraps the [Layer class](../v8-web-control/layer-class.md). This wrapper flattens all child entity collections of an **EntityCollection** into a single layer. This may result in some rendering differences when compared to V7. This **EntityCollection** class should only be used if migrating an app from V7 that requires minimal code changes.
