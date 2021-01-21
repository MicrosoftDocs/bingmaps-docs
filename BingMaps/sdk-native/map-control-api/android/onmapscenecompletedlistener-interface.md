---
title: "OnMapSceneCompletedListener Interface | Microsoft Docs"
author: "pablocan"
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
