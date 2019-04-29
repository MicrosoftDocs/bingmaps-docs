
# MapPolyline class

Displays a line on a map.

**Android**

>```java
> class MapPolyline extends MapElement
>```

**iOS**

>```objectivec
> @interface MSMapPolyline : MSMapPathElement
>```

_See also:_ [MSMapPathElement](iOS/MSMapPathElement.md)

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
> @property (nonatomic) MSGeopath *path```  
> (inherited from [MSMapPathElement](iOS/MSMapPathElement.md))
>```

_See also:_ [MSGeopath](Geopath.md)

### StrokeColor

The color to use to draw the border of the polygon.

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
> boolean getStrokeDashed()  
> void setStrokeDashed(boolean isDashed)
>```

**iOS**

>```objectivec
> @property BOOL strokeDashed
>```  

### StrokeWidth

The width of the line to use for the outside of the polygon.

**Android**

>```java
> float getStrokeWidth()```  
> void setStrokeWidth(float strokeWidth)
>```

**iOS**

>```objectivec
> @property int strokeWidth
>```  

## See Also

* [Drawing with Polylines and Polygons](../map-control-concepts/Drawing_with_Polylines_and_Polygons.md)
