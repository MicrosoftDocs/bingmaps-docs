---
title: "Map Style Sheet Entries | Microsoft Docs"
ms.custom: ""
ms.date: "05/26/2020"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: C22745F9-7DD9-4348-8476-DC1AC0F7AC98
caps.latest.revision: 3
author: "dbuerer"
ms.author: ""
manager: ""
ms.service: "bing-maps"
---
# Map Style Sheet Entries

The entries and properties listed below can be used in a [map style sheet](map-style-sheets.md) to customize the appearance of a Microsoft map.

Map style sheets can be created interactively using the [Map Style Sheet Editor application](https://www.microsoft.com/store/productId/9NBHTCJT72FT).

## Settings and Elements

The JSON entries that can be customized are represented in the following list.  They are represented as a tree structure where setting parent entry properties will override child entry properties.  The properties available to each entry can be found in the entry's property group.  This table uses ">" to represent levels in the entry hierarchy.

| Name               | Property Group | Web Arg | Windows Min | Android iOS Min | Description |
|--------------------|----------------|---------|-------------|-----------------|-------------|
| version            | [Version]      | version | 1703 | 1.0.0 | The style sheet version that you want to use. |
| settings           | [Settings]     | g       | 1703 | 1.0.0 | The settings that apply to the whole style sheet. |
| mapElement         | [MapElement]   | me      | 1703 | 1.0.0 | The parent entry to all map entries. |
| > baseMapElement   | [MapElement]   | bme     | 1703 | 1.0.0 | The parent entry to all non-user entries. |
| >> area            | [MapElement]   | ar      | 1703 | 1.0.0 | Areas describing land use. These should not to be confused with the physical buildings which are under the structure entry. |
| >>> airport        | [MapElement]   | ap      | 1703 | 1.0.0 | Areas that encompass airports. |
| >>> areaOfInterest | [MapElement]   | ai      | 1709 | 1.0.0 | Areas in which there are a high concentration of businesses or interesting points. |
| >>> cemetery       | [MapElement]   | cm      | 1703 | 1.0.0 | Areas that encompass cemeteries. |
| >>> continent      | [MapElement]   | ct      | 1703 | 1.0.0 | Continent area labels. |
| >>> education      | [MapElement]   | ed      | 1703 | 1.0.0 | Areas that encompass schools and other educational facilities. |
| >>> indigenousPeoplesReserve | [MapElement] | ipr | 1703 | 1.0.0 | Areas that encompass indigenous peoples reserves. |
| >>> industrial     | [MapElement]   | ind     | 1709 | 1.0.0 | Areas that are used for industrial purposes. |
| >>> island         | [MapElement]   | is      | 1703 | 1.0.0 | Island area labels. |
| >>> medical        | [MapElement]   | md      | 1703 | 1.0.0 | Areas that are used for medical purposes (For example: a hospital campus). |
| >>> military       | [MapElement]   | ima     | 1703 | 1.0.0 | Areas that encompass military bases or have military uses. |
| >>> nautical       | [MapElement]   | nt      | 1703 | 1.0.0 | Areas that are used for nautical related purposes. |
| >>> neighborhood   | [MapElement]   | nh      | 1703 | 1.0.0 | Neighborhood area labels. |
| >>> runway         | [MapElement]   | rw      | 1703 | 1.0.0 | Areas that is used as an airplane runway. |
| >>> sand           | [MapElement]   | sn      | 1703 | 1.0.0 | Sandy areas like beaches. |
| >>> shoppingCenter | [MapElement]   | sct     | 1703 | 1.0.0 | Areas of ground allocated for malls or other shopping centers. |
| >>> stadium        | [MapElement]   | sta     | 1703 | 1.0.0 | Areas that encompass stadiums. |
| >>> underground    | [MapElement]   | ug      | 1709 | 1.0.0 | Underground areas (For example: a metro station footprint). |
| >>> vegetation     | [MapElement]   | vg      | 1703 | 1.0.0 | Forests, grassy areas, etc. |
| >>>> forest        | [MapElement]   | fr      | 1703 | 1.0.0 | Areas of forest land. |
| >>>> golfCourse    | [MapElement]   | gc      | 1703 | 1.0.0 | Areas that encompass golf courses. |
| >>>> park          | [MapElement]   | pr      | 1703 | 1.0.0 | Areas that encompass parks. |
| >>>> playingField  | [MapElement]   | pf      | 1703 | 1.0.0 | Extracted pitches such as a baseball field or tennis court. |
| >>>> reserve       | [MapElement]   | rsv     | 1703 | 1.0.0 | Areas that encompass nature reserves. |
| >> frozenWater     | [PointStyle]   | fw      | 1903 | 1.0.0 | Frozen water, like glacier. |
| >> point           | [PointStyle]   | pt      | 1703 | 1.0.0 | All point features that are drawn with an icon of some sort. |
| >>> address        | [PointStyle]   | adr     | 1803 | 1.0.0 | Address numbers labels. |

[Version]: map-style-sheet-entry-properties.md#version-properties
[Settings]: map-style-sheet-entry-properties.md#settings-properties
[MapElement]: map-style-sheet-entry-properties.md#mapelement-properties
[PointStyle]: map-style-sheet-entry-properties.md#pointstyle-properties