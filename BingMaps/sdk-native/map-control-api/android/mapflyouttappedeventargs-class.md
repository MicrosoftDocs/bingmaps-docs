---
title: MapFlyoutTappedEventArgs Class | Microsoft Docs
description: Describes the MapFlyoutTappedEventArgs class for Android and outlines the Flyout and Parent Icon properties.
ms.author: pablocan
---

# MapFlyoutTappedEventArgs Class (Android only)

[!INCLUDE [bing-maps-sdk-for-android-iOS-retirement](../../../includes/bing-maps-sdk-for-android-iOS-retirement.md)]

Event arguments passed to MapElementLayer.MapFlyoutTapped callback.

## Properties

### Flyout

Gets the [MapFlyout](../MapFlyout-class.md) that corresponds to where the [MapElementLayer](../MapElementLayer-class.md) received user input.

>```java
> final MapFlyout flyout
>```

### Parent Icon

Gets the parent [MapIcon](../MapIcon-class.md) of the flyout that corresponds to where the [MapElementLayer](../MapElementLayer-class.md) received user input.

>```java
> final MapIcon parentIcon
>```

## See Also

* [OnMapFlyoutTappedListener](OnMapFlyoutTappedListener-interface.md)
* [MapView](../MapView-class.md)