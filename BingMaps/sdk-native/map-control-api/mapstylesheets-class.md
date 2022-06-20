---
title: MapStyleSheets Class | Microsoft Docs
description: Describes the MapStyleSheets class for Android and iOS and provides the class's static methods and additional references.
ms.author: pablocan
---

# MapStyleSheets Class

Contains built-in MapStyleSheets for easily changing how the MapView is rendered.

**Android**

>```java
> public class MapStyleSheets
>```

**iOS**

>```objectivec
> @interface MSMapStyleSheets : NSObject
>```

## Static methods

### Empty

A map style that renders nothing. Useful if you want to display a custom set of tiles with no underlying map data.

**Android**

>```java
> static MapStyleSheet empty()
>```

**iOS**

>```objectivec
> + (MSMapStyleSheet *)empty
>```

### Aerial

A photorealistic map style with no labels, roads, or borders.

**Android**

>```java
> static MapStyleSheet aerial()
>```

**iOS**

>```objectivec
> + (MSMapStyleSheet *)aerial
>```

### AerialWithOverlay

A photorealistic map style with labels, roads, and borders.

**Android**

>```java
> static MapStyleSheet aerialWithOverlay()
>```

**iOS**

>```objectivec
> + (MSMapStyleSheet *)aerialWithOverlay
>```

### RoadDark

A road map style with a dark theme.

**Android**

>```java
> static MapStyleSheet roadDark()
>```


**iOS**

>```objectivec
> + (MSMapStyleSheet *)roadDark
>```

### RoadLight

A road map style with a light theme.

**Android**

>```java
> static MapStyleSheet roadLight()
>```

**iOS**

>```objectivec
> + (MSMapStyleSheet *)roadLight
>```

### RoadCanvasLight

A road map style with a light theme which has some of the details such as hill shading disabled.

**Android**

>```java
> static MapStyleSheet roadCanvasLight()
>```

**iOS**

>```objectivec
> + (MSMapStyleSheet *)roadCanvasLight
>```

### RoadHighContrastDark

A road map style with a light theme with a higher contrast than RoadDark.

**Android**

>```java
> static MapStyleSheet roadHighContrastDark()
>```

**iOS**

>```objectivec
> + (MSMapStyleSheet *)roadHighContrastDark
>```

### RoadHighContrastLight

A road map style with a light theme with a higher contrast than RoadLight.

**Android**

>```java
> static MapStyleSheet roadHighContrastLight()
>```

**iOS**

>```objectivec
> + (MSMapStyleSheet *)roadHighContrastLight
>```

## See Also

[MapStyleSheet](MapStyleSheet-class.md)