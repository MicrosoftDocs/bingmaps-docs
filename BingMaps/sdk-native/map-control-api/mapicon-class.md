---
title: "MapIcon Class | Microsoft Docs"
ms.author: "pablocan"
---

# MapIcon Class

Displays a graphical image and optional text on the Map.

See [Icons](../map-control-concepts/map-icons.md) for more details on capabilities of the MapIcon class.

**Android**

>```java
> class MapIcon extends MapElement
>```

**iOS**

>```objectivec
> @interface MSMapIcon : MSMapElement
>```

## Properties

<!--
Allow drop feature is cut for V1 of the SDK.

### AllowDrop

Whether this icon can be drop target for purposes of drag-and-drop operation. The default value is `false`.

**Android**

>```java
> boolean isAllowDrop()
> void setAllowDrop(boolean)
>```

**iOS**

>```objectivec
> @property (nonatomic) BOOL allowDrop
>```
-->

### DesiredCollisionBehavior

Specifies the behavior of the icon when it collides with other map features due to zoom level.  
The default value is `MapElementCollisionBehavior.REMAIN_VISIBLE`.

_See also:_ [MapElementCollisionBehavior](MapElementCollisionBehavior-enumeration.md)

**Android**

>```java
> MapElementCollisionBehavior getDesiredCollisionBehavior()
> void setDesiredCollisionBehavior(MapElementCollisionBehavior behavior)
>```

**iOS**

>```objectivec
> @property (nonatomic) MSMapElementCollisionBehavior desiredCollisionBehavior
>```


### Flat

Determines whether the icon should appear to lie parallel and flat to the earth, versus standing up and facing the user. The default is false.

**Android**

>```java
> boolean isFlat()
> void setFlat(boolean isFlat)
>```

**iOS**

>```objectivec
> @property (nonatomic) BOOL flat
>```


### Flyout

Specifies the flyout associated with this icon.

_See also:_ [MapFlyout](mapflyout-class.md)

**Android**

>```java
> @Nullable MapFlyout getFlyout()
> void setFlyout(@Nullable MapFlyout flyout)
>```

**iOS**

>```objectivec
> @property (nonatomic, nullable) MSMapFlyout *flyout
>```


### Image

Specifies the image associated with this icon.

_See also:_ [MapImage](MapImage-class.md)

**Android**

>```java
> @Nullable MapImage getImage()
> void setImage(@Nullable MapImage image)
>```

**iOS**

>```objectivec
> @property (nullable, nonatomic) MSMapImage *image
>```

_Passing null/nil will reset the icon to use the default image._


### Location

Specifies the location of the icon.

_See also:_ [MSGeopoint](Geopoint-class.md)

**Android**

>```java
> Geopoint getLocation()
> void setLocation(Geopoint location)
>```

**iOS**

>```objectivec
> @property (nonatomic) MSGeopoint *location
>```


### NormalizedAnchorPoint

Specifies the anchor point for the icon. The anchor point is the point on the icon that is positioned at the geographic
location specified by Location property. For example, for a pin icon this generally will be the tip of the pin.  
`(0, 0)` represents the upper left corner of the graphical image, while `(1, 1)` represents its bottom right corner. The
default value is `(0.5, 0.5)`.

_See also:_ [Anchoring MapIcons](../map-control-concepts/anchoring-mapIcons.md)

**Android**

>```java
> android.graphics.PointF getNormalizedAnchorPoint()
> void setNormalizedAnchorPoint(android.graphics.PointF point)
>```

**iOS**

>```objectivec
> @property (nonatomic) CGPoint normalizedAnchorPoint
>```


### Opacity

Specifies the opacity of the rendered icon, in addition to any transparency defined in the image.  
`1` means completely opaque, and `0` means completely transparent. The default value is `1`.

**Android**

>```java
> float getOpacity()
> void setOpacity(float opacity)
>```

**iOS**

>```objectivec
> @property (nonatomic) float opacity
>```


### Rotation

Specifies the rotation in degrees of the icon around the anchor point clockwise. Values greater than `360` or less than
`0` are accepted. The default is `0` (no rotation).

**Android**

>```java
> float getRotation()
> void setRotation(float)
>```

**iOS**

>```objectivec
> @property (nonatomic) float rotation
>```


### Title

Specifies the text to be displayed alongside the icon.

**Android**

>```java
> String getTitle()
> void setTitle(String title)
>```

**iOS**

>```objectivec
> @property (nonatomic) NSString *title
>```

## See Also

* [Icons](../map-control-concepts/map-icons.md)
* [MapElement](mapelement-class.md)
* [MapFlyout class](mapflyout-class.md)
