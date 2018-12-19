---
title: "Optimized Itinerary Data | Microsoft Docs"
ms.custom: ""
ms.date: "11/26/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 64c43775-3911-4c76-a0b4-32dc5824a258
caps.latest.revision: 4
author: "rbrundritt"
ms.author: "v-chrfr"
manager: "stevelom"
ms.service: "bing-maps"
---

#  Multi-Itinerary Optimization Data

The response returned when making a request to Optimize Itinerary API contains an `OptimizeItinerary` resource. The information provided in the `OptimizeItinerary` resource includes an array of `AgentItineraries` corresponding to each agent defined in the request. 

For more information about the common response syntax for the Bing Maps REST Services, see [Common Response Description](../common-response-description.md).

The following tables describe the `OptimizeItinerary` resource fields.  

## `OptimizeItinerary` Resource

| JSON | XML | Type | Description |
|------|-----|------|-------------|
|`agentItinerary`| `AgentItinerary` | `AgentItinerary` Resource | List of agent resource items.|
|`isAccepted`| `IsAccepted` | `boolean` |Boolean value denoting if the request was accepted.|
|`isCompleted`| `IsCompleted` | `boolean`| Boolean value denoting if the request was accepted.|

## `AgentItinerary` Resource

| JSON | XML | Type | Description |
|------|-----|------|-------------|
|`agent` | `Agent`| `string`| Agent name, as defined in the request.|
|`instructions` | `Instructions` | `Instructions` Resource| A sorted array containing the itinerary Instructions.|
|`route`|`Route` |`Route` Resource| The itinerary route summary information.|


##  `Instructions` Resource

| JSON | XML | Type | Description |
|------|-----|------|-------------|
|`instructionType` |`InstructionType`| `string`| Type of instruction, any of the following:<br /><br />- `LeaveFromStartPoint` <br />- `TravelBetweenLocations`<br />- `VisitLocation`<br />- `ArriveToEndPoint`|
|`duration` | `Duration` | Time Delta | Estimated travel time. Applies only for `TravelBetweenLocations` instructions.|
|`distance` |`Distance` | `integer` | Estimate travel distance, in meters. |
|`startTime`| `StartTime`| `DateTime`| The estimated start time of the instruction. |
|`endTime`| `EndTime` | `DateTime` | The estimated end time of the instruction. |
|`itineraryItem`| `ItineraryItem` | Varies. The item type is determined by the request.|Optional value present when the instruction type references a location, agent shift start/end point, or a defined itinerary item. |


## `Route` Resource

| JSON | XML | Type | Description |
|------|-----|------|-------------|
|`startTime`| `StartTime` | `DateTime` | The estimated start time of the route. |
|`startLocation` |`StartLocation` | `Coordinate` Resource | The coordinates for the staring location of the agent's first shift. |
|`endTime` | `EndTime` | `DateTime` | The estimated end time of the route. |
|`endLocation` |`EndLocation` | `Coordinate` |  The coordinates for the ending location of the agent's last shift.|
|`wayPoints` | `WayPoints` | `Coordinate[]` | Sorted list of coordinate resources representing the waypoints of the constructed route between the agent's starting and ending locations. | 
|`totalTravelDistance` | `TotalTravelDistance` | `integer` | The estimated total travel distance for the agent itinerary in meters. |
|`totalTravelTime` |`TotalTravelTime` | `TimeSpan` | The estimated total travel time for the agent itinerary. |

## `Coordinate` Resource

| JSON | XML | Type | Description |
|------|-----|------|-------------|
| `latitude` | `Latitude` | `double` | Latitude for location. |
| `longitude` | `Longitude` | `double` | Longitude for location.|