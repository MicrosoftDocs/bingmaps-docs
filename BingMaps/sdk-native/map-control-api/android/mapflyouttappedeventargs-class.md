---
title: "MapFlyoutTappedEventArgs Class | Microsoft Docs"
author: "pablocan"
---

# MapFlyoutTappedEventArgs Class (Android only)

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