---
title: MapLocationPointCalculationMethod Enumeration | Microsoft Docs
description: Describes the MapLocationPointCalculationMethod enumeration for android and iOS and provides the enumeration's values and additional references.
ms.author: pablocan
---

# MapLocationPointCalculationMethod Enumeration

[!INCLUDE [bing-maps-sdk-for-android-iOS-retirement](../../includes/bing-maps-sdk-for-android-iOS-retirement.md)]

The method that was used to compute the geocode point.

**Android**

>```java
>public enum MapLocationPointCalculationMethod
>{
>    UNKNOWN(0),
>    INTERPOLATION(1),
>    INTERPOLATION_OFFSET(2),
>    PARCEL_CENTROID(3),
>    ROOFTOP(4);
>}
>```

**iOS**

>```objectivec
>typedef NS_ENUM(NSInteger, MSMapLocationPointCalculationMethod)
>{
>    MSMapLocationPointCalculationMethodUnknown = 0,
>    MSMapLocationPointCalculationMethodInterpolation = 1,
>    MSMapLocationPointCalculationMethodInterpolationOffset = 2,
>    MSMapLocationPointCalculationMethodParcelCentroid = 3,
>    MSMapLocationPointCalculationMethodRooftop = 4
>};
>```

## Values

### Unknown

Bing Maps SDK was unable to parse the value in the response.

### Interpolation

The geocode point was matched to a point on a road using interpolation.

### InterpolationOffset

The geocode point was matched to a point on a road using interpolation with an additional offset to shift the point to the side of the street.

### Parcel

The geocode point was matched to the center of a parcel.

### Rooftop

The geocode point was matched to the rooftop of a building.

## See Also

* [MapLocationPoint](MapLocationPoint-class.md)
