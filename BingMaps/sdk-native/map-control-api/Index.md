# API Reference

## Classes

Name                                                             | Details
---------------------------------------------------------------- | ------------------------------------------------------
[CustomTileMapLayer](CustomTileMapLayer.md)                      | Allows a developer to generate custom tiles on the client to overlay on the map.
[DefaultMapCameraAnimation](Android/DefaultMapCameraAnimation.md)| Lets a developer supply custom parameters for driving animated transitions on a map. Android only.
[GeoboundingBox](GeoboundingBox.md)                              | Used to describe a geographical rectangle.
[Geolocation](Geolocation.md)                                    | Describes a geographic point.
[Geopath](Geopath.md)                                            | Describes an ordered collection of points, usable for defining a polyline or polygon.
[GroundOverlayMapLayer](GroundOverlayMapLayer.md)                | Displays an image in a geographic area.
[MapCamera](MapCamera.md)                                        | A collection of properties that describes a camera from which to view a map
[MapCameraChangeCause](MapCameraChangeCause.md)                  | Specifies the reason the position of the map's camera has changed. iOS only.
[MapElement](MapElement.md)                                      | Base abstract class that serves as foundation for elements within the map.
[MapElementCollection](MapElementCollection.md)                  | A collection of MapElements, such as icons and lines.
[MapElementLayer](MapElementLayer.md)                            | Used to manage settings across a developer-configurable collection of elements.
[MapFlyout](MapFlyout.md)                                        | A custom user interface that pops up as users click on MapIcons.
[MapIcon](MapIcon.md)                                            | Displays a graphic image on the map.
[MapImage](MapImage.md)                                          | An image that can be displayed on the map via a MapIcon
[MapLayer](MapLayer.md)                                          | Base class for all map layers
[MapLayerCollection](MapLayerCollection.md)                      | Collection of map layers that are shown on a map
[MapPolygon](MapPolygon.md)                                      | Displays a shape on the map.
[MapPolyline](MapPolyline.md)                                    | Displays a line on the map.
[MapScene](MapScene.md)                                          | Base class and provides ways to control what is displayed on the map.
[MapStyleSheet](MapStyleSheet.md)                                | Controls the visual display of the map like road color and size.
[MapStyleSheets](MapStyleSheets.md)                               | Represents a set of rules that define the style of the map in a map control. Android only.
[MapUserInterfaceOptions](MapUserInterfaceOptions.md)            | Used for configuring which user interface elements to display on the Map View.
[MapView](MapView.md)                                            | The core view object that displays a map within a broader map view.
[TrafficFlowMapLayer](TrafficFlowMapLayer.md)                    | Displays active traffic flow on a map.
[UriTileMapLayer](UriTileMapLayer.md)                            | A tile map layer that retrieves tiles from a web server using developer-supplied URLs.

## Enumerations

Name                                                             | Details
---------------------------------------------------------------- | ------------------------------------------------------
[AltitudeReferenceSystem](AltitudeReferenceSystem.md)            | Indicates what an altitude value is relative to.
[CopyrightDisplay](Android/CopyrightDisplay.md)                  | Controls how the copyright is displayed on the map.
[MapAnimationKind](MapAnimationKind.md)                          | Describes types of animations supported for camera transitions.
[MapElementCollisionBehavior](MapElementCollisionBehavior.md)    | Describes the behavior of a MapIcon when it collides with other map features.
[MapLoadingStatus](MapLoadingStatus.md)                          | The status of the map indicating how much of the map is currently being rendered.
[MapProjection](MapProjection.md)                                | Controls how the map projects the world onto the screen.
[MapRenderMode](MapRenderMode.md)                                | Defines primary data source for rendering map.
