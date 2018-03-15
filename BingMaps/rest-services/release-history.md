---
title: "Release History1 | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: e2a0c66e-2cc0-43da-8a25-21f769203885
caps.latest.revision: 5
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Release History
The following is a release history for the Bing Maps REST Services starting with January, 2014.  
  
|Date and API|Release notes|  
|------------------|-------------------|  
|April 15, 2014<br /><br /> [Get Road Shield Images](http://msdn.microsoft.com/en-us/18611bc8-42fc-4609-998d-0150783a19d5)|New API that returns a road shield image when you provide road request parameter values from a [Routes](../rest-services/routes-api.md) response.|  
|April 15, 2014<br /><br /> [Calculate a Route](../rest-services/calculate-a-route.md)|<ul><li>A routeAttributes parameter is added. This takes one or more of the following values:<br /><br /> <ul><li>`excludeItinerary`: Specifies to not return itinerary items in the response.</li><li>`routePath`: Specifies to return a set of coordinates (latitude/longitude) that define the route. This route attribute gives the same result as setting routePathOutput=Points in the request and is now the recommended way to get route path coordinates (see note below).</li></ul></li><li>A mfa (metadata for alternate routes) is added. When set to 1 (true), detailed route instructions (itinerary items) are not included in the response for alternate routes.</li><li>Route sub-leg fields are added to provide summary information for the route leg segments between start and end waypoints and any intermediate via-waypoints</li></ul>|  
|January 7, 2014<br /><br /> [Get a Static Map](../rest-services/get-a-static-map.md)<br /><br /> [Locations](../rest-services/locations-api.md)|-   Forty (40) new static map pushpin icon styles were added (IDs 73-112)<br />-   Add `include=cios2` in your Locations API request, to return the [two-letter ISO 3166 country code](http://www.iso.org/iso/country_codes.htm) for each address in the response. The country code appears in the `CountryRegionIso2` field.|  
|January 7, 2014<br /><br /> [Locations](../rest-services/locations-api.md)|-   Add `include=cios2` in your Locations API request, to return the [two-letter ISO 3166 country code](http://www.iso.org/iso/country_codes.htm) for each address in the response. The country code appears in the `CountryRegionIso2` field.|