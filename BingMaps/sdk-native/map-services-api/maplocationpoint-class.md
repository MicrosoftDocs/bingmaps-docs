---
title: "MapLocationPoint Class | Microsoft Docs"
ms.author: "pablocan"
---

# MapLocationPoint Class

Contains geospatial data for a specific point associated with the location returned from a geocoding request.

## Properties

### Point

The geopoint for the resource.

_See also:_ [Geopoint](../map-control-api/Geopoint-class.md)

**Android**

>```java
>Geopoint getPoint()
>```

**iOS**

>```objectivec
>@property (nonatomic, readonly) MSGeopoint* point
>```

### CalculationMethod

The calculation method used for the resource.

_See also:_ [MapLocationPointCalculationMethod](MapLocationPointCalculationMethod-enumeration.md)

**Android**

>```java
>MapLocationPoint.CalculationMethod getCalculationMethod()
>```

**iOS**

>```objectivec
>@property (nonatomic, readonly) MSMapLocationPointCalculationMethod calculationMethod
>```

### UsageType

The usage type recommended for the resource.

_See also:_ [MapLocationPointUsageType](MapLocationPointUsageType-enumeration.md)

**Android**

>```java
>MapLocationPoint.UsageType getUsageType()
>```

**iOS**

>```objectivec
>@property (nonatomic, readonly) MSMapLocationPointUsageType usageType
>```

## See Also

* [MapLocation](MapLocation-class.md)
* [MapLocationPointCalculationMethod](MapLocationPointCalculationMethod-enumeration.md)
* [MapLocationPointUsageType](MapLocationPointUsageType-enumeration.md)
