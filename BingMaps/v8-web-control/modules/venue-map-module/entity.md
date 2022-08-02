---
title: Venue entity JSON class | Microsoft Docs
titleSuffix: Microsoft Bing Maps
description: Venue entity JSON class encapsulates an individual entity on the floor of a venue. Includes Properties and Example.
ms.custom: 
ms.date: 05/26/2020
ms.reviewer: 
ms.suite: 
ms.tgt_pltfrm: 
ms.topic: article
ms.assetid: 9D976057-A797-4DCA-A48B-ED6DD2654316
caps.latest.revision: 3
author: DavidBuerer
ms.author: dbuerer
manager: 
ms.service: bing-maps
---

# Venue entity JSON class

Encapsulates an individual entity on the [floor] of a [venue].

## Properties

| Property          | Type            | Req? | Description |
|-------------------|-----------------|------|-------------|
| address           | [address]       |      | The address of the entity where any missing fields populated from venue address. |
| geometry          | [geometry] []   |      | A list of any polygons or polylines that define the extents of the entity. |
| tag               | string          |      | Unique identifier for the entity so that it can be referenced. |
| label             | culture:[label] |      | Dictionary of culture-specific text and placement information for possible labels for the entity.  The text in a label is what will be drawn on the map. |
| xy                | number[]        |      | An X and Y coordinate that, once transform is applied, defines the location of a point entity or central location for a polygon or polyline entity. |
| name              | culture:string  |      | Dictionary of culture-specific names for the entity, where an empty key refers to the culture identified by the venue's defaultCultureProperty.  The text in the name is what will be displayed outside the map. |
| phoneNumber       | string          |      | The phone number for the entity. |
| type              | [styleEntry]    |  ✔   | The key that identifies how to display the entity. |

> [!WARNING]
> Even though `entity.geometry` technically supports multiple entries, currently only the first one is read.

## Example

```json
{
  "tag": "5005",
  "name": { "": "Empty Room" },
  "label": { "en-ca": { "text":"Empty\nRoom", "angle":-10,"xy":[0.5, 0.5],"width":5.01E-05,"height":2.1E-05 }},
  "type": "Room",
  "xy": [0.5, 0.5],
  "geometry": [{"closed":true,"x":[0,1,1,0],"y":[1,1,0,0]}]
}
```

[address]: address.md
[floor]: floor.md
[geometry]: geometry.md
[label]: label.md
[styleEntry]: ../../../styling/map-style-sheet-entries.md
[venue]: venue.md
