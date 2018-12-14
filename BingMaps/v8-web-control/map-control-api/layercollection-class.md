---
title: "LayerCollection Class | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: d497c5fb-bdc8-4938-9a8b-60838c7d176e
caps.latest.revision: 8
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# LayerCollection Class

The layers property of the map is a LayerCollection object and contains all the layers that have been added to the map.

**Note:** This class extends the Array class and can be iterated over just like an array. The class is only exposed in the `map.layers` property. No other instance of this class can be created.

## Properties

| Name | Type | Description                         |
|----------|----------|-----------------------------------------|
| `length`   | number   | The number of layers in the collection. |

## Methods

| Name                            | Return Type | Description                                               |
|-------------------------------------|--------|------------------------------------------------------------------------|
| `clear()`   |        | Removes all layers from the map.                                       |
| `indexOf(layer: ILayer)`                | number | Returns the index of a layer in the collection.   |
| `insert(layer: ILayer)`                |        | Adds a layer to the map.                         |
| `insertAll(layers: ILayer[])`        |        | Adds an array of layers to the map.              |
| `remove(layer: ILayer)`                |        | Removes a layer from the map.                    |
| `removeAt(idx: number)` |        | Removes a layer from the map at the specified index in the collection. |
