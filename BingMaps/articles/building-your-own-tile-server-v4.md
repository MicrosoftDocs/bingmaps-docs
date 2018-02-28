---
title: "Building Your Own Tile Server (V4) | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 5f8ff83e-a8df-4b4d-8d13-61c20ac3e9a3
caps.latest.revision: 13
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# Building Your Own Tile Server (V4)
> [!CAUTION]
>  The content in this article may still be applicable to the current version of the [!INCLUDE[vemc_product_name](../articles/includes/vemc-product-name-md.md)], but it uses a previous version of the [!INCLUDE[vemc_product_name](../articles/includes/vemc-product-name-md.md)] which is no longer supported. More information about the current version of the [!INCLUDE[vemc_product_name](../articles/includes/vemc-product-name-md.md)] is found in the [Bing Map Control SDK](http://msdn.microsoft.com/en-us/library/bb429619.aspx).  
  
 Although [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] provides good map and aerial coverage of most areas, you are still the best authority on data availability and data quality for your own needs.  Whether you have advanced imagery, engineering plans, or transportation maps, serving this information to your users is often a challenging problem.  Fortunately, you can take advantage of [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] Tile Layers to create your own imagery server that integrates fully with the navigation methods, data and tools built into [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)].  
  
 The [!INCLUDE[vemc_product_name](../articles/includes/vemc-product-name-md.md)] SDK is built on a foundation of tiles.  Each tile represents a particular view of a rectangular piece of information.  Out of the box, you can use the [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] tile sets for regular map views, aerial views and hybrid map views.  However, you can also use the tiling system to serve up your own geospatially oriented information.  In other words, you can build your own tiles and "roll your own tile server" so that your users can see not only the built in maps, but your specific information.  
  
 In this article, we will look at the techniques you need to serve up your own image data using [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] technology.  
  
 ***Please note that accessing the [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] tile servers directly is neither recommended nor supported by Microsoft. The tile server paths are subject to change at any time without notice.***  
  
## Generating Tiles  
 The most difficult challenge in building your own tile server lies in matching up your data with the [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] map data.  This process is often challenging because you have to overcome the joined problems of projection and registration.  That is, you need to stretch your image to fit a [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] Mercator projection, and you also have to determine latitude and longitude boundaries of your image.  
  
### Understanding [!INCLUDE[ve_product_abbr](../articles/includes/ve-product-abbr-md.md)] Tiles  
 Behind the scenes, [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] divides up each map and map style into a set of 256 x 256 pixel tiles.  The tiles are stitched together according to a naming scheme that is based on the images position and relative degree of resolution.  Each tile is numbered according to where it is with respect to a 4 square quadrant system.  
  
### The Naming Scheme  
 You can easily find the name of specific tiles by going to [!INCLUDE[livemaps_web_site](../articles/includes/livemaps-web-site-md.md)] and using either the Internet Explorer [DevToolBar](http://www.microsoft.com/downloads/details.aspx?familyid=e59c3964-672d-4511-bb3e-2d5e1db91038&displaylang=en), or FireFox's [Firebug](https://addons.mozilla.org/firefox/1843/) tool, and turning on image paths.  If you look at a [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] map at the highest level, you will see four images representing the 4 256x256 tiles that make up the projection of the Earth.  
  
 ![64c1036f&#45;fb24&#45;4f93&#45;8310&#45;4b7ec9536c3f](../articles/media/64c1036f-fb24-4f93-8310-4b7ec9536c3f.jpg "64c1036f-fb24-4f93-8310-4b7ec9536c3f")  
  
 Figure 1 *Tile Naming Scheme*  
  
 As you zoom in, each of these top level tiles is further divided into 4 tiles.  The tile numbering scheme is therefore as follows:  
  
-   A letter code indicating style (r - road, a - aerial, h - hybrid)  
  
-   A series of "quadrant" numbers. The numbers will always be between 0 and 3 (inclusive) and represent the relative position of the tile.  The more numbers in the sequence, the greater the zoom level.  
  
 For example, a "max zoom" hybrid image of Qwest Field (where the Seattle Seahawks play) is numbered h0212300302202032001.  This would indicate that the image is 19 layers deep, in the upper right corner of its quadrant.  
  
### Bounding Tiles  
 Unfortunately, finding the latitude and longitude boundaries of a tile is a bit more difficult.  You have to start by breaking apart the quadrant key naming scheme and recursively calculating the latitude and longitude.  Rob Blackwell has developed an excellent utility that you can download from [http://www.robblackwell.org.uk/wp-content/ve.zip](http://www.robblackwell.org.uk/wp-content/ve.zip).  
  
### Preparing Your Own Tiles  
 To prepare your own tiles, you will need to cut your image into 256x256 pixel chunks and create a meaningful naming scheme.  You will also have to decide how you want to host your images.  If you intend to follow Microsoft's naming scheme, you will need to figure "register" your images with respect to the [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] tiles.  That is, your tiles must share bounding boxes with [!INCLUDE[ve_product_abbr](../articles/includes/ve-product-abbr-md.md)] tiles.  
  
### MapCruncher - A Short Cut  
 If you have a large image, you may be able to leverage Microsoft Research's [MapCruncher](http://research.microsoft.com/mapcruncher/) tool.  MapCruncher is a desktop application that will allow you to pick "registration" points on your image and map them to [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] locations.  Once you have enough registration points, MapCruncher will automatically reshape your image and divide it into tiles that match the [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] tiles.  MapCruncher will even build a webpage showing your tiles on top of [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)].  
  
 However, MapCruncher is currently restricted to noncommercial use.  Please look at the licensing information to see if MapCruncher will work for you.  
  
### Tile Layers  
 Once you have your tiles, using them from a [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] map is surprisingly easy.  In previous control versions (prior to [!INCLUDE[ve_product_abbr](../articles/includes/ve-product-abbr-md.md)] 3), you had to modify the underlying control to intercept the mapping calls.  Thanks to the Tile Layers exposed in version 3 of the control, all you need to do is to make a few simple JavaScript calls.  
  
### Adding a Tile Layer  
 If your tiles are named according to the [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] naming scheme, all you need to do is create a `VETileSourceSpecification` and call the `VEMap.AddTileSource()` method.  
  
### The Specification for [!INCLUDE[ve_product_abbr](../articles/includes/ve-product-abbr-md.md)] Tile Names  
  
```  
var bounds = [new VELatLongRectangle(new VELatLong(49,-123),new VELatLong(47,-121))];  
  
var tileSourceSpec = new VETileSourceSpecification();  
tileSourceSpec.ID = "lidar";  
tileSourceSpec.TileSource = "http://www.microsoft.com/maps/isdk/ajax/layers/lidar/%4.png";  
tileSourceSpec.NumServers = 1;  
tileSourceSpec.Bounds = bounds;  
tileSourceSpec.MinZoom = 10;  
tileSourceSpec.MaxZoom = 18;  
```  
  
 *Listing 1 Defining a Tile Layer*  
  
 The `VETileSourceSpecification` has several important properties:  
  
-   ID - The ID field simply identifies your layer, and can be any string value  
  
-   TileSource - The `TileSource` contains a URL that points to the servers that are going to host the tiles.  You can use three place holder variables within your URL.  
  
    -   %1 - This parameter is a place holder for map style.  If your tile images start with 'a', 'r', or 'h', and your TileSource contains %1, then the map will only display your tiles if the view style matches your image names.  If you omit this parameter, then your tiles will display on every view type.  
  
    -   %2 - This parameter is a place holder for the server number if you are using more than one server.  Use this place holder if you are hosting your tiles on multiple severs (numbered sequentially).  [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] will make requests to each server in a round-robin fashion.  
  
    -   %4 - The last parameter is a place holder for the default [!INCLUDE[ve_product_abbr](../articles/includes/ve-product-abbr-md.md)] numbering scheme.  Use this if you followed the [!INCLUDE[ve_product_abbr](../articles/includes/ve-product-abbr-md.md)] numbering scheme.  
  
-   NumServers - Set this parameter to 1 unless you also used the %2 place holder in your TileSource path.  This number represents the number of server paths you are using to host your tiles.  The servers must be named sequentially starting from 0 (eg. TileServer0, TileServer1, TileServer2).  
  
-   Bounds - Bounds represents a `VELatLongRectangle` defining the borders of the area where your tiles exist.  If your user pans into this area, your tiles will appear.  If the user moves out of the area, your tiles will not be requested.  
  
-   MinZoom, MaxZoom - These parameters define the minimum and maximum zoom levels for your tiles.  If your user moves outside the zoom range, your tiles will not appear.  The zoom range is from 1 (least zoomed in) to 19 (most zoomed in).  
  
### The Specification for Custom Names  
 If you chose to use a custom naming scheme, you will need to set a different set of parameters.  Specifically, the `NumServers` parameter and `TileSource` are ignored.  Instead, you set the `GetTilePath()` property to point to a JavaScript function.  Your JavaScript function receives a `VETileContext` parameter which provides the x and y position of the center of the tile and the zoom level.  Your function would have to convert these values into a fully qualified path.  
  
 Note that this system only works for 2D tile layers.  If you want to see layers in 3D, you must use the [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] naming scheme.  
  
### Adding the Tile Layer  
 Once your specification is built, you need to add a new tile layer to your map.  Adding a Tile Layer requires adding the specification as a `TileSource` and then defining the opacity and z index for the actual layer.  
  
```  
map.AddTileSource(tileSourceSpec);  
  
var tileLayer = new VELayerSpecification(VELayerType.VETileSource,"1", "lidar");  
tileLayer.Opacity=0.5;  
tileLayer.ZIndex = 0;  
  
map.AddLayer(tileLayer);  
```  
  
 *Listing 2 Adding the Layer*  
  
 An `Opacity` of 1 means that your tiles will completely obscure the [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] tiles.  An `Opacity` of about 0.05 makes your tiles completely transparent.  The `ZIndex` indicates the relative "height" of your tile layer compared to other tile layers on the map.  The higher the value, the more likely your layer is to be "on top".  Ordinarily, you can set `ZIndex` to 0 unless you are adding multiple tile layers.  If you have multiple tile layers, you will need to decide which ones are "more important" and set the `ZIndex` values accordingly.  
  
### Manipulating Layers  
 Once you have your layer in place, you can manipulate it by using the `ShowLayer()`, `HideLayer()` and `DeleteLayer()` commands.  Each of these commands takes the Layer ID as a parameter.  For instance, to hide the layer defined in Listing 1, you would need the following code:  
  
```  
map.HideLayer('lidar');  
```  
  
 *Listing 3 Hiding a Layer*  
  
 Note that if you delete a layer, you can re-add it simply by calling `AddLayer()` again.  You do not need to re-add the source.  
  
### Conclusion  
 Although [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] provides an extensive set of maps, you may find a need to add your own imagery.  Using this article as a starting point, you should be able to work through the challenges of registering your image to [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)], dividing up your image into tiles, deciding on an appropriate naming scheme, and adding your tile source to a [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] map.  
  
 This article was written by [Robert McGovern MVP (Bing Maps/MapPoint)](https://mvp.support.microsoft.com/profile=A9159573-40DB-4BD1-A079-D57C675E1766) from [Infusion Development](http://www.infusiondev.com/technology/Microsoft/MapPoint.htm).  Some of the content was drawn directly from a Via [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] article by [Rob Blackwell](mailto:rob.blackwell@aws.net).  Rob would also like to thank numerous sources on the [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] product team for additional details and content review.