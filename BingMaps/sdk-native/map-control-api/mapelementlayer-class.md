---
title: "MapElementLayer Class | Microsoft Docs"
author: "bmnxplat"
---

# MapElementLayer Class

Displays primitives on the map.  The z-order of a primitive is in order of insertion (last inserted object will be on the top).

**Android**

>```java
> class MapElementLayer extends MapLayer
>```

**iOS**

>```objectivec
> @interface MSMapElementLayer : MSMapLayer
>```

## Events

### MapElementTapped

Occurs when the user taps a [MapElement](mapelement-class.md) that has been add to the MapElementsLayer.

**Android**

>```java
> void addOnMapElementTappedListener(OnMapElementTappedListener listener)
> void removeOnMapElementTappedListener(OnMapElementTappedListener listener)
>```
 
_See also:_ [OnMapElementTappedListener](Android/OnMapElementTappedListener-interface.md)

**iOS**

>```objectivec
> - (MSMapHandlerId)addUserDidTapHandler:(MSMapElementLayerUserDidTapHandler)handler
> - (BOOL)removeUserDidTapHandler:(MSMapHandlerId)handlerId
>```

_See also:_ [MSMapElementLayerUserDidTapHandler](iOS/MSMapElementLayerUserDidTapHandler-interface.md)

## Properties

### elements

The map elements in this layer. This collection may be freely modified.
_See also:_ [MapElementCollection](MapElementCollection-class.md)

**Android**

>```java
> MapElementCollection getElements()
>```

**iOS**

>```objectivec
> @property (nonatomic, readonly) MSMapElementCollection *elements
>```

## See also

* [MapLayer](MapLayer-class.md)
* [MapElement](MapElement-class.md)
