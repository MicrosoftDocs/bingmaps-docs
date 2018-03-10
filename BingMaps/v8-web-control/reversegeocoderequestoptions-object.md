---
title: "ReverseGeocodeRequestOptions Object2 | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 2998fdb6-3c57-44ee-9ae8-31d81d24e878
caps.latest.revision: 5
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# ReverseGeocodeRequestOptions Object
In order to reverse geocode a location you need to pass an object containing reverse geocode request options into the reverseGeocode method. The following is a list of properties that can be included in a reverse geocode request.

Name                         | Type                                           | Description
---------------------------- | ---------------------------------------------- | ---------------------------------------------
`callback`                   | function(result: [PlaceResult](../v8-web-control/placeresult-object.md), userData: any)     | A reference to a function to call when a successful result is returned from the geocode request. The callback function will receive a [PlaceResult](../v8-web-control/placeresult-object.md) object as an argument.
`errorCallback`              | function(result: [ReverseGeocodeRequestOptions](../v8-web-control/reversegeocoderequestoptions-object.md))     | A reference to a function to call when the request is returned with an error. The error callback function will receive an object containing the geocode request options used in the request.
`includeCountryIso2`         | boolean                                        | Specifies to include the [two-letter ISO country code](http://www.iso.org/iso/country_codes.htm). Default: **false**
`includeEntityTypes`         | string[]                                       | An array of entity types selected from the following options.<br/><br/>&nbsp;  • Address<br/>&nbsp;  • Neighborhood<br/>&nbsp;  • PopulatedPlace<br/>&nbsp;  • Postcode1<br/>&nbsp;  • AdminDivision1<br/>&nbsp;  • AdminDivision2<br/>&nbsp;  • CountryRegion<br/><br/>These entity types are ordered from the most specific entity to the least specific entity. When entities of more than one entity type are found, only the most specific entity is returned. For example, if you specify Address and AdminDistrict1 as entity types and entities were found for both types, only the Address entity information is returned in the response. One exception to this rule is when both PopulatedPlace and Neighborhood entity types are specified and information is found for both. In this case, the information for both entity types is returned. Also, more than one Neighborhood may be returned because the area covered by two different neighborhoods can overlap.
`includeNeighborhood`        | boolean                                        | A boolean that specifies that neighborhood information should be included when available. <br/><br/>**Note**: This feature isn’t available in all locations.
`location`                   | [Location](../v8-web-control/location-class.md)                                       | Required. The location to use to match to geographic entities and addresses.
`timeout`                    | number                                         | A number indicating how long to wait, in seconds, for the geocode request to return. Default: **5 seconds**
`userData`                   | any                                            | An object containing any data that needs to be passed to the callback when the request is completed.
