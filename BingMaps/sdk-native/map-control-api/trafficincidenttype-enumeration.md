---
title: TrafficIncidentType Enumeration | Microsoft Docs
description: Describes the TrafficIncidentType enumeration for Android and iOS and provides the enumeration's syntax and additional references.
ms.author: pablocan
---

# TrafficIncidentType Enumeration

Specifies the type of traffic incident.

**Android**

>```java
> public enum TrafficIncidentType {
>   ACCIDENT,
>   CONGESTION,
>   DISABLED_VEHICLE,
>   MASS_TRANSIT,
>   MISCELLANEOUS,
>   OTHER_NEWS,
>   PLANNED_EVENT,
>   ROAD_HAZARD,
>   CONSTRUCTION,
>   ALERT,
>   WEATHER
> }
>```

**iOS**

>```objectivec
> typedef NS_ENUM(NSInteger, MSMapTrafficIncidentType) {
>   MSMapTrafficIncidentTypeAccident,
>   MSMapTrafficIncidentTypeCongestion,
>   MSMapTrafficIncidentTypeDisabledVehicle,
>   MSMapTrafficIncidentTypeMassTransit,
>   MSMapTrafficIncidentTypeMiscellaneous,
>   MSMapTrafficIncidentTypeOtherNews,
>   MSMapTrafficIncidentTypePlannedEvent,
>   MSMapTrafficIncidentTypeRoadHazard,
>   MSMapTrafficIncidentTypeConstruction,
>   MSMapTrafficIncidentTypeAlert,
>   MSMapTrafficIncidentTypeWeather
> }
>```

* [TrafficIncident](TrafficIncident-class.md)