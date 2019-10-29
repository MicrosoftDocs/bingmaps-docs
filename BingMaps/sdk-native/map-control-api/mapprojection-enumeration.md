---
title: "MapProjection Enumeration | Microsoft Docs"
author: "bmnxplat"
---

# MapProjection Enumeration

Controls how the map projects the world onto the screen.

**Android**

>```java
> enum MapProjection
> {
>     WEB_MERCATOR,
>     GLOBE
> }
>```

**iOS**

>```objectivec
> typedef NS_ENUM(NSInteger, MSMapProjection)
> {
>     MSMapProjectionMercator,
>     MSMapProjectionGlobe,
> }
>```

## Values

### Web mercator

Uses the web mercator projection common to many map rendering engines. Because of limitations of the projection the poles cannot be rendered in this projection.

### Globe

The earth is displayed as a globe allowing the whole earth to be viewed. 