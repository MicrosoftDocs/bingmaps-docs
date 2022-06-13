---
title: MSMapDidChangeSceneCallback Interface | Microsoft Docs
description: Describes the MSMapDidChangeSceneCallback interface for iOS and provides the interface's syntax and additional references.
ms.author: pablocan
---

# MSMapDidChangeSceneCallback Interface (iOS only)

Callback interface to notify when the map scene has successfully changed after asyncronous methods such as MapView.beginRotate, MapView.beginSetScene.

>```objectivec
> typedef void (^MSMapDidChangeSceneCallback)(bool result)
>```

## See Also

* [MapView](../MapView-class.md)