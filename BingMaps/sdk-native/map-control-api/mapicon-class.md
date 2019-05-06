
# MapIcon class

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

### AllowDrop

Whether this MapIcon can be drop target for purposes of drag-and-drop operation. Default is false.

**Android**

>```java
> boolean isAllowDrop()  
> void setAllowDrop(boolean)
>```

**iOS**

>```objectivec
> @property (nonatomic) BOOL allowDrop
>```  

### CollisionBehaviorDesired
Specifies the behavior of a MapIcon when it collides with other map features due to zoom level.
Default is set to MapElementCollisionBehavior.REMAIN_VISIBLE

**Android**

>```java
> MapElementCollisionBehavior getCollisionBehaviorDesired() 
> void setCollisionBehaviorDesired(MapElementCollisionBehavior behavior)
>```

**iOS**

>```objectivec
> @property (nonatomic) MSMapElementCollisionBehavior collisionBehaviorDesired
>```
_See also:_ [MapElementCollisionBehavior](MapElementCollisionBehavior-enumeration.md)

### Flyout

The flyout associated with this MapIcon.

**Android**

>```java
> MapFlyout getMapFlyout()
>```

**iOS**

>```objectivec 
> @property (nonatomic, nullable) MSMapFlyout *flyout
>```  

### Image

The image associated with this MapIcon.

_See also:_ [MapImage](MapImage-class.md)

**Android**

>```java
> MapImage getImage() 
> void setImage(MapImage image)
>```

**iOS**

>```objectivec
> @property (nonatomic) MSMapImage *image
>```  

### IsFlat

Determines whether the icon should appear to lie parallel and flat to the earth, versus standing up and facing the user. The default is false.

**Android**

>```java
> boolean getIsFlat()
> void setIsFlat(boolean isFlat)  
>```

**iOS**

>```objectivec
> @property (nonatomic) BOOL isFlat
>```  


### IsFlyoutVisible

Returns whether the flyout for this MapIcon is currently visible or not.

**Android**

>```java
> boolean getFlyoutShown()
>```

**iOS**

> ```objectivec
> @property (nonatomic) BOOL isFlyoutVisible
>```  


### Location

The location of the MapIcon.

_See also:_ [MSGeolocation](Geolocation-class.md)

**Android**

>```java
> Geolocation getLocation()
> void setLocation(Geolocation location)
>```

**iOS**

>```objectivec
> @property (nonatomic) MSGeolocation *location
>```  

### NormalizedAnchorPoint
The offset coordinate in pixels to display the icon relative to the selected location. (0,0) will place the upper left of the image at the location.

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

Determines whether the icon should render transparently. 1 means completely opaque, and 0 means completely transparent. This is in addition to any transparency defined in the image. The default is 1 (completely opaque).

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

The rotation in degrees of the icon around the anchor point clockwise. Values greater than 360 or less than 0 are accepted. The default is 0 (no rotation).

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

Text to be displayed along side the MapIcon.

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

[Icons](../map-control-concepts/map-icons.md)
