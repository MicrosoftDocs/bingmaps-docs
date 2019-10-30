---
title: "Drawing with Polylines and Polygons | Microsoft Docs"
author: "pablocan"
---

# Drawing with Polylines and Polygons

Frequently, you want to add a simple annotation to the map, which [MapIcons](../map-control-api/mapIcon-class.md)
are well suited for. Sometimes you will want to highlight a geographic region, or draw additional paths between points on the map. To do
this, you will want to use [MapPolygon](../map-control-api/mappolygon-class.md) and
[MapPolyline](../map-control-api/MapPolyline-class.md) classes, respectively.

## Examples

### Adding a line

Display a line by using the [MapPolyline](../map-control-api/mappolyline-class.md).
The following example shows how to add a dashed black line on a map.

**Java**

>```java
> void drawLineOnMap() {
>     Geoposition center = mapView.getCenter().getPosition();
>
>     ArrayList<Geoposition> geopoints = new ArrayList<Geoposition>();
>     geopoints.add(new Geoposition(center.getLatitude() - 0.0005, center.getLongitude() - 0.001));
>     geopoints.add(new Geoposition(center.getLatitude() + 0.0005, center.getLongitude() + 0.001));
>
>     MapPolyline mapPolyline = new MapPolyline();
>     mapPolyline.setPath(new Geopath(geopoints));
>     mapPolyline.setStrokeColor(Color.BLACK);
>     mapPolyline.setStrokeWidth(3);
>     mapPolyline.setStrokeDashed(true);
>
>     // Add Polyline to a layer on the map control.
>     MapElementLayer linesLayer = new MapElementLayer();
>     linesLayer.setZIndex(1.0f);
>     linesLayer.getElements().add(mapPolyline);
>     mapView.getLayers().add(linesLayer);
> }
>```

**Swift**

>```swift
> func drawLineOnMap() {
>     let center = self.mapView.mapCenter.position
>
>     let geopath = MSGeopath(positions:
>         [MSGeoposition(latitude: center.latitude-0.0005, longitude: center.longitude-0.001),
>          MSGeoposition(latitude: center.latitude+0.0005, longitude: center.longitude+0.001)])
>
>     let mapPolyline = MSMapPolyline()
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
>```

**Objective-C**

>```objectivec
> - (void) drawLineOnMap
> {
>     MSGeoposition *center = self.mapView.mapCenter.position;
>
>     NSMutableArray<MSGeoposition*>* positions;
>     [positions addObject:[MSGeoposition geopositionWithLatitude: center.latitude-0.0005 longitude: center.longitude-0.001]];
>     [positions addObject:[MSGeoposition geopositionWithLatitude: center.latitude+0.0005 longitude: center.longitude+0.001]];
>     MSGeopath *geopath = [MSGeopath geopathWithPositions:positions];
>
>     MSMapPolyline* mapPolyline = [MSMapPolyline polyline];
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
>```

### Adding a shape

Display a multi-point shape on a map by using the [MapPolygon](../map-control-api/mappolygon-class.md).
The following exampe shows how to add a red box with blue outline on a map.

**Java**

>```java
> void highlightArea() {
>     Geoposition center = mapView.getCenter().getPosition();
>
>     ArrayList<Geoposition> geopoints = new ArrayList<Geoposition>();
>     geopoints.add(new Geoposition(center.getLatitude() + 0.0005, center.getLongitude() - 0.001));
>     geopoints.add(new Geoposition(center.getLatitude() - 0.0005, center.getLongitude() - 0.001));
>     geopoints.add(new Geoposition(center.getLatitude() - 0.0005, center.getLongitude() + 0.001));
>
>     MapPolygon mapPolygon = new MapPolygon();
>     mapPolygon.setPaths(Arrays.asList(new Geopath(geopoints)));
>     mapPolygon.setFillColor(Color.RED);
>     mapPolygon.setStrokeColor(Color.BLUE);
>     mapPolygon.setStrokeWidth(3);
>     mapPolygon.setStrokeDashed(false);
>
>     MapElementLayer highlightsLayer = new MapElementLayer();
>     highlightsLayer.setZIndex(1.0f);
>     highlightsLayer.getElements().add(mapPolygon);
>     mapView.getLayers().add(highlightsLayer);
> }
>```

**Swift**

>```swift
> func highlightArea() {
>     let center = self.mapView.mapCenter.position
>
>     let geopath = MSGeopath(positions:
>         [MSGeoposition(latitude: center.latitude+0.0005, longitude: center.longitude-0.001),
>          MSGeoposition(latitude: center.latitude-0.0005, longitude: center.longitude-0.001),
>          MSGeoposition(latitude: center.latitude-0.0005, longitude: center.longitude+0.001)])
>
>     let mapPolygon = MSMapPolygon()
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
>```

**Objective-C**

>```objectivec
> - (void) highlightArea
> {
>     MSGeoposition *center = self.mapView.mapCenter.position;
>
>     NSMutableArray<MSGeoposition*>* positions;
>     [positions addObject:[MSGeoposition geopositionWithLatitude: center.latitude+0.0005 longitude: center.longitude-0.001]];
>     [positions addObject:[MSGeoposition geopositionWithLatitude: center.latitude-0.0005 longitude: center.longitude-0.001]];
>     [positions addObject:[MSGeoposition geopositionWithLatitude: center.latitude-0.0005 longitude: center.longitude+0.001]];
>     [positions addObject:[MSGeoposition geopositionWithLatitude: center.latitude+0.0005 longitude: center.longitude+0.001]];
>     MSGeopath *geopath = [MSGeopath geopathWithPositions:positions];
>
>     MSMapPolygon* mapPolygon = [MSMapPolygon polygon];
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

_See also_
[Map Polylines and Polygons](map-polylines-and-polygons.md)
