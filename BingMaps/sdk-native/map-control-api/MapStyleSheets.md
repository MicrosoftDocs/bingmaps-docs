
# MapStyleSheets class (Android only)

Contains built-in MapStyleSheets for easily changing how the MapView is rendered.

## Static properties

### Empty

A map style that renders nothing. Useful if you want to display a custom set of tiles with no underlying map data.

>```java
> static MapStyleSheet empty()
> ```

### Aerial

A photorealistic map style with no labels, roads, or borders. 

>```java
> static MapStyleSheet aerial()
> ```

### AerialWithOverlay

A photorealistic map style with labels, roads, and borders.

>```java
> static MapStyleSheet aerialWithOverlay()
>```

### RoadLight

A road map style with a light theme.

>```java
> static MapStyleSheet roadLight()
>```

### RoadCanvasLight

A road map style with a light theme which has some of the details such as hill shading disabled.

>```java
> static MapStyleSheet roadCanvasLight()
>```

### RoadDark

A road map style with a dark theme.

>```java
> static MapStyleSheet roadDark()
>```

### RoadHighContrastLight

A road map style with a light theme with a higher contrast than RoadLight.

>```java
> static MapStyleSheet roadHighContrastLight()
>```

### RoadHighContrastDark

A road map style with a light theme with a higher contrast than RoadDark.

>```java
> static MapStyleSheet roadHighContrastDark()
>```

_See also_:
[MapStyleSheet](MapStyleSheet.md)