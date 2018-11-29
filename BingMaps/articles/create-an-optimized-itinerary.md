
---
title: "Create an Optimized Itinerary | Microsoft Docs"
ms.custom: ""
ms.date: "11/26/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 64c43775-3911-4c76-a0b4-32dc5824a258
caps.latest.revision: 4
author: "v-chrfr"
ms.author: "v-chrfr"
manager: "stevelom"
ms.service: "bing-maps"
---

# Create an Optimized Itinerary

The Bing Maps [Optimized Itinerary API](../rest-services/routes/optimized-itinerary.md) returns a delivery schedule for a set of agents and itinerary times. 

This article demonstrates how to use this API with a POST request to create an optimized itinerary for three agents and seven itinerary items.

## Overview

The developer must provide specific information about each agent and itinerary item, summarized by the lists below:

### Agents:

* Name
* Starting Location (Query or Point)
* Ending Location (Query or Point)
* For each shift:
    -- Shift ending time
    -- Shift starting time

### Itinerary Items: 

* Visit duration
* Business opening time
* Business ending time
* Location (Query of Point)
* Priority (on a scale from `1` to `99`, from lowest to highest)

## Example

### Formatting the Agent Data

Suppose we have three agents: Yuan, Charlie, and Andre. Each agent has at least one shift, each consisting of: the agent's starting location, staring time, ending location, and ending time.

For example, if Charlie delivers packages from 9 A.M. to 5 P.M., but has a one hour lunch break at noon, then Charlie will have two shifts: one from 9 A.M to noon, and another from 1 P.M. to 5 P.M.

To keep our example simple, we will assume that, although our agents will start and end at different locations, they will all take their lunch break at the same location, at Zeitgeist Cafe, Downtown Seattle, on South Jackson Street (or, in coordinates: `47.599018, -122.331871`).

> [!NOTE]
>
> Below we use a use latitude and longitude coordinates for the Agent's starting and ending locations. Instead, We could instead string query to specify starting/ending locations.

Here is the table of our agent's starting and ending information:

|Agent Name| Shift Starting Location | Shift Starting Coords | Shift Ending Location | Shift Ending Coords|
|:-----:|-----|:---:|----|:---:|
|Yuan   |Pike Place Market|`47.608970, -122.340914`| Westlake Park|`47.610966, -122.337095`
|Charlie|UW Campus | `47.655000, -122.308000`|Ballard Ave.|`47.666423, -122.383223`|
|Andre  |Northgate Mall|`47.706123, -122.325867`|Downtown Bellevue|`47.614151, -122.195686`|

#### Shift Data

The images below show the starting (green circle) and ending (red circle) locations for each agent.

__Yuan__:

|Start Time|Start Coords|End Time End Coords|
|---|----|----|---|
|`11/29/2018+08:00:00`|`47.608970, -122.340914`|`11/29/2018+12:00:00`|`47.599018, -122.331871`|
|`11/29/2018+13:00:00`|`47.599018, -122.331871`|`11/29/2018+17:00:00`|`47.610966,-122.337095`|

![yuan_starting_image.png](media/yuan_starting_image.png)

__Charlie__:

|Start Time|Start Coords|End Time End Coords|
|---|----|----|---|
|`11/29/2018+08:00:00`|`47.655000, -122.308000`|`11/29/2018+12:00:00`|`47.666423, -122.383223`|
|`11/29/2018+13:00:00`|`47.599018, -122.331871`|`11/29/2018+17:00:00`|`47.610966,-122.337095`|

![charlie_starting_image.png](media/charlie_starting_image.png)

__Andre__:

|Start Time|Start Coords|End Time End Coords|
|---|----|----|---|
|`11/29/2018+08:00:00`|`47.706123, -122.325867`|`11/29/2018+12:00:00`|`47.599018, -122.331871`|
|`11/29/2018+13:00:00`|`47.599018, -122.331871`|`11/29/2018+17:00:00`|`47.614151, -122.195686`|

![andre_starting_image.png](media/andre_starting_image.png)






### Formatting the Itinerary Data


### GET vs POST Requests

