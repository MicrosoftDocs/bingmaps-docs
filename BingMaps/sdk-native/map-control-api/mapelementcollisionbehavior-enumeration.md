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

## Values

### Hide

 Hide the MapIcon when it collides with other map elements

### RemainVisible

Show MapIcon at all zoom levels. REMAIN_VISIBLE applies to the MapIcon image only. Text from the map icon may still be hidden at times.
Even when the I's CollisionBehaviorDesired property is set to REMAIN_VISIBLE

### RemainAlwaysVisible

Always show the map point. If it collides with base or user map entities, it is overlapped with them.
This applies to the map point image only. Text from the map point may still be hidden at times by another
user map elements (but not by base map elements)

## See Also

* [MapIcon](MapIcon-class.md)