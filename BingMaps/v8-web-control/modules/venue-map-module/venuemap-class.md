---
title: "Venue Map Class | Microsoft Docs"
ms.custom: ""
ms.date: "06/12/2020"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: ""
caps.latest.revision: 0
author: "SimonShapiroMsft"
ms.author: "simshap"
manager: "cordellj"
ms.service: "bing-maps"
---

# VenueMap
The **VenueMap** class represents a venue map in a specific instance of a [Map](../../map-control-api/map-class.md). The **VenueMap** provides functionality to toggle visibility and active floor. The **VenueMap** also exposes properties that can be leveraged for optimizing map view.


## Methods

Below are the list of methods for **VenueMap**.

Name                               | Return Type           | Description
---------------------------------- | --------------------- | -----------------------------------
`dispose()` | | Disposes the venue map instance, removing it from the map.
`getActiveFloor()` | string | Returns the name of the active floor of the venue map.
`getVisible()` | boolean | Returns `true` if the venue map is visible. Returns `false` otherwise.
`hide()` | | Hides the venue map if it is not already hidden.
`setActiveFloor(floorName: string)` | | Sets the active floor of the venue map to `floorName`.
`show()` | | Shows the venue map if it is not already displayed.
 
## Properties
Below are the list of properties for **VenueMap**.

Name                               | Type           | Description
---------------------------------- | --------------------- | -----------------------------------
`bestMapView` | [ViewOptions](../../map-control-api/viewoptions-object.md) | The best map view for the venue
`bounds` | [LocationRect](../../map-control-api/locationrect-class.md) | The bounds of the venue.
`center` | [Location](../../map-control-api/location-class.md) | The centroid of the venue.
`id` | string | The id of the venue.
`name` | string | The name of the venue.



## Events

Below are the list of events for **VenueMap**.

Name                               | Arguments           | Description
---------------------------------- | --------------------- | -----------------------------------
`activeFloorChanged` | string | Triggered when the active floor is changed. Event arguments provides the name of the new floor.