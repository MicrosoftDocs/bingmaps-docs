---
title: GeoshapeType Enumeration | Microsoft Docs
description: Describes the GeoshapeType enumeration for Android and iOS and provides the enumeration's Geopoint, Geocircle, Geopath, and GeoboundingBox values.
ms.author: pablocan
---

# GeoshapeType Enumeration

[!INCLUDE [bing-maps-sdk-for-android-iOS-retirement](../../includes/bing-maps-sdk-for-android-iOS-retirement.md)]

Indicates the shape of the geographic region.

**Android**

>```java
> public enum GeoshapeType
> {
>      GEOPOINT,
>      GEOCIRCLE,
>      GEOPATH,
>      GEOBOUNDINGBOX
> }
>```

**iOS**

>```objectivec
> typedef NS_ENUM(NSInteger, MSGeoshapeType)
> {
>      MSGeoshapeTypeGeopoint,
>      MSGeoshapeTypeGeocircle,
>      MSGeoshapeTypeGeopath,
>      MSGeoshapeTypeGeoboundingBox
> }
>```

## Values

### Geopoint

The geographic region is a point.

### Geocircle

The geographic region is a circle with a center point and a radius.

### Geopath

The geographic region is an ordered series of points.

### GeoboundingBox

The geographic region is a rectangular region.