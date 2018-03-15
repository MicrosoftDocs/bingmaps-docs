---
title: "Warning Types | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: fa146e18-716a-49b7-88b3-17f78e617245
caps.latest.revision: 6
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Warning Types
The following warning type values are used to set the warningType attribute that is returned with warning text by the [Routes](../rest-services/routes-api.md) when there is a potential issue along a route segment. For more information about warnings and other information returned in the Routes API response, see [Route Data](../rest-services/route-data.md).  
  
|Warning Type|Description|  
|------------------|-----------------|  
|Accident|There is a traffic accident.|  
|AdminDivisionChange|The route has left one administrative division and entered another.|  
|BlockedRoad|The road is closed or blocked.|  
|CheckTimetable|Check a time table. This usually refers to a ferry or Autorail time table.|  
|Congestion|The traffic is slow.|  
|CountryChange|The route has left one country and entered another.|  
|DisabledVehicle|There is a disabled vehicle.|  
|GateAccess|A gate blocks the road and access is required to continue along the route.|  
|GetOffTransit|Get off the transit at this location.|  
|GetOnTransit|Get on the transit at this location.|  
|IllegalUTurn|A U-turn is illegal at this location.|  
|MassTransit|There is mass transit incident.|  
|Miscellaneous|A miscellaneous warning is available for this location.|  
|NoIncident|There is no incident at this location.|  
|None|There is no warning at this location.|  
|Other|There is a warning at this location that cannot be classified as any other type of warning.|  
|OtherNews|There is additional traffic incident information.|  
|OtherTrafficIncidents|There are other traffic incidents at this location.|  
|PlannedEvents|There are scheduled events in the area.|  
|PrivateRoad|The road being travelled on is private.|  
|RestrictedTurn|The turn may be restricted.|  
|RoadClosures|There are road closures at this location.|  
|RoadHazard|There is a road hazard.|  
|ScheduledConstruction|There is construction along the route. The ScheduledConstruction value is used for any type of construction and not just construction that has specific start and end dates.|  
|SeasonalClosures|A seasonal closure occurs at this location.|  
|Tollbooth|A toll is required at this location to continue along the route.|  
|TollRoad|The road is a toll road.|  
|TollZoneEnter|The entrance to a toll zone.|  
|TollZoneExit|The exit of a toll zone.|  
|TrafficFlow|The warning is about traffic flow.|  
|TransitLineChange|There is a transit line change but a change of vehicle is not required.|  
|UnpavedRoad|The road is unpaved.|  
|Weather|There is significant weather at this location.|