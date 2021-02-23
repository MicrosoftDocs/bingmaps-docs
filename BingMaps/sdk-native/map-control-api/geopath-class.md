---
title: "Geopath Class | Microsoft Docs"
ms.author: "pablocan"
---

# Geopath Class

Represents an ordered series of geographic points that form a path.

**Android**

>```java
> public class Geopath extends Geoshape implements Iterable<Geoposition>
>```

**iOS**

>```objectivec
> @interface MSGeopath : MSGeoshape<NSFastEnumeration>
>```


## Constructors

Constructor takes one argument: a non-empty collection of Geopositions that form the Geopath.  
All Geopositions must use the same altitude reference system.

**Android**

>```java
> Geopath(List<Geoposition> positions)
> Geopath(List<Geoposition> positions, AltitudeReferenceSystem altitudeReference)
>```

**iOS**

>```objectivec
> + (instancetype)geopathWithPositions:(NSArray<MSGeoposition*>*)positions
> + (instancetype)geopathWithPositions:(NSArray<MSGeoposition*>*)positions
>              altitudeReferenceSystem:(MSMapAltitudeReferenceSystem)altitudeReferenceSystem
>```

_See also:_ 
* [Geoposition](geoposition-class.md)
* [AltitudeReferenceSystem](AltitudeReferenceSystem-enumeration.md)


## Properties

### AltitudeReferenceSystem

Altitude reference system used for all positions in the geopath.

**Android**

>```java
> AltitudeReferenceSystem getAltitudeReferenceSystem()
>```

**iOS**

>```objectivec
> @property (nonatomic, readonly) MSMapAltitudeReferenceSystem altitudeReferenceSystem
>```

_See also:_ [AltitudeReferenceSystem](AltitudeReferenceSystem-enumeration.md)

### Size

The number of positions in the Geopath.

**Android**

>```java
> int size()
>```

**iOS**

>```objectivec
> @property (nonatomic, readonly) NSUInteger size
>```

## Methods

### GetGeoposition

**Android**

>```java
> Geoposition get(int index)
>```

**iOS**

>```objectivec
> - (MSGeoposition *)positionAtIndex:(NSUInteger)index
>```

## See Also

* [Geoshape](Geoshape-class.md)
* [Geoposition](Geoposition-class.md)
