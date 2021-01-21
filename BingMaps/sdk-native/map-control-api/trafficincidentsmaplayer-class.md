---
title: "TrafficIncidentsMapLayer Class | Microsoft Docs"
author: "pablocan"
---

# TrafficIncidentsMapLayer Class

Displays traffic incidents on the map.

**Android**

>```java
> class TrafficIncidentsMapLayer extends MapLayer
>```

**iOS**

>```objectivec
> @interface MSMapTrafficIncidentsMapLayer : MSMapLayer
>```


## Events

### TrafficIncidentTapped

Fired when a traffic incident is tapped.

**Android**

>```java
> void addOnTrafficIncidentTappedListener(OnTrafficIncidentTappedListener listener)
> void removeOnTrafficIncidentTappedListener(OnTrafficIncidentTappedListener listener)
>```

_See also:_ [TrafficIncidentTappedListener](Android/OnTrafficIncidentTappedListener-interface.md)

**iOS**

>```objectivec
> - (MSMapHandlerId)addUserDidTapTrafficIncidentHandler:(MSMapTrafficIncidentLayerUserDidTapTrafficIncidentHandler)handler
> - (BOOL)removeUserDidTapTrafficIncidentHandler:(MSMapHandlerId)handlerId

_See also:_ [MSMapTrafficIncidentLayerUserDidTapTrafficIncidentHandler](iOS/MSMapTrafficIncidentLayerUserDidTapTrafficIncidentHandler-interface.md)

## See Also

[TrafficFlowMapLayer](TrafficFlowMapLayer-class.md)