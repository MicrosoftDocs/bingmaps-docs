---
title: "EntityCollectionChangedEventArgs Object | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 4ebaa473-7632-42ec-a89b-e13ec245537a
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# EntityCollectionChangedEventArgs Object

**Deprecated**: This class is deprecated in Bing Maps V8. The new [Layer class](layer-class.md) should be used instead. This class is still available in V8, but has been added to provide partial backwards compatibility with V7 apps for simple use cases such as adding individual shapes directly to the map, rather than to a layer or collection.

Represents the event argument returned by the [EntityCollection](entitycollection-class.md) events.

## Properties

| Name       | Type                      | Description                                         |
|------------|---------------------------|-----------------------------------------------------|
| collection | [EntityCollection](entitycollection-class.md)          | The entity collection the event was triggered from. |
| data       | [IPrimitive](iprimitive-class.md) _or_ [IPrimitive](iprimitive-class.md)\[\] | The [IPrimitive](iprimitive-class.md) object that the event occurred for.  |
