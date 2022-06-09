---
title: MapServices API Reference | Microsoft Docs
description: Provides a reference of MapServices API through tables that outline details for various classes, enumerations, and interfaces.
ms.author: pablocan
---

# MapServices API Reference

## Classes 

Name                                                        | Details
----------------------------------------------------------- | ------------------------------------------------------
[Geopoint](../map-control-api/Geopoint-class.md)            | Describes a geographic point.
[MapLocation](MapLocation-class.md)                         | Contains data about a specific location returned from a geocoding request.
[MapLocationAddress](MapLocationAddress-class.md)           | Contains address data for a specific location returned from a geocoding request.
[MapLocationFinder](MapLocationFinder-class.md)             | Forms and sends geocoding requests.
[MapLocationOptions](MapLocationOptions-class.md)           | Forms optional parameters for a geocoding request.
[MapLocationPoint](MapLocationPoint-class.md)               | Contains geospatial data for a specific point associated with the location returned from a geocoding request.
[MapLocationFinderResult](MapLocationFinderResult-class.md) | Contains status code and result location data for a geocoding request.
[MapServices](MapServices-class.md)                         | Provides common methods for map services.

## Enumerations

Name                                                                                  | Details
------------------------------------------------------------------------------------- | ------------------------------------------------------
[MapLocationEntityTypes](MapLocationEntityTypes-enumeration.md)                       | The entity types to be included in the response for a geocoding request.
[MapLocationMatchCode](MapLocationMatchCode-enumeration.md)                           | The geocoding level for a location returned from a geocoding request.
[MapLocationPointCalculationMethod](MapLocationPointCalculationMethod-enumeration.md) | The method that was used to compute the geopoint for a location returned from a geocoding request.
[MapLocationPointUsageType](MapLocationPointUsageType-enumeration.md)                 | The best use for the geopoint for a location returned from a geocoding request.
[MapLocationFinderStatus](MapLocationFinderStatus-enumeration.md)                     | Status code for a geocoding request.

## Interfaces

Name                                                                                                  | Details
----------------------------------------------------------------------------------------------------- | ------------------------------------------------------
[OnMapLocationFinderResultListener](Android/OnMapLocationFinderResultListener-interface.md) (Android) | Represents an interface for handling the results of a geocoding request, on Android.
[MapLocationFinderResultHandler](iOS/MapLocationFinderResultHandler-interface.md) (iOS)               | Represents an interface for handling the results of a geocoding request, on iOS.
