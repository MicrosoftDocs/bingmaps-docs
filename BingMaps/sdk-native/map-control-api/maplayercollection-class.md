---
title: MapLayerCollection Class | Microsoft Docs
description: Describes the MapLayerCollection class for Android and iOS and provides the class' properties, methods, and additional references.
ms.author: pablocan
---

# MapLayerCollection Class

[!INCLUDE [bing-maps-sdk-for-android-iOS-retirement](../../includes/bing-maps-sdk-for-android-iOS-retirement.md)]

Contains all the layers that have been added to the map.

**Android**

>```java
> class MapLayerCollection implements Iterable<MapLayer>
>```

**iOS**

>```objectivec
> @interface MSMapLayerCollection : NSObject<NSFastEnumeration>
>```

## Properties

### Size

Returns the number of MapLayers in the collection.

**Android**

>```java
> int size()
>```

**iOS**

>```objectivec
> @property (readonly) NSUInteger count
>```

## Methods

### Add

Adds a MapLayer to the collection.

**Android**

>```java
> boolean add(MapLayer layer)
>```

**iOS**

>```objectivec
> - (BOOL)addMapLayer:(MSMapLayer *)mapLayer
>```

### Clear

Removes all MapLayers from the collection

**Android**

>```java
> void clear()
>```

**iOS**

>```objectivec
> - (void)clear
>```

### Contains

Returns true if the collection contains the specified layer.

**Android**

>```java
> boolean contains(MapLayer layer)
>```

**iOS**

>```objectivec
> - (BOOL)contains:(MSMapLayer *)mapLayer
>```

### Insert

Insert the specified layer at the specified index.

**Android**

>```java
> void add(int index, MapLayer layer)
>```

**iOS**

>```objectivec
> - (void)insertMapLayer:(MSMapLayer *)mapLayer atIndex:(NSInteger)index
>```

### Remove

Removes the specified MapLayer from the collection and and returns whether it was removed or not/ 

**Android**

>```java
> boolean remove(MapLayer layer)
>```

**iOS**

>```objectivec
> - (BOOL)removeMapLayer:(MSMapLayer *)mapLayer
>```

### RemoveAtIndex

Removes a MapLayer at the specified index from the collection.

**Android**

>```java
> void remove(int index)
>```

**iOS**

>```objectivec
> - (BOOL)removeMapLayeAtIndexr:(NSUInteger)index
>```

## See Also

* [MapLayer](MapLayer-class.md)