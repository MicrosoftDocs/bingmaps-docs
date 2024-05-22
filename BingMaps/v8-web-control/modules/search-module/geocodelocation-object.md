---
title: "GeocodeLocation Object | Microsoft Docs"
description: Describes the GeocodeLocation object, which represents a geocode location, and provides a list of properties.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 07b6295e-58c5-46bc-ba4f-b4ba01095dc0
caps.latest.revision: 6
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# GeocodeLocation Object

[!INCLUDE [bing-maps-web-control-sdk-retirement](../../../includes/bing-maps-web-control-sdk-retirement.md)]

Represents a geocode location object.

## Properties

Name              | Type                                                       | Description
----------------- | ---------------------------------------------------------- | -------------------------------------
`latitude`        | number                          | The latitude value of the location.
`longitude`        | number                          | The longitude value of the location.
`name`            | string                                                     | The name of this geocode location match.
`precision`       | string    | The precision of this geocode location match. Possible values:<br/><br/>&nbsp;&nbsp;• **Interpolated** - The geocode result was matched to a point on a road using interpolation.<br/>&nbsp;&nbsp;• **InterpolatedOffset** - The geocode result was matched to a point on a road using interpolation with an additional offset to shift the Location to the side of the street.<br/>&nbsp;&nbsp;• **Parcel** - The geocode result was matched to the center of a parcel.<br/>&nbsp;&nbsp;• **Rooftop** - The geocode result was matched to the rooftop of a building.
