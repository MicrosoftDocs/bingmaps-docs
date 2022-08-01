---
title: Venue Maps | Microsoft Docs
description: The root class of a venue JSON definition is the venue. Classes include address, entity, floor, geometry, inner, label, rectangle, venue, and venueTile.
ms.custom: 
ms.date: 05/26/2020
ms.reviewer: 
ms.suite: 
ms.tgt_pltfrm: 
ms.topic: article
ms.assetid: CC2918FE-1B5D-4E7E-8441-B4CC2A3439CB
caps.latest.revision: 3
author: DavidBuerer
ms.author: dbuerer
manager: 
ms.service: bing-maps
---
# Venue Maps

## Getting Started

The root class of a venue JSON definition is the [venue].  See also, this [sample] venue.

## Classes

| Class       | Description |
|-------------|-------------|
| [address]   | Contains the address of a [venue] or [entity] in the venue. |
| [entity]    | Contains an entity on the [floor] of a [venue] such as a room or point feature. |
| [floor]     | Contains a single floor of a [venue]. |
| [geometry]  | Contains a polyline or polygon representation of an [entity]. |
| [inner]     | Contains an inner hole of a polygon [geometry]. |
| [label]     | Contains information about where the label for an [entity] will be drawn. |
| [rectangle] | Contains an oriented rectangle. |
| [venue]     | Contains an entire venue, made up of [floor] values, and [entity] instances in those floors. |
| [venueTile] | For a spatial tile, contains a list of [venue] instances that intersect the tile. |

[address]: address.md
[entity]: entity.md
[floor]: floor.md
[geometry]: geometry.md
[inner]: inner.md
[label]: label.md
[rectangle]: rectangle.md
[venue]: venue.md
[venueTile]: venueTile.md
[sample]: sample.md
