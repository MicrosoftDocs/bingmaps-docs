---
title: "MapStylePickerTrafficSwitchToggledEventArgs Class | Microsoft Docs"
ms.author: "pablocan"
---

# MapStylePickerTrafficSwitchToggledEventArgs Class (Android only)

Event arguments passed to UserInterfaceOptions.MapStylePickerTrafficSwitchToggled callback. Use the `trafficFlowMapLayer` and `trafficIncidentsMapLayer` event arguments to cache, configure, and attach handlers.

## Properties

### IsOn

Whether the switch was toggled on or off.

>```java
> boolean isOn()
>```

### TrafficFlowMapLayer

The traffic flow layer that will be added to the map, or null if the layer was removed.

>```java
> @Nullable TrafficFlowMapLayer getTrafficFlowMapLayer()
> void setTrafficFlowMapLayer(TrafficFlowMapLayer trafficFlowMapLayer)
>```

### TrafficIncidentsMapLayer

The traffic incident layer that will be added to the map, or null if the layer was removed. Set this to null while `isOn` is true to indicate that the incidents layer should not be added.

>```java
> @Nullable TrafficIncidentsMapLayer getTrafficIncidentsMapLayer()
> void setTrafficIncidentsMapLayer(@Nullable TrafficIncidentsMapLayer trafficIncidentsMapLayer)
>```


## See Also

* [MapStylePickerTrafficSwitchToggled](OnMapStylePickerTrafficSwitchToggledListener-interace.md)
* [TrafficFlowMapLayer](../TrafficFlowMapLayer-class.md)
* [TrafficIncidentsMapLayer](../TrafficIncidentsMapLayer-class.md)
