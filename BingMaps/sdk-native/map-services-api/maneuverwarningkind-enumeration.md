---
title: "ManeuverWarningKind Enumeration | Microsoft Docs"
author: "kezhang"
---

# ManeuverWarningKind Enumeration

Represents the type of potential issue along a route leg.

**Android**

>```java
>public enum ManeuverWarningKind {
>  NONE(0),
>  ACCIDENT(1),
>  ADMINISTRATIVE_DIVISION_CHANGE(2),
>  ALERT(3),
>  BLOCKED_ROAD(4),
>  CHECK_TIME_TABLE(5),
>  CONGESTION(6),
>  CONSTRUCTION(7),
>  COUNTRY_CHANGE(8),
>  DISABLED_VEHICLE(9),
>  GATE_ACCESS(10),
>  GET_OFF_TRANSIT(11),
>  GET_ON_TRANSIT(12),
>  ILLEGAL_UTURN(13),
>  MASS_TRANSIT(14),
>  MISCELLANEOUS(15),
>  NO_INCIDENT(16),
>  OTHER(17),
>  OTHER_NEWS(18),
>  OTHER_TRAFFIC_INCIDENTS(19),
>  PLANNED_EVENT(20),
>  PRIVATE_ROAD(21),
>  RESTRICTED_TURN(22),
>  ROAD_CLOSURES(23),
>  ROAD_HAZARD(24),
>  SCHEDULED_CONSTRUCTION(25),
>  SEASONAL_CLOSURES(26),
>  TOLL_BOOTH(27),
>  TOLL_ROAD(28),
>  TOLL_ZONE_ENTER(29),
>  TOLL_ZONE_EXIT(30),
>  TRAFFIC_FLOW(31),
>  TRANSIT_LINE_CHANGE(32),
>  UNPAVED_ROAD(33),
>  UNSCHEDULED_CONSTRUCTION(34),
>  WEATHER(35);
>}
>```

**iOS**

>```objectivec
>typedef NS_ENUM(NSInteger, MSMapManeuverWarningKind) {
>    MSMapManeuverWarningKindNone = 0,
>    MSMapManeuverWarningKindAccident,
>    MSMapManeuverWarningKindAdministrativeDivisionChange,
>    MSMapManeuverWarningKindAlert,
>    MSMapManeuverWarningKindBlockedRoad,
>    MSMapManeuverWarningKindCheckTimeTable,
>    MSMapManeuverWarningKindCongestion,
>    MSMapMapManeuverWarningKindConstruction,
>    MSMapMapManeuverWarningKindCountryChange,
>    MSMapMapManeuverWarningKindDisabledVehicle,
>    MSMapMapManeuverWarningKindGateAccess,
>    MSMapMapManeuverWarningKindGetOffTransit,
>    MSMapMapManeuverWarningKindGetOnTransit,
>    MSMapMapManeuverWarningKindIllegalUturn,
>    MSMapMapManeuverWarningKindMassTransit,
>    MSMapMapManeuverWarningKindMiscellAneous,
>    MSMapMapManeuverWarningKindNoIncident,
>    MSMapMapManeuverWarningKindOther,
>    MSMapMapManeuverWarningKindOtherNews,
>    MSMapMapManeuverWarningKindOtherTrafficIncidents,
>    MSMapMapManeuverWarningKindPlannedEvent,
>    MSMapMapManeuverWarningKindPrivateRoad,
>    MSMapMapManeuverWarningKindRestrictedTurn,
>    MSMapMapManeuverWarningKindRoadClosures,
>    MSMapMapManeuverWarningKindRoadHazard,
>    MSMapMapManeuverWarningKindScheduledConstruction,
>    MSMapMapManeuverWarningKindSeasonalClosures,
>    MSMapMapManeuverWarningKindTollBooth,
>    MSMapMapManeuverWarningKindTollRoad,
>    MSMapMapManeuverWarningKindTollZoneEnter,
>    MSMapMapManeuverWarningKindTollZoneExit,
>    MSMapMapManeuverWarningKindTrafficFlow,
>    MSMapMapManeuverWarningKindTransitLineChange,
>    MSMapMapManeuverWarningKindUnpavedRoad,
>    MSMapMapManeuverWarningKindUnscheduledConstruction,
>    MSMapMapManeuverWarningKindWeather
>};
>```

## Values

### None

There is no warning at this location

### Accident

There is a traffic accident.

### Administrative_Division_Change

The route has left one administrative division and entered another.

### Alert

There is an alert.

### BlockedRoad

The road is closed or blocked.

### CheckTimeTable

Check a time table. This usually refers to a ferry or auto rail time table.

### Congestion

The traffic is slow.

### Construction

There is construction along the route. This value is used for any type of construction and not just construction that has specific start and end dates.

### CountryChange

The route has left one country and entered another.

### DisabledVehicle

There is a disabled vehicle.

### GateAccess

A gate blocks the road and access is required to continue along the route.

### GetOffTransit

Get off the transit at this location.

### GetOnTransit

Get on the transit at this location.

### IllegalUTurn

A U-turn is illegal at this location.

### MassTransit

There is mass transit incident.
 
### Miscellaneous

A miscellaneous warning is available for this location.

### NoIncident

There is no incident at this location.

### Other

There is a warning at this location that cannot be classified as any other type of warning.

### OtherNews

There is additional traffic incident information.

### OtherTrafficIncidents

There are other traffic incidents at this location.

### PlannedEvent

There are scheduled events in the area.

### PrivateRoad

The road being travelled on is private.

### RestrictedTurn

The turn may be restricted. 

### RoadClosures

There are road closures at this location.

### RoadHazard

There is a road hazard.

### ScheduledConstruction

There is construction along the route that has specific start and end dates.

### SeasonalClosures

A seasonal closure occurs at this location.

### TollBooth

A toll is required at this location to continue along the route.

### TollRoad

The road is a toll road.

### TollZoneEnter

The entrance to a toll zone.

### TollZoneExit

The exit of a toll zone.

### TrafficFlow

The warning is about traffic flow.

### TransitLineChange

There is a transit line change but a change of vehicle is not required.

### UnpavedRoad

The road is unpaved.

### UnscheduledConstruction

There is construction along the route that does not have any specific start and end dates.

### Weather

There is significant weather at this location.

## See Also

* [ManeuverWarning](maneuverwarning-class.md)
* [ManeuverWarningSeverity](maneuverwarningseverity-enumeration.md)