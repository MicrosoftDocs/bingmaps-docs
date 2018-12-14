---
title: "MapTypeEventArgs Object | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 7f33b8c1-1caa-4f87-93ce-b14ff55514ee
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# MapTypeEventArgs Object
A MapTypeEventArgs object that is returned by the map event handler when using the **maptypechanged** event.

## Properties


| Name         | Type      | Description                                                             |
|--------------|-----------|-------------------------------------------------------------------------|
| newMapTypeId | [MapTypeId](maptypeid-enumeration.md) | The map type that the map has changed to.                               |
| oldMapTypeId | [MapTypeId](maptypeid-enumeration.md) | The map type that the map has changed from.                             |
| target       | [Map](map-class.md)       | The map instance that fired the event.                                  |
| targetType   | string    | The type of the object that fired the event. This will always be 'map'. |
