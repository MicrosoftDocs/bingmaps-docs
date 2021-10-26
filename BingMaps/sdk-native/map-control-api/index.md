---
title: Map Control API Reference
description: Bing Maps Map Control API Reference for the Android and iOS SDK
author: stevemunk
ms.author: v-munksteve
ms.date: 10/26/2021
ms.topic: reference
ms.service: bing-maps
---

# Map Control API Reference

> [!Note]
> In Android APIs, consider unannotated parameters and methods implicitly annotated as non-null. Nullable annotations are explicit.  
> In iOS APIs, all nullability annotations are explicit.

## Classes

Name                                                                   | Details
----------------------------------------------------------------       | ------------------------------------------------------
[CustomTileMapLayer](CustomTileMapLayer-class.md)                      | Allows a developer to generate custom tiles on the client to overlay on the map.
[GeoboundingBox](GeoboundingBox-class.md)                              | Describes a geographical rectangle.
[Geocircle](Geocircle-class.md)                                        | Describes a geographical circle with a center point and radius.
[Geopath](Geopath-class.md)                                            | Describes an ordered series of geographic points, usable for defining a polyline or polygon.
[Geopoint](Geopoint-class.md)                                          | Describes a geographic point.
[Geoposition](Geoposition-class.md)                                    | Describes a geographic position's basic information: latitude, longitude, and altitude.
[Geoshape](Geoshape-class.md)                                          | Describes a geographic shape.
[GroundOverlayMapLayer](GroundOverlayMapLayer-class.md)                | Displays an image in a geographic area.
[MapCamera](MapCamera-class.md)                                        | A collection of properties that describes a camera from which to view a map
[MapElement](MapElement-class.md)                                      | Base abstract class that serves as foundation for elements within the map.
[MapElementCollection](MapElementCollection-class.md)                  | A collection of MapElements, such as icons and lines.
[MapElementLayer](MapElementLayer-class.md)                            | Used to manage settings across a developer-configurable collection of elements.
[MapFlyout](MapFlyout-class.md)                                        | A custom user interface that pops up as users click on MapIcons.
[MapIcon](MapIcon-class.md)                                            | Displays a graphic image on the map.
[MapImage](MapImage-class.md)                                          | An image that can be displayed on the map via a MapIcon.
[MapLayer](MapLayer-class.md)                                          | Base class for all map layers.
[MapLayerCollection](MapLayerCollection-class.md)                      | Collection of map layers that are shown on a map.
[MapLocationData](maplocationdata-class.md)                            | Contains the location information retrieved by tracking the user's location.
[MapPolygon](MapPolygon-class.md)                                      | Displays a shape on the map.
[MapPolyline](MapPolyline-class.md)                                    | Displays a line on the map.
[MapRouteLine](MapRouteLine-class.md)                                  | Displays a route line on the map.
[MapRouteSegment](MapRouteSegment-class.md)                            | Represents a road segment displayed on the map.
[MapScene](MapScene-class.md)                                          | Base class and provides ways to control what is displayed on the map.
[MapStyleSheet](MapStyleSheet-class.md)                                | Controls the visual display of the map like road color and size.
[MapStyleSheets](MapStyleSheets-class.md)                              | Represents a set of rules that define the style of the map in a map control.
[MapUserInterfaceOptions](MapUserInterfaceOptions-class.md)            | Used for configuring which user interface elements to display on the Map View.
[MapUserLocation](mapuserlocation-class.md)                            | Allows to track the user's location and display it on the map with an accuracy radius and a heading.
[MapView](MapView-class.md)                                            | The core view object that displays a map within a broader map view.
[TrafficFlowMapLayer](TrafficFlowMapLayer-class.md)                    | Displays active traffic flow on a map.
[UriTileMapLayer](UriTileMapLayer-class.md)                            | A tile map layer that retrieves tiles from a web server using developer-supplied URLs.
[ViewPadding](ViewPadding-class.md)                                    | Represents the view padding information.

## Enumerations

Name                                                                         | Details
----------------------------------------------------------------             | ------------------------------------------------------
[AltitudeReferenceSystem](AltitudeReferenceSystem-enumeration.md)            | Indicates what an altitude value is relative to.
[CopyrightDisplay](CopyrightDisplay-enumeration.md)                          | Controls how the copyright is displayed on the map.
[GeoshapeType](GeoshapeType-enumeration.md)                                  | Describes the shape of a geographic region.
[MapAnimationKind](MapAnimationKind-enumeration.md)                          | Describes types of animations supported for camera transitions.
[MapCameraChangeReason](MapCameraChangeReason-enumeration.md)                | Specifies the reason the position of the map's camera has changed. iOS only.
[MapElementCollisionBehavior](MapElementCollisionBehavior-enumeration.md)    | Describes the behavior of a MapIcon when it collides with other map features.
[MapLoadingStatus](maploadingstatus-enumeration.md)                          | The status of the map indicating how much of the map is currently being. rendered.
[MapProjection](MapProjection-enumeration.md)                                | Controls how the map projects the world onto the screen.
[MapRenderMode](MapRenderMode-enumeration.md)                                | Defines primary data source for rendering map.
[MapRouteLineState](maproutelinestate-enumeration.md)                        | Define the route state of MapRouteLine.
[MapRouteLineTrafficCongestion](maproutelinetrafficcongestion-enumeration.md)| Define the travel congestion of MapRouteSegment.
[MapRouteLineTravelMode](maproutelinetravelmode-enumeration.md)              | Define the travel mode of MapRouteSegment.
[MapUserLocationTrackingMode](mapuserlocationtrackingmode-enumeration.md)    | Defines tracking mode for user location.
[MapUserLocationTrackingState](mapuserlocationtrackingstate-enumeration.md)  | Defines tracking state for user location.
