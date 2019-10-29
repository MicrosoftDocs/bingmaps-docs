---
title: "OnMapSceneCompletedListener Interface | Microsoft Docs"
author: "bmnxplat"
---

# OnMapSceneCompletedListener Interface (Android only)

Callback interface to notify when the map scene has successfully changed after asyncronous methods such as MapView.beginRotate, MapView.beginSetScene.

>```java
> public interface OnMapSceneCompletedListener
> {
>     public void onMapSceneCompleted(boolean succeeded);
> }
>```

## See also

* [MapView](../MapView-class.md)