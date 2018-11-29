
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

This article demonstrates how to use this API with a POST request to create an optimized itinerary for three agents and thirteen itinerary items.

## Overview

The developer must provide specific information about each agent and itinerary item, summarized by the lists below:

### Agents:

* Name
* Agent shift information; for each shift:
    - Shift ending time
    - Shift starting time
    - Shift staring location (Query or Point)
    - Shift ending location (Query or Point)

### Itinerary Items: 

* Delivery/visit duration, called "dwell time"
* Business opening time
* Business ending time
* Location (Query of Point)
* Item Priority (on a scale from `1` to `99`, from lowest to highest)

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

We will use 13 itinerary items. To simplify things, we'll assume all the coffee shops our agents are delivering goods to have the same opening and closing hours. However, we will assign different priorities and dwell times to each shop (for our example, the priorities and dwell times are chosen randomly).

|Coffee Shop | Coordiantes | Dwell Time | Priority |
|----------|--------------|---|----|
Starbucks   |  47.6140060424805,-122.347236633301 | 01:31:08.3850000 | 2
Storyville Coffee Company|    47.6088790893555,-122.340362548828 | 02:00:00.00 | 5
Seattle Coffee Works|   47.6087913513184,-122.339477539062 | 00:05:00.00 | 67
Monorail Espresso|  47.6110000610352,-122.33544921875 | 00:30:00.00 | 14
Moore Coffee | 47.6116981506348,-122.34105682373 | 03:00:00.00 | 9
Citizen  | 47.6257209777832,-122.345993041992 | 00:10:00.00 | 23
Bang Bang Cafe  | 47.6139373779297,-122.349090576172 | 01:15:00.00 | 7
Espresso Vivace  | 47.6237602233887,-122.32063293457 | 00:01:00.00 | 54
Cafe Cesura  | 47.6195220947266,-122.196739196777 | 01:15:00.00 | 34
Top Pot Doughnuts  | 47.6186218261719,-122.198760986328 | 00:05:00.00 | 6
Seattle Coffee Gear | 47.6176605224609,-122.196708679199 | 00:18:00.00 | 8
777 Cafe | 47.6168899536133,-122.19686126709 | 00:19:30.00 | 91
Starbucks | 47.614330291748,-122.199150085449 | 00:45:00.00 | 99

### Creating The Request

The above example is large: It includes 6 shifts (two for each agent: one before and one after lunch), and 13 itinerary items.

Because the Optimized Itinerary API only allows for a maximum of two agent shifts for synchronous API calls, we have to make an asynchronous request. Moreover, We will also use a POST instead of a GET method to deliver our agent and itinerary. 

The body of the POST request is as follows:

```json
{
    "agents": [
        {
            "name": "Yuan",
            "shifts": [
                {
                    "startTime": "11/29/2018+08:00:00",
                    "startLocation": {
                        "latitude": 47.608970,
                        "longitude": -122.340914
                    },
                    "endTime": "11/29/2018+12:00:00",
                    "endLocation": {
                        "latitude": 47.599018,
                        "longitude": -122.331871
                    }
                },
                {
                    "startTime": "11/29/2018+13:00:00",
                    "startLocation": {
                        "latitude": 47.599018,
                        "longitude": -122.331871
                    },
                    "endTime": "11/29/2018+17:00:00",
                    "endLocation": {
                        "latitude": 47.610966,
                        "longitude": -122.337095
                    }
                }
			]
        },
        {
            "name": "Charlie",
            "shifts": [
                {
                    "startTime": "11/29/2018+08:00:00",
                    "startLocation": {
                        "latitude": 47.655000,
                        "longitude": -122.308000
                    },
                    "endTime": "11/29/2018+12:00:00",
                    "endLocation": {
                        "latitude": 47.666423,
                        "longitude": -122.383223
                    }
                },
                {
                    "startTime": "11/29/2018+13:00:00",
                    "startLocation": {
                        "latitude": 47.599018,
                        "longitude": -122.331871
                    },
                    "endTime": "11/29/2018+17:00:00",
                    "endLocation": {
                        "latitude": 47.610966,
                        "longitude": -122.337095
                    }
                }
			]
        },
        {
            "name": "Andre",
            "shifts": [
                {
                    "startTime": "11/29/2018+08:00:00",
                    "startLocation": {
                        "latitude": 47.706123,
                        "longitude": -122.325867
                    },
                    "endTime": "11/29/2018+12:00:00",
                    "endLocation": {
                        "latitude": 47.599018,
                        "longitude": -122.331871
                    }
                },
                {
                    "startTime": "11/29/2018+13:00:00",
                    "startLocation": {
                        "latitude": 47.599018,
                        "longitude": -122.331871
                    },
                    "endTime": "11/29/2018+17:00:00",
                    "endLocation": {
                        "latitude": 47.614151,
                        "longitude": -122.195686
                    }
                }
			]
        }
    ],
    "itineraryItems": [
        {
            "openingTime": "11/29/2018+08:00:00",
            "closingTime": "11/29/2018+17:00:00",
            "dwellTime": "01:31:08.3850000",
            "priority": 2,
            "location": {
                "latitude": 47.6140060424805,
                "longitude": -122.347236633301
            }
        },
        {
            "openingTime": "11/29/2018+08:00:00",
            "closingTime": "11/29/2018+17:00:00",
            "dwellTime": "02:00:00.00",
            "priority": 5,
            "location": {
                "latitude": 47.6088790893555,
                "longitude": -122.340362548828
            }
        },
        {
            "openingTime": "11/29/2018+08:00:00",
            "closingTime": "11/29/2018+17:00:00",
            "dwellTime": "00:05:00.00",
            "priority": 67,
            "location": {
                "latitude": 47.6087913513184,
                "longitude": -122.339477539062
            }
        },
        {
            "openingTime": "11/29/2018+08:00:00",
            "closingTime": "11/29/2018+17:00:00",
            "dwellTime": "00:30:00.00",
            "priority": 14,
            "location": {
                "latitude": 47.6110000610352,
                "longitude": -122.33544921875
            }
        },
        {
            "openingTime": "11/29/2018+08:00:00",
            "closingTime": "11/29/2018+17:00:00",
            "dwellTime": "03:00:00.00",
            "priority": 9,
            "location": {
                "latitude": 47.6116981506348,
                "longitude": -122.34105682373
            }
        },
        {
            "openingTime": "11/29/2018+08:00:00",
            "closingTime": "11/29/2018+17:00:00",
            "dwellTime": "00:10:00.00",
            "priority": 23,
            "location": {
                "latitude": 47.6257209777832,
                "longitude": -122.345993041992
            }
        },
        {
            "openingTime": "11/29/2018+08:00:00",
            "closingTime": "11/29/2018+17:00:00",
            "dwellTime": "01:15:00.00",
            "priority": 7,
            "location": {
                "latitude": 47.6139373779297,
                "longitude": -122.349090576172
            }
        },
        {
            "openingTime": "11/29/2018+08:00:00",
            "closingTime": "11/29/2018+17:00:00",
            "dwellTime": "00:01:00.00",
            "priority": 54,
            "location": {
                "latitude": 47.6237602233887,
                "longitude": -122.32063293457
            }
        },
        {
            "openingTime": "11/29/2018+08:00:00",
            "closingTime": "11/29/2018+17:00:00",
            "dwellTime": "01:15:00.00",
            "priority": 34,
            "location": {
                "latitude": 47.6195220947266,
                "longitude": -122.196739196777
            }
        },
        {
            "openingTime": "11/29/2018+08:00:00",
            "closingTime": "11/29/2018+17:00:00",
            "dwellTime": "00:05:00.00",
            "priority": 6,
            "location": {
                "latitude": 47.6186218261719,
                "longitude": -122.198760986328
            }
        },
        {
            "openingTime": "11/29/2018+08:00:00",
            "closingTime": "11/29/2018+17:00:00",
            "dwellTime": "00:18:00.00",
            "priority": 8,
            "location": {
                "latitude": 47.6176605224609,
                "longitude": -122.196708679199
            }
        },
        {
            "openingTime": "11/29/2018+08:00:00",
            "closingTime": "11/29/2018+17:00:00",
            "dwellTime": "00:19:30.00",
            "priority": 91,
            "location": {
                "latitude": 47.6168899536133,
                "longitude": -122.19686126709
            }
        },
        {
            "openingTime": "11/29/2018+08:00:00",
            "closingTime": "11/29/2018+17:00:00",
            "dwellTime": "00:45:00.00",
            "priority": 99,
            "location": {
                "latitude": 47.614330291748,
                "longitude": -122.199150085449
            }
        }
    ]
}
```


We then send this JSON data in the POST body of our API request, making sure to add the POST header `Content-Type: application/json`, with the following URL:

```url
https://dev.virtualearth.net/REST/V1/Routes/OptimizeItineraryAsync?key={BingMapsKey}
```

