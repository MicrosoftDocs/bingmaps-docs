---
title: "Directly accessing the Bing Maps tiles | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: d9659e0f-0fd0-4661-8d03-9c93c5c38e38
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Directly accessing the Bing Maps tiles
Adding Bing Maps as a tile layer in a non-Bing Maps control can be done as outlined in this document. It should be noted that the tile URLs for Bing Maps change regularly and as such directly accessing tiles from a hardcoded URL is not allowed. It should also be noted that Bing Maps data cannot be integrated with competing mapping platforms as noted in the [terms of use](http://www.microsoft.com/maps/product/terms.html).

In order to access the Bing Maps tiles in a supported way you will first need to get the current tile URL's from the Bing Maps Imagery REST service every time your application starts. The main purpose of this is to ensure your application is using the latest tile URLs, which helps to prevent your application from breaking, and also provides a way to track the usage of the service in such a way that aligns with the Bing Maps terms of use. The [Bing Maps REST Imagery Medata service](../rest-services/get-imagery-metadata.md) can be used to get the current tile URLs. If you need to use this service from .NET, see the [Using the REST Services with .NET](../rest-services/using-the-rest-services-with-net.md) document. Making a request to the imagery service like this:

```
http://dev.virtualearth.net/REST/V1/Imagery/Metadata/Road?output=json&include=ImageryProviders&key=BingMapsKey
```

This will return a response that contains an Image URL property. This URL will look something like this:

```
http://ecn.{subdomain}.tiles.virtualearth.net/tiles/r{quadkey}.jpeg?g=129&mkt={culture}&shading=hill&stl=H ```
```

You can then replace the different parts of the URL to request each tile as needed. The `imageUrlSubdomains` property in the imagery metadata response provides a list of valid subdomain that can be used in the tile URL. Using a different one for each tile request you can increase performance by get around browser URL request limits i.e. many browsers allow up to 8 concurrent requests to the same domain. Using subdomains allows up to 8 requests per subdomain. The culture value can be any value listed in the [Supported Culture Codes](../rest-services/supported-culture-codes.md) document. The quadkey value can be calculated based on the zoom level and the tile you wish to render. Information on the tile system along with some useful code can be found here:

* [Bing Maps Tile System](../articles/bing-maps-tile-system.md)
* [Understanding Scale and Resolution](../articles/understanding-scale-and-resolution.md)

In addition to this, the query will also return information on the imagery providers and copyright information which should be displayed with the imagery to align with the requirments of the [terms of use](http://www.microsoft.com/maps/product/terms.html).

Licensing queries can be sent [here](http://www.microsoft.com/maps/contact-us.aspx).