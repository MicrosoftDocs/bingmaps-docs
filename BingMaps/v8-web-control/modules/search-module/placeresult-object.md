---
title: "PlaceResult Object | Microsoft Docs"
description: Describes the PlaceResult object, which represents a place result, and provides a list of related properties.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 55e87c38-1f77-46a2-b51d-1349a306f83b
caps.latest.revision: 6
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# PlaceResult Object

Represents a place result in the Search module.

## Properties

Name                | Type                                              | Description
------------------- | ------------------------------------------------- | ----------------------------------
`address`           | [Address](../autosuggest-module/address-object.md)                             | A structured address object.
`bestView`          | [LocationRect](../../map-control-api/locationrect-class.md)          | The location rectangle that defines the boundaries of the best map view of the place result.
`entityType`        | string                                            | The classification of the geographic entity returned, such as PopulatedPlace.
`location`          | [Location](../../map-control-api/location-class.md)                  | The geocoded location of the best result.
`locations`         | [GeocodeLocation](geocodelocation-object.md)[]  | The geocoded locations.
`matchCode`         | [MatchCode](matchcode-enumeration.md)                                            | The match code of the best result. The possible values are:<br/><br/>&nbsp;  • **Good**: The location has only one match or all returned matches are considered strong matches. For example, a query for New York returns several Good matches.<br/>&nbsp;  • **Ambiguous**: The location is one of a set of possible matches. For example, when you query for the street address 128 Main St., the response may return two locations for 128 North Main St. and 128 South Main St. because there is not enough information to determine which option to choose.<br/>&nbsp;  • **UpHierarchy**: The location represents a move up the geographic hierarchy. This occurs when a match for the location request was not found, so a less precise result is returned. For example, if a match for the requested address cannot be found, then a match code of UpHierarchy with a RoadBlock entity type may be returned.
`matchConfidence`   | [MatchConfidence](matchconfidence-enumeration.md)                                            | The match confidence of the best result. The possible values are:<br/><br/>&nbsp;  • High<br/>&nbsp;  • Medium<br/>&nbsp;  • Low<br/><br/>For more information on this property, see the documentation on the [Bing Maps REST Location Data object](../../../rest-services/locations/location-data.md).
`name`              | string                                            | The name of the place result, if one exists.

