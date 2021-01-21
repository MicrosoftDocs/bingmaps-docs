---
title: "OnTrafficIncidentTappedListener Interface | Microsoft Docs"
ms.author: "pablocan"
---

# OnTrafficIncidentTappedListener Interface (Android only)

Listener used with TrafficIncidentsMapLayer.TrafficIncidentTapped event. Return true from this event to prevent other OnMapTappedListeners from receiving this event or false to allow other listeners to receive this notification as well. Events are processed in the order they were attached to the TrafficIncidentsMapLayer.

>```java
> public interface OnTrafficIncidentTappedListener
>{
>    /** Called when traffic incident is tapped. */
>    boolean onTrafficIncidentTapped(TrafficIncidentTappedEventArgs e);
>}
>```

## See Also

* [TrafficIncidentTappedEventArgs](TrafficIncidentTappedEventArgs-class.md)
* [TrafficIncidentsMapLayer](../TrafficIncidentsMapLayer-class.md)