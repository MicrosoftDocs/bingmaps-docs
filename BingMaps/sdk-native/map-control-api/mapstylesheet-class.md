---
title: "MapStyleSheet Class | Microsoft Docs"
author: "pablocan"
---

# MapStyleSheet Class

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

### FromJson

Creates a new MapStyleSheet from an input string. Returns false in iOS and Optional.absent() in Android if the json was invalid.

**Android**

>```java
> static @Nullable MapStyleSheet fromJson(String json)
>```

**iOS**

>```objectivec
> + (BOOL)tryToParseJson:(NSString*)json intoStyleSheet:(MSMapStyleSheet * _Nullable * _Nonnull)styleSheet
>```

### Combine

Combines several MapStyleSheets into one.

**Android**

>```java
> static MapStyleSheet combine(Iterable<MapStyleSheet> mapStyleSheets)
>```

**iOS**

>```objectivec
> + (instancetype)combineStyleSheets:(NSArray*)styleSheetsToCombine
>```

## See Also

[Changing the appearance of a map](../map-control-concepts/map-styles-sheets.md)
