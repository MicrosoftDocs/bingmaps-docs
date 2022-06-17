---
title: AltitudeReferenceSystem Enumeration | Microsoft Docs
description: Describes the AltitudeReferenceSystem enumeration and provides how values will appear on Android iOS systems, and provides additional value types.
ms.author: pablocan
---

# AltitudeReferenceSystem Enumeration

An altitude reference system to indicate what an altitude value is relative to.

**Android**

>```java
> enum AltitudeReferenceSystem
> {
>     UNSPECIFIED,
>     TERRAIN,
>     ELLIPSOID,
>     GEOID,
>     SURFACE
> }
>```

**iOS**

>```objectivec
> typedef NS_ENUM(NSInteger, MSMapAltitudeReferenceSystem)
> {
>     MSMapAltitudeReferenceSystemUnspecified = 0,
>     MSMapAltitudeReferenceSystemTerrain = 1,
>     MSMapAltitudeReferenceSystemEllipsoid = 2,
>     MSMapAltitudeReferenceSystemGeoid = 3,
>     MSMapAltitudeReferenceSystemSurface = 4
> }
>```

## Values

### Unspecified

The altitude value has no meaning.

### Terrain

The altitude value is relative to the terrain (not including surface objects like trees and buildings).

### Ellipsoid

The altitude value is relative to the WGS84 ellipsoid.

### Geoid

The altitude value is relative to sea level.

### Surface

The altitude value is relative to the surface (including objects like buildings that are on top of the terrain).

## See Also

[Geopoint](Geopoint-class.md)
