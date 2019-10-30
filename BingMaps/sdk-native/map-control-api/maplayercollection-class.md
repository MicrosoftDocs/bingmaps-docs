---
title: "MapLayerCollection Class | Microsoft Docs"
author: "pablocan"
---

# MapLayerCollection Class

Contains all the layers that have been added to the map.

**Android**

>```java
> class MapLayerCollection implements Iterable<MapLayer>
>```

**iOS**

>```objectivec
> @interface MSMapLayerCollection : NSObject<NSFastEnumeration>
>```

## Methods

### add

Adds a MapLayer to the collection.

**Android**

>```java
> boolean add(MapLayer layer)
>```

**iOS**

>```objectivec
> - (BOOL)addMapLayer:(MSMapLayer *)mapLayer
>```

### clear

Removes all MapLayers from the collection

**Android**

>```java
> void clear()
>```

**iOS**

>```objectivec
> - (void)clear
>```

### contains

Returns true if the collection contains the specified layer.

**iOS**

>```objectivec
> - (BOOL)contains:(MSMapLayer *)mapLayer
>```

### insert

Insert the specified layer at the specified index.

**Android**

>```java
> void add(int index, MapLayer layer)
>```

**iOS**

>```objectivec
> - (void)insertMapLayer:(MSMapLayer *)mapLayer atIndex:(NSInteger)index
>```

### remove

Removes the specified MapLayer from the collection and and returns whether it was removed or not/ 

**Android**

>```java
> boolean remove(MapLayer layer)
>```

**iOS**

>```objectivec
> - (BOOL)removeMapLayer:(MSMapLayer *)mapLayer
>```

### removeAtIndex

Removes a MapLayer at the specified index from the collection.

**Android**

>```java
> void remove(int index)
>```

**iOS**

>```objectivec
> - (BOOL)removeMapLayeAtIndexr:(NSUInteger)index
>```

## Properties

### size

Returns the number of MapLayers in the collection.

**Android**

>```java
> int size()
>```

**iOS**

>```objectivec
> @property (readonly) NSUInteger count
>```

## See also

* [MapLayer](MapLayer-class.md)