---
title: MapFlyout Class | Microsoft Docs
description: Describes the MapFlyout class for Android and iOS and provides the class' properties, methods, and additional references.
ms.author: pablocan
---

# MapFlyout Class

[!INCLUDE [bing-maps-sdk-for-android-iOS-retirement](../../includes/bing-maps-sdk-for-android-iOS-retirement.md)]

Represents a user control that displays lightweight informational UI.

**Android**

>```java
> public class MapFlyout
>```

**iOS**

>```objectivec
> @interface MSMapFlyout : NSObject
>```

## Properties

### Visible

Whether flyout is currently being displayed.

**Android**

>```java
> boolean isVisible()
>```

**iOS**

>```objectivec
> @property (nonatomic, readonly) BOOL visible
>```


### Title

Primary text to be displayed on flyout's default view. Can be null; empty string is treated as null.

**Android**

>```java
> @Nullable String getTitle()
> void setTitle(@Nullable String title)
>```

**iOS**

>```objectivec
> @property (nonatomic, nullable) NSString *title
>```

### Description

Secondary text to be displayed on flyout's default view. Can be null; empty string is treated as null.

**Android**

>```java
> @Nullable String getDescription()
> void setDescription(@Nullable String description)
>```

**iOS**

>```objectivec
> @property (nonatomic, nullable) NSString *description
>```

### NormalizedAnchorPoint

Point on the flyout that will be used as its anchor.  
Possible values range between `(0, 0)` and `(1, 1)`. The default is `(0.5, 1.0)` (bottom center).

**Android**

>```java
> android.graphics.PointF getNormalizedAnchorPoint()
> void setNormalizedAnchorPoint(android.graphics.PointF point)
>```

**iOS**

>```objectivec
> @property (nonatomic) CGPoint normalizedAnchorPoint
>```

### NormalizedRelativePosition

Point on the associated MapIcon that the flyout will be anchored to.  
Possible values range between `(0, 0)` and `(1, 1)`. The default is `(0.5, 0.0)` (top center).

**Android**

>```java
> android.graphics.PointF getNormalizedRelativePosition()
> void setNormalizedRelativePosition(android.graphics.PointF position)
>```

**iOS**

>```objectivec
> @property (nonatomic) CGPoint normalizedRelativePosition
>```

### LightDismissEnabled

Whether flyout can be closed by tapping outside of it. *Defaults to true.*

**Android**

>```java
> boolean isLightDismissEnabled()
> void setLightDismissEnabled(boolean enabled)
>```

**iOS**

>```objectivec
> @property (nonatomic) BOOL lightDismissEnabled
>```

### CustomViewAdapter

Provides custom view for the flyout. If set to null, the default view with flyout's title and description will be used.  
***Important: View will be rendered on canvas, with interactive elements no longer interactive.***

**Android**

>```java
> void setCustomViewAdapter(@Nullable MapFlyout.CustomViewAdapter adapter)
>```

**iOS**

>```objectivec
> @property (nonatomic) MSMapFlyoutCustomViewAdapter customViewAdapter
>```

_See also:_ [MapFlyoutCustomViewAdapter](mapflyoutcustomviewadapter-interface.md)

## Methods

### Show

Shows the flyout at the specified relative position. If another flyout is active at the time, it will be hidden.

**Android**

>```java
> void show()
>```

**iOS**

>```objectivec
> - (void)show
>```


### Hide

Hides the flyout.

**Android**

>```java
> void hide()
>```

**iOS**

>```objectivec
> - (void)hide
>```


### StyleDefaultView

Styles default view with customizable background color and text color in ARGB format. The default background color is dark gray (0xff555555) and text color is white (0xffffffff)

**Android**

>```java
> void styleDefaultView(int colorBackground, int colorText)
>```

**iOS**

>```objectivec
> - (void)styleDefaultViewWithBackgroundColor:(UIColor*)backgroundColor textColor:(UIColor*)textColor
>```

## See Also

* [MapFlyoutCustomViewAdapter](mapflyoutcustomviewadapter-interface.md)
