---
title: "MSMapDidChangeSceneCallback Interface | Microsoft Docs"
ms.author: "pablocan"
---

# MSMapDidChangeSceneCallback Interface (iOS only)

Callback interface to notify when the map scene has successfully changed after asyncronous methods such as MapView.beginRotate, MapView.beginSetScene.

>```objectivec
> typedef void (^MSMapDidChangeSceneCallback)(bool result)
>```

## See Also

* [MapView](../MapView-class.md)