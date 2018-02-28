---
title: "AnimatedTileLayer Class | Microsoft Docs"
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
---
# AnimatedTileLayer Class
Provides a layer which can smoothly animate through an array of tile layer sources.

## Constructor

> AnimatedTileLayer(options?: [AnimatedTileLayerOptions](../v8-web-control/animatedtilelayeroptions-object.md))

## Methods

| Name                                          | Return Type    | Description                                                             |
|-----------------------------------------------|----------------|-------------------------------------------------------------------------|
| `getFrameRate()`                                | number         | Gets the frame rate of this animated tile layer.                        |
| `getLoadingScreen()`                            | [CustomOverlay](../v8-web-control/customoverlay-class.md)  | Gets the loading screen overlay when tiles are being fetched.           |
| `getMaxTotalLoadTime()`                         | number         | Gets the maximum total tile fetching time of this animated tile layer   |
| `getTileSources()`                              | [TileSource](TileSource%20Class.md)\[\] | Gets the tile sources associated with this layer.                       |
| `getVisible()`                                  | boolean        | Gets the visibility of this animated tile layer.                        |
| `pause()`                                       |                | Pause the tile layer animation.                                         |
| `play()`                                        |                | Play the animation either from start or where it was paused.            |
| setOptions(options: [AnimatedTileLayerOptions](../v8-web-control/animatedtilelayeroptions-object.md)) |                | Sets the options for the animated tile layer.                           |
| `stop()`                                        |                | Stop the layer animation, hide layer, and reset frame to the beginning. |

## Events

| Name           | Return Type            | Description                                                                       |
|----------------|------------------------|-----------------------------------------------------------------------------------|
| onFrameLoaded  | [AnimatedFrameEventArgs](../v8-web-control/animatedframeeventargs-object.md) | An event that fires every time a new tile layer frame is loaded in the animation. |
| preLoadEnded   |                        | An event that fires when preloading tiles for the current view ends.              |
| preLoadStarted |                        | An event that fires when preloading tiles for the current view starts.            |

### Examples

  * [Animated Weather Radar Map](../v8-web-control/animated-weather-radar-map.md)
  * [AnimatedTileLayer Events](../v8-web-control/animatedtilelayer-events.md)
  * [Controlling an AnimatedTileLayer](../v8-web-control/controlling-an-animatedtilelayer.md)