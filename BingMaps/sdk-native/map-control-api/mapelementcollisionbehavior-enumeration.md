---
title: "MapElementCollisionBehavior Enumeration | Microsoft Docs"
author: "pablocan"
---

# MapElementCollisionBehavior Enumeration

Specifies the behavior of a MapIcon when it collides with other map features due to zoom level.

**Android**

>```java
> public enum MapElementCollisionBehavior
> {
>     HIDE,
>     REMAIN_VISIBLE,
>     REMAIN_ALWAYS_VISIBLE
> }
>```

**iOS**

>```objectivec
> typedef NS_ENUM(NSInteger, MSMapElementCollisionBehavior)
> {
>     MSMapElementCollisionBehaviorHide,
>     MSMapElementCollisionBehaviorRemainVisible,
>     MSMapElementCollisionBehaviorRemainAlwaysVisible
> }
>```

## Values

### Hide

Hide the MapIcon when it collides with other map elements.

### RemainVisible

Show MapIcon at all zoom levels. Applies to the map icon image only.
If it collides with base or user map elements, its icon can be overlapped with them. Text for the map icon may still be hidden at times.

### RemainAlwaysVisible

Show MapIcon at all zoom levels. Applies to the map icon image and text.
If it collides with base or user map elements, its icon and text can be overlapped with them. Text for the map icon may still be hidden at times by other user map elements (but not by base map elements).

## See Also

* [MapIcon](MapIcon-class.md)
