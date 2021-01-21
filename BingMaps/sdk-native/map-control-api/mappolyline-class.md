---
title: "MapPolyline Class | Microsoft Docs"
ms.author: "pablocan"
---

# MapPolyline Class

Displays a line on a map.

**Android**

>```java
> class MapPolyline extends MapElement
>```

**iOS**

>```objectivec
> @interface MSMapPolyline : MSMapElement
>```

_See also:_ [MapElement](mapelement-class.md)


## Properties

### Path

The path making up this line.

**Android**

>```java
> Geopath getPath()
> void setPath(Geopath path)
>```

**iOS**

>```objectivec
> @property (nonatomic) MSGeopath *path  
>```

### StrokeColor

The color in ARGB format to use to draw the border of the polygon. The default value is blue (0xff0000ff).

**Android**

>```java
> int getStrokeColor()  
> void setStrokeColor(int strokeColor)
>```

**iOS**

>```objectivec
> @property (nonatomic) UIColor *strokeColor
>```

### StrokeDashed

Indicates whether the line is dashed.

**Android**

>```java
> boolean isStrokeDashed()
> void setStrokeDashed(boolean isDashed)
>```

**iOS**

>```objectivec
> @property BOOL strokeDashed
>```

### StrokeWidth

The width of the line to use for the outside of the polygon. The default value is 1.

**Android**

>```java
> float getStrokeWidth()  
> void setStrokeWidth(float strokeWidth)
>```

**iOS**

>```objectivec
> @property int strokeWidth
>```

## See Also

* [Drawing with Polylines and Polygons](../map-control-concepts/map-polylines-and-polygons.md)
* [MapElement](mapelement-class.md)
