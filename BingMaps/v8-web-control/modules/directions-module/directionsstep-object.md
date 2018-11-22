---
title: "DirectionsStep Object | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: bcbba11a-c007-4536-b9de-d38425b6bd32
caps.latest.revision: 7
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# DirectionsStep Object
Represents one direction in a set of route directions.

| Name                    | Type               | Description                                                             |
|-------------------------|--------------------|-------------------------------------------------------------------------|
| `childItineraryItems`   | [DirectionsStep](directionsstep-object.md)\[\] | The child direction items for this directions step.                     |
| `coordinate`            | [Location](../../map-control-api/location-class.md) | The location of the start of the direction.                |
| `distance`              | string             | The total distance of the step in the unit specified in the `distanceUnit` property of the [DirectionsRequestOptions](directionsrequestoptions-object.md).                         |
| `durationInSeconds`     | number             | The total time, in seconds, of the direction step.                      |
| `formattedText`         | string             | The HTML formatted route instruction associated with the step.          |
| `isImageRoadShield`     | boolean            | A boolean indicating whether the maneuver image is a road shield image. |
| `maneuver`     | string             | The type of maneuver being performed                                         |
| `monetaryCost`          | number             | The cost of the step.                                                   |
| `postIntersectionHints` | string\[\]         | An array of strings, where each string is a hint to help determine when to move to the next direction step. Not all direction steps have hints.      |
| `preIntersectionHints`  | string\[\]         | An array of strings, where each string is a hint to help determine when you have arrived at this direction step. Not all direction steps have hints. |
| `startStopName`         | string             | The name of the transit stop where this step originates.                |
| `transitLine`           | [TransitLine](transitline-object.md) | The transit line associated with this step. | 
| `transitStepIcon`       | string             | The URL of the image to use for transit direction steps.                |
| `transitStopId`         | string             | The ID of the transit stop.                                             |
| `transitTerminus`       | string             | The name of the transit line end.                                       |
| `warnings` | [DirectionsStepWarning](directionsstepwarning.md)[] | An array of route warnings associated with this step. |