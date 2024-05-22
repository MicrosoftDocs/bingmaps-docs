---
title: Tile Layers | Microsoft Docs
description: Describes TileLayer class as part of the Bing Maps native controls and provides syntax examples to show traffic on maps and removing overlay tiles on maps.
ms.author: pablocan
---

# Tile Layers

[!INCLUDE [bing-maps-sdk-for-android-iOS-retirement](../../includes/bing-maps-sdk-for-android-iOS-retirement.md)]

In the Bing Maps native controls we have introduced a TileLayer class that makes it easy to separate multiple data sets as layers.

Note that a few different types of tile layers are provided, giving you flexibility in how you overlay custom information on the map.

Class                                                     |  Description
----------------------------------------------------------| -------------------
[UriTileMapLayer](../map-control-api/UriTileMapLayer-class.md)              | Retrieves custom tiles using a URL template that the map will use to retrieve specific tiles from an HTTP Web Server.
[CustomTileMapLayer](../map-control-api/CustomTileMapLayer-class.md)        | Retrieves tiles from developer code.
[GroundOverlayMapLayer](../map-control-api/GroundOverlayMapLayer-class.md)  | Displays an image in a geographic area.


Also, an out-of-the box TileMapLayer is provider for displaying Traffic Flow:

Class                                                  |  Description
------------------------------------------------------ | -------------------
[TrafficFlowMapLayer](../map-control-api/TrafficFlowMapLayer-class.md)      | Displays traffic on the map.

## Examples

### Show traffic on the map

**Android**

>```java
>TrafficFlowMapLayer trafficFlowMapLayer = new TrafficFlowMapLayer();
>mMap.getLayers().add(trafficFlowMapLayer);
>```

**Swift**

>```swift
> let trafficLayer = MSMapTrafficFlowMapLayer()
> mMap.layers.add(trafficLayer)
>```

**Objective-C**

>```Objectivec
>MSMapTrafficFlowMapLayer *trafficLayer = [MSMapTrafficFlowMapLayer layer];
>[self.mMap.layers addMapLayer:trafficLayer];
>```

### Overlay tiles from a web service

The following example shows how to overlay tiles retrieved from a web services by instantiating an `UriTileMapLayer` and specifying the
format of URL to the tiles.

**Swift**

>```swift
> let urlLayer = MSMapUriTileMapLayer()
> urlLayer.uriFormatString = "http://www.<web service name>.com/z={zoomlevel}&x={x}&y={y}"
> self.mapView.layers.add(urlLayer)
>```

### Overlay tiles from a custom source

The following example shows how to overlay custom tiles on a map by using `CustomTileMapLayer`. Create tiles programmatically in memory on
the fly, or write your own code to load existing tiles from another source.

The following examples show how to provide custom tiles by specifying the callback which return tiled image to be displayed on a map.

**swift**

>```swift
> // In your ViewController, subclass of MKMapViewDelegate.
> class ViewController: UIViewController, MSMapCustomTileMapLayerDelegate {
>
> ...
> //  Set the delegate and add the custom tile map layer to map.
> let customLayer = MSMapCustomTileMapLayer()
> customLayer.delegate = self;
> self.mapView.layers.add(customLayer)
> ...
>
> // This example creates random colored tiles with random alpha value between 200 and 255 (fully opaque).
> func customTileMapLayerOnBitmapRequestedAt(x: Int32, y: Int32, zoom: Int32, completionHandler: ((Data?) -> Void)!) {
>     let pixelHeight:Int32 = 256
>     let pixelWidth:Int32 = 256
>     let bpp:Int32 = 4
>     let bitsPerComponent = 8
>     let red = UInt8.random(in:0 ... 255)
>     let green = UInt8.random(in:0 ... 255)
>     let blue = UInt8.random(in:0 ... 255)
>     let alpha = UInt8.random(in:200 ... 255)
>
>     var bytes = [UInt8](repeating: UInt8(128), count:Int(pixelHeight * pixelWidth * bpp))
>
>     for i in 0..<pixelHeight {
>         for j in 0..<pixelWidth {
>             let pixelIndex = i * pixelWidth + j
>             let byteIndex = pixelIndex * bpp
>
>             bytes[Int(byteIndex)] = red
>             bytes[Int(byteIndex + 1)] = green
>             bytes[Int(byteIndex + 2)] = blue
>             bytes[Int(byteIndex + 3)] = alpha
>         }
>     }
>
>     let colorSpace = CGColorSpaceCreateDeviceRGB()
>     let bitmapInfo:CGBitmapInfo = CGBitmapInfo(rawValue:CGImageAlphaInfo.premultipliedLast.rawValue)
>     guard let provider = CGDataProvider(data: NSData(bytes:bytes, length:bytes.count)
>         )
>         else {
>             completionHandler(nil)
>             return
>         }
>
>     guard let imageRef = CGImage(
>         width: Int(pixelWidth),
>         height: Int(pixelHeight),
>         bitsPerComponent: bitsPerComponent,
>         bitsPerPixel: Int(bpp) * bitsPerComponent,
>         bytesPerRow: Int(pixelWidth * bpp),
>         space: colorSpace,
>         bitmapInfo: bitmapInfo,
>         provider: provider,
>         decode: nil,
>         shouldInterpolate: false,
>         intent: .defaultIntent)
>         else {
>             completionHandler(nil)
>             return
>     }
>
>     let image = UIImage(cgImage:imageRef)
>
>     completionHandler(image.pngData())
> }
>```

### Overlay tiles by binding an image to a bounding box area on a map

The following example shows how to overlay tiles by instantiating a `GroundOverlayMapLayer` and specifying the image and bounding box of
the layer.

**Swift**

>```swift
> let url = URL(string: "https://bingmapsisdk.blob.core.windows.net/isdksamples/us_counties.png")
> let boundingBox = MSGeoboundingBox(
>     northwestCorner: MSGeoposition(latitude: 50, longitude: -126),
>     southeastCorner: MSGeoposition(latitude: 25, longitude: -66))
>
> do{
>     let data = try Data(contentsOf: url!)
>     groundOverlayLayer = MSMapGroundOverlayMapLayer(
>         image:UIImage(data:data)!,
>         boundingBox: boundingBox)
>
>     let scene = MSMapScene(location: MSGeopoint(latitude: 40, longitude: -98), zoomLevel: 4)
>     self.mapView.setScene(scene, with: .none)
>     mapView.layers.add(groundOverlayLayer)
> }
> catch{
> }
>```

## Removing overlay tiles from a map

The following example shows how to remove all overlay tiles from a map.

**Swift**

>```swift
> self.mapView.layers.clear();
>```
