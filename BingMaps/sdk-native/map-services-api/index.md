---
title: MapServices API Reference | Microsoft Docs
description: The overview page for the MapServices API Reference section contains tables containing descriptions and links to more information for each of the MapServices classes, enumerations and interfaces.
author: pablocan
ms.author: pablocan
ms.date: 08/12/2022
ms.topic: reference
ms.service: bing-maps
---

# Map Services API Reference

> [!Note]
>
> In Android APIs, consider unannotated parameters and methods implicitly annotated as non-null. Nullable annotations are explicit.
>
> In iOS APIs, all nullability annotations are explicit.


## Geospatial

### Classes

Name                                                        | Details
----------------------------------------------------------- | ------------------------------------------------------
[GeoboundingBox](../map-control-api/GeoboundingBox-class.md)| Describes a geographic rectangular area.
[Geopoint](../map-control-api/Geopoint-class.md)            | Describes a geographic point.
[Geoposition](../map-control-api/Geoposition-class.md)      | Describes a geographic position's basic information: latitude, longitude, and altitude.
[Geoshape](../map-control-api/Geoshape-class.md)            | Describes a geographic shape.

### Enumerations

Name                                                                                  | Details
------------------------------------------------------------------------------------- | ------------------------------------------------------
[AltitudeReferenceSystem](../map-control-api/AltitudeReferenceSystem-enumeration.md)  | Indicates what an altitude value is relative to.
[GeoshapeType](../map-control-api/GeoshapeType-enumeration.md)                        | Describes the shape of a geographic region.

## Map Services

### Classes

Name                                                        | Details
----------------------------------------------------------- | ------------------------------------------------------
[MapLocation](MapLocation-class.md)                         | Contains data about a specific location returned from a geocoding request.
[MapLocationAddress](MapLocationAddress-class.md)           | Contains address data for a specific location returned from a geocoding request.
[MapLocationFinder](MapLocationFinder-class.md)             | Forms and sends geocoding requests.
[MapLocationOptions](MapLocationOptions-class.md)           | Forms optional parameters for a geocoding request.
[MapLocationPoint](MapLocationPoint-class.md)               | Contains geospatial data for a specific point associated with the location returned from a geocoding request.
[MapLocationFinderResult](MapLocationFinderResult-class.md) | Contains status code and result location data for a geocoding request.
[MapServices](MapServices-class.md)                         | Provides common methods for map services.

### Enumerations

Name                                                                                  | Details
------------------------------------------------------------------------------------- | ------------------------------------------------------
[MapLocationEntityTypes](MapLocationEntityTypes-enumeration.md)                       | The entity types to be included in the response for a geocoding request.
[MapLocationMatchCode](MapLocationMatchCode-enumeration.md)                           | The geocoding level for a location returned from a geocoding request.
[MapLocationPointCalculationMethod](MapLocationPointCalculationMethod-enumeration.md) | The method that was used to compute the geopoint for a location returned from a geocoding request.
[MapLocationPointUsageType](MapLocationPointUsageType-enumeration.md)                 | The best use for the geopoint for a location returned from a geocoding request.
[MapLocationFinderStatus](MapLocationFinderStatus-enumeration.md)                     | Status code for a geocoding request.

### Interfaces

Name                                                                                                  | Details
----------------------------------------------------------------------------------------------------- | ------------------------------------------------------
[OnMapLocationFinderResultListener](Android/OnMapLocationFinderResultListener-interface.md) (Android) | Represents an interface for handling the results of a geocoding request, on Android.
[MapLocationFinderResultHandler](iOS/MapLocationFinderResultHandler-interface.md) (iOS)               | Represents an interface for handling the results of a geocoding request, on iOS.
