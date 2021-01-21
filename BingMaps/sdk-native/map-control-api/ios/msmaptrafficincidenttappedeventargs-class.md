---
title: "MSMapTrafficIncidentTappedEventArgs Class | Microsoft Docs"
ms.author: "pablocan"
---

# MSMapTrafficIncidentTappedEventArgs Class (iOS only)

Event arguments passed to TrafficIncidentsMapLayer.TrafficIncidentTapped event.

>```objectivec
> @interface MSMapTrafficIncidentTappedEventArgs : NSObject
>```

## Properties

### Location

Gets the geographic location that corresponds to where the input was received.

>```objectivec
> @property(nonatomic, readonly) MSGeopoint* location
>```

### Position

Gets the physical position of where the input was received.

>```objectivec
> @property(nonatomic, readonly) CGPoint position
>```

### TrafficIncidents

Gets a list of traffic incidents that correspond to where the input was received.

>```objectivec
> @property(nonatomic, readonly) NSSet<MSMapTrafficIncident*>* trafficIncidents
>```

_See also:_ [MSMapTrafficIncident](../TrafficIncident-class.md)

## See Also

* [MSMapTrafficIncidentLayerUserDidTapTrafficIncidentHandler](MSMapTrafficIncidentLayerUserDidTapTrafficIncidentHandler-interface.md)
