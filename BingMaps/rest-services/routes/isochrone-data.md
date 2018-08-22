---
title: "Isochrone Data | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: a5ed1a3f-0ada-48a9-a2d3-442a73a114b2
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Isochrone Data

The response returned by the Isochrone API contains either an `IsochoneResponse` resource or an `RouteProxyAsyncStatus` resource. The `IsochroneResponse` contains the generated polygon isochrone data while the `RouteProxyAsyncStatus` contains status information about an asynchronous request that was made for an isochrone. The following tables provide the descriptions of the `IsochroneResponse` resource fields.

For more information about the common response syntax for the Bing Maps REST Services, see [Common Response Description](../common-response-description.md).

## IsochroneResponse Resource

The IsochroneResponse resource contains the polygons that represent the requested isochrone.

| JSON     | XML      | Type        | Description                                     |
|----------|----------|-------------|-------------------------------------------------|
| origin   | Origin   | Cooridnate  | The origin point used to calculate the isochrone area. |
| polygons | Polygons | Polygon\[\] | The polygons that represent the isochrone area. |

## Polygon Class

This class represents a polygon object.

| JSON        | XML         | Type               | Description     |
|-------------|-------------|--------------------|-----------------|
| coordinates | Coordinates | double\[\]\[\]\[\] | The coordinate rings that make up the polygon. Where double\[\] represents a single coordinate \[latitude, longitude\], and double\[\]\[\] represents a single ring within a polygon. |

## See Also

* [Using the REST Services with .NET](../using-the-rest-services-with-net.md)
* [Isochrone Example](../examples/isochrone-example.md)
