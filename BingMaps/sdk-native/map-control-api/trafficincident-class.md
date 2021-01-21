---
title: "TrafficIncident Class | Microsoft Docs"
author: "pablocan"
---

# TrafficIncident Class

Contains information about a specific traffic incident returned by tap events from the [Traffic Incidents Map Layer](trafficincidentsmaplayer-class.md).

## Properties

### Location

The latitude and longitude coordinates where you encounter the incident.

**Android**

>```java
> Geoposition getLocation()
>```

**iOS**

>```objectivec
> @property(nonatomic, readonly) MSGeopoint* location
>```

_See also:_ [Geoposition](Geoposition-class.md)

### Identifier

A unique ID for the incident.

**Android**
>```java
> String getIdentifier()
>```

**iOS**

>```objectivec
> @property(nonatomic, readonly) NSString* identifier
>```

### Description

A description of the incident.

**Android**
>```java
> String getDescription()
>```

**iOS**

>```objectivec
> @property(nonatomic, readonly) NSString* incidentDescription
>```

### StartTime

The time the incident alert started

**Android**
>```java
> java.util.Date getStartTime()
>```

**iOS**

>```objectivec
> @property(nonatomic, readonly) NSDate* startTime
>```

### EndTime

The time the incident alert will end. If the incident does not have an end time, null will be returned.

**Android**
>```java
> @Nullable java.util.Date getEndTime()
>```

**iOS**

>```objectivec
> @property(nonatomic, readonly, nullable) NSDate* endTime
>```

### RoadClosed

Indicates whether there is a road closure.

**Android**
>```java
> boolean isRoadClosed()
>```

**iOS**

>```objectivec
> @property(nonatomic, readonly) BOOL roadClosed
>```

### Severity

Specifies the severity of incident.

**Android**
>```java
> TrafficIncidentSeverity getSeverity()
>```

**iOS**

>```objectivec
> @property(nonatomic, readonly) MSMapTrafficIncidentSeverity severity
>```

_See also:_ [TrafficIncidentSeverity](TrafficIncidentSeverity-enumeration.md)

### Type

Specifies the type of incident.

**Android**
>```java
> TrafficIncidentType getType()
>```

**iOS**

>```objectivec
> @property(nonatomic, readonly) MSMapTrafficIncidentType type
>```

_See also:_ [TrafficIncidentType](TrafficIncidentType-enumeration.md)

## See Also

* [TrafficIncidentsMapLayer](trafficincidentsmaplayer-class.md)