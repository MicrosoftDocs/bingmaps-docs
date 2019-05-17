---
title: "Find an Optimized Route with Multiple Waypoints | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms:assetid: 232a3fcd-5c04-4a9a-a9c9-ca821e0c0636
caps.latest.revision: 3
author: "eriklind"
ms.author: "eriklind"
manager: "dirabel"
ms.service: "bing-maps"
---

# Find an Optimized Route with Multiple Waypoints

The following example shows how to use the Routes API to optimize a driving route with three or more waypoints (up to 25). The ordering of the waypoints is optimized according to the `optimize` parameter. For more on the differences between the `optimize` and `optimizeWaypoints` parameters, see [Path and Waypoint Optimization](https://msdn.microsoft.com/library/ff701717.aspx#anchor_1).

When the `optimizeWaypoints` parameter is set to `false` (the default value), the Routes API respects the ordering of the waypoints specified in the request URL.


> [!NOTE]
> <P>The Routes API always optimizes driving directions <EM>between</EM> waypoints, even when the <CODE>optimizeWaypoints</CODE> parameter is set to <CODE>false</CODE>.</P>



For example, a driving route with five waypoints which is not optimized is visualized below using the [Bing Maps V8 Web Control](https://msdn.microsoft.com/library/mt712542.aspx). Driving directions are always given in the same order as specified in the request URL, i.e., the ordering `wp.0`, `wp.1`, `wp.2`, `wp.3`, `wp.4`.

 ![BM-aUnoptimizedWaypointSmall](../media/bm_aunoptimizedwaypointsmall.PNG)
 
The waypoints for this route can be optimized by setting the parameter `optimizeWaypoints` to `true` and, optionally, by specifying one of the following values for the `optimize` parameter (the default value is `time`):

<table>
<thead>
<tr class="header">
<th style="text-align: center;">Value of <code>optimize</code></th>
<th style="text-align: center;">Waypoint Optimization Description (<code>optimizeWaypoints=true</code>)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: center;"><code>distance</code></td>
<td style="text-align: center;">Waypoints are reordered to minimize distance traveled along the entire route. Traffic information is not used.</td>
</tr>
<tr class="even">
<td style="text-align: center;"><code>time</code> <strong>[Default]</strong></td>
<td style="text-align: center;">Waypoints are reordered to minimize time traveled along the entire route. Traffic information is not used.</td>
</tr>
<tr class="odd">
<td style="text-align: center;"><code>timeWithTraffic</code></td>
<td style="text-align: center;">Waypoints are reordered to minimize the time traveled along the entire route. Traffic information is not used.</td>
</tr>
<tr class="even">
<td style="text-align: center;"><code>timeAvoidClosure</code></td>
<td style="text-align: center;">Waypoints are reordered to minimize time traveled along the entire route. Traffic information, including road closure information, is not used.</td>
</tr>
</tbody>
</table>


Below is the same route, but with `optimizeWaypoints` set to `true`. The waypoints are rearranged to optimize driving travel time: `wp.0`, `wp.3`, `wp.2`, `wp.1`, `wp.4`.

 ![BM-aOptimizedWaypointSmall](../media/bm_aoptimizedwaypointsmall.PNG)

Next we show how to use the Routes API to minimize driving time for the current traffic situation using these five waypoints.


> [!NOTE]
> <P>Route optimization is only available for driving routes.</P>



## Example

When optimizing waypoints, only the first (`wp.0`) and last (`wp.n`) waypoints remain fixed.

The five waypoints from the above example are in the table below:

<table>
<thead>
<tr class="header">
<th style="text-align: center;">Waypoint</th>
<th style="text-align: center;">Place Name</th>
<th style="text-align: center;">Address</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: center;"><code>wp.0</code></td>
<td style="text-align: center;">Pike Place Market</td>
<td style="text-align: center;">86 Pike Pl, Seattle, WA 98101</td>
</tr>
<tr class="even">
<td style="text-align: center;"><code>wp.1</code></td>
<td style="text-align: center;">Fremont Troll</td>
<td style="text-align: center;">Troll Ave N, Seattle, WA 98103</td>
</tr>
<tr class="odd">
<td style="text-align: center;"><code>wp.2</code></td>
<td style="text-align: center;">UW Stadium</td>
<td style="text-align: center;">3800 Montlake Blvd NE, Seattle, WA 98195</td>
</tr>
<tr class="even">
<td style="text-align: center;"><code>wp.3</code></td>
<td style="text-align: center;">Seattle Central Library</td>
<td style="text-align: center;">1000 4th Ave, Seattle, WA 98104</td>
</tr>
<tr class="odd">
<td style="text-align: center;"><code>wp.4</code></td>
<td style="text-align: center;">Marvin's Garden</td>
<td style="text-align: center;">5400 Ballard Ave NW, Seattle, WA 98107</td>
</tr>
</tbody>
</table>


The optimized route (with `optimize=timeWithTraffic`) is: `wp.0`, `wp.3`, `wp.2`, `wp.1`, `wp.4`.

When making the URL request to optimize waypoints, we can change the middle waypoints `wp.1`, `wp.2`, and `wp.3` just so long as we keep the first (`wp.0`) and last (`wp.4`) waypoints the same.

For example, we could use this ordering to make the request URL:

<table>
<thead>
<tr class="header">
<th style="text-align: center;">Waypoint</th>
<th style="text-align: center;">Place Name</th>
<th style="text-align: center;">Address</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: center;"><code>wp.0</code></td>
<td style="text-align: center;">Pike Place Market</td>
<td style="text-align: center;">86 Pike Pl, Seattle, WA 98101</td>
</tr>
<tr class="even">
<td style="text-align: center;"><code>wp.1</code></td>
<td style="text-align: center;">UW Stadium</td>
<td style="text-align: center;">3800 Montlake Blvd NE, Seattle, WA 98195</td>
</tr>
<tr class="odd">
<td style="text-align: center;"><code>wp.2</code></td>
<td style="text-align: center;">Seattle Central Library</td>
<td style="text-align: center;">1000 4th Ave, Seattle, WA 98104</td>
</tr>
<tr class="even">
<td style="text-align: center;"><code>wp.3</code></td>
<td style="text-align: center;">Fremont Troll</td>
<td style="text-align: center;">Troll Ave N, Seattle, WA 98103</td>
</tr>
<tr class="odd">
<td style="text-align: center;"><code>wp.4</code></td>
<td style="text-align: center;">Marvin's Garden</td>
<td style="text-align: center;">5400 Ballard Ave NW, Seattle, WA 98107</td>
</tr>
</tbody>
</table>


In this case, we get the same optimized route: `wp.0`, `wp.3`, `wp.2`, `wp.1`, `wp.4`.

However, suppose that we switch the waypoint for the Fremont Troll with the waypoint for Marvin's Garden.

<table>
<thead>
<tr class="header">
<th style="text-align: center;">Waypoint</th>
<th style="text-align: center;">Place Name</th>
<th style="text-align: center;">Address</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: center;"><code>wp.0</code></td>
<td style="text-align: center;">Pike Place Market</td>
<td style="text-align: center;">86 Pike Pl, Seattle, WA 98101</td>
</tr>
<tr class="even">
<td style="text-align: center;"><code>wp.1</code></td>
<td style="text-align: center;">UW Stadium</td>
<td style="text-align: center;">3800 Montlake Blvd NE, Seattle, WA 98195</td>
</tr>
<tr class="odd">
<td style="text-align: center;"><code>wp.2</code></td>
<td style="text-align: center;">Seattle Central Library</td>
<td style="text-align: center;">1000 4th Ave, Seattle, WA 98104</td>
</tr>
<tr class="even">
<td style="text-align: center;"><code>wp.3</code></td>
<td style="text-align: center;">Marvin's Garden</td>
<td style="text-align: center;">5400 Ballard Ave NW, Seattle, WA 98107</td>
</tr>
<tr class="odd">
<td style="text-align: center;"><code>wp.4</code></td>
<td style="text-align: center;">Fremont Troll</td>
<td style="text-align: center;">Troll Ave N, Seattle, WA 98103</td>
</tr>
</tbody>
</table>


Then the Routes API will always provide us with an optimized route which ends in the Seattle neighborhood of Fremont instead of Ballard (which is where Marvin's Garden is).

### URL Request

Now we show how to make the full URL request.

First, assign waypoints to the above addresses to create the first part of the URL request (using `+` or `%20` to replace spaces):

    Driving?wp.0=86+Pike+Pl%2C+Seattle%2C+WA+98101&wp.1=Troll+Ave+N%2C+Seattle%2C+WA+98103&wp.2=3800+Montlake+Blvd+NE%2C+Seattle%2C+WA+98195&wp.3=1000+4th+Ave%2C+Seattle%2C+WA+98104&wp.4=5400+Ballard+Ave+NW%2C+Seattle%2C+WA+98107

To include a route with more waypoints simply add more waypoints to the list.

Second, make sure to set the parameter `optimizeWaypoints` (or the alias `optwp`) to `true`:

    &optimizeWaypoints=true

Lastly, specify a value for the `optimize` parameter.

In our example, we set `optimize` to `timeWithTraffic`. This will optimize both the *paths* (route legs) between waypoints and the order of the waypoints to minimize time traveled. However, current traffic information is only used for path optimization. It is *not* used for waypoint optimization (see [Path and Waypoint Optimization](https://msdn.microsoft.com/library/ff701717.aspx#anchor_1)):

    &optimize=timeWithTraffic

Below is the full URL request.

``` url
http://dev.virtualearth.net/REST/V1/Routes/Driving?wp.0=86+Pike+Pl%2C+Seattle%2C+WA+98101&wp.1=Troll+Ave+N%2C+Seattle%2C+WA+98103&wp.2=3800+Montlake+Blvd+NE%2C+Seattle%2C+WA+98195&wp.3=1000+4th+Ave%2C+Seattle%2C+WA+98104&wp.4=5400+Ballard+Ave+NW%2C+Seattle%2C+WA+98107&optwp=true&optimize=timeWithTraffic&key=<BingMapsAPIKey>
```

### Response

The optimized route is then returned as a JSON response (if an XML response is required, set the parameter `output` to `XML`):

``` JSON
    {
        "authenticationResultCode": "ValidCredentials",
        "brandLogoUri": "http:\/\/dev.virtualearth.net\/Branding\/logo_powered_by.png",
        "copyright": "Copyright © 2018 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.",
        "resourceSets": [
            {
                "estimatedTotal": 1,
                "resources": [
                    {
                        "__type": "Route:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",
                        "bbox": [
                            47.60586,
                            -122.384961,
                            47.667744,
                            -122.303817
                        ],
                        "id": "v69,h-1233900653,i0,a0,cen-US,dAAAAAAAAAAA1,y0,s1,m1,o1,t7,w86_llevNR0AiqYWSyZVewA2~AqpJWbqR-TMBAADgASDGPT8A0~ODYgUGlrZSBTdCwgU2VhdHRsZSwgV0EgOTgxMDE1~~~~v11,wCD2bVZ_NR0CsPIGwU5VewA2~AqpJWbpRDzQBAADgAQDtJT4A0~MTAwMCA0dGggQXZlLCBTZWF0dGxlLCBXQSA5ODEwNA2~~~~v11,whEiGHFvTR0ABvtu8cZNewA2~AqpJWbpBpi0BAADgAaDiQz4A0~MzgwMCBNb250bGFrZSBCbHZkIE5FLCBTZWF0dGxlLCBXQSA5ODE5NQ2~~~~v11,w8-UF2EfTR0CneccpOpZewA2~AqpJWbox1QoBAADgAQAAAD8A0~VHJvbGwgQXZlIE4sIFNlYXR0bGUsIFdBIDk4MTAz0~~~~v11,w1AyponjVR0AST3Yzo5hewA2~AqpJWboh9QkBAADgASdPoz4A0~NTQwMCBCYWxsYXJkIEF2ZSBOVywgU2VhdHRsZSwgV0EgOTgxMDc1~~~~v11,k1",
                        "distanceUnit": "Kilometer",
                        "durationUnit": "Second",
                        "routeLegs": [
                            {
                                "actualEnd": {
                                    "type": "Point",
                                    "coordinates": [
                                        47.606425,
                                        -122.333233
                                    ]
                                },
                                "actualStart": {
                                    "type": "Point",
                                    "coordinates": [
                                        47.608752,
                                        -122.340428
                                    ]
                                },
                                "alternateVias": [],
                                "cost": 0,
                                "description": "1st Ave, Spring St",
                                "endLocation": {
                                    "bbox": [
                                        47.646767,
                                        -122.354945,
                                        47.654493,
                                        -122.339655
                                    ],
                                    "name": "Troll Ave N, Seattle, WA 98103",
                                    "point": {
                                        "type": "Point",
                                        "coordinates": [
                                            47.65063,
                                            -122.3473
                                        ]
                                    },
                                    "address": {
                                        "addressLine": "Troll Ave N",
                                        "adminDistrict": "WA",
                                        "adminDistrict2": "King County",
                                        "countryRegion": "United States",
                                        "formattedAddress": "Troll Ave N, Seattle, WA 98103",
                                        "locality": "Seattle",
                                        "postalCode": "98103"
                                    },
                                    "confidence": "High",
                                    "entityType": "RoadBlock",
                                    "geocodePoints": [
                                        {
                                            "type": "Point",
                                            "coordinates": [
                                                47.65063,
                                                -122.3473
                                            ],
                                            "calculationMethod": "Interpolation",
                                            "usageTypes": [
                                                "Display"
                                            ]
                                        }
                                    ],
                                    "matchCodes": [
                                        "Good"
                                    ]
                                },
                                "itineraryItems": [
                                    {
                                        "compassDirection": "southwest",
                                        "details": [
                                            {
                                                "compassDegrees": 246,
                                                "endPathIndices": [
                                                    1
                                                ],
                                                "maneuverType": "DepartStart",
                                                "mode": "Driving",
                                                "names": [
                                                    "Pike St"
                                                ],
                                                "roadType": "Street",
                                                "startPathIndices": [
                                                    0
                                                ]
                                            }
                                        ],
                                        "exit": "",
                                        "iconType": "Auto",
                                        "instruction": {
                                            "formattedText": null,
                                            "maneuverType": "DepartStart",
                                            "text": "Depart Pike St toward Pike Pl"
                                        },
                                        "isRealTimeTransit": false,
                                        "maneuverPoint": {
                                            "type": "Point",
                                            "coordinates": [
                                                47.608752,
                                                -122.340428
                                            ]
                                        },
                                        "realTimeTransitDelay": 0,
                                        "sideOfStreet": "Unknown",
                                        "tollZone": "",
                                        "towardsRoadName": "Pike Pl",
                                        "transitTerminus": "",
                                        "travelDistance": 0.01,
                                        "travelDuration": 1,
                                        "travelMode": "Driving"
                                    },
                                    {
                                        "compassDirection": "northwest",
                                        "details": [
                                            {
                                                "compassDegrees": 300,
                                                "endPathIndices": [
                                                    3
                                                ],
                                                "maneuverType": "RoadNameChange",
                                                "mode": "Driving",
                                                "names": [
                                                    "Pike Pl"
                                                ],
                                                "roadType": "Street",
                                                "startPathIndices": [
                                                    1
                                                ]
                                            }
                                        ],
                                        "exit": "",
                                        "iconType": "Auto",
                                        "instruction": {
                                            "formattedText": null,
                                            "maneuverType": "RoadNameChange",
                                            "text": "Road name changes to Pike Pl"
                                        },
                                        "isRealTimeTransit": false,
                                        "maneuverPoint": {
                                            "type": "Point",
                                            "coordinates": [
                                                47.6087,
                                                -122.34055
                                            ]
                                        },
                                        "realTimeTransitDelay": 0,
                                        "sideOfStreet": "Unknown",
                                        "tollZone": "",
                                        "transitTerminus": "",
                                        "travelDistance": 0.123,
                                        "travelDuration": 15,
                                        "travelMode": "Driving"
                                    },
                                    {
                                        "compassDirection": "northeast",
                                        "details": [
                                            {
                                                "compassDegrees": 63,
                                                "endPathIndices": [
                                                    7
                                                ],
                                                "maneuverType": "TurnRight",
                                                "mode": "Driving",
                                                "names": [
                                                    "Pine St"
                                                ],
                                                "roadType": "Street",
                                                "startPathIndices": [
                                                    3
                                                ]
                                            }
                                        ],
                                        "exit": "",
                                        "iconType": "Auto",
                                        "instruction": {
                                            "formattedText": null,
                                            "maneuverType": "TurnRight",
                                            "text": "Turn right onto Pine St"
                                        },
                                        "isRealTimeTransit": false,
                                        "maneuverPoint": {
                                            "type": "Point",
                                            "coordinates": [
                                                47.60943,
                                                -122.34179
                                            ]
                                        },
                                        "realTimeTransitDelay": 0,
                                        "sideOfStreet": "Unknown",
                                        "tollZone": "",
                                        "transitTerminus": "",
                                        "travelDistance": 0.075,
                                        "travelDuration": 14,
                                        "travelMode": "Driving"
                                    },
                                    {
                                        "compassDirection": "southeast",
                                        "details": [
                                            {
                                                "compassDegrees": 138,
                                                "endPathIndices": [
                                                    9
                                                ],
                                                "locationCodes": [
                                                    "114+08308"
                                                ],
                                                "maneuverType": "TurnRight",
                                                "mode": "Driving",
                                                "names": [
                                                    "1st Ave"
                                                ],
                                                "roadType": "Arterial",
                                                "startPathIndices": [
                                                    7
                                                ]
                                            }
                                        ],
                                        "exit": "",
                                        "iconType": "Auto",
                                        "instruction": {
                                            "formattedText": null,
                                            "maneuverType": "TurnRight",
                                            "text": "Turn right onto 1st Ave"
                                        },
                                        "isRealTimeTransit": false,
                                        "maneuverPoint": {
                                            "type": "Point",
                                            "coordinates": [
                                                47.60981,
                                                -122.34095
                                            ]
                                        },
                                        "realTimeTransitDelay": 0,
                                        "sideOfStreet": "Unknown",
                                        "tollZone": "",
                                        "transitTerminus": "",
                                        "travelDistance": 0.388,
                                        "travelDuration": 49,
                                        "travelMode": "Driving"
                                    },
                                    {
                                        "compassDirection": "southeast",
                                        "details": [
                                            {
                                                "compassDegrees": 66,
                                                "endPathIndices": [
                                                    10
                                                ],
                                                "maneuverType": "TurnLeft",
                                                "mode": "Driving",
                                                "names": [
                                                    "University St"
                                                ],
                                                "roadType": "Arterial",
                                                "startPathIndices": [
                                                    9
                                                ]
                                            },
                                            {
                                                "compassDegrees": 137,
                                                "endPathIndices": [
                                                    12
                                                ],
                                                "locationCodes": [
                                                    "114-08017"
                                                ],
                                                "maneuverType": "TurnRight",
                                                "mode": "Driving",
                                                "names": [
                                                    "2nd Ave"
                                                ],
                                                "roadType": "MajorRoad",
                                                "startPathIndices": [
                                                    10
                                                ]
                                            }
                                        ],
                                        "exit": "",
                                        "iconType": "Auto",
                                        "instruction": {
                                            "formattedText": null,
                                            "maneuverType": "TurnLeftThenTurnRight",
                                            "text": "Turn left onto University St, and then immediately turn right onto 2nd Ave"
                                        },
                                        "isRealTimeTransit": false,
                                        "maneuverPoint": {
                                            "type": "Point",
                                            "coordinates": [
                                                47.60683,
                                                -122.33822
                                            ]
                                        },
                                        "realTimeTransitDelay": 0,
                                        "sideOfStreet": "Unknown",
                                        "tollZone": "",
                                        "transitTerminus": "",
                                        "travelDistance": 0.285,
                                        "travelDuration": 63,
                                        "travelMode": "Driving"
                                    },
                                    {
                                        "compassDirection": "east",
                                        "details": [
                                            {
                                                "compassDegrees": 68,
                                                "endPathIndices": [
                                                    14
                                                ],
                                                "locationCodes": [
                                                    "114-51334",
                                                    "114-51335"
                                                ],
                                                "maneuverType": "TurnLeft",
                                                "mode": "Driving",
                                                "names": [
                                                    "Spring St"
                                                ],
                                                "roadType": "Arterial",
                                                "startPathIndices": [
                                                    12
                                                ]
                                            }
                                        ],
                                        "exit": "",
                                        "iconType": "Auto",
                                        "instruction": {
                                            "formattedText": null,
                                            "maneuverType": "TurnLeft",
                                            "text": "Turn left onto Spring St"
                                        },
                                        "isRealTimeTransit": false,
                                        "maneuverPoint": {
                                            "type": "Point",
                                            "coordinates": [
                                                47.60586,
                                                -122.3358
                                            ]
                                        },
                                        "realTimeTransitDelay": 0,
                                        "sideOfStreet": "Unknown",
                                        "tollZone": "",
                                        "transitTerminus": "",
                                        "travelDistance": 0.296,
                                        "travelDuration": 71,
                                        "travelMode": "Driving"
                                    },
                                    {
                                        "compassDirection": "west",
                                        "details": [
                                            {
                                                "compassDegrees": 134,
                                                "endPathIndices": [
                                                    18
                                                ],
                                                "locationCodes": [
                                                    "114+08542"
                                                ],
                                                "maneuverType": "TurnRight",
                                                "mode": "Driving",
                                                "names": [
                                                    "5th Ave"
                                                ],
                                                "roadType": "Arterial",
                                                "startPathIndices": [
                                                    14
                                                ]
                                            },
                                            {
                                                "compassDegrees": 248,
                                                "endPathIndices": [
                                                    20
                                                ],
                                                "locationCodes": [
                                                    "114-08209"
                                                ],
                                                "maneuverType": "TurnRight",
                                                "mode": "Driving",
                                                "names": [
                                                    "Madison St"
                                                ],
                                                "roadType": "MajorRoad",
                                                "startPathIndices": [
                                                    18
                                                ]
                                            }
                                        ],
                                        "exit": "",
                                        "iconType": "Auto",
                                        "instruction": {
                                            "formattedText": null,
                                            "maneuverType": "TurnRightThenTurnRight",
                                            "text": "Turn right onto 5th Ave, and then immediately turn right onto Madison St"
                                        },
                                        "isRealTimeTransit": false,
                                        "maneuverPoint": {
                                            "type": "Point",
                                            "coordinates": [
                                                47.60726,
                                                -122.33244
                                            ]
                                        },
                                        "realTimeTransitDelay": 0,
                                        "sideOfStreet": "Unknown",
                                        "tollZone": "",
                                        "transitTerminus": "",
                                        "travelDistance": 0.191,
                                        "travelDuration": 36,
                                        "travelMode": "Driving"
                                    },
                                    {
                                        "compassDirection": "northwest",
                                        "details": [
                                            {
                                                "compassDegrees": 316,
                                                "endPathIndices": [
                                                    23
                                                ],
                                                "locationCodes": [
                                                    "114-08028"
                                                ],
                                                "maneuverType": "TurnRight",
                                                "mode": "Driving",
                                                "names": [
                                                    "4th Ave"
                                                ],
                                                "roadType": "MajorRoad",
                                                "startPathIndices": [
                                                    20
                                                ]
                                            }
                                        ],
                                        "exit": "",
                                        "iconType": "Auto",
                                        "instruction": {
                                            "formattedText": null,
                                            "maneuverType": "TurnRight",
                                            "text": "Turn right onto 4th Ave"
                                        },
                                        "isRealTimeTransit": false,
                                        "maneuverPoint": {
                                            "type": "Point",
                                            "coordinates": [
                                                47.60611,
                                                -122.33293
                                            ]
                                        },
                                        "realTimeTransitDelay": 0,
                                        "sideOfStreet": "Unknown",
                                        "tollZone": "",
                                        "transitTerminus": "",
                                        "travelDistance": 0.041,
                                        "travelDuration": 17,
                                        "travelMode": "Driving"
                                    },
                                    {
                                        "compassDirection": "northwest",
                                        "details": [
                                            {
                                                "compassDegrees": 315,
                                                "endPathIndices": [
                                                    23
                                                ],
                                                "locationCodes": [
                                                    "114-08028"
                                                ],
                                                "maneuverType": "ArriveFinish",
                                                "mode": "Driving",
                                                "names": [
                                                    "4th Ave"
                                                ],
                                                "roadType": "MajorRoad",
                                                "startPathIndices": [
                                                    23
                                                ]
                                            }
                                        ],
                                        "exit": "",
                                        "hints": [
                                            {
                                                "hintType": "PreviousIntersection",
                                                "text": "The last intersection is Madison St"
                                            },
                                            {
                                                "hintType": "NextIntersection",
                                                "text": "If you reach Spring St, you've gone too far"
                                            }
                                        ],
                                        "iconType": "Auto",
                                        "instruction": {
                                            "formattedText": null,
                                            "maneuverType": "ArriveIntermediateStop",
                                            "text": "Arrive at 1000 4th Ave, Seattle, WA 98104"
                                        },
                                        "isRealTimeTransit": false,
                                        "maneuverPoint": {
                                            "type": "Point",
                                            "coordinates": [
                                                47.606425,
                                                -122.333233
                                            ]
                                        },
                                        "realTimeTransitDelay": 0,
                                        "sideOfStreet": "Unknown",
                                        "tollZone": "",
                                        "transitTerminus": "",
                                        "travelDistance": 0,
                                        "travelDuration": 0,
                                        "travelMode": "Driving"
                                    }
                                ],
                                "routeRegion": "NAv2",
                                "routeSubLegs": [
                                    {
                                        "endWaypoint": {
                                            "type": "Point",
                                            "coordinates": [
                                                47.606425,
                                                -122.333233
                                            ],
                                            "description": "1000 4th Ave, Seattle, WA 98104",
                                            "isVia": false,
                                            "locationIdentifier": "2|170|73|89|186|81|15|52|1|0|0|224|1|0|237|37|62|0|47.606425,-122.333233",
                                            "routePathIndex": 23
                                        },
                                        "startWaypoint": {
                                            "type": "Point",
                                            "coordinates": [
                                                47.608752,
                                                -122.340428
                                            ],
                                            "description": "86 Pike St, Seattle, WA 98101",
                                            "isVia": false,
                                            "locationIdentifier": "2|170|73|89|186|145|249|51|1|0|0|224|1|32|198|61|63|0|47.608752,-122.340428",
                                            "routePathIndex": 0
                                        },
                                        "travelDistance": 1.409,
                                        "travelDuration": 269
                                    }
                                ],
                                "startLocation": {
                                    "bbox": [
                                        47.604967,
                                        -122.348139,
                                        47.612693,
                                        -122.332861
                                    ],
                                    "name": "86 Pike St, Seattle, WA 98101",
                                    "point": {
                                        "type": "Point",
                                        "coordinates": [
                                            47.60883,
                                            -122.3405
                                        ]
                                    },
                                    "address": {
                                        "addressLine": "86 Pike St",
                                        "adminDistrict": "WA",
                                        "adminDistrict2": "King County",
                                        "countryRegion": "United States",
                                        "formattedAddress": "86 Pike St, Seattle, WA 98101",
                                        "locality": "Seattle",
                                        "postalCode": "98101"
                                    },
                                    "confidence": "High",
                                    "entityType": "Address",
                                    "geocodePoints": [
                                        {
                                            "type": "Point",
                                            "coordinates": [
                                                47.60883,
                                                -122.3405
                                            ],
                                            "calculationMethod": "Rooftop",
                                            "usageTypes": [
                                                "Display"
                                            ]
                                        },
                                        {
                                            "type": "Point",
                                            "coordinates": [
                                                47.608752,
                                                -122.340428
                                            ],
                                            "calculationMethod": "Rooftop",
                                            "usageTypes": [
                                                "Route"
                                            ]
                                        }
                                    ],
                                    "matchCodes": [
                                        "Good"
                                    ]
                                },
                                "travelDistance": 1.409,
                                "travelDuration": 758
                            },
                            {
                                "actualEnd": {
                                    "type": "Point",
                                    "coordinates": [
                                        47.651218,
                                        -122.303817
                                    ]
                                },
                                "actualStart": {
                                    "type": "Point",
                                    "coordinates": [
                                        47.606425,
                                        -122.333233
                                    ]
                                },
                                "alternateVias": [],
                                "cost": 0,
                                "description": "I-5 N, WA-520 E",
                                "endLocation": {
                                    "bbox": [
                                        47.647339,
                                        -122.3114,
                                        47.655065,
                                        -122.29611
                                    ],
                                    "name": "3800 Montlake Blvd NE, Seattle, WA 98195",
                                    "point": {
                                        "type": "Point",
                                        "coordinates": [
                                            47.651202,
                                            -122.303755
                                        ]
                                    },
                                    "address": {
                                        "addressLine": "3800 Montlake Blvd NE",
                                        "adminDistrict": "WA",
                                        "adminDistrict2": "King County",
                                        "countryRegion": "United States",
                                        "formattedAddress": "3800 Montlake Blvd NE, Seattle, WA 98195",
                                        "locality": "Seattle",
                                        "postalCode": "98195"
                                    },
                                    "confidence": "High",
                                    "entityType": "Address",
                                    "geocodePoints": [
                                        {
                                            "type": "Point",
                                            "coordinates": [
                                                47.651202,
                                                -122.303755
                                            ],
                                            "calculationMethod": "InterpolationOffset",
                                            "usageTypes": [
                                                "Display"
                                            ]
                                        },
                                        {
                                            "type": "Point",
                                            "coordinates": [
                                                47.651218,
                                                -122.303817
                                            ],
                                            "calculationMethod": "Interpolation",
                                            "usageTypes": [
                                                "Route"
                                            ]
                                        }
                                    ],
                                    "matchCodes": [
                                        "Good"
                                    ]
                                },
                                "itineraryItems": [
                                    {
                                        "compassDirection": "northwest",
                                        "details": [
                                            {
                                                "compassDegrees": 315,
                                                "endPathIndices": [
                                                    1
                                                ],
                                                "locationCodes": [
                                                    "114-08028"
                                                ],
                                                "maneuverType": "DepartStart",
                                                "mode": "Driving",
                                                "names": [
                                                    "4th Ave"
                                                ],
                                                "roadType": "MajorRoad",
                                                "startPathIndices": [
                                                    0
                                                ]
                                            }
                                        ],
                                        "exit": "",
                                        "iconType": "Auto",
                                        "instruction": {
                                            "formattedText": null,
                                            "maneuverType": "DepartIntermediateStop",
                                            "text": "Depart 4th Ave toward Spring St"
                                        },
                                        "isRealTimeTransit": false,
                                        "maneuverPoint": {
                                            "type": "Point",
                                            "coordinates": [
                                                47.606425,
                                                -122.333233
                                            ]
                                        },
                                        "realTimeTransitDelay": 0,
                                        "sideOfStreet": "Unknown",
                                        "tollZone": "",
                                        "towardsRoadName": "Spring St",
                                        "transitTerminus": "",
                                        "travelDistance": 0.232,
                                        "travelDuration": 17,
                                        "travelMode": "Driving"
                                    },
                                    {
                                        "compassDirection": "northeast",
                                        "details": [
                                            {
                                                "compassDegrees": 67,
                                                "endPathIndices": [
                                                    3
                                                ],
                                                "locationCodes": [
                                                    "114N51350",
                                                    "114-51350",
                                                    "114-51351"
                                                ],
                                                "maneuverType": "TurnRight",
                                                "mode": "Driving",
                                                "names": [
                                                    "University St"
                                                ],
                                                "roadType": "Arterial",
                                                "startPathIndices": [
                                                    1
                                                ]
                                            }
                                        ],
                                        "exit": "",
                                        "iconType": "Auto",
                                        "instruction": {
                                            "formattedText": null,
                                            "maneuverType": "TurnRight",
                                            "text": "Turn right onto University St"
                                        },
                                        "isRealTimeTransit": false,
                                        "maneuverPoint": {
                                            "type": "Point",
                                            "coordinates": [
                                                47.60819,
                                                -122.33487
                                            ]
                                        },
                                        "realTimeTransitDelay": 0,
                                        "sideOfStreet": "Unknown",
                                        "tollZone": "",
                                        "transitTerminus": "",
                                        "travelDistance": 0.269,
                                        "travelDuration": 45,
                                        "travelMode": "Driving"
                                    },
                                    {
                                        "compassDirection": "north",
                                        "details": [
                                            {
                                                "compassDegrees": 65,
                                                "endPathIndices": [
                                                    7
                                                ],
                                                "locationCodes": [
                                                    "114-51351",
                                                    "114N51352"
                                                ],
                                                "maneuverType": "TakeRampStraight",
                                                "mode": "Driving",
                                                "roadType": "Ramp",
                                                "startPathIndices": [
                                                    3
                                                ]
                                            },
                                            {
                                                "compassDegrees": 18,
                                                "endPathIndices": [
                                                    22
                                                ],
                                                "maneuverType": "Merge",
                                                "mode": "Driving",
                                                "names": [
                                                    "I-5 N"
                                                ],
                                                "roadShieldRequestParameters": {
                                                    "bucket": 656001,
                                                    "shields": [
                                                        {
                                                            "labels": [
                                                                "5"
                                                            ],
                                                            "roadShieldType": 1
                                                        }
                                                    ]
                                                },
                                                "roadType": "LimitedAccessHighway",
                                                "startPathIndices": [
                                                    7
                                                ]
                                            }
                                        ],
                                        "exit": "",
                                        "iconType": "Auto",
                                        "instruction": {
                                            "formattedText": null,
                                            "maneuverType": "RampToHighwayStraight",
                                            "text": "Take ramp for I-5 N"
                                        },
                                        "isRealTimeTransit": false,
                                        "maneuverPoint": {
                                            "type": "Point",
                                            "coordinates": [
                                                47.60944,
                                                -122.33179
                                            ]
                                        },
                                        "realTimeTransitDelay": 0,
                                        "sideOfStreet": "Unknown",
                                        "tollZone": "",
                                        "transitTerminus": "",
                                        "travelDistance": 3.419,
                                        "travelDuration": 128,
                                        "travelMode": "Driving",
                                        "warnings": [
                                            {
                                                "origin": "47.63619,-122.32272",
                                                "severity": "Moderate",
                                                "text": "Moderate Congestion",
                                                "to": "47.636719,-122.322671",
                                                "warningType": "TrafficFlow"
                                            }
                                        ]
                                    },
                                    {
                                        "compassDirection": "east",
                                        "details": [
                                            {
                                                "compassDegrees": 12,
                                                "endPathIndices": [
                                                    30
                                                ],
                                                "maneuverType": "TakeRampRight",
                                                "mode": "Driving",
                                                "roadType": "Ramp",
                                                "startPathIndices": [
                                                    22
                                                ]
                                            },
                                            {
                                                "compassDegrees": 84,
                                                "endPathIndices": [
                                                    34
                                                ],
                                                "maneuverType": "Merge",
                                                "mode": "Driving",
                                                "names": [
                                                    "WA-520"
                                                ],
                                                "roadShieldRequestParameters": {
                                                    "bucket": 656001,
                                                    "shields": [
                                                        {
                                                            "labels": [
                                                                "520"
                                                            ],
                                                            "roadShieldType": 3
                                                        }
                                                    ]
                                                },
                                                "roadType": "LimitedAccessHighway",
                                                "startPathIndices": [
                                                    30
                                                ]
                                            }
                                        ],
                                        "exit": "168B",
                                        "iconType": "Auto",
                                        "instruction": {
                                            "formattedText": null,
                                            "maneuverType": "RampThenHighwayRight",
                                            "text": "At exit 168B, take ramp right for WA-520 toward Bellevue \/ Kirkland"
                                        },
                                        "isRealTimeTransit": false,
                                        "maneuverPoint": {
                                            "type": "Point",
                                            "coordinates": [
                                                47.63895,
                                                -122.32261
                                            ]
                                        },
                                        "realTimeTransitDelay": 0,
                                        "sideOfStreet": "Unknown",
                                        "signs": [
                                            "Bellevue",
                                            "Kirkland",
                                            "WA-520"
                                        ],
                                        "tollZone": "",
                                        "transitTerminus": "",
                                        "travelDistance": 1.364,
                                        "travelDuration": 67,
                                        "travelMode": "Driving"
                                    },
                                    {
                                        "compassDirection": "east",
                                        "details": [
                                            {
                                                "compassDegrees": 85,
                                                "endPathIndices": [
                                                    39
                                                ],
                                                "locationCodes": [
                                                    "114P14424"
                                                ],
                                                "maneuverType": "TakeRampRight",
                                                "mode": "Driving",
                                                "roadType": "Ramp",
                                                "startPathIndices": [
                                                    34
                                                ]
                                            }
                                        ],
                                        "exit": "",
                                        "iconType": "Auto",
                                        "instruction": {
                                            "formattedText": null,
                                            "maneuverType": "TakeRampRight",
                                            "text": "Take ramp right for Montlake Blvd toward Univ of Wash"
                                        },
                                        "isRealTimeTransit": false,
                                        "maneuverPoint": {
                                            "type": "Point",
                                            "coordinates": [
                                                47.64341,
                                                -122.30838
                                            ]
                                        },
                                        "realTimeTransitDelay": 0,
                                        "sideOfStreet": "Unknown",
                                        "signs": [
                                            "Univ of Wash",
                                            "Montlake Blvd"
                                        ],
                                        "tollZone": "",
                                        "transitTerminus": "",
                                        "travelDistance": 0.354,
                                        "travelDuration": 29,
                                        "travelMode": "Driving"
                                    },
                                    {
                                        "compassDirection": "north",
                                        "details": [
                                            {
                                                "compassDegrees": 338,
                                                "endPathIndices": [
                                                    44
                                                ],
                                                "locationCodes": [
                                                    "114-08231",
                                                    "114N14838"
                                                ],
                                                "maneuverType": "TurnLeft",
                                                "mode": "Driving",
                                                "names": [
                                                    "Montlake Blvd E"
                                                ],
                                                "roadType": "MajorRoad",
                                                "startPathIndices": [
                                                    39
                                                ]
                                            }
                                        ],
                                        "exit": "",
                                        "hints": [
                                            {
                                                "hintType": "Landmark",
                                                "text": "76 on the corner"
                                            }
                                        ],
                                        "iconType": "Auto",
                                        "instruction": {
                                            "formattedText": null,
                                            "maneuverType": "TurnLeft",
                                            "text": "Turn left onto Montlake Blvd E"
                                        },
                                        "isRealTimeTransit": false,
                                        "maneuverPoint": {
                                            "type": "Point",
                                            "coordinates": [
                                                47.64398,
                                                -122.3041
                                            ]
                                        },
                                        "realTimeTransitDelay": 0,
                                        "sideOfStreet": "Unknown",
                                        "tollZone": "",
                                        "transitTerminus": "",
                                        "travelDistance": 0.419,
                                        "travelDuration": 80,
                                        "travelMode": "Driving"
                                    },
                                    {
                                        "compassDirection": "north",
                                        "details": [
                                            {
                                                "endPathIndices": [
                                                    47
                                                ],
                                                "locationCodes": [
                                                    "114-14838",
                                                    "114N08233",
                                                    "114-08233"
                                                ],
                                                "maneuverType": "RoadNameChange",
                                                "mode": "Driving",
                                                "names": [
                                                    "Montlake Blvd NE"
                                                ],
                                                "roadType": "MajorRoad",
                                                "startPathIndices": [
                                                    44
                                                ]
                                            }
                                        ],
                                        "exit": "",
                                        "iconType": "Auto",
                                        "instruction": {
                                            "formattedText": null,
                                            "maneuverType": "RoadNameChange",
                                            "text": "Road name changes to Montlake Blvd NE"
                                        },
                                        "isRealTimeTransit": false,
                                        "maneuverPoint": {
                                            "type": "Point",
                                            "coordinates": [
                                                47.647709999999996,
                                                -122.30461
                                            ]
                                        },
                                        "realTimeTransitDelay": 0,
                                        "sideOfStreet": "Unknown",
                                        "tollZone": "",
                                        "transitTerminus": "",
                                        "travelDistance": 0.4,
                                        "travelDuration": 44,
                                        "travelMode": "Driving"
                                    },
                                    {
                                        "compassDirection": "northeast",
                                        "details": [
                                            {
                                                "compassDegrees": 29,
                                                "endPathIndices": [
                                                    47
                                                ],
                                                "locationCodes": [
                                                    "114-08233"
                                                ],
                                                "maneuverType": "ArriveFinish",
                                                "mode": "Driving",
                                                "names": [
                                                    "Montlake Blvd NE"
                                                ],
                                                "roadType": "MajorRoad",
                                                "startPathIndices": [
                                                    47
                                                ]
                                            }
                                        ],
                                        "exit": "",
                                        "hints": [
                                            {
                                                "hintType": "PreviousIntersection",
                                                "text": "The last intersection is NE Pacific Pl"
                                            }
                                        ],
                                        "iconType": "Auto",
                                        "instruction": {
                                            "formattedText": null,
                                            "maneuverType": "ArriveIntermediateStop",
                                            "text": "Arrive at 3800 Montlake Blvd NE, Seattle, WA 98195"
                                        },
                                        "isRealTimeTransit": false,
                                        "maneuverPoint": {
                                            "type": "Point",
                                            "coordinates": [
                                                47.651218,
                                                -122.303817
                                            ]
                                        },
                                        "realTimeTransitDelay": 0,
                                        "sideOfStreet": "Unknown",
                                        "tollZone": "",
                                        "transitTerminus": "",
                                        "travelDistance": 0,
                                        "travelDuration": 0,
                                        "travelMode": "Driving"
                                    }
                                ],
                                "routeRegion": "NAv2",
                                "routeSubLegs": [
                                    {
                                        "endWaypoint": {
                                            "type": "Point",
                                            "coordinates": [
                                                47.651218,
                                                -122.303817
                                            ],
                                            "description": "3800 Montlake Blvd NE, Seattle, WA 98195",
                                            "isVia": false,
                                            "locationIdentifier": "2|170|73|89|186|65|166|45|1|0|0|224|1|160|226|67|62|0|47.651218,-122.303817",
                                            "routePathIndex": 70
                                        },
                                        "startWaypoint": {
                                            "type": "Point",
                                            "coordinates": [
                                                47.606425,
                                                -122.333233
                                            ],
                                            "description": "1000 4th Ave, Seattle, WA 98104",
                                            "isVia": false,
                                            "locationIdentifier": "2|170|73|89|186|81|15|52|1|0|0|224|1|0|237|37|62|0|47.606425,-122.333233",
                                            "routePathIndex": 23
                                        },
                                        "travelDistance": 6.457,
                                        "travelDuration": 413
                                    }
                                ],
                                "startLocation": {
                                    "bbox": [
                                        47.646767,
                                        -122.354945,
                                        47.654493,
                                        -122.339655
                                    ],
                                    "name": "Troll Ave N, Seattle, WA 98103",
                                    "point": {
                                        "type": "Point",
                                        "coordinates": [
                                            47.65063,
                                            -122.3473
                                        ]
                                    },
                                    "address": {
                                        "addressLine": "Troll Ave N",
                                        "adminDistrict": "WA",
                                        "adminDistrict2": "King County",
                                        "countryRegion": "United States",
                                        "formattedAddress": "Troll Ave N, Seattle, WA 98103",
                                        "locality": "Seattle",
                                        "postalCode": "98103"
                                    },
                                    "confidence": "High",
                                    "entityType": "RoadBlock",
                                    "geocodePoints": [
                                        {
                                            "type": "Point",
                                            "coordinates": [
                                                47.65063,
                                                -122.3473
                                            ],
                                            "calculationMethod": "Interpolation",
                                            "usageTypes": [
                                                "Display"
                                            ]
                                        }
                                    ],
                                    "matchCodes": [
                                        "Good"
                                    ]
                                },
                                "travelDistance": 6.457,
                                "travelDuration": 740
                            },
                            {
                                "actualEnd": {
                                    "type": "Point",
                                    "coordinates": [
                                        47.65063,
                                        -122.3473
                                    ]
                                },
                                "actualStart": {
                                    "type": "Point",
                                    "coordinates": [
                                        47.651218,
                                        -122.303817
                                    ]
                                },
                                "alternateVias": [],
                                "cost": 0,
                                "description": "NE Pacific St, N 34th St",
                                "endLocation": {
                                    "bbox": [
                                        47.602817,
                                        -122.340298,
                                        47.610543,
                                        -122.325022
                                    ],
                                    "name": "1000 4th Ave, Seattle, WA 98104",
                                    "point": {
                                        "type": "Point",
                                        "coordinates": [
                                            47.60668,
                                            -122.33266
                                        ]
                                    },
                                    "address": {
                                        "addressLine": "1000 4th Ave",
                                        "adminDistrict": "WA",
                                        "adminDistrict2": "King County",
                                        "countryRegion": "United States",
                                        "formattedAddress": "1000 4th Ave, Seattle, WA 98104",
                                        "locality": "Seattle",
                                        "postalCode": "98104"
                                    },
                                    "confidence": "High",
                                    "entityType": "Address",
                                    "geocodePoints": [
                                        {
                                            "type": "Point",
                                            "coordinates": [
                                                47.60668,
                                                -122.33266
                                            ],
                                            "calculationMethod": "Rooftop",
                                            "usageTypes": [
                                                "Display"
                                            ]
                                        },
                                        {
                                            "type": "Point",
                                            "coordinates": [
                                                47.606425,
                                                -122.333233
                                            ],
                                            "calculationMethod": "Rooftop",
                                            "usageTypes": [
                                                "Route"
                                            ]
                                        }
                                    ],
                                    "matchCodes": [
                                        "Good"
                                    ]
                                },
                                "itineraryItems": [
                                    {
                                        "compassDirection": "southwest",
                                        "details": [
                                            {
                                                "compassDegrees": 209,
                                                "endPathIndices": [
                                                    2
                                                ],
                                                "locationCodes": [
                                                    "114+08232"
                                                ],
                                                "maneuverType": "DepartStart",
                                                "mode": "Driving",
                                                "names": [
                                                    "Montlake Blvd NE"
                                                ],
                                                "roadType": "MajorRoad",
                                                "startPathIndices": [
                                                    0
                                                ]
                                            }
                                        ],
                                        "exit": "",
                                        "iconType": "Auto",
                                        "instruction": {
                                            "formattedText": null,
                                            "maneuverType": "DepartIntermediateStop",
                                            "text": "Depart Montlake Blvd NE toward NE Pacific Pl"
                                        },
                                        "isRealTimeTransit": false,
                                        "maneuverPoint": {
                                            "type": "Point",
                                            "coordinates": [
                                                47.651218,
                                                -122.303817
                                            ]
                                        },
                                        "realTimeTransitDelay": 0,
                                        "sideOfStreet": "Unknown",
                                        "tollZone": "",
                                        "towardsRoadName": "NE Pacific Pl",
                                        "transitTerminus": "",
                                        "travelDistance": 0.202,
                                        "travelDuration": 19,
                                        "travelMode": "Driving"
                                    },
                                    {
                                        "compassDirection": "northwest",
                                        "details": [
                                            {
                                                "compassDegrees": 296,
                                                "endPathIndices": [
                                                    11
                                                ],
                                                "locationCodes": [
                                                    "114-11050",
                                                    "114+11051"
                                                ],
                                                "maneuverType": "TurnRight",
                                                "mode": "Driving",
                                                "names": [
                                                    "NE Pacific St"
                                                ],
                                                "roadType": "Arterial",
                                                "startPathIndices": [
                                                    2
                                                ]
                                            }
                                        ],
                                        "exit": "",
                                        "iconType": "Auto",
                                        "instruction": {
                                            "formattedText": null,
                                            "maneuverType": "TurnRight",
                                            "text": "Turn right onto NE Pacific St"
                                        },
                                        "isRealTimeTransit": false,
                                        "maneuverPoint": {
                                            "type": "Point",
                                            "coordinates": [
                                                47.64949,
                                                -122.30454
                                            ]
                                        },
                                        "realTimeTransitDelay": 0,
                                        "sideOfStreet": "Unknown",
                                        "tollZone": "",
                                        "transitTerminus": "",
                                        "travelDistance": 1.275,
                                        "travelDuration": 182,
                                        "travelMode": "Driving"
                                    },
                                    {
                                        "compassDirection": "west",
                                        "details": [
                                            {
                                                "compassDegrees": 282,
                                                "endPathIndices": [
                                                    13
                                                ],
                                                "locationCodes": [
                                                    "114P10958",
                                                    "114+10958"
                                                ],
                                                "maneuverType": "KeepStraight",
                                                "mode": "Driving",
                                                "names": [
                                                    "NE Northlake Way"
                                                ],
                                                "roadType": "Arterial",
                                                "startPathIndices": [
                                                    11
                                                ]
                                            }
                                        ],
                                        "exit": "",
                                        "iconType": "Auto",
                                        "instruction": {
                                            "formattedText": null,
                                            "maneuverType": "KeepStraight",
                                            "text": "Keep straight onto NE Northlake Way"
                                        },
                                        "isRealTimeTransit": false,
                                        "maneuverPoint": {
                                            "type": "Point",
                                            "coordinates": [
                                                47.65442,
                                                -122.31908
                                            ]
                                        },
                                        "realTimeTransitDelay": 0,
                                        "sideOfStreet": "Unknown",
                                        "tollZone": "",
                                        "transitTerminus": "",
                                        "travelDistance": 0.258,
                                        "travelDuration": 35,
                                        "travelMode": "Driving"
                                    },
                                    {
                                        "compassDirection": "south",
                                        "details": [
                                            {
                                                "compassDegrees": 180,
                                                "endPathIndices": [
                                                    22
                                                ],
                                                "locationCodes": [
                                                    "114+10958"
                                                ],
                                                "maneuverType": "TurnToStayLeft",
                                                "mode": "Driving",
                                                "names": [
                                                    "NE Northlake Way"
                                                ],
                                                "roadType": "Arterial",
                                                "startPathIndices": [
                                                    13
                                                ]
                                            }
                                        ],
                                        "exit": "",
                                        "iconType": "Auto",
                                        "instruction": {
                                            "formattedText": null,
                                            "maneuverType": "TurnToStayLeft",
                                            "text": "Turn left to stay on NE Northlake Way"
                                        },
                                        "isRealTimeTransit": false,
                                        "maneuverPoint": {
                                            "type": "Point",
                                            "coordinates": [
                                                47.6545,
                                                -122.32251
                                            ]
                                        },
                                        "realTimeTransitDelay": 0,
                                        "sideOfStreet": "Unknown",
                                        "tollZone": "",
                                        "transitTerminus": "",
                                        "travelDistance": 0.761,
                                        "travelDuration": 102,
                                        "travelMode": "Driving"
                                    },
                                    {
                                        "compassDirection": "southwest",
                                        "details": [
                                            {
                                                "compassDegrees": 228,
                                                "endPathIndices": [
                                                    28
                                                ],
                                                "locationCodes": [
                                                    "114+11053"
                                                ],
                                                "maneuverType": "KeepStraight",
                                                "mode": "Driving",
                                                "names": [
                                                    "N Pacific St"
                                                ],
                                                "roadType": "Arterial",
                                                "startPathIndices": [
                                                    22
                                                ]
                                            }
                                        ],
                                        "exit": "",
                                        "iconType": "Auto",
                                        "instruction": {
                                            "formattedText": null,
                                            "maneuverType": "KeepStraight",
                                            "text": "Keep straight onto N Pacific St"
                                        },
                                        "isRealTimeTransit": false,
                                        "maneuverPoint": {
                                            "type": "Point",
                                            "coordinates": [
                                                47.65098,
                                                -122.33036
                                            ]
                                        },
                                        "realTimeTransitDelay": 0,
                                        "sideOfStreet": "Unknown",
                                        "tollZone": "",
                                        "transitTerminus": "",
                                        "travelDistance": 0.401,
                                        "travelDuration": 65,
                                        "travelMode": "Driving"
                                    },
                                    {
                                        "compassDirection": "southwest",
                                        "details": [
                                            {
                                                "compassDegrees": 246,
                                                "endPathIndices": [
                                                    32
                                                ],
                                                "locationCodes": [
                                                    "114P11052",
                                                    "114N08827",
                                                    "114-08827",
                                                    "114-08828"
                                                ],
                                                "maneuverType": "RoadNameChange",
                                                "mode": "Driving",
                                                "names": [
                                                    "N 34th St"
                                                ],
                                                "roadType": "Arterial",
                                                "startPathIndices": [
                                                    28
                                                ]
                                            }
                                        ],
                                        "exit": "",
                                        "iconType": "Auto",
                                        "instruction": {
                                            "formattedText": null,
                                            "maneuverType": "RoadNameChange",
                                            "text": "Road name changes to N 34th St"
                                        },
                                        "isRealTimeTransit": false,
                                        "maneuverPoint": {
                                            "type": "Point",
                                            "coordinates": [
                                                47.64816,
                                                -122.33323
                                            ]
                                        },
                                        "realTimeTransitDelay": 0,
                                        "sideOfStreet": "Unknown",
                                        "tollZone": "",
                                        "transitTerminus": "",
                                        "travelDistance": 1.07,
                                        "travelDuration": 123,
                                        "travelMode": "Driving"
                                    },
                                    {
                                        "compassDirection": "north",
                                        "details": [
                                            {
                                                "endPathIndices": [
                                                    35
                                                ],
                                                "maneuverType": "TurnRight",
                                                "mode": "Driving",
                                                "names": [
                                                    "Troll Ave N"
                                                ],
                                                "roadType": "Street",
                                                "startPathIndices": [
                                                    32
                                                ]
                                            }
                                        ],
                                        "exit": "",
                                        "iconType": "Auto",
                                        "instruction": {
                                            "formattedText": null,
                                            "maneuverType": "TurnRight",
                                            "text": "Turn right onto Troll Ave N"
                                        },
                                        "isRealTimeTransit": false,
                                        "maneuverPoint": {
                                            "type": "Point",
                                            "coordinates": [
                                                47.64922,
                                                -122.3473
                                            ]
                                        },
                                        "realTimeTransitDelay": 0,
                                        "sideOfStreet": "Unknown",
                                        "tollZone": "",
                                        "transitTerminus": "",
                                        "travelDistance": 0.157,
                                        "travelDuration": 28,
                                        "travelMode": "Driving"
                                    },
                                    {
                                        "compassDirection": "north",
                                        "details": [
                                            {
                                                "endPathIndices": [
                                                    35
                                                ],
                                                "maneuverType": "ArriveFinish",
                                                "mode": "Driving",
                                                "names": [
                                                    "Troll Ave N"
                                                ],
                                                "roadType": "Street",
                                                "startPathIndices": [
                                                    35
                                                ]
                                            }
                                        ],
                                        "exit": "",
                                        "hints": [
                                            {
                                                "hintType": "PreviousIntersection",
                                                "text": "The last intersection is N 35th St"
                                            },
                                            {
                                                "hintType": "NextIntersection",
                                                "text": "If you reach N 36th St, you've gone too far"
                                            }
                                        ],
                                        "iconType": "Auto",
                                        "instruction": {
                                            "formattedText": null,
                                            "maneuverType": "ArriveIntermediateStop",
                                            "text": "Arrive at Troll Ave N, Seattle, WA 98103"
                                        },
                                        "isRealTimeTransit": false,
                                        "maneuverPoint": {
                                            "type": "Point",
                                            "coordinates": [
                                                47.65063,
                                                -122.3473
                                            ]
                                        },
                                        "realTimeTransitDelay": 0,
                                        "sideOfStreet": "Unknown",
                                        "tollZone": "",
                                        "transitTerminus": "",
                                        "travelDistance": 0,
                                        "travelDuration": 0,
                                        "travelMode": "Driving"
                                    }
                                ],
                                "routeRegion": "NAv2",
                                "routeSubLegs": [
                                    {
                                        "endWaypoint": {
                                            "type": "Point",
                                            "coordinates": [
                                                47.65063,
                                                -122.3473
                                            ],
                                            "description": "Troll Ave N, Seattle, WA 98103",
                                            "isVia": false,
                                            "locationIdentifier": "2|170|73|89|186|49|213|10|1|0|0|224|1|0|0|0|63|0|47.65063,-122.3473",
                                            "routePathIndex": 105
                                        },
                                        "startWaypoint": {
                                            "type": "Point",
                                            "coordinates": [
                                                47.651218,
                                                -122.303817
                                            ],
                                            "description": "3800 Montlake Blvd NE, Seattle, WA 98195",
                                            "isVia": false,
                                            "locationIdentifier": "2|170|73|89|186|65|166|45|1|0|0|224|1|160|226|67|62|0|47.651218,-122.303817",
                                            "routePathIndex": 70
                                        },
                                        "travelDistance": 4.124,
                                        "travelDuration": 557
                                    }
                                ],
                                "startLocation": {
                                    "bbox": [
                                        47.647339,
                                        -122.3114,
                                        47.655065,
                                        -122.29611
                                    ],
                                    "name": "3800 Montlake Blvd NE, Seattle, WA 98195",
                                    "point": {
                                        "type": "Point",
                                        "coordinates": [
                                            47.651202,
                                            -122.303755
                                        ]
                                    },
                                    "address": {
                                        "addressLine": "3800 Montlake Blvd NE",
                                        "adminDistrict": "WA",
                                        "adminDistrict2": "King County",
                                        "countryRegion": "United States",
                                        "formattedAddress": "3800 Montlake Blvd NE, Seattle, WA 98195",
                                        "locality": "Seattle",
                                        "postalCode": "98195"
                                    },
                                    "confidence": "High",
                                    "entityType": "Address",
                                    "geocodePoints": [
                                        {
                                            "type": "Point",
                                            "coordinates": [
                                                47.651202,
                                                -122.303755
                                            ],
                                            "calculationMethod": "InterpolationOffset",
                                            "usageTypes": [
                                                "Display"
                                            ]
                                        },
                                        {
                                            "type": "Point",
                                            "coordinates": [
                                                47.651218,
                                                -122.303817
                                            ],
                                            "calculationMethod": "Interpolation",
                                            "usageTypes": [
                                                "Route"
                                            ]
                                        }
                                    ],
                                    "matchCodes": [
                                        "Good"
                                    ]
                                },
                                "travelDistance": 4.124,
                                "travelDuration": 801
                            },
                            {
                                "actualEnd": {
                                    "type": "Point",
                                    "coordinates": [
                                        47.667744,
                                        -122.384961
                                    ]
                                },
                                "actualStart": {
                                    "type": "Point",
                                    "coordinates": [
                                        47.65063,
                                        -122.3473
                                    ]
                                },
                                "alternateVias": [],
                                "cost": 0,
                                "description": "Leary Way NW, NW Leary Way",
                                "endLocation": {
                                    "bbox": [
                                        47.663917,
                                        -122.392567,
                                        47.671642,
                                        -122.377272
                                    ],
                                    "name": "5400 Ballard Ave NW, Seattle, WA 98107",
                                    "point": {
                                        "type": "Point",
                                        "coordinates": [
                                            47.66778,
                                            -122.38492
                                        ]
                                    },
                                    "address": {
                                        "addressLine": "5400 Ballard Ave NW",
                                        "adminDistrict": "WA",
                                        "adminDistrict2": "King County",
                                        "countryRegion": "United States",
                                        "formattedAddress": "5400 Ballard Ave NW, Seattle, WA 98107",
                                        "locality": "Seattle",
                                        "postalCode": "98107"
                                    },
                                    "confidence": "High",
                                    "entityType": "Address",
                                    "geocodePoints": [
                                        {
                                            "type": "Point",
                                            "coordinates": [
                                                47.66778,
                                                -122.38492
                                            ],
                                            "calculationMethod": "InterpolationOffset",
                                            "usageTypes": [
                                                "Display"
                                            ]
                                        },
                                        {
                                            "type": "Point",
                                            "coordinates": [
                                                47.667744,
                                                -122.384961
                                            ],
                                            "calculationMethod": "Interpolation",
                                            "usageTypes": [
                                                "Route"
                                            ]
                                        }
                                    ],
                                    "matchCodes": [
                                        "Good"
                                    ]
                                },
                                "itineraryItems": [
                                    {
                                        "compassDirection": "south",
                                        "details": [
                                            {
                                                "compassDegrees": 180,
                                                "endPathIndices": [
                                                    2
                                                ],
                                                "maneuverType": "DepartStart",
                                                "mode": "Driving",
                                                "names": [
                                                    "Troll Ave N"
                                                ],
                                                "roadType": "Street",
                                                "startPathIndices": [
                                                    0
                                                ]
                                            }
                                        ],
                                        "exit": "",
                                        "iconType": "Auto",
                                        "instruction": {
                                            "formattedText": null,
                                            "maneuverType": "DepartIntermediateStop",
                                            "text": "Depart Troll Ave N toward N 35th St"
                                        },
                                        "isRealTimeTransit": false,
                                        "maneuverPoint": {
                                            "type": "Point",
                                            "coordinates": [
                                                47.65063,
                                                -122.3473
                                            ]
                                        },
                                        "realTimeTransitDelay": 0,
                                        "sideOfStreet": "Unknown",
                                        "tollZone": "",
                                        "towardsRoadName": "N 35th St",
                                        "transitTerminus": "",
                                        "travelDistance": 0.056,
                                        "travelDuration": 5,
                                        "travelMode": "Driving"
                                    },
                                    {
                                        "compassDirection": "west",
                                        "details": [
                                            {
                                                "compassDegrees": 278,
                                                "endPathIndices": [
                                                    4
                                                ],
                                                "locationCodes": [
                                                    "114-08853"
                                                ],
                                                "maneuverType": "TurnRight",
                                                "mode": "Driving",
                                                "names": [
                                                    "N 35th St"
                                                ],
                                                "roadType": "Arterial",
                                                "startPathIndices": [
                                                    2
                                                ]
                                            }
                                        ],
                                        "exit": "",
                                        "iconType": "Auto",
                                        "instruction": {
                                            "formattedText": null,
                                            "maneuverType": "TurnRight",
                                            "text": "Turn right onto N 35th St"
                                        },
                                        "isRealTimeTransit": false,
                                        "maneuverPoint": {
                                            "type": "Point",
                                            "coordinates": [
                                                47.65013,
                                                -122.3473
                                            ]
                                        },
                                        "realTimeTransitDelay": 0,
                                        "sideOfStreet": "Unknown",
                                        "tollZone": "",
                                        "transitTerminus": "",
                                        "travelDistance": 0.225,
                                        "travelDuration": 33,
                                        "travelMode": "Driving"
                                    },
                                    {
                                        "compassDirection": "northwest",
                                        "details": [
                                            {
                                                "compassDegrees": 305,
                                                "endPathIndices": [
                                                    6
                                                ],
                                                "maneuverType": "BearRight",
                                                "mode": "Driving",
                                                "names": [
                                                    "Fremont Pl N"
                                                ],
                                                "roadType": "Arterial",
                                                "startPathIndices": [
                                                    4
                                                ]
                                            }
                                        ],
                                        "exit": "",
                                        "iconType": "Auto",
                                        "instruction": {
                                            "formattedText": null,
                                            "maneuverType": "BearRight",
                                            "text": "Bear right onto Fremont Pl N"
                                        },
                                        "isRealTimeTransit": false,
                                        "maneuverPoint": {
                                            "type": "Point",
                                            "coordinates": [
                                                47.65062,
                                                -122.35023
                                            ]
                                        },
                                        "realTimeTransitDelay": 0,
                                        "sideOfStreet": "Unknown",
                                        "tollZone": "",
                                        "transitTerminus": "",
                                        "travelDistance": 0.12,
                                        "travelDuration": 13,
                                        "travelMode": "Driving"
                                    },
                                    {
                                        "compassDirection": "northwest",
                                        "details": [
                                            {
                                                "compassDegrees": 298,
                                                "endPathIndices": [
                                                    8
                                                ],
                                                "locationCodes": [
                                                    "114N08862",
                                                    "114-08862"
                                                ],
                                                "maneuverType": "KeepStraight",
                                                "mode": "Driving",
                                                "names": [
                                                    "N 36th St"
                                                ],
                                                "roadType": "Arterial",
                                                "startPathIndices": [
                                                    6
                                                ]
                                            }
                                        ],
                                        "exit": "",
                                        "iconType": "Auto",
                                        "instruction": {
                                            "formattedText": null,
                                            "maneuverType": "KeepStraight",
                                            "text": "Keep straight onto N 36th St"
                                        },
                                        "isRealTimeTransit": false,
                                        "maneuverPoint": {
                                            "type": "Point",
                                            "coordinates": [
                                                47.65141,
                                                -122.35132
                                            ]
                                        },
                                        "realTimeTransitDelay": 0,
                                        "sideOfStreet": "Unknown",
                                        "tollZone": "",
                                        "transitTerminus": "",
                                        "travelDistance": 0.505,
                                        "travelDuration": 61,
                                        "travelMode": "Driving"
                                    },
                                    {
                                        "compassDirection": "west",
                                        "details": [
                                            {
                                                "compassDegrees": 282,
                                                "endPathIndices": [
                                                    11
                                                ],
                                                "locationCodes": [
                                                    "114-08862",
                                                    "114N08863"
                                                ],
                                                "maneuverType": "RoadNameChange",
                                                "mode": "Driving",
                                                "names": [
                                                    "NW 36th St"
                                                ],
                                                "roadType": "Arterial",
                                                "startPathIndices": [
                                                    8
                                                ]
                                            }
                                        ],
                                        "exit": "",
                                        "iconType": "Auto",
                                        "instruction": {
                                            "formattedText": null,
                                            "maneuverType": "RoadNameChange",
                                            "text": "Road name changes to NW 36th St"
                                        },
                                        "isRealTimeTransit": false,
                                        "maneuverPoint": {
                                            "type": "Point",
                                            "coordinates": [
                                                47.65296,
                                                -122.35766
                                            ]
                                        },
                                        "realTimeTransitDelay": 0,
                                        "sideOfStreet": "Unknown",
                                        "tollZone": "",
                                        "transitTerminus": "",
                                        "travelDistance": 0.135,
                                        "travelDuration": 16,
                                        "travelMode": "Driving"
                                    },
                                    {
                                        "compassDirection": "northwest",
                                        "details": [
                                            {
                                                "compassDegrees": 303,
                                                "endPathIndices": [
                                                    14
                                                ],
                                                "locationCodes": [
                                                    "114N10637",
                                                    "114-10637",
                                                    "114N10638",
                                                    "114-10638"
                                                ],
                                                "maneuverType": "KeepStraight",
                                                "mode": "Driving",
                                                "names": [
                                                    "Leary Way NW"
                                                ],
                                                "roadType": "Arterial",
                                                "startPathIndices": [
                                                    11
                                                ]
                                            }
                                        ],
                                        "exit": "",
                                        "iconType": "Auto",
                                        "instruction": {
                                            "formattedText": null,
                                            "maneuverType": "KeepStraight",
                                            "text": "Keep straight onto Leary Way NW"
                                        },
                                        "isRealTimeTransit": false,
                                        "maneuverPoint": {
                                            "type": "Point",
                                            "coordinates": [
                                                47.65343,
                                                -122.35931
                                            ]
                                        },
                                        "realTimeTransitDelay": 0,
                                        "sideOfStreet": "Unknown",
                                        "tollZone": "",
                                        "transitTerminus": "",
                                        "travelDistance": 1.365,
                                        "travelDuration": 161,
                                        "travelMode": "Driving"
                                    },
                                    {
                                        "compassDirection": "west",
                                        "details": [
                                            {
                                                "compassDegrees": 284,
                                                "endPathIndices": [
                                                    16
                                                ],
                                                "locationCodes": [
                                                    "114-10638",
                                                    "114N10639",
                                                    "114-10639"
                                                ],
                                                "maneuverType": "RoadNameChange",
                                                "mode": "Driving",
                                                "names": [
                                                    "NW Leary Way"
                                                ],
                                                "roadType": "Arterial",
                                                "startPathIndices": [
                                                    14
                                                ]
                                            }
                                        ],
                                        "exit": "",
                                        "iconType": "Auto",
                                        "instruction": {
                                            "formattedText": null,
                                            "maneuverType": "RoadNameChange",
                                            "text": "Road name changes to NW Leary Way"
                                        },
                                        "isRealTimeTransit": false,
                                        "maneuverPoint": {
                                            "type": "Point",
                                            "coordinates": [
                                                47.66355,
                                                -122.36952
                                            ]
                                        },
                                        "realTimeTransitDelay": 0,
                                        "sideOfStreet": "Unknown",
                                        "tollZone": "",
                                        "transitTerminus": "",
                                        "travelDistance": 0.652,
                                        "travelDuration": 93,
                                        "travelMode": "Driving"
                                    },
                                    {
                                        "compassDirection": "west",
                                        "details": [
                                            {
                                                "compassDegrees": 285,
                                                "endPathIndices": [
                                                    19
                                                ],
                                                "locationCodes": [
                                                    "114-10639"
                                                ],
                                                "maneuverType": "KeepStraight",
                                                "mode": "Driving",
                                                "names": [
                                                    "Leary Ave NW"
                                                ],
                                                "roadType": "Arterial",
                                                "startPathIndices": [
                                                    16
                                                ]
                                            }
                                        ],
                                        "exit": "",
                                        "iconType": "Auto",
                                        "instruction": {
                                            "formattedText": null,
                                            "maneuverType": "KeepStraight",
                                            "text": "Keep straight onto Leary Ave NW"
                                        },
                                        "isRealTimeTransit": false,
                                        "maneuverPoint": {
                                            "type": "Point",
                                            "coordinates": [
                                                47.66369,
                                                -122.37821
                                            ]
                                        },
                                        "realTimeTransitDelay": 0,
                                        "sideOfStreet": "Unknown",
                                        "tollZone": "",
                                        "transitTerminus": "",
                                        "travelDistance": 0.474,
                                        "travelDuration": 56,
                                        "travelMode": "Driving"
                                    },
                                    {
                                        "compassDirection": "southwest",
                                        "details": [
                                            {
                                                "compassDegrees": 242,
                                                "endPathIndices": [
                                                    21
                                                ],
                                                "maneuverType": "TurnLeft",
                                                "mode": "Driving",
                                                "names": [
                                                    "NW Vernon Pl"
                                                ],
                                                "roadType": "Street",
                                                "startPathIndices": [
                                                    19
                                                ]
                                            }
                                        ],
                                        "exit": "",
                                        "iconType": "Auto",
                                        "instruction": {
                                            "formattedText": null,
                                            "maneuverType": "TurnLeft",
                                            "text": "Turn left onto NW Vernon Pl"
                                        },
                                        "isRealTimeTransit": false,
                                        "maneuverPoint": {
                                            "type": "Point",
                                            "coordinates": [
                                                47.66686,
                                                -122.38238
                                            ]
                                        },
                                        "realTimeTransitDelay": 0,
                                        "sideOfStreet": "Unknown",
                                        "tollZone": "",
                                        "transitTerminus": "",
                                        "travelDistance": 0.081,
                                        "travelDuration": 30,
                                        "travelMode": "Driving"
                                    },
                                    {
                                        "compassDirection": "northwest",
                                        "details": [
                                            {
                                                "compassDegrees": 310,
                                                "endPathIndices": [
                                                    24
                                                ],
                                                "maneuverType": "TurnRight",
                                                "mode": "Driving",
                                                "names": [
                                                    "Ballard Ave NW"
                                                ],
                                                "roadType": "Street",
                                                "startPathIndices": [
                                                    21
                                                ]
                                            }
                                        ],
                                        "exit": "",
                                        "iconType": "Auto",
                                        "instruction": {
                                            "formattedText": null,
                                            "maneuverType": "TurnRight",
                                            "text": "Turn right onto Ballard Ave NW"
                                        },
                                        "isRealTimeTransit": false,
                                        "maneuverPoint": {
                                            "type": "Point",
                                            "coordinates": [
                                                47.66642,
                                                -122.38323
                                            ]
                                        },
                                        "realTimeTransitDelay": 0,
                                        "sideOfStreet": "Unknown",
                                        "tollZone": "",
                                        "transitTerminus": "",
                                        "travelDistance": 0.197,
                                        "travelDuration": 32,
                                        "travelMode": "Driving"
                                    },
                                    {
                                        "compassDirection": "northwest",
                                        "details": [
                                            {
                                                "compassDegrees": 297,
                                                "endPathIndices": [
                                                    24
                                                ],
                                                "maneuverType": "ArriveFinish",
                                                "mode": "Driving",
                                                "names": [
                                                    "Ballard Ave NW"
                                                ],
                                                "roadType": "Street",
                                                "startPathIndices": [
                                                    24
                                                ]
                                            }
                                        ],
                                        "exit": "",
                                        "hints": [
                                            {
                                                "hintType": "PreviousIntersection",
                                                "text": "The last intersection is 22nd Ave NW"
                                            },
                                            {
                                                "hintType": "NextIntersection",
                                                "text": "If you reach NW Market St, you've gone too far"
                                            }
                                        ],
                                        "iconType": "Auto",
                                        "instruction": {
                                            "formattedText": null,
                                            "maneuverType": "ArriveFinish",
                                            "text": "Arrive at 5400 Ballard Ave NW, Seattle, WA 98107"
                                        },
                                        "isRealTimeTransit": false,
                                        "maneuverPoint": {
                                            "type": "Point",
                                            "coordinates": [
                                                47.667744,
                                                -122.384961
                                            ]
                                        },
                                        "realTimeTransitDelay": 0,
                                        "sideOfStreet": "Unknown",
                                        "tollZone": "",
                                        "transitTerminus": "",
                                        "travelDistance": 0,
                                        "travelDuration": 0,
                                        "travelMode": "Driving"
                                    }
                                ],
                                "routeRegion": "NAv2",
                                "routeSubLegs": [
                                    {
                                        "endWaypoint": {
                                            "type": "Point",
                                            "coordinates": [
                                                47.667744,
                                                -122.384961
                                            ],
                                            "description": "5400 Ballard Ave NW, Seattle, WA 98107",
                                            "isVia": false,
                                            "locationIdentifier": "2|170|73|89|186|33|245|9|1|0|0|224|1|39|79|163|62|0|47.667744,-122.384961",
                                            "routePathIndex": 129
                                        },
                                        "startWaypoint": {
                                            "type": "Point",
                                            "coordinates": [
                                                47.65063,
                                                -122.3473
                                            ],
                                            "description": "Troll Ave N, Seattle, WA 98103",
                                            "isVia": false,
                                            "locationIdentifier": "2|170|73|89|186|49|213|10|1|0|0|224|1|0|0|0|63|0|47.65063,-122.3473",
                                            "routePathIndex": 105
                                        },
                                        "travelDistance": 3.81,
                                        "travelDuration": 506
                                    }
                                ],
                                "startLocation": {
                                    "bbox": [
                                        47.602817,
                                        -122.340298,
                                        47.610543,
                                        -122.325022
                                    ],
                                    "name": "1000 4th Ave, Seattle, WA 98104",
                                    "point": {
                                        "type": "Point",
                                        "coordinates": [
                                            47.60668,
                                            -122.33266
                                        ]
                                    },
                                    "address": {
                                        "addressLine": "1000 4th Ave",
                                        "adminDistrict": "WA",
                                        "adminDistrict2": "King County",
                                        "countryRegion": "United States",
                                        "formattedAddress": "1000 4th Ave, Seattle, WA 98104",
                                        "locality": "Seattle",
                                        "postalCode": "98104"
                                    },
                                    "confidence": "High",
                                    "entityType": "Address",
                                    "geocodePoints": [
                                        {
                                            "type": "Point",
                                            "coordinates": [
                                                47.60668,
                                                -122.33266
                                            ],
                                            "calculationMethod": "Rooftop",
                                            "usageTypes": [
                                                "Display"
                                            ]
                                        },
                                        {
                                            "type": "Point",
                                            "coordinates": [
                                                47.606425,
                                                -122.333233
                                            ],
                                            "calculationMethod": "Rooftop",
                                            "usageTypes": [
                                                "Route"
                                            ]
                                        }
                                    ],
                                    "matchCodes": [
                                        "Good"
                                    ]
                                },
                                "travelDistance": 3.81,
                                "travelDuration": 693
                            }
                        ],
                        "trafficCongestion": "Heavy",
                        "trafficDataUsed": "Flow",
                        "travelDistance": 15.8,
                        "travelDuration": 1745,
                        "travelDurationTraffic": 2992,
                        "waypointsOrder": [
                            "wp.0",
                            "wp.3",
                            "wp.2",
                            "wp.1",
                            "wp.4"
                        ]
                    }
                ]
            }
        ],
        "statusCode": 200,
        "statusDescription": "OK",
        "traceId": "0ad87264ede548959b9293add5c4a692|CO3C4CD6C0|7.7.0.0|CO40110138, CO40070716, CO40070801|Ref A: 2F727259D61946948479FDFAD2A915C1 Ref B: CH1EDGE1013 Ref C: 2018-07-17T23:09:49Z|Ref A: 20F9452DC134427AB109C4B4B4076091 Ref B: CH1EDGE0112 Ref C: 2018-07-17T23:09:49Z|Ref A: E479DC0DC18C4EC0A746A65106131C7D Ref B: CH1EDGE0919 Ref C: 2018-07-17T23:09:49Z|Ref A: 610B31AAC6FF4C82909DCCF85AEE313D Ref B: CH1EDGE0915 Ref C: 2018-07-17T23:09:49Z|Ref A: 02CA46D22BB74FA0AC667D89D1A4C0FD Ref B: CH1EDGE1010 Ref C: 2018-07-17T23:09:49Z"
    }
```    

## See Also

[Using the REST Services with .NET](https://msdn.microsoft.com/en-us/library/jj819168\(v=msdn.10\))  
[JSON Data Contracts](https://msdn.microsoft.com/en-us/library/jj870778\(v=msdn.10\))
