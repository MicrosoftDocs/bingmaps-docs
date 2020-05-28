---
title: "Venue Tile JSON class | Microsoft Docs"
ms.custom: ""
ms.date: "05/26/2020"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: E917F6EC-F5EE-4F98-8C33-05868734390C
caps.latest.revision: 3
author: "dbuerer"
ms.author: ""
manager: ""
ms.service: "bing-maps"
---
# Venue Tile JSON class

Encapsulates a venue, consisting of one or more floors.

## Properties

| Property        | Type       | Req? | Description |
|-----------------|------------|------|-------------|
| id              | string     |  ✔   | [Web Mercator quadkey](../articles/bing-maps-tile-system.md) for the tile.  Typically this is a level 10 tile. |
| venues          | [venue] [] |      | Venues containing only footprints that overlap this tile. |

## Example

```json
{
  "id": "0212300302",
  "venues": [{
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

[venue]: venue.md
