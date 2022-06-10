---
title: MapUserLocationOrientation Enumeration | Microsoft Docs
description: Describes the mapUserLocationOrientation enumeration for Android and iOS and provides the enumeration's Heading and Bearing values.
ms.author: adl
---

# MapUserLocationOrientation Enumeration

Specifies the orientation of user location's directionality cone.

**Android**

>```java
> public enum MapUserLocationOrientation {
>   HEADING,
>   BEARING
> }
>```

**iOS**

>```objectivec
> typedef NS_ENUM(NSInteger, MapUserLocationOrientation) {
>   MSMapUserLocationOrientationHeading,
>   MSMapUserLocationOrientationBearing
> };
>```

## Values

### Heading

Use the direction the phone is facing. Useful for non-navigation purposes.

### Bearing

Use the direction the user is moving towards. Useful for navigation purposes.

## See Also

* [MapUserLocation](mapuserlocation-class.md)
