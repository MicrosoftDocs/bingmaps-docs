---
title: "TrafficIncidentTappedEventArgs Class | Microsoft Docs"
author: "pablocan"
---

# TrafficIncidentTappedEventArgs Class (Android only)

Event arguments passed to TrafficIncidentsMapLayer.TrafficIncidentTapped event.

## Properties

### Location

Gets the geographic location that corresponds to where the input was received.

>```java
> Geopoint getLocation()
>```

### Position

Gets the physical screen position relative to the MapView where the input was received.

>```java
> Point getPosition()
>```

### TrafficIncidents

Gets a list of traffic incidents that correspond to where the input was received.

>```java
> List<TrafficIncident> getTrafficIncidents()
>```

_See also:_ [TrafficIncident](../TrafficIncident-class.md)

## See Also

* [OnTrafficIncidentTappedListener](OnTrafficIncidentTappedListener-interface.md)
* [TrafficIncidentsMapLayer](../TrafficIncidentsMapLayer-class.md)
