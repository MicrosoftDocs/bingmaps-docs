
# MapFlyout Class

Represents a user control that display lightweight UI that is either information or requires user interaction.

**Android**

>```java
> public class MapFlyout
>```

**iOS**

>```objectivec
> @interface MSMapFlyout : UIView
>```

_See also:_ [UIView](https://developer.apple.com/documentation/uikit/uiview)

## Properties

### Description (Android only)

The description to be displayed on the default flyout.  This is ignored if custom template selector (Android only) is used.

>```java
> String getDescription()  
> void setDescription(String description)
>```

### PlacementOffset

Relative location of the flyout compared to the MapIcon it is anchored to. The x and y offset range between (0, 0) and (1, 1). The default is (0.5, 0.0) which is the top center. 

**Android**

>```java
> android.graphics.PointF getPlacementOffset()
> void setPlacementOffset(android.graphics.PointF placementOffset)
>```

**iOS**

>```objectivec
> @property (nonatomic) CGPoint placementOffset
>```

### LightDismissEnabled (Android only)

Whether the flyout can be closed by clicking or tapping off of it. The default is true.

>```java
> boolean getLightDismissEnabled()  
> void setLightDismissEnabled(boolean lightDismissEnabled)
>```

### Title (Android only)

The title to be displayed on the default flyout. This is ignored if a custom template selector (Android only) is used.

>```java
> String getTitle()  
> void setTitle (String title)
>```

## Methods

### setTemplateSelector (Android only)

Sets template selector for the flyout.

>```java
> void setTemplateSelector(MapFlyout TemplateSelector selector)
>```

## Events

### Tapped (Android only)

Fired when the flyout is tapped by the user.

>```java
> void addOnTappedListener(OnMapFlyoutTappedListener listener)  
> void removeOnTappedListener(OnMapFlyoutTappedListener listener)
>```