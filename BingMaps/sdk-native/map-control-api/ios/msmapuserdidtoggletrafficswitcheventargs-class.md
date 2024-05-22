---
title: MSMapUserDidToggleTrafficSwitchEventArgs Class | Microsoft Docs
description: Describes the MSMapUserDidToggleTrafficSwitchEventArgs class for iOS and provides the class' syntax, properties, and additional references.
ms.author: pablocan
---

# MSMapUserDidToggleTrafficSwitchEventArgs Class (iOS only)

[!INCLUDE [bing-maps-sdk-for-android-iOS-retirement](../../../includes/bing-maps-sdk-for-android-iOS-retirement.md)]

Event arguments passed to UserInterfaceOptions.MapStylePickerTrafficSwitchToggled callback. Use the `trafficFlowMapLayer` and `trafficIncidentsMapLayer` event arguments to cache, configure, and attach handlers.

>```objectivec
> @interface MSMapUserDidToggleTrafficSwitchEventArgs : NSObject
>```

## Properties

### IsOn

Gets whether the switch was toggled on or off.

>```objectivec
> @property(nonatomic, readonly) BOOL isOn
>```

### TrafficFlowMapLayer

The traffic flow map layer added to the map. This will be nil if the switch is toggled off.

>```objectivec
> @property(nonatomic) MSMapTrafficFlowMapLayer* trafficFlowMapLayer
>```

### TrafficIncidentsMapLayer

 The traffic incidents map layer added to the map. This will be nil if the switch is toggled off.

>```objectivec
> @property(nonatomic, nullable) MSMapTrafficIncidentsMapLayer* trafficIncidentsMapLayer
>```

## See Also

* [MSMapUserDidToggleTrafficSwitchHandler](MSMapUserDidToggleTrafficSwitchHandler-interface.md)
* [MapUserInterfaceOptions](../MapUserInterfaceOptions-class.md)
* [TrafficFlowMapLayer](../TrafficFlowMapLayer-class.md)
* [TrafficIncidentsMapLayer](../TrafficIncidentsMapLayer-class.md)
