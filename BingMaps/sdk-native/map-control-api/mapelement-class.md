
# MapElement class

Represents an element displayed on a MapControl.

**Android**

>```java
> public abstract class MapElement
>```

**iOS**

> ```objectivec
> @interface MSMapElement : NSObject
>```

## Properties

### ZIndex

The ZIndex of the map element. Elements with a higher ZIndex will render on top of elements with a lower ZIndex.

**Android**

>```java
> float getZIndex()
> void setZIndex(float zIndex)
>```

**iOS**

>```objectivec
> @property (nonatomic) int zIndex
>```

#### Visible

Whether the item is visible or not.

**Android**

>```java
>boolean isVisible()
>void setVisible(boolean visible)
>```

**iOS**

>```objectivec 
> @property (nonatomic) BOOL isVisible
> ```

#### HitTestVisible

Whether this shape is hit testable.  Default is false for MapPolygon and MapPolyline and true for MapIcon. Note that adding lots of elements that are hit testable can negatively impact user experence.

**Android**

>```java
> boolean isHitTestVisible()
> void setHitTestVisible(boolean hitTestVisible)
>```

**iOS**

>```objectivec
> @property (nonatomic) BOOL isHitTestVisible
>```

#### Tag

Gets or sets an arbitrary object value that can be used to store custom information about this object.

**Android**

>```java
> Object getTag()
> void setTag(Object newTag)
>```

**iOS**

>```objectivec
> @property (nonatomic) id tag;
>```

## See Also

* [MapIcon](MapIcon-class.md)
* [MapPolyline](MapPolyline-class.md)
* [MapPolygon](MapPolygon-class.md)