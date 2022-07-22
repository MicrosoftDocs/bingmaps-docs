---
title: OnMapSceneCompletedListener Interface | Microsoft Docs
description: Describes the OnMapSceneCompletedListener callback interface for Android and provides the MapView reference.
ms.author: pablocan
---

# OnMapSceneCompletedListener Interface (Android only)

Callback interface to notify when the map scene has successfully changed after asyncronous methods such as MapView.beginRotate, MapView.beginSetScene.

>```java
> public interface OnMapSceneCompletedListener
> {
>     void onMapSceneCompleted(boolean succeeded);
> }
>```

## See Also

* [MapView](../MapView-class.md)
