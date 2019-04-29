
# MapStyleSheet class

Represents a set of rules that define the style of the map in a map control.

**Android**

>```java
> public class MapStyleSheet
>```

**iOS**

>```objectivec
> @interface MSMapStyleSheet : NSObject
>```

## Static methods

### fromJson

Creates a new MapStyleSheet from an input string. Returns false in iOS and Optional.absent() in Android if the json was invalid.

**Android**

>```java
> public static Optional<MapStyleSheet> fromJson(String json)
>```

**iOS**

>```objectivec
> + (BOOL)tryToParseJson:(NSString*)json intoStyleSheet:(MSMapStyleSheet * _Nullable * _Nonnull)styleSheet
> ```  

### combine

Combines several MapStyleSheets into one.

**Android**

>```java
> public static MapStyleSheet combine(Iterable<MapStyleSheet> mapStyleSheets)
>```

**iOS**

>```objectivec
> + (instancetype)combineStyleSheets:(NSArray*)styleSheetsToCombine
>```

## Built-in MapStyleSheets (iOS only)

For Android, please use [MapStyleSheets](MapStyleSheets.md)
### empty

A map style that renders nothing. Useful if you want to display a custom set of tiles with no underlying map data.

>```java
> public static MapStyleSheet combine(Iterable<MapStyleSheet> mapStyleSheets)
>```

**iOS**

>```objectivec
> + (instancetype)empty
>```

### aerial

A photorealistic map style with no labels, roads, or borders. 

>```objectivec
> + (instancetype)aerial
>```

### AerialWithOverlay

A photorealistic map style with labels, roads, and borders.

>```objectivec
> + (instancetype)aerialWithOverlay
>```

### roadLight

A road map style with a light theme.

>```objectivec
> + (instancetype)roadLight
>```

### roadCanvasLight

A road map style with a light theme which has some of the details such as hill shading disabled.

>```objectivec
> + (instancetype)roadCanvasLight
>```

### roadDark

A road map style with a dark theme.

>```objectivec
> + (instancetype)roadDark
>```

### roadHighContrastLight

A road map style with a light theme with a higher contrast than RoadLight.

>```objectivec
> + (instancetype)roadHighContrastLight
>```

### roadHighContrastDark

A road map style with a light theme with a higher contrast than RoadDark.

>```objectivec
> + (instancetype)roadHighContrastDark
>```


## See also
* [Changing the appearance of a map](../map-control-concepts/Change_map_styles.md)
