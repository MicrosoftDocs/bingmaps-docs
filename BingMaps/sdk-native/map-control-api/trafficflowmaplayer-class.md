---
title: TrafficFlowMapLayer Class | Microsoft Docs
description: Describes the TrafficFlowMapLayer class for Android and iOS and provides the class's properties and additional references.
ms.author: pablocan
---

# TrafficFlowMapLayer Class

[!INCLUDE [bing-maps-sdk-for-android-iOS-retirement](../../includes/bing-maps-sdk-for-android-iOS-retirement.md)]

Display traffic flow on the map.

**Android**

>```java
> class TrafficFlowMapLayer extends MapLayer
>```

**iOS**

>```objectivec
> @interface MSMapTrafficFlowMapLayer : MSMapLayer
>```

## Properties

### LegendVisible

Whether the traffic legend is displayed. Consider using this for accessibility purposes.

**Android**

>```java
> boolean isLegendVisible()
> void setLegendVisible(boolean visible)
>```

**iOS**

>```objectivec
> @property(nonatomic) BOOL legendVisible
>```

## See Also

[Custom Overlays](../map-control-concepts/tile-layers.md)