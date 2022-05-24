---
title: "Venue floor JSON class | Microsoft Docs"
description: Describes the Venue floor JSON class, which encapsulates the entities on a floor of a venue, and provides the class's properties and a code example.
ms.custom: ""
ms.date: "05/26/2020"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 8FAB7B0D-C5AB-47B9-93AD-1FEF531B97B7
caps.latest.revision: 3
author: "dbuerer"
ms.author: ""
manager: ""
ms.service: "bing-maps"
---
# Venue floor JSON class

Encapsulates an individual floor of a [venue] that contains the each [entity] on that floor.

## Properties

| Property          | Type            | Req? | Description |
|-------------------|-----------------|------|-------------|
| display           | string          |  ✔   | Text that both uniquely identifies a floor and would be displayed on a floor selector or an elevator button. |
| name              | culture:string  |      | Dictionary of culture-specific names for the floor, where an empty key refers to the culture identified by the venue's defaultCultureProperty. |
| entities          | [entity] []     |  ✔   | The entities contained in this floor. |

## Example

```json
{
  "display": "1",
  "name": { "en-ca": "Level 1" },
  "entities": [
    { "type":"Room","geometry":[{"closed":true,"x":[0,1,1,0],"y":[1,1,0,0]}] }
  ]
}
```

[venue]: venue.md
[entity]: entity.md
