---
title: MapElementLayer Class | Microsoft Docs
description: Describes the MapElementLayer class for Android and iOS and provides the class' properties, events, and additional references.
ms.author: pablocan
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

## Properties

### Elements

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

## Events

### MapElementTapped

Occurs when the user taps a [MapElement](mapelement-class.md) that has been added to the MapElementLayer.

**Android**

>```java
> void addOnMapElementTappedListener(OnMapElementTappedListener listener)
> void removeOnMapElementTappedListener(OnMapElementTappedListener listener)
>```
 
_See also:_ [OnMapElementTappedListener](Android/OnMapElementTappedListener-interface.md)

**iOS**

>```objectivec
> - (MSMapHandlerId)addUserDidTapElementHandler:(MSMapElementLayerUserDidTapElementHandler)handler
> - (BOOL)removeUserDidTapElementHandler:(MSMapHandlerId)handlerId
>```

_See also:_ [MSMapElementLayerUserDidTapElementHandler](iOS/MSMapElementLayerUserDidTapElementHandler-interface.md)

*DEPRECATED*  
Use ```addUserDidTapElementHandler``` and ```removeUserDidTapElementHandler``` instead.

>```objectivec
> - (MSMapHandlerId)addUserDidTapHandler:(MSMapElementLayerUserDidTapHandler)handler
> - (BOOL)removeUserDidTapHandler:(MSMapHandlerId)handlerId
>```

_See also:_ [MSMapElementLayerUserDidTapHandler](iOS/MSMapElementLayerUserDidTapHandler-interface.md)

### MapFlyoutTapped

Occurs when the user taps a [MapFlyout](mapflyout-class.md) that has been added to the MapElementLayer.

**Android**

>```java
> void addOnMapFlyoutTappedListener(OnMapFlyoutTappedListener listener)
> void removeOnMapFlyoutTappedListener(OnMapFlyoutTappedListener listener)
>```
 
_See also:_ [OnMapFlyoutTappedListener](Android/OnMapFlyoutTappedListener-interface.md)

**iOS**

>```objectivec
> - (MSMapHandlerId)addUserDidTapFlyoutHandler:(MSMapElementLayerUserDidTapFlyoutHandler)handler
> - (BOOL)removeUserDidTapFlyoutHandler:(MSMapHandlerId)handlerId
>```

_See also:_ [MSMapElementLayerUserDidTapFlyoutHandler](iOS/MSMapElementLayerUserDidTapFlyoutHandler-interface.md)

## See Also

* [MapLayer](MapLayer-class.md)
* [MapElement](MapElement-class.md)
