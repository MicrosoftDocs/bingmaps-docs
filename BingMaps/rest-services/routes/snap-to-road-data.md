---
title: "Snap to Road Data | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 72f560c2-f49b-49a6-820e-a28521b856f2
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Snap to Road Data

The response returned by the Snap to Road API contains either an `SnapToRoadResponse` resource or an `RouteProxyAsyncStatus` resource. The `SnapToRoadResponse` contains the snapped point data while the `RouteProxyAsyncStatus` contains status information about an asynchronous request that was made for an isochrone. The following tables provide the descriptions of the `SnapToRoadResponse` resource fields.

[!INCLUDE [get-common-response-note](../../includes/get-common-response-note.md)]

## SnapToRoadResponse Resource

Represents a list of snapped or interpolated points returned by the Snap to Road API.

| JSON          | XML           | Type             | Description                                               |
|---------------|---------------|------------------|-----------------------------------------------------------|
| snappedPoints | SnappedPoints | SnappedPoint\[\] | The array of points that have been snapped as well as any points added through interpolation. |

## SnappedPoint Class

Represents a snapped or interpolated point.

| JSON            | XML             | Type       | Description                    |
|-----------------|-----------------|------------|--------------------------------|
| coordinate      | Coordinate      | Coordinate | The coordinate in which a point was snapped to or an interpolated point.   |
| index           | Index           | integer    | The index in the original list of points passed into the query that this snapped point corresponds to. Can be a value between -1 and the number of points – 1. The index will be set to -1 when the point is an interpolated point and not one of the snapped input points. |
| name            | Name            | string     | The name of the street this snapped point lies on, if available. |
| speedLimit      | SpeedLimit      | double?    | The posted speed limit. There are some special values which may be returned:<br/><br/> • Null – Speed limit not requested.<br/> • 0 – Speed limit unavailable. |
| truckSpeedLimit | TruckSpeedLimit | double?    | The posted truck speed limit. There are some special values which may be returned:<br/> <br/> • Null – Truck speed limit not requested.<br/> • 0 – Truck speed limit unavailable, consider using standard speed limit.<br/> • -1 - The road does not allow trucks.  |

## See Also

* [Using the REST Services with .NET](../using-the-rest-services-with-net.md)
* [Snap to Road Example](../examples/snap-to-road-example.md)
