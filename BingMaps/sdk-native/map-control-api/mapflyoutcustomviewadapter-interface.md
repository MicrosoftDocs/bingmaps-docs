---
title: MapFlyoutCustomViewAdapter Interface | Microsoft Docs
description: Describes the MapFlyoutCustomViewAdapter interface for iOS and provides the interface's parameters and additional references.
ms.author: pablocan
---

# MapFlyoutCustomViewAdapter Interface

[!INCLUDE [bing-maps-sdk-for-android-iOS-retirement](../../includes/bing-maps-sdk-for-android-iOS-retirement.md)]

Interface for providing custom views for flyouts, on per-icon basis.  
If a null view is returned, the default view with flyout's title and description will be used.

>```java
> public interface MapFlyout.CustomViewAdapter
> {
>     @Nullable View getFlyoutView(MapElement mapElement);
> }
>```

**iOS**

>```objectivec
> typedef UIView* _Nullable (^MSMapFlyoutCustomViewAdapter)(MSMapElement*)
>```

## Parameters

### MapElement
The map element that the flyout is being invoked on.

## See Also

* [MapElement](mapelement-class.md)
* [MapFlyout](mapflyout-class.md)
