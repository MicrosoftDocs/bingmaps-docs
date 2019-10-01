
# Drawing with Polylines and Polygons

Frequently, you want to add a simple annotation to the map, which [MapIcons](../map-control-api/MapIcon-class.md) are well suited for. Sometimes you will want to highlight a geographic region, or draw additional paths between points on the map. To do this, you will want to use [MapPolygon](../map-control-api/MapPolygon-class.md) and [MapPolyline](../map-control-api/MapPolyline-class.md) classes, respectively.

## Examples

### Adding a line

Display a line by using the [MapPolyline](../map-control-api/MapPolyline-class.md). The following example shows how to add a dashed black line on a map.

**Swift**

> ``` swift
> func drawLineOnMap() {
>     let centerLatitude = mapView.mapCenter.position.latitude;
>     let centerLongitude = mapView.mapCenter.position.longitude;
>
>     let mapPolyline = MSMapPolyline()
>     let geopath = MSGeopath(positions:
>           [MSGeoposition(latitude: centerLatitude-0.0005, longitude: centerLongitude-0.001),
>            MSGeoposition(latitude: centerLatitude+0.0005, longitude: centerLongitude+0.001)])
>
>     mapPolyline.path = geopath
>     mapPolyline.strokeColor = UIColor.black
>     mapPolyline.strokeWidth = 3
>     mapPolyline.strokeDashed = true
>
>     // Add Polyline to a layer on the map control.
>     let linesLayer = MSMapElementLayer()
>     linesLayer.zIndex = 1
>     linesLayer.elements.add(mapPolyline)
>     mapView.layers.add(linesLayer);
> }
> ```

**Objective-C**

>``` objectivec
> - (void) drawLineOnMap
> {
>     MSGeopoint *center = self.mapView.mapCenter;
>     double centerLatitude = center.position.latitude;
>     double centerLongitude = center.position.longitude;
>
>     NSMutableArray<MSGeoposition*>* positions;
>     [positions addObject:[MSGeoposition geopositionWithLatitude: centerLatitude-0.0005 longitude: centerLongitude-0.001]];
>     [positions addObject:[MSGeoposition geopositionWithLatitude: centerLatitude+0.0005 longitude: centerLongitude+0.001]];
>
>     MSMapPolyline* mapPolyline = [MSMapPolyline polyline];
>     MSGeopath *geopath = [MSGeopath geopathWithPositions:positions];
>
>     mapPolyline.path = geopath;
>     mapPolyline.strokeColor = [UIColor blackColor];
>     mapPolyline.strokeWidth = 3;
>     mapPolyline.strokeDashed = YES;
>
>     // Add Polyline to a layer on the map control.
>     MSMapElementLayer* linesLayer = [MSMapElementLayer layer];
>     linesLayer.zIndex = 1;
>     [[linesLayer elements] addMapElement:mapPolyline];
>     [[self.mapView layers] addMapLayer: linesLayer];
> }
> ```

### Adding a shape

Display a multi-point shape on a map by using the [MapPolygon](../map-control-api/MapPolygon-class.md). The following example show how to add a red box with a blue outline on a map.

**Swift**

> ``` swift
> func highlightArea() {
>     let centerLatitude = mapView.mapCenter.position.latitude;
>     let centerLongitude = mapView.mapCenter.position.longitude;
>
>     let mapPolygon = MSMapPolygon()
>     let geopath = MSGeopath(positions:
>         [MSGeoposition(latitude: centerLatitude+0.0005, longitude: centerLongitude-0.001),
>         MSGeoposition(latitude: centerLatitude-0.0005, longitude: centerLongitude-0.001),
>         MSGeoposition(latitude: centerLatitude-0.0005, longitude: centerLongitude+0.001)])
>
>     mapPolygon.paths = [geopath]
>     mapPolygon.zIndex = 1
>     mapPolygon.fillColor = UIColor.red
>     mapPolygon.strokeColor = UIColor.blue
>     mapPolygon.strokeWidth = 3
>     mapPolygon.strokeDashed = false
>
>     let highlightsLayer = MSMapElementLayer()
>     highlightsLayer.zIndex = 1
>     highlightsLayer.elements.add(mapPolygon)
>     mapView.layers.add(highlightsLayer)
> }
> ```

**Objective-C**

>``` objectivec
> - (void) highlightArea
> {
>     MSGeopoint *center = self.mapView.mapCenter;
>     double centerLatitude = center.position.latitude;
>     double centerLongitude = center.position.longitude;
>
>     NSMutableArray<MSGeoposition*>* positions;
>     [positions addObject:[MSGeoposition geopositionWithLatitude: centerLatitude+0.0005 longitude: centerLongitude-0.001]];
>     [positions addObject:[MSGeoposition geopositionWithLatitude: centerLatitude-0.0005 longitude: centerLongitude-0.001]];
>     [positions addObject:[MSGeoposition geopositionWithLatitude: centerLatitude-0.0005 longitude: centerLongitude+0.001]];
>     [positions addObject:[MSGeoposition geopositionWithLatitude: centerLatitude+0.0005 longitude: centerLongitude+0.001]];
>
>     MSMapPolygon* mapPolygon = [MSMapPolygon polygon];
>     MSGeopath *geopath = [MSGeopath geopathWithPositions:positions];
>
>     mapPolygon.paths = [NSArray arrayWithObject:geopath];
>     mapPolygon.zIndex = 1;
>     mapPolygon.fillColor = [UIColor redColor];
>     mapPolygon.strokeColor = [UIColor blueColor];
>     mapPolygon.strokeWidth = 3;
>     mapPolygon.strokeDashed = NO;
>
>     MSMapElementLayer* highlightsLayer = [MSMapElementLayer layer];
>     highlightsLayer.zIndex = 1;
>     [[highlightsLayer elements] addMapElement:mapPolygon];
>     [[self.mapView layers] addMapLayer: highlightsLayer];
> }
>```
