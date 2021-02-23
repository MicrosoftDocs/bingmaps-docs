---
title: "GeoshapeType Enumeration | Microsoft Docs"
ms.author: "pablocan"
---

# GeoshapeType Enumeration

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