
# Drawing with Polylines and Polygons

Frequently, you want to add a simple annotation to the map, which [MapIcons](../map-control-api/MapIcon.md) are well suited for. Sometimes you will want to highlight a geographic region, or draw additional paths between points on the map. To do this, you will want to use [MapPolygon](../map-control-api/MapPolygon.md) and [MapPolyline](../map-control-api/MapPolyline.md) classes, respectively.

## Examples

### Adding a line

Display a line by using the [MapPolyline](../map-control-api/MapPolyline.md). The following example shows how to add a dashed black line on an map.

**Swift**

> ``` swift
> func drawLineOnMap() {
>     let centerLatitude = mapView.mapCenter.latitude;
>     let centerLongitude = mapView.mapCenter.longitude;
>
>     let mapPolyline = MSMapPolyline()
>     let geopath = MSGeopath()
>     geopath.add(MSGeolocation(latitude: centerLatitude-0.0005, longitude: centerLongitude-0.001))
>     geopath.add(MSGeolocation(latitude: centerLatitude+0.0005, longitude: centerLongitude+0.001))
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
>     MSGeolocation *center = self.mapView.mapCenter;
>     double centerLatitude = center.latitude;
>     double centerLongitude = center.longitude;
>
>     MSMapPolyline* mapPolyline = [MSMapPolyline polyline];
>     MSGeopath *geopath = [MSGeopath geopath];
>     [geopath addLocation:[MSGeolocation locationWithLatitude: centerLatitude-0.0005 longitude: centerLongitude-0.001]];
>     [geopath addLocation:[MSGeolocation locationWithLatitude: centerLatitude+0.0005 longitude: centerLongitude+0.001]];
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

Display a multi-point shape on a map by using the [MapPolygon](../map-control-api/MapPolygon.md). The following example show how to add a red box with blue outline on a map.

**Swift**

> ``` swift
> func highlightArea() {
>     let centerLatitude = mapView.mapCenter.latitude;
>     let centerLongitude = mapView.mapCenter.longitude;
>
>     let mapPolygon = MSMapPolygon()
>     let geopath = MSGeopath()
>     geopath.add(MSGeolocation(latitude: centerLatitude+0.0005, longitude: centerLongitude-0.001))
>     geopath.add(MSGeolocation(latitude: centerLatitude-0.0005, longitude: centerLongitude-0.001))
>     geopath.add(MSGeolocation(latitude: centerLatitude-0.0005, longitude: centerLongitude+0.001))
>
>     mapPolygon.path = geopath
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
>     MSGeolocation *center = self.mapView.mapCenter;
>     double centerLatitude = center.latitude;
>     double centerLongitude = center.longitude;
>
>     MSMapPolygon* mapPolygon = [MSMapPolygon polygon];
>     MSGeopath *geopath = [MSGeopath geopath];
>     [geopath addLocation:[MSGeolocation locationWithLatitude: centerLatitude+0.0005 longitude: centerLongitude-0.001]];
>     [geopath addLocation:[MSGeolocation locationWithLatitude: centerLatitude-0.0005 longitude: centerLongitude-0.001]];
>     [geopath addLocation:[MSGeolocation locationWithLatitude: centerLatitude-0.0005 longitude: centerLongitude+0.001]];
>     [geopath addLocation:[MSGeolocation locationWithLatitude: centerLatitude+0.0005 longitude: centerLongitude+0.001]];
>
>     mapPolygon.path = geopath;
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
