---
title: "AnimatedFrameEventArgs Object | Microsoft Docs"
description: "The AnimatedFrameEventArgs Object provides the event arguments for when a layer frame is being loaded in an AnimatedTileLayer."
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 208e516f-27a0-446c-97cf-dbe75e4bed58
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# AnimatedFrameEventArgs Object

The event arguments for when a layer frame is being loaded in an [AnimatedTileLayer](animatedtilelayer-class.md).

| Name              | Type              | Description                                        |
|-------------------|-------------------|----------------------------------------------------|
| `animatedTileLayer` | [AnimatedTileLayer](animatedtilelayer-class.md) | The animated tile layer that the frame belongs to. |
| `index`             | number            | The index of the frame being loaded.               |
