---
title: MapImage Class | Microsoft Docs
description: Describes the MapImage class for Android and iOS and provides the class' constructor, properties, and additional references.
ms.author: pablocan
---

# MapImage Class

[!INCLUDE [bing-maps-sdk-for-android-iOS-retirement](../../includes/bing-maps-sdk-for-android-iOS-retirement.md)]

An image that can be used with [MapIcon](MapIcon-class.md).

**Android**

>```java
> public class MapImage
>```

**iOS**

>```objectivec
> @interface MSMapImage : NSObject
>```

## Constructor

**Android**

>```java
> MapImage(android.graphics.Bitmap bitmap)
> MapImage(InputStream stream)
>```

**iOS**

>```objectivec
> + (instancetype)imageFromSvg:(NSData *)svgData
> + (instancetype)imageWithUIImage:(UIImage *)image
> + (instancetype)imageWithUIView:(UIView *)view
>```

## Properties

### Bitmap (Android only)

The bitmap associated with this MapImage.

>```java
> @Nullable android.graphics.Bitmap getBitmap()
>```


## See Also

[Icons](../map-control-concepts/map-icons.md)
