---
title: "Breaking API changes in version 1.0 | Microsoft Docs"
author: "bmnxplat"
---

# Breaking API changes in version 1.0


## Overview
One of the main motivations behind the SDK changes for V1 has been to provide a more stable API baseline for our customers. Another major motivation has been to unify our APIs and to get closer parity on all supported platforms.  
In some cases, these challenges have meant making important but necessary breaking changes that clients can depend on going forward. Our own API cleanup efforts have been an important part of the process as well.
Most breaking changes are the result of one of the following:
- Making the overall API leaner.
- Fixing of APIs, notably some events that used to fire outside of the UI thread.
- Overhauling of some features like MapFlyout to make them friendlier and easier to use.
- Renaming of some APIs to better align them with the native platform and/or to conform with established naming conventions.


## Android
Updated various public classes.

### GeoboundingBox
- Now inherited from `Geoshape`.
- Replaced field `north` with accessor `getNorth`.
- Replaced field `east` with accessor `getEast`.
- Replaced field `south` with accessor `getSouth`.
- Replaced field `west` with accessor `getWest`.
- Changed constructors to take `Geoposition` objects instead of `Geolocation`.

### Geolocation
- Renamed `Geolocation` to `Geopoint`.
- Now inherited from `Geoshape`.
- Replaced properties `latitude`, `longitude`, `altitude` with property `position`.
- Moved property `altitudeReference` to base class `Geoshape`; it is now read-only.

### Geopath
- Now inherited from `Geoshape`.
- Changed constructors to take `Geoposition` objects instead of `Geolocation`.

### Geoshape
- Introduced as base class for following types: `GeoboundingBox`, `Geopath`, `Geopoint`.
- Exposes read-only properties `geoshapeType` and `altitudeReferenceSystem`.

### MapIcon
- Renamed property accessor: `getIsFlat` to `isFlat`.
- Renamed property accessor: `getMapFlyout` to `getFlyout`.
- Removed property: `flyoutVisible`.
- Removed method: `addOnMapIconDragListeners`.
- Removed method: `addOnMapIconDragStartListeners`.
- Removed method: `addOnMapIconDragStopListeners`.
- Removed method: `removeOnMapIconDragListeners`.
- Removed method: `removeOnMapIconDragStartListeners`.
- Removed method: `removeOnMapIconDragStopListeners`.

### MapStyleSheet
- Changed return type for method `fromJson`: from `Optional<MapStyleSheet>` to `MapStyleSheet`.

### MapFlyout
- Complete API overhaul.

### MapLocation.MatchCode
- Change to top-level enum; now `MapLocationMatchCode`.

### MapLocationFinder.Status
- Change to top-level enum; now `MapLocationFinderStatus`.

### MapLocationPoint.CalculationMethod
- Change to top-level enum; now `MapLocationPointCalculationMethod`.

### MapLocationPoint.UsageType
- Change to top-level enum; now `MapLocationPointUsageType`.

### MapPolygon
- Renamed property accessor: `getStrokeDashed` to `isStrokeDashed`.
- Replaced property `path` of type `Geopath` with `paths` of type `List<Geopath>`.

### MapPolyline
- Renamed property accessor: `getStrokeDashed` to `isStrokeDashed`.

### MapUserInterfaceOptions
- Renamed property accessor: `isPanGesturesEnabled` to `isPanGestureEnabled`.
- Renamed property accessor: `isRotateGesturesEnabled` to `isRotateGestureEnabled`.
- Renamed property accessor: `isTiltGesturesEnabled` to `isTiltGestureEnabled`.
- Renamed property accessor: `isZoomGesturesEnabled` to `isZoomGestureEnabled`.
- Removed property: `myLocationButtonVisible`.

### MapView
- Renamed method: `resume` to `onResume`.
- Renamed method: `suspend` to `onPause`.
- Renamed method: `close` to `onDestroy`.
- Renamed property accessor: `getBuildingsVisible` to `isBuildingsVisible`.
- Renamed property accessor: `getBusinessLandmarksVisible` to `isBusinessLandmarksVisible`.
- Renamed property accessor: `getTransitFeaturesVisible` to `isTransitFeaturesVisible`.
- Changed return type for method `getLocationFromOffset`: from `Optional<Geolocation>` to `Geolocation`.
- Changed return type for method `getOffsetFromLocation`: from `Optional<Point>` to `Point`.
- Removed method: `clear`.
- Removed property: `userLocationTrackingMode`.
- Removed property: `userLocationVisible`.

### OnMapIconDragListener
- Removed.

### OnMapIconDragStartListener
- Removed.

### OnMapIconDragStopListener
- Removed.

### Optional\<T>
- Removed.


## iOS
Updated various public interfaces, as well as universal and various individual headers.

### MSGeoboundingBox
- Now inherited from `MSGeoshape`.
- Renamed method: `geoboundingBoxWithNorthwest:southwest:` to `geoboundingBoxWithNorthwestCorner:southwestCorner:`.
- Changed constructors to take `MSGeoposition` objects instead of `MSGeolocation`.

### MSGeolocation
- Renamed `MSGeolocation` to `MSGeopoint`.
- Now inherited from `MSGeoshape`.
- Replaced properties `latitude`, `longitude`, `altitude` with property `position`.
- Moved property `altitudeReference` to base class `MSGeoshape`; it is now read-only.

### MSGeopath
- Now inherited from `MSGeoshape`.
- Changed constructors to take `MSGeoposition` objects instead of `MSGeolocation`.

### MSGeoshape
- Introduced as base class for following types: `MSGeoboundingBox`, `MSGeopath`, `MSGeopoint`.
- Exposes read-only properties `geoshapeType` and `altitudeReferenceSystem`.

### MSMapElement
- Renamed property: `isVisible` to `visible`.

### MSMapGroundOverlayMapLayer
- Changed `initWithImage:geoBoundingBox:` method signature  to `initWithImage:boundingBox:`.

### MSMapIcon
- Renamed property: `isFlat` to `flat`.

### MSMapFlyout
- Complete API overhaul.

### MSMapLayer
- Renamed property: `isVisible` to `visible`.

### MSMapPolygon
- Replaced property `path` of type `MSGeopath*` with `paths` of type `NSArray<MSGeopath*>*`.

### MSMapUserInterfaceOptions
- Renamed property: `isPanGesturesEnabled` to `panGestureEnabled`.
- Renamed property: `isRotateGesturesEnabled` to `rotateGestureEnabled`.
- Renamed property: `isTiltGesturesEnabled` to `tiltGestureEnabled`.
- Renamed property: `isZoomGesturesEnabled` to `zoomGestureEnabled`.
- Renamed property: `isCompassButtonVisible` to `compassButtonVisible`.
- Renamed property: `isZoomButtonsVisible` to `zoomButtonsVisible`.
- Renamed property: `isTiltButtonVisible` to `tiltButtonVisible`.
- Removed property: `isMyLocationButtonVisible`.
- Changed property: `(BOOL)isCopyrightVisible` to `(MSCopyrightDisplay)copyrightDisplay`.

### MSMapView
- Removed property: `userLocationTrackingMode`.
- Removed property: `userLocationVisible`.


## See also
* [Bing Maps SDK for Android and iOS documentation](Index.md)
