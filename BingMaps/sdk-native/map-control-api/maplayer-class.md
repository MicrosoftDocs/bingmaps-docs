---
title: MapLayer Class | Microsoft Docs
description: Describes the MapLayer class for Android and iOS and provides the class' properties and additional references.
ms.author: pablocan
---

# MapLayer Class

Base class for a layer on the map. Not directly usable, only exists to provide functionality common to all MapLayers.

**Android**

>```java
> public class MapLayer
>```

**iOS**

>```objectivec
> @interface MSMapLayer : NSObject
>```

## Properties

### Visible
Whether this layer is rendered or not.

**Android**

>```java
> boolean isVisible()
> void setVisible(boolean visible)
>```

**iOS**

>```objectivec
> @property (nonatomic) BOOL visible
>```

### ZIndex
The z-index of this layer. Layers with higher z-indexes will render on top of those with lower z-indexes.

**Android**

>```java
> float getZIndex() 
> void setZIndex(float zIndex)
>```

**iOS**

>```objectivec
> @property (nonatomic) int zIndex
>```

## See Also

* [CustomTileMapLayer](CustomTileMapLayer-class.md)
* [GroundOverlayMapLayer](GroundOverlayMapLayer-class.md)
* [MapElementLayer](MapElementLayer-class.md)
* [TrafficFlowMapLayer](TrafficFlowMapLayer-class.md)
* [UriTileMapLayer](UriTileMapLayer-class.md)
