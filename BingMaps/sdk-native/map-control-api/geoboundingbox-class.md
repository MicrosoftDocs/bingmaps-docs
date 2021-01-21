---
title: "GeoboundingBox Class | Microsoft Docs"
ms.author: "pablocan"
---

# GeoboundingBox Class

Represents a bounded geographic area.

**Android**

>```java
> public class GeoboundingBox extends Geoshape
>```

**iOS**

>```objectivec
> @interface MSGeoboundingBox : MSGeoshape
>```

## Constructors

_See also:_ [MSGeoposition](Geoposition-class.md)

**Android**

>```java
> // Creates a bounding box based on two opposite corners. 
> GeoboundingBox(Geoposition northwestCorner, Geoposition southeastCorner)
> // Creates a bounding box based on two opposite corners and specified altitude reference system. 
> GeoboundingBox(Geoposition northwestCorner, Geoposition southeastCorner, AltitudeReferenceSystem altitudeReferenceSystem)
> // Creates a bounding box to contain the specified positions. Positions must contain at least 1 element.
> GeoboundingBox(List<Geoposition> positions)
> // Creates a bounding box to contain the specified positions and altitude reference system. Positions must contain at least 1 element.
> GeoboundingBox(List<Geoposition> positions, AltitudeReferenceSystem altitudeReferenceSystem)
>```

**iOS**
>```objectivec
>+ (instancetype)geoboundingBoxWithNorthwestCorner:(MSGeoposition *)northwestCorner southeastCorner:(MSGeoposition *)southeastCorner
>+ (instancetype)geoboundingBoxWithNorthwestCorner:(MSGeoposition *)northwestCorner southeastCorner:(MSGeoposition *)southeastCorner altitudeReferenceSystem:(MSMapAltitudeReferenceSystem altitudeReferenceSystem
>+ (instancetype)geoboundingBoxWithPositions:(NSArray<MSGeoposition *> *)positions
>+ (instancetype)geoboundingBoxWithPositions:(NSArray<MSGeoposition *> *)positions altitudeReferenceSystem:(MSMapAltitudeReferenceSystem)altitudeReferenceSystem
>```


## Properties

### North

The latitude of the northern border of the bounding box.

**Android**

>```java
> double getNorth()
>```

**iOS**

>```objectivec
> @property (nonatomic, readonly) CLLocationDegrees north
>```


### East

The longitude of the eastern border of the bounding box.

**Android**

>```java
> double getEast()
>```

**iOS**

>```objectivec
> @property (nonatomic, readonly) CLLocationDegrees east
>```

### South

The latitude of the southern border of the bounding box.

**Android**

>```java
> double getSouth()
>```

**iOS**

>```objectivec
> @property (nonatomic, readonly) CLLocationDegrees south
>```

### West

The longitude of the western border of the bounding box.

**Android**

>```java
> double getWest()
>```

**iOS**

>```objectivec
> @property (nonatomic, readonly) CLLocationDegrees west
>```

### MinimumAltitude

The minimum altitude of all the points within the bounding box.

**Android**

>```java
> double getMinimumAltitude()
>```

**iOS**

>```objectivec
> @property (nonatomic, readonly) CLLocationDistance minimumAltitude
>```

### MaximumAltitude

Gets the maximum altitude of all the points within the bounding box.

**Android**

>```java
> double getMaximumAltitude()
>```

**iOS**

>```objectivec
> @property (nonatomic, readonly) CLLocationDistance maximumAltitude
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

### NorthwestCorner

The north west corner of the bounding box.
_See also:_ [Geoposition](Geoposition-class.md)

**Android**

>```java
> Geoposition getNorthwestCorner()
>```

**iOS**

>```objectivec
> @property (nonatomic, readonly) Geoposition *northWestCorner
>```

### SoutheastCorner

The south east corner of the bounding box.
_See also:_ [Geoposition](Geoposition-class.md)

**Android**

>```java
> Geoposition getSoutheastCorner()
>```

**iOS**

>```objectivec
> @property (nonatomic, readonly) Geoposition *southEastCorner
>```

## See Also

* [Geoshape](Geoshape-class.md)
* [Geoposition](Geoposition-class.md)