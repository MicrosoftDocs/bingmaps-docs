---
title: GroundOverlayMapLayer Class | Microsoft Docs
description: Describes the GroundOverlayMapLayer class for Android and iOS and provides the class' constructors and additional references.
ms.author: pablocan
---

# GroundOverlayMapLayer Class

[!INCLUDE [bing-maps-sdk-for-android-iOS-retirement](../../includes/bing-maps-sdk-for-android-iOS-retirement.md)]

Displays an image in a geographic area.

**Android**

>```java
> public class GroundOverlayMapLayer extends MapLayer
>```

**iOS**

>```objectivec
> @interface MSMapGroundOverlayMapLayer : MSMapLayer
>```

_See also:_ [MapLayer](MapLayer-class.md)

## Constructors

**Android**

>```java
> GroundOverlayMapLayer(android.graphics.Bitmap bitmap, GeoboundingBox latLongBox)
>```

**iOS**

>```objectivec
> - (id)initWithImage:(UIImage*)image boundingBox:(MSGeoboundingBox *)boundingBox
>```

## See Also

[Overlay tiled images on a map](../map-control-concepts/tile-layers.md)
