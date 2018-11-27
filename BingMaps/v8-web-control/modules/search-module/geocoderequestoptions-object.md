---
title: "GeocodeRequestOptions Object | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: e9b57b26-a547-4087-98b5-e96377af26a7
caps.latest.revision: 9
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# GeocodeRequestOptions Object
In order to geocode a location, you need to pass an object containing geocode request options into the geocode method. The following is a list of properties that can be included in a geocode request.

Name                   | Type                                      | Description
---------------------- | ----------------------------------------- | -----------------------------------------------
`bounds`                 | [LocationRect](map-control-api/locationrect-class.md)                              |A location rectangle that defines a boundary that is used to influence the weight of the search results. This will often change the order of results such that more relevant results to users of the specified area appear higher in the results. By default the current bounds of the map view is used by the SearchManager.
`callback`               | function(result: [GeocodeResult](../v8-web-control/geocoderesult-object.md), userData: any)       | A reference to a function to call when a successful result is returned from the geocode request. 
`count`                  | number                                    | The maximum number of results to return. The maximum number that can be returned is 20.
`errorCallback`          | function (request: [GeocodeRequestOptions](../v8-web-control/geocoderequestoptions-object.md))                                 | A reference to a function to call when the request is returned with an error. The error callback function will receive an object containing the geocode request options used in the request.
`includeCountryIso2`     | boolean                                   | Specifies to include the [two-letter ISO country code](http://www.iso.org/iso/country_codes.htm).
`includeNeighborhood`    | boolean                                   | A boolean that specifies that neighborhood information should be included when available. <br/><br/>**Note**: This feature isn’t available in all locations.
`timeout`                | number                                    | A number indicating how long to wait, in seconds, for the geocode request to return. The default value is 5 seconds.
`userData`               | any                                       | An object containing any data that needs to be passed to the callback when the request is completed.
`where`                  | string                                    | Required. A string containing the address or place to be matched to a location on the map. Required.
