
# MapPolygon class

Draws a filled shape upon the map.

**Android**

>```java
> class MapPolygon extends MapElement
>```

**iOS**

>```objectivec
> @interface MSMapPolygon : MSMapPathElement
>```  

>_See also:_ [MSMapPathElement](iOS/MSMapPathElement-class.md)

## Properties

### Path

The path making up this polygon.

**Android**

>```java
> Geopath getPath()  
> void setPath(Geopath path)
>```

**iOS**

Inherited from [MSMapPathElement](iOS/MSMapPathElement-class.md

>```objectivec
> @property (nonatomic) MSGeopath *path
>```  


### FillColor

The color to use to fill the inside of the polygon.

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
> float getStrokeWidth()
> void setStrokeWidth(float strokeWidth)
>```

**iOS**

>```objectivec
> @property int strokeWidth
>```

## See Also

[Drawing with Polylines and Polygons](../map-control-concepts/map-polylines-and-polygons.md)
