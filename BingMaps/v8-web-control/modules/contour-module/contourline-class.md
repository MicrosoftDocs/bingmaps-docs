---
title: "ContourLine Class | Microsoft Docs"
description: Describes the ContourLine class, which extends from the Polygon class and supports all the same methods and events, but has a different constructor.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: aa735bcb-3761-4e51-87e4-d3e097aae52b
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# ContourLine Class

The ContourLine class extends from the [Polygon](../../map-control-api/polygon-class.md) class and supports all the same methods and events, but has a different constructor. The constructor takes in an array of locations that specify the outline boundary of the contour line. Optionally a value can be associated with the contour line which is passed to the `colorCallback` and used to colorize the contour.

## Constructor

> ContourLine(boundary: [Location](../../map-control-api/location-class.md)\[\], contourValue?: number | string)

## Properties 

| Name         | Type            | Description                                                                   |
|--------------|-----------------|-------------------------------------------------------------------------------|
| `contourValue` | number _or_ string | A value that is passed to the `colorCallback` and used to colorize the contour. |
