---
title: "InfoboxEventArgs Object | Microsoft Docs"
description: A description of the InfoboxEventArgs Object, an object containing information about an infobox event, including a table with descriptions for each of its properties.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 655de4f3-459f-43bb-9ab3-66cca4624f21
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# InfoboxEventArgs Object

An object that contains information about an infobox event.

| Name       | Type    | Description                                                                 |
|------------|---------|-----------------------------------------------------------------------------|
| `eventName`  | string  | The event that occurred.                                                    |
| `originalEvent` | MouseEvent | The original JavaScript mouse event object.                           |
| `pageX`      | number  | The x-value of the pixel coordinate on the page of the mouse cursor.        |
| `pageY`      | number  | The y-value of the pixel coordinate on the page of the mouse cursor.        |
| `target`     | [Infobox](infobox-class.md) | The infobox object that fired the event.              |
| `targetType` | string  | The type of the object that fired the event. This will always be 'infobox'. |