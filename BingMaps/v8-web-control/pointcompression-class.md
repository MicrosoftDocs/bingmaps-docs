---
title: "PointCompression Class | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 355afb32-ca53-4fb0-b16e-d29ff931721a
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# PointCompression Class
This is a static class that provides a compression algorithm to encodes/decodes a collection of Location objects into a string and back. This algorithm is used for generating a compressed collection of locations for use with the Bing Maps REST Elevation Service. This algorithm is also used for decoding the compressed coordinates returned by the GeoData API. Note that the `GeoDataAPIManager` automatically converts the compressed polygon rings in the `Primatives` property of the response into a Polygon object for you. In addition to the REST Elevation service and the GeoData API this class can be also be used to encode/decode your own data. The encoded data is much smaller than most other formats such as GeoJSON or Well Known Text which is useful if passing data between a client application and a server. The algorithm for decoding the string is documented [here](geodata-api.md), and encoding is documented [here](../rest-services/elevations/point-compression-algorithm.md).

## Static Methods

| Name                  | Return Value | Description                                                   |
|-----------------------------|--------------|---------------------------------------------------------------|
| decode(value: string)        | [Location](../v8-web-control/location-class.md)\[\] | Decodes a collection of coordinates from a compressed string. |
| encode(points: [Location](../v8-web-control/location-class.md)\[\]) | string       | Encodes a collection of coordinates into a compressed string. |

## See Also

* [Point Compression Example](../v8-web-control/point-compression-example.md)