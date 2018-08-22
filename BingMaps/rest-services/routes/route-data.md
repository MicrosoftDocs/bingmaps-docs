---
title: "Route Data | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: d0cff67e-eef0-4ea5-af1b-24d78347bd5a
caps.latest.revision: 8
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Route Data

The response returned by Routes URL contains a Route resource. The information provided in the Route resource includes the route distance, the travel time, and the itinerary details for each route leg. A route leg is a section of the route defined by two waypoints, and it provides a set of route steps to follow. A route step includes instructions, as well as further details (warnings and hints) about the route, when available. When a route path is requested by setting the *routeAttributes* parameter to *routePath* in the request, the Route resource also provides a set of Point (latitude and longitude) values for each route leg. The following tables provide the descriptions of the Route resource fields, followed by XML and JSON examples.  
  
[!INCLUDE [get-common-response-note](../../includes/get-common-response-note.md)]
  
## Route Resource

The following tables describe the fields in the Route resource in a hierarchical manner.  
  
> [!WARNING]
>  Any fields that are returned in the response and that are not in these tables are not supported.  
  
 A route has the following basic structure:  
  
-   Route [one or more]  
  
    -   RouteLeg [For each set of waypoints]  
  
        -   RouteSubLeg [For a set of route leg waypoints and any via-waypoints]  
  
        -   ItineraryItem [one or more route leg steps]  
  
            -   Detail [one or more set of detailed instructions for a route step]  
  
    -   RoutePath [when requested]  
  
### Top-level Route Resource Fields

The following fields are the top-level fields in the Routes resource. Additional tables describe the fields in each of the collections.  
  
|JSON|XML|Type|Description|  
|----------|---------|----------|-----------------|  
|id|Id|string|A unique ID for the resource.|  
|bbox|BoundingBox|Array of Numbers|Defines a rectangular area by using latitude and longitude boundaries that contain the corresponding route or location. A bounding box contains SouthLatitude, WestLongitude, NorthLatitude, and EastLongitude elements.|  
|distanceUnit|DistanceUnit|string|The unit used for distance.|  
|durationUnit|DurationUnit|string|The unit used for time of travel.|  
|travelDistance|TravelDistance|double|The physical distance covered by the entire route. **Note:**  This value is not supported for the Transit travel mode.|  
|travelDuration|TravelDuration|double|The time that it takes, in seconds, to travel a corresponding TravelDistance.|  
|travelDurationTraffic|TravelDurationTraffic|double|The time that it takes, in seconds, to travel a corresponding TravelDistance with current traffic conditions.<br /><br /> This value is always provided for the complete route and does not depend on the availability of traffic information.|  
|routeLegs|RouteLeg|collection|Information about a section of a route between two waypoints. For more information about the fields contained ina  routeLeg, see the Route Leg Fields section below.|  
|routePath|RoutePath|Complex object|A representation of the path of a route. A RoutePath is defined by a Line element that contains of a collection of latitude and longitude points. The path of the route is the line that connects these points. For more information about the fields contained in a route Path, see the **Route Path Fields** section below. A RoutePath is returned only if one of the following parameters is set in the request.<br /><br /> -   routeAttributes=routePath [recommended]<br />-   routePathOutput=Points|  
|__type||String|This field tells you the version of REST API being used. This data field should not have any effect on your application's handling of the response.|  
  
### Route Leg Fields  

These fields are specific to the RouteLeg collection in the Route resource.  
  
|JSON|XML|Type|Description|  
|----------|---------|----------|-----------------|  
|alternateVias||Array of String|This is meant for identifying separate routes when the parameter maxSolutions is used to show more than one route.|  
|cost||Integer||  
|travelDistance|TravelDistance|double|The physical distance covered by a route leg.|  
|travelDuration|TravelDuration|double|The time that it takes, in seconds, to travel a corresponding TravelDistance.|  
|description|Description|street|A short description of the route.|  
|actualStart|ActualStart|Point. For more information about the Point type, see [Location and Area Types](../common-parameters-and-types/location-and-area-types.md).|The Point (latitude and longitude) that was used as the actual starting location for the route leg. In most cases, the ActualStart is the same as the requested waypoint. However, if a waypoint is not close to a road, the Routes API chooses a location on the nearest road as the starting point of the route. This ActualStart element contains the latitude and longitude of this new location.|  
|actualEnd|ActualEnd|Point. For more information about the Point type, see [Location and Area Types](../common-parameters-and-types/location-and-area-types.md).|The Point (latitude and longitude) that was used as the actual ending location for the route leg. In most cases, the ActualEnd is the same as the requested waypoint. However, if a waypoint is not close to a road, the Routes API chooses a location on the nearest road as the ending point of the route. This ActualEnd element contains the latitude and longitude of this new location.|  
|startLocation|StartLocation|Complex object|Information about the location of the starting waypoint for a route. A StartLocation is provided only when the waypoint is specified as a landmark or an address. For more information about the fields contained in a Location collection, see the Location Fields table below.|  
|endLocation|EndLocation|Complex object|Information about the location of the endinpoint for a route. An EndLocation is provided only when the waypoint is specified as a landmark or an address. For more information about the fields contained in a Location collection, see the Locations Fields table below.|  
|startTime||String|Used for transit route responses. Shows the starting time for the starting point of the route. This tells you when to be at the starting waypoint depending on what you select as the dateTime and the timeType. **Important:**  The transit API expects the user to provide start time, end time parameters in the local timezone of the region they are querying. The underlying API also uses data in the local timezone of that region. The API does not need to know and does not return the exact timezone of the region. Therefore any datetime values in transit API response are also in the local timezone of the region where the transit agency operates.|  
|endTime||String|Used for transit route responses. Shows the time of arrival when specific route is taken. This tells you when to be at the ending waypoint depending on what you select as the dateTime and the timeType parameters **Important:**  The transit API expects the user to provide start time, end time parameters in the local timezone of the region they are querying. The underlying API also uses data in the local timezone of that region. The API does not need to know and does not return the exact timezone of the region. Therefore any datetime values in transit API response are also in the local timezone of the region where the transit agency operates.|  
|routeSubLegs|RouteSubLeg|collection|Information about a segments of the route leg defined by the route leg waypoints and any intermediate via-waypoints. For example, if the route leg has two via-waypoints in addition to start and end waypoints, there would be three (3) route sub-legs. For information about the fields that make up a sub-leg, see the Route Sub-Leg fields table below.|  
|itineraryItem|ItineraryItem|collection|Information that defines a step in the route. For information about the fields that make up the ItineraryItem collection, see the Itinerary Item Fields table below.|  
  
 **Route Sub-Leg Fields**  
  
|JSON|XML|Type|Description|  
|----------|---------|----------|-----------------|  
|travelDistance|TravelDistance|double|The physical distance covered by the sub-leg. The units are defined by the DistanceUnit field.|  
|travelDuration|TravelDuration|integer|The time, in seconds, that it takes to travel the corresponding TravelDistance.|  
|StartWaypoint, EndWaypoint|startWaypoint, endWaypoint|collection|Information about the start and end waypoints of the route sub-leg. See the **Waypoint Fields** table below for a list of the values.|  
  
 **Waypoint Fields**  
  
 These fields are found within the StartWaypoint and EndWaypoint collections of a RouteSubLeg.  
  
|JSON|XML|Type|Description|  
|----------|---------|----------|-----------------|  
|Point|Latitude,Longitude|[Point](../common-parameters-and-types/location-and-area-types.md)|The latitude and longitude coordinates of the waypoint.|  
|Description|Description|string|A short description identifying the waypoint.|  
|isVia|IsVia|Boolean|A value of true indicates that this is a via-waypoint.|  
|routepathIndex|RoutePathIndex|integer|Specifies the route path point associated with the waypoint. You can get a list of route path points by setting the `routeAttributes` parameter to `routePath`.|  
  
 **Location Fields**  
  
 These fields are found in the StartLocation and EndLocation collections.  
  
|JSON|XML|Type|Description|  
|----------|---------|----------|-----------------|  
|name|Name|string|The name of a location, such as San Francisco, CA.|  
|point|Point|Point. For more information about the Point type, see [Location and Area Types](../common-parameters-and-types/location-and-area-types.md).|The coordinates of a point on the Earth. A point contains Latitude and Longitude elements. This point is also included in the geocode points collection.|  
|geocodePoints|GeocodePoint|collection|A collection of geocoded points that differ in how they were calculated and their suggested use. For a description of the points in this collection, see the **Geocode Point Fields** section below.|  
|bbox|BoundingBox|Array of Numbers|Defines a rectangular area by using latitude and longitude boundaries that contain the corresponding route or location. A bounding box contains SouthLatitude, WestLongitude, NorthLatitude, and EastLongitude elements.|  
|entityType|EntityType|string|A type of location. Examples include PopulatedPlace and Monument.|  
|address|Address|Address|The postal address of a location. An Address can contain AddressLine, AdminDistrict, AdminDistrict2, CountryRegion, FormattedAddress, Locality, and PostalCode elements.|  
|confidence|Confidence|One of the following values:<br /><br /> High, Medium, Low, Unknown|The confidence of the match.|  
|matchCodes|MatchCode|One or more of the following values: Good, Ambiguous, UpHierarchy|A collection of match code values that represent the geocoding level for each location in the response. The possible values are:<br /><br /> **Good**: The location has only one match.<br /><br /> **Ambiguous**: The location is one of a set of possible matches. For example, when you query for the street address 128 Main St., the response may return two locations for 128 North Main St. and 128 South Main St. because there is not enough information to determine which option to choose.<br /><br /> **UpHierarchy**: The location represents a move up the geographic hierarchy. This occurs when a match for the location request was not found, so a less precise result is returned. For example, if a match for the requested address cannot be found, then a match code of UpHierarchy with a postal code may be returned.|  
  
 **Geocode Point Fields**  
  
 The following fields are provided for each geocode point in the Geocode Points collection.  
  
|JSON|XML|Type|Description|  
|----------|---------|----------|-----------------|  
|point|Point|Point. For more information about the Point type, see [Location and Area Types](../common-parameters-and-types/location-and-area-types.md).|The latitude and longitude coordinates of the geocode point.|  
|calculationMethod|CalculationMethod|One of the following values:<br /><br /> -   Interpolation: The geocode point was matched to a point on a road using interpolation.<br />-   InterpolationOffset: The geocode point was matched to a point on a road using interpolation with an additional offset to shift the point to the side of the street.<br />-   ParcelCentroid: The geocode point was matched to the center of a parcel.<br />-   Rooftop: The geocode point was matched to the rooftop of a building.|The method that was used to compute the geocode point.|  
|coordinates||Array of Numbers|A set of "Latitude, Longitude" coordinates|  
|type||String|Describes what the coordinates within the corresponding field represent.|  
|usageTypes|usageType|One or more of the following values:<br /><br /> -   Display<br />-   Route|The best use for the geocode point.<br /><br /> Each geocode point is defined as a Route point, a Display point or both.<br /><br /> Use Route points if you are creating a route to the location. Use Display points if you are showing the location on a map. For example, if the location is a park, a Route point may specify an entrance to the park where you can enter with a car, and a Display point may be a point that specifies the center of the park.|  
  
 **Itinerary Item Fields**  
  
 These fields are found in the ItineraryItem collection. Each itinerary item provides information about a route step.  
  
|JSON|XML|Type|Description|  
|----------|---------|----------|-----------------|  
|childItineraryItems|ChildItineraryItems|collection|A collection of ItineraryItems that divides an itinerary item into smaller steps. An itinerary item can have only one set of ChildItineraryItems.|  
|compassDirection|CompassDirection|string|The direction of travel associated with a maneuver on a route, such as south or southwest. **Note:**  This value is not supported for the Transit travel mode.|  
|details|Detail|collection|Information about one of the maneuvers that is part of the itinerary item. An ItineraryItem can contain more than one Detail collection. For information about the fields contained in a Detail collection, see the Detail Fields table below.|  
|exit|Exit|string|The name or number of the exit associated with this itinerary step.|  
|hints|Hint|string|Additional information that may be helpful in following a route. In addition to the hint text, this element has an attribute hintType that specifies what the hint refers to, such as “NextIntersection.” Hint is an optional element and a route step can contain more than one hint.|  
|iconType|IconType|string|The type of icon to display.<br /><br /> Possible values include:<br /><br /> -   None<br />-   Airline<br />-   Auto<br />-   Bus<br />-   Ferry<br />-   Train<br />-   Walk<br />-   Other|  
|instruction|Instruction|string|A description of a maneuver in a set of directions.<br /><br /> **[XML]**<br /><br /> The content of this field represents the plain text description. It also has an attribute "maneuverType" that is set to the type of maneuver, such as “TurnLeft.”<br /><br /> **[JSON]**<br /><br /> -   **text**: The plain text description of the instruction<br />-   **maneuverType**: The textual representation of the maneuver.|  
|maneuverPoint|ManeuverPoint|Point. For more information about the Point type, see [Location and Area Types](../common-parameters-and-types/location-and-area-types.md).|The coordinates of a point on the Earth where a maneuver is required, such as a left turn. A ManeuverPoint contains Latitude and Longitude elements. **Note:**  This value is not supported for ItineraryItems that are part of a ChildItineraryItems collection.|  
|sideOfStreet|SideOfStreet|string|The side of the street where the destination is found based on the arrival direction. This field applies to the last itinerary item only.<br /><br /> Possible values include:<br /><br /> -   Left<br />-   Right<br />-   Unknown|  
|signs|Sign|string|Signage text for the route. There may be more than one sign value for an itinerary item.|  
|time|Time|DateTime|The arrival or departure time for the transit step.<br /><br /> **Examples**:<br /><br /> XML: 2011-10-7T9:37:47<br /><br /> JSON: 1318005467000-0700<br /><br /> The JSON response returns departure and arrival times as DateTime strings, such as `1318005467000-0700`. The first integer in the string (1318005467000) represents the number of seconds since 12:00:00 midnight, January 1, 1970 UTC. The remainder of the string (-0700) represents an offset in hours that you must apply to get the local time. For example, the integer 1318005467000 represents the time '10/7/2011 4:37:47 PM'. When you apply the -0700 offset, you compute the local time as '10/7/2011 9:37:47 AM'. For more information, see [DateTime Structure](http://msdn.microsoft.com/en-us/library/system.datetime.aspx).|  
|tollZone|tollZone|string|The name or number of the toll zone.|  
|towardsRoadName|TowardsRoadName|string|The name of the street that the route goes towards in the first itinerary item.|  
|transitLine|TransitLine|collection|Information about the transit line associated with the itinerary item. For more information about the fields contained in the TransitLine collection, see the Transit Line Fields table below.|  
|transitStopId|TransitStopId|string|The ID assigned to the transit stop by the transit agency.|  
|transitTerminus|TransitTerminus|string|The end destination for the transit line in the direction you are traveling.|  
|travelDistance|TravelDistance|double|The physical distance covered by this route step. **Note:**  This value is not supported for the Transit travel mode.|  
|travelDuration|TravelDuration|double|The time that it takes, in seconds, to travel a corresponding TravelDistance.|  
|travelMode|TravelMode|string|The mode of travel for a specific step in the route. **Note:**  This value is not supported for ItineraryItems that are part of a ChildItineraryItems collection.|  
|warnings|Warning|string|Information about a condition that may affect a specific step in the route. Warning is an optional element and a route step can contain more than one warning. Warnings can include traffic incident information such as congestion, accident and blocked road reports.<br /><br /> Warning elements are further defined by two attributes: Severity and WarningType.<br /><br /> Severity can have the following values: Low Impact, Minor, Moderate, or Serious.<br /><br /> See [Warning Types](warning-types.md) for a list of warning types.|  
  
 **Detail Fields**  
  
|JSON|XML|Type|Description|  
|----------|---------|----------|-----------------|  
|compassDegrees|CompassDegrees|Number|The direction in degrees. **Note:**  This value is not supported for the Transit travel mode.|  
|maneuverType|ManeuverType|string|The type of maneuver described by this detail collection. The ManeuverType in A detail collection can provide information for a portion of the maneuver described by the maneuverType attribute of the corresponding Instruction. For example the maneuverType attribute of an Instruction may specify TurnLeftThenTurnRight as the maneuver while the associated detail items may specify specifics about the TurnLeft and TurnRight maneuvers.<br /><br /> For a list of maneuver types, see [Maneuver Types](maneuver-types.md).|  
|mode||String|Describes the mode of transportation used between a pair of indexes. This can differ depending whether the route requires walking, driving, or transit. **Tip:**  Not all regions or cultures support all values of this field. If you use a value that is not supported, the end user may receive an error message. If you are unsure which markets the URL will be used in, it is recommended to not use this parameter.  Without the “mode” parameter, Bing Maps will silently fall to a default value of **Transit**.|  
|names|Name|string|A street, highway or intersection where the maneuver occurs. If the maneuver is complex, there may be more than one name field in the details collection. The name field may also have no value. This can occur if the name is not known or if a street, highway or intersection does not have a name. **Note:**  This value is only supported for the transit travel mode.|  
|startPathIndices<br /><br /> endPathIndices|StartPathIndex<br /><br /> EndPathIndex|Array of Numbers|These fields specify index values for specific route path points that are returned in the response when a route path is returned. Together, these two index values define a range of route path points that correspond to a maneuver. Route path index values are integers where the first route path point has an index value of 0.|  
|roadType|RoadType|string|The type of road.|  
|locationCode|LocationCode|Array of strings|A traffic location code. Each location code provides traffic incident information for pre-defined road segments. There may be multiple codes for each Detail collection in the response. A subscription is typically required to be able to interpret these codes for a geographical area or country.|  
  
 **Transit Line Fields**  
  
|JSON|XML|Type|Description|  
|----------|---------|----------|-----------------|  
|verboseName|VerboseName|string|The full name of the transit line.|  
|abbreviatedName|AbbreviatedName|string|The abbreviated name of the transit line, such as the bus number.|  
|AgencyId|AgencyId|integer|The ID associated with the transit agency.|  
|agencyName|AgencyName|string|The name of the transit agency.|  
|lineColor|LineColor|integer|The color associated with the transit line. The color is provided as an RGB value.|  
|lineTextColor|LineTextColor|integer|The color to use for text associated with the transit line. The color is provided as an RGB value.|  
|uri|Uri|string|The URI for the transit agency.|  
|phoneNumber|PhoneNumber|string|The phone number of the transit agency.|  
|providerInfo|ProviderInfo|string|The contact information for the provider of the transit information.|  
  
### Route Path Fields  
 A RoutePath is included in the response when one of following parameters is set in the request. Of the route path options, the routeAttributes method is the newest and the recommended way to request a route path. The routeAttributes parameter can also take other values (see [Calculate a Route](calculate-a-route.md)),and when it is set, the routePathOutput parameter is ignored. Therefore, of these two options, it is best to use the routeAttributes parameter.  
  
1.  routeAttributes=routePath [recommended]  
  
2.  routePathOutput=Points  
  
 When tolerances are specified in the request, subsets of these points called route path generalizations are provided that can be used to represent the route on maps that do not need the accuracy of the complete set of points.  
  
|JSON|XML|Type|Description|  
|----------|---------|----------|-----------------|  
|line|Line|A Complex object|A collection of point (latitude and longitude) elements. When the points in the line are connected, they represent the path of the route. **Note:**  Coordinates is an array of array of numbers rather than an array|  
|point|Point|Point. For more information about the point type, see [Location and Area Types](../common-parameters-and-types/location-and-area-types.md).|The coordinates of a point on the Earth. A point contains Latitude and Longitude elements.|  
|generalizations|RoutePathGeneralization|collection|A generalization is a collection of index elements and a latlongtolerance element specifying a subset of route points that satisfy the tolerance.|  
|pathIndices|Index|integer|Specifies a subset of points from the complete set of route path points (line collection) to include in the RoutePathGeneralization. The list of point values in the route path line collection are given indices starting with 0. For example, an index value of 0 indicates that the first point in the Line collection is included in this RoutePathGeneralization.|  
|latLongTolerance|LatLongTolerance|integer|The tolerance specified in the route request that is associated with the RoutePathGeneralization.|  
  
## Examples

 See the following topics for response examples.  
  
-   [Walking Route Example](../examples/walking-route-example.md)  
  
-   [Driving Route Example](../examples/driving-route-example.md)  
  
-   [Transit Route Example](../examples/transit-route-example.md)  
  
-   [Driving Route with Route Path Example](../examples/driving-route-with-route-path-example.md)  
  
-   [Driving Route using Tolerances Example](../examples/driving-route-using-tolerances-example.md)
