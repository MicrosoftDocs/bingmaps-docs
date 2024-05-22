---
title: "AnimatedTileLayer Class | Microsoft Docs"
description: "This article describes events and methods related to the AnimatedTileLayer Class, which provides a layer that can smoothly animate through an array of tile layer sources."
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 4caaf766-45b9-4ab2-85ce-e086a5bab009
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# AnimatedTileLayer Class

[!INCLUDE [bing-maps-web-control-sdk-retirement](../../includes/bing-maps-web-control-sdk-retirement.md)]

Provides a layer which can smoothly animate through an array of tile layer sources.

## Constructor

> AnimatedTileLayer(options?: [AnimatedTileLayerOptions](animatedtilelayeroptions-object.md))

## Methods

| Name                                          | Return Type    | Description                                                             |
|-----------------------------------------------|----------------|-------------------------------------------------------------------------|
| `getFrameRate()`                                | number         | Gets the frame rate of this animated tile layer.                        |
| `getLoadingScreen()`                            | [CustomOverlay](customoverlay-class.md)  | Gets the loading screen overlay when tiles are being fetched.           |
| `getMaxTotalLoadTime()`                         | number         | Gets the maximum total tile fetching time of this animated tile layer   |
| `getTileSources()`                              | [TileSource](tilesource-class.md)\[\] | Gets the tile sources associated with this layer.                       |
| `getVisible()`                                  | boolean        | Gets the visibility of this animated tile layer.                        |
| `pause()`                                       |                | Pause the tile layer animation.                                         |
| `play()`                                        |                | Play the animation either from start or where it was paused.            |
| setOptions(options: [AnimatedTileLayerOptions](animatedtilelayeroptions-object.md)) |                | Sets the options for the animated tile layer.                           |
| `stop()`                                        |                | Stop the layer animation, hide layer, and reset frame to the beginning. |

## Events

| Name           | Return Type            | Description                                                                       |
|----------------|------------------------|-----------------------------------------------------------------------------------|
| onFrameLoaded  | [AnimatedFrameEventArgs](animatedframeeventargs-object.md) | An event that fires every time a new tile layer frame is loaded in the animation. |
| preLoadEnded   |                        | An event that fires when preloading tiles for the current view ends.              |
| preLoadStarted |                        | An event that fires when preloading tiles for the current view starts.            |

### Examples

  * [Animated Weather Radar Map](../map-control-concepts/layers/animated-weather-radar-map.md)
  * [AnimatedTileLayer Events](../map-control-concepts/layers/animatedtilelayer-events.md)
  * [Controlling an AnimatedTileLayer](../map-control-concepts/layers/controlling-an-animatedtilelayer.md)