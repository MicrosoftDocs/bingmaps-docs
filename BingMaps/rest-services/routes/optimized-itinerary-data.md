---
title: Optimized Itinerary Data | Microsoft Docs
ms.custom: 
ms.date: 11/26/2018
ms.reviewer: 
ms.suite: 
ms.tgt_pltfrm: 
ms.topic: article
ms.assetid: 64c43775-3911-4c76-a0b4-32dc5824a258
caps.latest.revision: 4
author: rbrundritt
ms.author: richbrun
manager: stevelom
ms.service: bing-maps
---

#  Multi-Itinerary Optimization Data

The response returned when making a request to Optimize Itinerary API contains an `OptimizeItinerary` resource. The information provided in the `OptimizeItinerary` resource includes an array of `AgentItineraries` corresponding to each agent defined in the request. 

For more information about the common response syntax for the Bing Maps REST Services, see [Common Response Description](../common-response-description.md).

The following tables describe the `OptimizeItinerary` resource fields.  

## `OptimizeItinerary` Resource

| JSON | XML | Type | Description |
|------|-----|------|-------------|
|`agentItineraries`| `AgentItineraries` | `AgentItinerary` Resource | List of AgentItinerary resource items.|
|`isAccepted`| `IsAccepted` | `boolean` |Boolean value denoting if the request was accepted.|
|`isCompleted`| `IsCompleted` | `boolean` | Boolean value denoting if the request was accepted.|
|`unscheduledItems`| `UnscheduledItems` | `ItineraryItem` Resource | List of ItineraryItem resource items that could not be scheduled with the current constraints.|
|`unusedAgents`| `UnusedAgents` | `Agent` Resource | List of Agent items that were not used to construct the current solution.|

## `Agent` Resource

| JSON | XML | Type | Description |
|------|-----|------|-------------|
|`name` | `Name`| `string`| Agent name, as defined in the request.|
|`capacity` | `Capacity` | `integer[]` | Agent capacity, as defined in the request.|
|`price` | `Price` | `Price` Resource | Agent price, as defined in the request or default value.|
|`shifts`|`Shifts` | `Shift` Resource| Agent shifts, as defined in the request.|

## `ItineraryItem` Resource

| JSON | XML | Type | Description |
|------|-----|------|-------------|
|`name` | `Name`| `string`| Item name, as defined in the request.|
|`openingTime` | `OpeningTime`| `DateTime`| Item opening time window, as defined in the request.|
|`closingTime` | `ClosingTime`| `DateTime`| Item closing time window, as defined in the request.|
|`dwellTime` | `DwellTime`| `Duration`| The time required to service the location, as defined in the request.|
|`location` | `Location`| `Coordinate`| Item location, as defined in the request.|
|`dropOffFrom` | `DropOffFrom`| `string[]`| String array of item names, allowing to define item ordering constraint, for example go to A before B, as defined in the request.|
|`priority` | `Priority` | `integer` | Item priority, as defined in the request.|
|`quantity` | `Quantity` | `integer[]` | Quantity values to be loaded, if positive, or unloaded if negative, as defined in the request.|
|`depot` | `Depot` | `boolean` | Flag denoting if the item is a depot and multiple trips are allowed to it, as defined in the request.|

## `AgentItinerary` Resource

| JSON | XML | Type | Description |
|------|-----|------|-------------|
|`agent` | `Agent`| `Agent` Resource| Agent resource associated with the this itinerary, as defined in the request.|
|`instructions` | `Instructions` | `Instructions` Resource| A sorted array containing the itinerary Instructions.|
|`route`|`Route` |`Route` Resource| The itinerary route summary information.|

## `Instructions` Resource

| JSON | XML | Type | Description |
|------|-----|------|-------------|
|`instructionType` |`InstructionType`| `string`| Type of instruction, any of the following:<br /><br />- `LeaveFromStartPoint` <br />- `TravelBetweenLocations`<br />- `VisitLocation`<br /> - `TakeABreak`<br /> - `ArriveToEndPoint`|
|`duration` | `Duration` | Time Delta | Estimated travel time. Applies only for `TravelBetweenLocations` instructions.|
|`distance` |`Distance` | `integer` | Estimate travel distance, in meters. |
|`startTime`| `StartTime`| `DateTime`| The estimated start time of the instruction. |
|`endTime`| `EndTime` | `DateTime` | The estimated end time of the instruction. |
|`itineraryItem`| `ItineraryItem` | ItineraryItem Resource. |Optional value present when the instruction type references a location, agent shift start/end point, or a defined itinerary item as defined in the request. |

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