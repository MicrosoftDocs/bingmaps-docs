---
title: Venue Tile JSON class | Microsoft Docs
titleSuffix: Microsoft Bing Maps
description: Venue Tile JSON class encapsulates a tile containing the footprints of venues that overlap that tile. These tiles are used to select a venue.
ms.custom: 
ms.date: 05/26/2020
ms.reviewer: 
ms.suite: 
ms.tgt_pltfrm: 
ms.topic: article
ms.assetid: E917F6EC-F5EE-4F98-8C33-05868734390C
caps.latest.revision: 3
author: DavidBuerer
ms.author: dbuerer
manager: 
ms.service: bing-maps
---

# Venue Tile JSON class

Encapsulates a tile containing the footprints of venues that overlap that tile.  These tiles are used to select a venue.

While this contains a list of [venue] objects, it is expected that these objects will only have an id, a name, and a single [floor] with the footprint [geometry] in it.

## Properties

| Property        | Type       | Req? | Description |
|-----------------|------------|------|-------------|
| id              | string     |  ✔   | Web Mercator [quadkey] for the tile.  Typically this is a level 10 tile. |
| venues          | [venue]    |      | Venues containing only footprints that overlap this tile. |

## Example

```json
{
  "id": "0212300302",
  "venues": [{
    "id": "sample-venue",
    "name": { "": "Sample Venue" },
    "floors": [{"entities":[{"type":"Footprint","geometry":[{
      "closed": true,
      "x": [-76.302,49.619,76.591,-49.777],
      "y": [6.794,39.483,-7.388,-40.279]}]}]}],
    "transform": [
      8.999567514436891E-06, 0.0, 0.0,
      0.0, 8.983152841195214E-06, 0.0,
      -122.139084, 47.64425, 1.0]
  }]
}
```

[floor]: floor.md
[geometry]: geometry.md
[quadkey]: ../../../articles/bing-maps-tile-system.md#tile-coordinates-and-quadkeys
[venue]: venue.md
