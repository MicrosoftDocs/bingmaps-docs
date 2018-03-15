---
title: "IPrimitiveChangedEventArgs Object | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: c544bef3-eb99-4f29-b4df-23bb14e79271
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms:service: "bing-maps"
---
# IPrimitiveChangedEventArgs Object
A IPrimitiveChangedEventArgs object that is returned when a **changed** event occurs on an IPrimitve shape.

## Properties

| Name       | Type       | Description                                                    |
|------------|------------|----------------------------------------------------------------|
| `name`     | string     | The IPrimitive shape the event occured on.                     |
| `sender`   | [IPrimitive](../v8-web-control/iprimitive-class.md) | The name of the change that occured; 'locations' or 'options'. |