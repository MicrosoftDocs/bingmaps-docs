---
title: "MapPolygon Class | Microsoft Docs"
ms.author: "pablocan"
---

# MapPolygon Class

Draws a complex filled shape upon the map.

**Android**

>```java
> class MapPolygon extends MapElement
>```

**iOS**

>```objectivec
> @interface MSMapPolygon : MSMapElement
>```

_See also:_ [MapElement](mapelement-class.md)


## Properties

### Paths

The paths making up rings of this polygon. The use of paths and shapes are mutually exclusive.

**Android**

>```java
> List<Geopath> getPaths()
> void setPaths(List<Geopath> paths)
>```

**iOS**

>```objectivec
> @property (nonatomic) NSArray<MSGeopath *> *paths
>```

### Shapes

The shapes making up the rings of this polygon. The use of paths and shapes are mutually exclusive.

**Android**

>```java
> List<? extends Geoshape> getShapes()
> void setShapes(List<? extends Geoshape> shapes)
>```

**iOS**

>```objectivec
> @property (nonatomic) NSArray<MSGeoshape *> *shapes
>```

_See also:_ [Geoshape](Geoshape-class.md)

### FillColor

The color in ARGB format to use to fill the inside of the polygon. The default value is blue (0xff0000ff).

**Android**

>```java
> int getFillColor()
> void setFillColor(int fillColor)
>```

**iOS**

>```objectivec
> @property (nonatomic) UIColor *fillColor
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
