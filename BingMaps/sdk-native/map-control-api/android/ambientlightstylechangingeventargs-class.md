---
title: "AmbientLightStyleChangingEventArgs Class | Microsoft Docs"
description: "AmbientLightStyleChangingEventArgs Class"
ms.author: "krihenri"
ms.author: "krihenri"
---

# AmbientLightStyleChangingEventArgs Class (Android only)

Event args for AmbientLightStyleChangingListener allowing changing or providing the map style sheet being changed to.

## Properties

### AmbientLightLevel

The new ambient light level.

>```java
> AmbientLightLevel getAmbientLightLevel()
>```

### NewMapStyleSheet

The new map style sheet being changed to. May be null if the MapView is not using one of the predefined map styles in the dark/light set or may be set
to null to indicate that the map style sheet should not change.

>```java
> @Nullable MapStyleSheet getNewMapStyleSheet()
> void setNewMapStyleSheet(@Nullable MapStyleSheet newMapStyleSheet)
>```

## See Also

* [AmbientLightLevel](ambientlightlevel-enumeration.md)
* [AmbientLightStyleChangingListener](ambientlightstylechanginglistener-interface.md)
* [MapView](../MapView-class.md)
