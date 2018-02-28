---
title: "Location and Area Types | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: dd0019e9-6f51-4ca2-83d3-031e2874ca64
caps.latest.revision: 18
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# Location and Area Types
Use the following formats to specify locations and areas on the Earth.  
  
|Type|Description|Values and Syntax|  
|----------|-----------------|-----------------------|  
|Point|A point on the Earth specified by a latitude and longitude.|The coordinates are `double` values that are separated by commas and are specified in the following order.<br /><br /> Latitude,Longitude<br /><br /> Use the following ranges of values:<br /><br /> -   Latitude (degrees): [-90, +90]<br />-   Longitude (degrees): [-180,+180]<br /><br /> **Example**: 47.610679194331169,-122.10788659751415|  
|BoundingBox|A rectangular area on the Earth.|A bounding box is defined by two latitudes and two longitudes that represent the four sides of a rectangular area on the Earth. Use the following syntax to specify a bounding box.<br /><br /> South Latitude, West Longitude, North Latitude, East Longitude<br /><br /> **Example**: 45.219,-122.325,47.610,-122.107|  
|Address|Details about a point on the Earth that has additional location information.|An address can contain the following fields: address line, locality, neighborhood, admin district, admin district 2, formatted address, postal code and country or region. For descriptions see the **Address Fields** section below.|  
  
## Address Fields  
  
|Address|Description|  
|-------------|-----------------|  
|addressLine|The official street line of an address relative to the area, as specified by the Locality, or PostalCode, properties. Typical use of this element would be to provide a street address or any official address.<br /><br /> **Example**: 1 Microsoft Way|  
|locality|A string specifying the populated place for the address. This typically refers to a city, but may refer to a suburb or a neighborhood in certain countries.<br /><br /> **Example**: Seattle|  
|neighborhood|A string specifying the neighborhood for an address.<br /><br /> You must specify includeNeighborhood=1 in your request to return the neighborhood.<br /><br /> **Example**: Ballard|  
|adminDistrict|A string specifying the subdivision name in the country or region for an address. This element is typically treated as the first order administrative subdivision, but in some cases it is the second, third, or fourth order subdivision in a country, dependency, or region.<br /><br /> **Example**: WA|  
|adminDistrict2|A string specifying the subdivision name in the country or region for an address. This element is used when there is another level of subdivision information for a location, such as the county.<br /><br /> **Example**: King|  
|formattedAddress|A string specifying the complete address. This address may not include the country or region.<br /><br /> **Example**: 1 Microsoft Way, Redmond, WA 98052-8300|  
|postalCode|A string specifying the post code, postal code, or ZIP Code of an address.<br /><br /> **Example**: 98178|  
|countryRegion|A string specifying the country or region name of an address.<br /><br /> **Example**: United States|  
|countryRegionIso2|A string specifying the [two-letter ISO country code](http://www.iso.org/iso/country_codes.htm).<br /><br /> You must specify include=ciso2 in your request to return this ISO country code.<br /><br /> **Example**: US|  
|landmark|A string specifying the name of the landmark when there is a landmark associated with an address.<br /><br /> **Example**: Eiffel Tower|