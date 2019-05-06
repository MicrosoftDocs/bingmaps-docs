# MapLocationPoint

Contains geospatial data for a specific point associated with the location returned from a geocoding request.

## Properties

### Point

The geolocation for the resource.

_See also:_ [Geolocation](../map-control-api/Geolocation-class.md)

**Android**

>```java
>Geolocation getPoint()
>```

**iOS**

>```objectivec
>@property (nonatomic, readonly) MSGeolocation* point
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

## See also

* [MapLocation](MapLocation-class.md)
* [MapLocationPointCalculationMethod](MapLocationPointCalculationMethod-enumeration.md)
* [MapLocationPointUsageType](MapLocationPointUsageType-enumeration.md)
