---
title: "MSMapTrafficIncidentLayerUserDidTapTrafficIncidentHandler Interface | Microsoft Docs"
ms.author: "pablocan"
---

# MSMapTrafficIncidentLayerUserDidTapTrafficIncidentHandler Interface (iOS only)

Listener used with TrafficIncidentsMapLayer.TrafficIncidentTapped event. Return true from this event to prevent other OnMapTappedListeners from receiving this event or false to allow other listeners to receive his notification as well. Events are processed in the order they were attached to the TrafficIncidentsMapLayer.

>```objectivec
> typedef BOOL (^MSMapTrafficIncidentLayerUserDidTapTrafficIncidentHandler)(MSMapTrafficIncidentTappedEventArgs*)
>```

## See Also

* [MSMapTrafficIncidentTappedEventArgs](MSMapTrafficIncidentTappedEventArgs-class.md)
* [TrafficIncidentsMapLayer](../TrafficIncidentsMapLayer-class.md)