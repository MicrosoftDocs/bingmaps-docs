---
title: "Geocircle Class | Microsoft Docs"
author: "pablocan"
---

# Geocircle Class

Describes a geographic circle with a center point and radius.

**Android**

>```java
> public class Geocircle extends Geoshape
>```

**iOS**

>```objectivec
> @interface MSGeocircle : MSGeoshape
>```

## Constructors

_See also:_ [MSGeoposition](Geoposition-class.md)

**Android**

>```java
> Geocircle(Geoposition center, double radius)
> Geocircle(Geoposition center, double radius, AltitudeReferenceSystem altitudeReferenceSystem)
>```

**iOS**
>```objectivec
> + (instancetype)geocircleWithCenter:(MSGeoposition *)center
>                              radius:(CLLocationDistance)radius
> + (instancetype)geocircleWithCenter:(MSGeoposition *)center
>                              radius:(CLLocationDistance)radius
>                   altitudeReference:(MSMapAltitudeReferenceSystem)altitudeReferenceSystem
>```

## Properties

### Center

The center point of a geographical circle.

**Android**

>```java
> Geoposition getCenter()
>```

**iOS**

>```objectivec
> @property (nonatomic, readonly) MSGeoposition *center
>```

### Radius

Radius of a geographical circle in meters.

**Android**

>```java
> double getRadius()
>```

**iOS**

>```objectivec
> @property (nonatomic, readonly) CLLocationDistance radius
>```

### AltitudeReferenceSystem

Gets the altitude reference system used by the GeoboundingBox.

**Android**

>```java
> AltitudeReferenceSystem getAltitudeReferenceSystem()
>```

**iOS**

>```objectivec 
> @property (nonatomic, readonly) MSMapAltitudeReferenceSystem altitudeReferenceSystem
>```

_See also:_ [AltitudeReferenceSystem](AltitudeReferenceSystem-enumeration.md)

## See Also

* [Geoshape](Geoshape-class.md)
* [Geoposition](Geoposition-class.md)