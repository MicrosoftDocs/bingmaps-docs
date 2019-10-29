---
title: "MapElement Class | Microsoft Docs"
author: "bmnxplat"
---

# MapElement Class

Represents an element displayed on a MapControl.

**Android**

>```java
> public abstract class MapElement
>```

**iOS**

>```objectivec
> @interface MSMapElement : NSObject
>```

## Properties

### Tag

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

### Visible

Whether the item is visible or not.

**Android**

>```java
> boolean isVisible()
> void setVisible(boolean visible)
>```

**iOS**

>```objectivec
> @property (nonatomic) BOOL visible
>```

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

## See Also

* [MapIcon](MapIcon-class.md)
* [MapPolyline](MapPolyline-class.md)
* [MapPolygon](MapPolygon-class.md)
