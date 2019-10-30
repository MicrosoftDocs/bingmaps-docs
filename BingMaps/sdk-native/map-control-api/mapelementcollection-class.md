---
title: "MapElementCollection Class | Microsoft Docs"
author: "pablocan"
---

# MapElementCollection Class

Contains all the elements that have been added to the map.

**Android**

>```java
> class MapElementCollection implements Iterable<MapElement>
>```

**iOS**

>```objectivec
> @interface MSMapElementCollection : NSObject<NSFastEnumeration>
>```

## Methods

### add

Adds a MapIcon, MapPolyline, or MapPolygon to the MapView. Returns false if the MapElement is already in the MapView.

**Android**

>```java
> boolean add(MapElement element)
>```

**iOS**

>```objectivec
> - (BOOL)addMapElement:(MSMapElement *)mapElement
>```

### clear

Removes all elements from the collection.

**Android**

>```java
> void clear()
>```

**iOS**

>```objectivec
> - (void)clear
>```

### contains

Returns true if the collection contains the specified element.

**Android**

>```java
> boolean contains(MapElement element)
>```

**iOS**

>```objectivec
> - (BOOL)contains:(MSMapElement*)mapElement

### iterator (Android only)

Allows enumerating over the elements in the collection.

>```java
> Iterator<MapElement> iterator()
>```

### insert

Insert the specified element at the specified index.

**Android**

>```java
> void add(int index, MapElement element)
>```

**iOS**

>```objectivec
> - (void)insertMapElement:(MSMapElement *)mapElement atIndex:(NSInteger)index
>```

### remove

Removes the specified element from the collection.

**Android**

>```java
> boolean remove(MapElement element)
>```

**iOS**

>```objectivec
> - (BOOL)removeMapElement:(MSMapElement *)mapElement
>```

### removeAtIndex

Removes element at the specified index from the collection.

**Android**

>```java
> void remove (int index)
>```

**iOS**

>```objectivec
> - (void)removeMapElementAtIndex:(NSUInteger)index
>```

## Properties

### size

Returns the number of items in the collection.

**Android**

>```java
>  public int size()
>```

**iOS**

>```objectivec
> @property (readonly) NSUInteger count
>```

## Notes

### Sequence protocol in Swift

In Swift, to be able to iterate through `MSMapElementCollection` using a `for-in` loop, you will need to add the following extension that conforms to the required `Sequence` protocol.

>```swift
> extension MSMapElementCollection: Sequence {
>     public func makeIterator() -> NSFastEnumerationIterator {
>         return NSFastEnumerationIterator(self)
>     }
> }
>```

## See Also

* [MapView](MapView-class.md)
* [MapElement](MapElement-class.md)
* [MapIcon](MapIcon-class.md)
* [MapPolyline](MapPolyline-class.md)
* [MapPolygon](MapPolygon-class.md)
