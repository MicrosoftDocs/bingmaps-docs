---
title: "MapRenderMode Enumeration | Microsoft Docs"
author: "pablocan"
---

# MapRenderMode Enumeration

Defines primary data source for rendering map.

**Android**
>```java
> public enum MapRenderMode
> {
>     RASTER,
>     VECTOR
> }
>```

**iOS**

>```objectivec
> typedef NS_ENUM(NSInteger, MSMapRenderMode)
> {
>     MSMapRenderModeRaster,
>     MSMapRenderModeVector
> }
>```

## Values

### Raster

Pre-rendered raster tiles are downloaded and used to display the map. This will generally give the fastest framerate.

### Vector

Vector data is downloaded and rendered client side to display the map. This will use less data for sustained map use since vector data covers a larger area
with a smaller amount of data than raster tiles. Labels are also rendered client side which makes them more readable since they are not scaled like
the background tiles.
