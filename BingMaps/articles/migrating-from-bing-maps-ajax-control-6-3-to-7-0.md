---
title: "Migrating from Bing Maps AJAX Control 6.3 to 7.0 | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 850b2330-86dc-45ae-a9f5-5f78e65d9375
caps.latest.revision: 7
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# Migrating from Bing Maps AJAX Control 6.3 to 7.0
This topic contains information to help you migrate your [!INCLUDE[vemc_product_name](../articles/includes/vemc-product-name-md.md)] code to [!INCLUDE[bmmc_product_name](../articles/includes/bmmc-product-name-md.md)].  
  
## 6.3 to 7.0 API Migration Tables  
  
### All Types  
 The table below lists every type found in the [!INCLUDE[vemc_product_name](../articles/includes/vemc-product-name-md.md)] API and provides the corresponding [!INCLUDE[bmmc_product_name](../articles/includes/bmmc-product-name-md.md)] type or functionality to use.  
  
|[!INCLUDE[vemc_product_name](../articles/includes/vemc-product-name-md.md)] 6.3 Type|Corresponding [!INCLUDE[bmmc_product_name](../articles/includes/bmmc-product-name-md.md)] Functionality|  
|--------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|  
|[VEAltitudeMode Enumeration](http://msdn.microsoft.com/en-us/5bdff0ae-b89e-4393-b5e6-134c7fec5fee)|AltitudeReference Enumeration|  
|[VEBirdseyeScene Class](http://msdn.microsoft.com/en-us/1c543c1c-549c-41d1-ba15-695d1897bf7f)|To set the map type to bird’s eye, use the **birdseye** member of the [MapTypeId Enumeration](../Topic/MapTypeId%20Enumeration1.md).|  
|[VEClusteringOptions Class](http://msdn.microsoft.com/en-us/21e1a9b9-09ff-4b06-bfbf-4ca1dea0033c)|Pushpin clustering it not supported.|  
|[VEClusteringType Enumeration](http://msdn.microsoft.com/en-us/14378073-cc4b-4230-9e31-2b817468252d)|Pushpin clustering it not supported.|  
|[VEClusterSpecification Class](http://msdn.microsoft.com/en-us/35141c39-76da-472f-bc89-fac272827492)|Pushpin clustering it not supported.|  
|[VEColor Class](http://msdn.microsoft.com/en-us/36f8276e-0efa-4a8e-99cf-5271b9441637)|[Color Class](../Topic/Color%20Class1.md)|  
|[VECustomIconSpecification Class](http://msdn.microsoft.com/en-us/7d81cf78-5c38-4e8b-8ce5-dabf079d1597)|Use the **icon** property of the [PushpinOptions Object](../Topic/PushpinOptions%20Object1.md) to customize your pushpin icon.|  
|[VEDashboardSize Enumeration](http://msdn.microsoft.com/en-us/b5fbd356-2261-4ceb-b638-d6d8c1220a36)|Use the **showDashboard** and **showMapTypeSelector** options of the [MapOptions Object](../Topic/MapOptions%20Object2.md) to customize the map navigation control.|  
|[VEDataType Enumeration](http://msdn.microsoft.com/en-us/2c93da6d-d205-4d1c-a320-5fa7d1f20d0c)|Data import is not supported in 7.0.|  
|[VEDistanceUnit Enumeration](http://msdn.microsoft.com/en-us/51473a47-00be-467b-a342-ecbcb21d5449)|Both miles and kilometers are displayed on the map control. Meters are used for API measurements.|  
|[VEException Class](http://msdn.microsoft.com/en-us/3894bfc0-6009-409d-bc8b-0ca3a10e00f9)|An error message is returned.|  
|[VEFailedShapeRequest Enumeration](http://msdn.microsoft.com/en-us/c41bb7bf-f013-42d4-af84-f7023df324b5)|Due to implementation differences, there is not a need for a corresponding type.|  
|[VEFindResult Class](http://msdn.microsoft.com/en-us/43632ca8-4d62-4b6b-9274-259d7f6a5679)|Find a location by [address](../rest-services/find-a-location-by-address.md), [point](../rest-services/find-a-location-by-point.md), or [query](../rest-services/find-a-location-by-query.md) using the [Bing Maps REST Services](../rest-services/bing-maps-rest-services.md) and display it on the map as described in [Geocoding a Location](../Topic/Geocoding%20a%20Location.md).|  
|[VEFindType Enumeration](http://msdn.microsoft.com/en-us/66c41234-157c-4f48-bbfc-8d726301f32a)|Find a location by [address](../rest-services/find-a-location-by-address.md), [point](../rest-services/find-a-location-by-point.md), or [query](../rest-services/find-a-location-by-query.md) using the [Bing Maps REST Services](../rest-services/bing-maps-rest-services.md) and display it on the map as described in [Geocoding a Location](../Topic/Geocoding%20a%20Location.md).|  
|[VEGeocodeLocation Class](http://msdn.microsoft.com/en-us/255fbe5f-b633-4a16-9b20-29af94aaab40)|Find a location by [address](../rest-services/find-a-location-by-address.md), [point](../rest-services/find-a-location-by-point.md), or [query](../rest-services/find-a-location-by-query.md) using the [Bing Maps REST Services](../rest-services/bing-maps-rest-services.md) and display it on the map as described in [Geocoding a Location](../Topic/Geocoding%20a%20Location.md).|  
|[VEGeocodeOptions Class](http://msdn.microsoft.com/en-us/1f8153f9-5f86-41be-b193-4a9c1ce535c0)|Find a location by [address](../rest-services/find-a-location-by-address.md), [point](../rest-services/find-a-location-by-point.md), or [query](../rest-services/find-a-location-by-query.md) using the [Bing Maps REST Services](../rest-services/bing-maps-rest-services.md) and display it on the map as described in [Geocoding a Location](../Topic/Geocoding%20a%20Location.md).|  
|[VEImageryMetadata Class](http://msdn.microsoft.com/en-us/6939a2fa-a9a3-4d33-ad68-6989dc78e5ea)|Use the [Bing Maps REST Services](../rest-services/bing-maps-rest-services.md) to retrieve imagery metadata as described in the [Get Imagery Metadata](../rest-services/get-imagery-metadata.md) topic.|  
|[VEImageryMetadataOptions Class](http://msdn.microsoft.com/en-us/04431299-46ef-404c-8f6c-a9b0aa2836d7)|Use the [Bing Maps REST Services](../rest-services/bing-maps-rest-services.md) to retrieve imagery metadata as described in the [Get Imagery Metadata](../rest-services/get-imagery-metadata.md) topic.|  
|[VELatLong Class](http://msdn.microsoft.com/en-us/663fe8e0-447b-4fe7-b72b-d84aeb280950)|[Location Class](../Topic/Location%20Class2.md)|  
|[VELatLongRectangle Class](http://msdn.microsoft.com/en-us/0b1bfeea-6941-457d-b49f-ba0bfaaeee22)|[LocationRect Class](../Topic/LocationRect%20Class1.md)|  
|[VELocationPrecision Enumeration](http://msdn.microsoft.com/en-us/044d779f-72e9-4179-b31e-950f0d5805bd)|Find a location by [address](../rest-services/find-a-location-by-address.md), [point](../rest-services/find-a-location-by-point.md), or [query](../rest-services/find-a-location-by-query.md) using the [Bing Maps REST Services](../rest-services/bing-maps-rest-services.md) and display it on the map as described in [Geocoding a Location](../Topic/Geocoding%20a%20Location.md).|  
|[VEMap Class](http://msdn.microsoft.com/en-us/bed0388a-f4a9-4b36-bbb8-c0d88038c14c)|[Map Class](../Topic/Map%20Class3.md)|  
|[VEMapMode Enumeration](http://msdn.microsoft.com/en-us/356199a6-8284-42d8-ac5c-760bce47d87a)|3D is not supported. All available map types are found in the [MapTypeId Enumeration](../Topic/MapTypeId%20Enumeration1.md).|  
|[VEMapOptions Class](http://msdn.microsoft.com/en-us/4bfe4cda-4b5d-421e-8457-462d852736cd)|[MapOptions Object](../Topic/MapOptions%20Object2.md)|  
|[VEMapStyle Enumeration](http://msdn.microsoft.com/en-us/63c1ea03-24ba-41ff-bad5-dafc9fc1c74e)|[MapTypeId Enumeration](../Topic/MapTypeId%20Enumeration1.md)|  
|[VEMapViewSpecification Class](http://msdn.microsoft.com/en-us/b19f6f2d-92ff-45cc-ad88-4afe735a506e)|[ViewOptions Object](../Topic/ViewOptions%20Object2.md)|  
|[VEMatchCode Enumeration](http://msdn.microsoft.com/en-us/d5f33505-89db-4d7a-8ee3-d01cfa1c5c61)|Find a location by [address](../rest-services/find-a-location-by-address.md), [point](../rest-services/find-a-location-by-point.md), or [query](../rest-services/find-a-location-by-query.md) using the [Bing Maps REST Services](../rest-services/bing-maps-rest-services.md) and display it on the map as described in [Geocoding a Location](../Topic/Geocoding%20a%20Location.md).|  
|[VEMatchConfidence Enumeration](http://msdn.microsoft.com/en-us/a59ffebc-d0f2-4569-a88f-2909533b23c2)|Find a location by [address](../rest-services/find-a-location-by-address.md), [point](../rest-services/find-a-location-by-point.md), or [query](../rest-services/find-a-location-by-query.md) using the [Bing Maps REST Services](../rest-services/bing-maps-rest-services.md) and display it on the map as described in [Geocoding a Location](../Topic/Geocoding%20a%20Location.md).|  
|[VEMiniMapSize Enumeration](http://msdn.microsoft.com/en-us/59d7924a-16c2-475c-aa7d-33c183635dca)|The mini map, also known as the overview map, is not supported. Add a second smaller map to your HTML page to simulate the overview map.|  
|[VEModelFormat Enumeration](http://msdn.microsoft.com/en-us/f81d90f9-a297-4fc0-97e8-5d1510491d1d)|Models are not supported.|  
|[VEModelOrientation Class](http://msdn.microsoft.com/en-us/3206cbea-1d39-408a-9f8e-11fedbc1698f)|Models are not supported.|  
|[VEModelScale Class](http://msdn.microsoft.com/en-us/a3a30dfd-6d7f-4f20-a780-a77741d6d303)|Models are not supported.|  
|[VEModelScaleUnit Enumeration](http://msdn.microsoft.com/en-us/207d38cf-ca05-45ea-a091-9f66b89da40d)|Models are not supported.|  
|[VEModelSourceSpecification Class](http://msdn.microsoft.com/en-us/09798087-e6b4-4bde-b607-22d6b675997d)|Models are not supported.|  
|[VEModelStatusCode Enumeration](http://msdn.microsoft.com/en-us/0aab9cf2-a193-4a6c-8f5d-9413006cc871)|Models are not supported.|  
|[VEOrientation Enumeration](http://msdn.microsoft.com/en-us/a1207b80-2f4f-4dac-8185-0f50b95fda93)|Use the **heading** property of the [ViewOptions Object](../Topic/ViewOptions%20Object2.md).|  
|[VEPixel Class](http://msdn.microsoft.com/en-us/4da7a9d9-f466-454d-a211-d3bc3289b0ec)|[Point Class](../Topic/Point%20Class2.md)|  
|[VEPlace Class](http://msdn.microsoft.com/en-us/dfe97615-15cf-42c5-93c2-46f32940e040)|Find a location by [address](../rest-services/find-a-location-by-address.md), [point](../rest-services/find-a-location-by-point.md), or [query](../rest-services/find-a-location-by-query.md) using the [Bing Maps REST Services](../rest-services/bing-maps-rest-services.md) and display it on the map as described in [Geocoding a Location](../Topic/Geocoding%20a%20Location.md).|  
|[VEPrintOptions Class](http://msdn.microsoft.com/en-us/113860ae-db3b-4c09-a8f5-96c812f91bf0)|Printing is fully supported.|  
|[VERoute Class](http://msdn.microsoft.com/en-us/9e2ce903-0ad6-4e1e-b8cd-4a2a6ee32bf6)|[Route Class](../Topic/Route%20Class1.md)|  
|[VERouteDistanceUnit Enumeration](http://msdn.microsoft.com/en-us/6150807b-1ea9-4803-bee0-6802148a35e7)|[DistanceUnit Enumeration](../Topic/DistanceUnit%20Enumeration2.md)|  
|[VERouteHint Class](http://msdn.microsoft.com/en-us/b6dead71-02de-41f8-8b0e-66496b0ce8ba)|Use the **postIntersectionHint** and **preIntersectionHint** properties of the [DirectionsStep Class](../Topic/DirectionsStep%20Class.md).|  
|[VERouteItinerary Class](http://msdn.microsoft.com/en-us/a18d8c70-437e-4ef3-b1ff-a9cd91971530)|Use the **itineraryItems** property of the [RouteLeg Class](../Topic/RouteLeg%20Class1.md).|  
|[VERouteItineraryItem Class](http://msdn.microsoft.com/en-us/427a1bd7-da10-48e7-a89d-1c8a5a21bbc2)|[DirectionsStep Class](../Topic/DirectionsStep%20Class.md)|  
|[VERouteLeg Class](http://msdn.microsoft.com/en-us/2b53a4ae-ea71-4de3-979b-2459007a258e)|[RouteLeg Class](../Topic/RouteLeg%20Class1.md)|  
|[VERouteLocation Class](http://msdn.microsoft.com/en-us/5329fc7e-54ad-4790-9f7a-437fa311ce6d)|Use the **address** or **location** property of the [WaypointOptions Object](../Topic/WaypointOptions%20Object1.md).|  
|[VERouteMode Enumeration](http://msdn.microsoft.com/en-us/b9aa132b-f99e-4e75-9185-13e437af6ff5)|[RouteMode Enumeration](../Topic/RouteMode%20Enumeration1.md)|  
|[VERouteOptimize Enumeration](http://msdn.microsoft.com/en-us/cb4e7ee6-1c68-4bf8-bc13-15cde90440b3)|[RouteOptimization Enumeration](../Topic/RouteOptimization%20Enumeration3.md)|  
|[VERouteOptions Class](http://msdn.microsoft.com/en-us/0126e389-c562-4a0e-81e0-e598db6f01d2)|[DirectionsRequestOptions Object](../Topic/DirectionsRequestOptions%20Object1.md) or [DirectionsRenderOptions Object](../Topic/DirectionsRenderOptions%20Object2.md)|  
|[VERouteSegment Class](http://msdn.microsoft.com/en-us/203ffd5a-e520-4979-8b37-69a27fe5db64)|[RouteLeg Class](../Topic/RouteLeg%20Class1.md)|  
|[VERouteType Enumeration](http://msdn.microsoft.com/en-us/1bfd2a5b-9cd4-4015-9277-510ab73c4fe8)|[RouteOptimization Enumeration](../Topic/RouteOptimization%20Enumeration3.md)|  
|[VERouteWarning Class](http://msdn.microsoft.com/en-us/8b354edd-745b-420d-ba52-093a3c9318a3)|Use the **warnings** property of the [DirectionsStep Class](../Topic/DirectionsStep%20Class.md).|  
|[VERouteWarningSeverity Enumeration](http://msdn.microsoft.com/en-us/39cf25db-5937-4dc0-82da-6aa04d6ea69a)|Use the **warnings** property of the [DirectionsStep Class](../Topic/DirectionsStep%20Class.md).|  
|[VESearchOptions Class](http://msdn.microsoft.com/en-us/9439037d-eeac-428f-8f3b-cb890fc21f0d)|Find a location by [address](../rest-services/find-a-location-by-address.md), [point](../rest-services/find-a-location-by-point.md), or [query](../rest-services/find-a-location-by-query.md) using the [Bing Maps REST Services](../rest-services/bing-maps-rest-services.md) and display it on the map as described in [Geocoding a Location](../Topic/Geocoding%20a%20Location.md).|  
|[VEShape Class](http://msdn.microsoft.com/en-us/730eed44-2c58-46ba-abd5-7fc5c04d353a)|[Pushpin Class](../Topic/Pushpin%20Class2.md), [Polygon Class](../Topic/Polygon%20Class3.md), [Polyline Class](../Topic/Polyline%20Class2.md)|  
|[VEShapeLayer Class](http://msdn.microsoft.com/en-us/0d140439-c977-455e-be98-4a61dc71ddc1)|Shapes and other objects on the map are items in the **entities** collection of the [Map Class](../Topic/Map%20Class3.md), which is an [EntityCollection](../Topic/EntityCollection%20Class1.md).|  
|[VEShapeAccuracy Enumeration](http://msdn.microsoft.com/en-us/e845fba3-2146-4f84-8d17-094925fe4d2f)|Due to implementation differences, there is not a need for a corresponding type.|  
|[VEShapeSourceSpecification Class](http://msdn.microsoft.com/en-us/4101d35a-33ff-4cd4-bf5f-ed4f42239367)|Shapes and other objects on the map are items in the **entities** collection of the [Map Class](../Topic/Map%20Class3.md), which is an [EntityCollection](../Topic/EntityCollection%20Class1.md).|  
|[VEShapeType Enumeration](http://msdn.microsoft.com/en-us/7bef306c-051f-42a7-a68a-8c2c3e5ab4fc)|Shapes can be either a [pushpin](../Topic/Pushpin%20Class2.md), [polygon](../Topic/Polygon%20Class3.md), or a [polyline](../Topic/Polyline%20Class2.md).|  
|[VETileSourceSpecification Class](http://msdn.microsoft.com/en-us/8c811e99-32b2-4fe1-8407-e32713f82b7f)|[TileSource Class](../Topic/TileSource%20Class2.md)|  
  
### VEMap Methods  
 The table below lists every method found in the [VEMap Class](http://msdn.microsoft.com/en-us/bed0388a-f4a9-4b36-bbb8-c0d88038c14c) of the [!INCLUDE[vemc_product_name](../articles/includes/vemc-product-name-md.md)] and provides the corresponding [!INCLUDE[bmmc_product_name](../articles/includes/bmmc-product-name-md.md)] functionality to use.  
  
|VEMap Class Method|Corresponding [!INCLUDE[bmmc_product_name](../articles/includes/bmmc-product-name-md.md)] Functionality|  
|------------------------|---------------------------------------------------------------------------------------------------|  
|[VEMap.AddControl Method](http://msdn.microsoft.com/en-us/2169ce78-863b-462f-b5b7-2fd9edcc48bf)|Use the **getRootElement** method of the [Map Class](../Topic/Map%20Class3.md) to retrieve the map `div` and add your own control.|  
|[VEMap.AddCustomLayer Method](http://msdn.microsoft.com/en-us/570e5d21-a864-40c0-b140-33d74a6ced09)|Custom layers are not supported.|  
|[VEMap.AddShape Method](http://msdn.microsoft.com/en-us/2381955d-d08c-4145-ab06-6f91f0050947)|Shapes and other objects on the map are items in the **entities** collection of the [Map Class](../Topic/Map%20Class3.md), which is an [EntityCollection](../Topic/EntityCollection%20Class1.md). Use the **push** or **insert** method of the [EntityCollection Class](../Topic/EntityCollection%20Class1.md) to add a shape to the map.|  
|[VEMap.AddShapeLayer Method](http://msdn.microsoft.com/en-us/44d227d2-bc88-43b3-ae34-f3b9f3a44e1d)|Shapes and other objects on the map are items in the **entities** collection of the [Map Class](../Topic/Map%20Class3.md), which is an [EntityCollection](../Topic/EntityCollection%20Class1.md).|  
|[VEMap.AddTileLayer Method](http://msdn.microsoft.com/en-us/f14b33af-e90f-4020-ad1e-a0962587c938)|Shapes and other objects on the map are items in the **entities** collection of the [Map Class](../Topic/Map%20Class3.md), which is an [EntityCollection](../Topic/EntityCollection%20Class1.md). Use the **push** or **insert** method of the [EntityCollection Class](../Topic/EntityCollection%20Class1.md) to add a [TileLayer Class](../Topic/TileLayer%20Class2.md) to the map.|  
|[VEMap.AttachEvent Method](http://msdn.microsoft.com/en-us/5163d7c9-6ad9-4725-be55-435ba36d03c8)|Use the **addHandler** or **addThrottledHandler** methods of the [Events Object](../Topic/Events%20Object.md).|  
|[VEMap.Clear Method](http://msdn.microsoft.com/en-us/db2decca-73c7-4b09-8e74-d12e2a2c1d85)|Objects on the map are items in the **entities** collection of the [Map Class](../Topic/Map%20Class3.md). Use the **clear** method of the [EntityCollection Class](../Topic/EntityCollection%20Class1.md) to clear the map.|  
|[VEMap.ClearInfoBoxStyles Method](http://msdn.microsoft.com/en-us/2b6459c8-63c8-4e67-8420-2d342941f7b4)|Customize your own info box using the **htmlContent** property of the [InfoboxOptions Object](../Topic/InfoboxOptions%20Object1.md). Set your options using the **setOptions** method of the [Infobox Class](../Topic/Infobox%20Class1.md).|  
|[VEMap.ClearTraffic Method](http://msdn.microsoft.com/en-us/d829f24b-524b-45cf-8ebd-cc1030201138)|Use the **hide** method of the [TrafficLayer Class (deprecated)](../Topic/TrafficLayer%20Class%20\(deprecated\).md).|  
|[VEMap.DeleteAllShapeLayers Method](http://msdn.microsoft.com/en-us/6374cd0e-905d-42e1-86a0-eaf32897a697)|Shapes and other objects on the map are items in the **entities** collection of the [Map Class](../Topic/Map%20Class3.md), which is an [EntityCollection](../Topic/EntityCollection%20Class1.md). Use the **clear** method of the [EntityCollection Class](../Topic/EntityCollection%20Class1.md) to delete all shapes on the map.|  
|[VEMap.DeleteAllShapes Method](http://msdn.microsoft.com/en-us/e27cf502-b91d-4e81-8e32-1770fa97e697)|Shapes and other objects on the map are items in the **entities** collection of the [Map Class](../Topic/Map%20Class3.md), which is an [EntityCollection](../Topic/EntityCollection%20Class1.md). Use the **clear** method of the [EntityCollection Class](../Topic/EntityCollection%20Class1.md) to delete all shapes on the map.|  
|[VEMap.DeleteControl Method](http://msdn.microsoft.com/en-us/3536a134-7b2c-49c2-a559-f9f8d8198816)|Use the **getRootElement** method of the [Map Class](../Topic/Map%20Class3.md) to retrieve the map `div` to delete the control you added.|  
|[VEMap.DeleteRoute Method](http://msdn.microsoft.com/en-us/6cd5e984-af34-48bf-89d8-2f0e63436bc2)|Use the **clearDisplay** or **resetDirections** methods of the [DirectionsManager Class](../Topic/DirectionsManager%20Class3.md).|  
|[VEMap.DeleteShape Method](http://msdn.microsoft.com/en-us/adce0438-7695-4dc5-aa2f-f915d268fde7)|Shapes and other objects on the map are items in the **entities** collection of the [Map Class](../Topic/Map%20Class3.md), which is an [EntityCollection](../Topic/EntityCollection%20Class1.md). Use the **remove** method of the [EntityCollection Class](../Topic/EntityCollection%20Class1.md) to remove a shape from the map.|  
|[VEMap.DeleteShapeLayer Method](http://msdn.microsoft.com/en-us/4ae3353c-8ade-4c27-9214-f329888f1d48)|Shapes and other objects on the map are items in the **entities** collection of the [Map Class](../Topic/Map%20Class3.md), which is an [EntityCollection](../Topic/EntityCollection%20Class1.md).|  
|[VEMap.DeleteTileLayer Method](http://msdn.microsoft.com/en-us/02ee5ca8-d479-4564-9900-286b2f3931c0)|Tile layers and other objects on the map are items in the **entities** collection of the [Map Class](../Topic/Map%20Class3.md), which is an [EntityCollection](../Topic/EntityCollection%20Class1.md). Use the **remove** method of the [EntityCollection Class](../Topic/EntityCollection%20Class1.md) to remove a tile layer from the map.|  
|[VEMap.DetachEvent Method](http://msdn.microsoft.com/en-us/73c97eec-ad1a-4332-991d-4757951667c0)|Use the **removeHandler** method of the [Events Object](../Topic/Events%20Object.md).|  
|[VEMap.Dispose Method](http://msdn.microsoft.com/en-us/7e11ffc8-1078-4f1a-a81a-9c436600ee42)|Use the **dispose** method of the [Map Class](../Topic/Map%20Class3.md).|  
|[VEMap.EnableShapeDisplayThreshold Method](http://msdn.microsoft.com/en-us/ab32e26b-a048-4c0a-814f-9d45a121b5d4)|Shape display threshold is not supported.|  
|[VEMap.EndContinuousPan Method](http://msdn.microsoft.com/en-us/cf4e7c54-65f5-4a67-859e-e939059af24f)|Use the Java Script **setTimeout** method and the **setView** method of the [Map Class](../Topic/Map%20Class3.md). Example code is found in the Appendix section at the end of this topic.|  
|[VEMap.Find Method](http://msdn.microsoft.com/en-us/fccbb414-44e1-47f0-a9a7-eb20728fc79d)|Find a location by [address](../rest-services/find-a-location-by-address.md), [point](../rest-services/find-a-location-by-point.md), or [query](../rest-services/find-a-location-by-query.md) using the [Bing Maps REST Services](../rest-services/bing-maps-rest-services.md) and display it on the map as described in [Geocoding a Location](../Topic/Geocoding%20a%20Location.md).|  
|[VEMap.FindLocations Method](http://msdn.microsoft.com/en-us/2bb1467e-4676-4e9e-9711-7707cb03c00f)|Find a location by [address](../rest-services/find-a-location-by-address.md), [point](../rest-services/find-a-location-by-point.md), or [query](../rest-services/find-a-location-by-query.md) using the [Bing Maps REST Services](../rest-services/bing-maps-rest-services.md) and display it on the map as described in [Geocoding a Location](../Topic/Geocoding%20a%20Location.md).|  
|[VEMap.Geocode Method](http://msdn.microsoft.com/en-us/37e0725f-fdae-4363-ae16-6ccea5348a21)|Find a location by [address](../rest-services/find-a-location-by-address.md), [point](../rest-services/find-a-location-by-point.md), or [query](../rest-services/find-a-location-by-query.md) using the [Bing Maps REST Services](../rest-services/bing-maps-rest-services.md) and display it on the map as described in [Geocoding a Location](../Topic/Geocoding%20a%20Location.md).|  
|[VEMap.GetAltitude Method](http://msdn.microsoft.com/en-us/e920d7bd-4537-4d0d-88c8-14d54053ddff)|Use the **getCenter** method of the [Map Class](../Topic/Map%20Class3.md) to return a [Location Class](../Topic/Location%20Class2.md), from which you can retrieve the **altitude**.|  
|[VEMap.GetBirdseyeScene Method](http://msdn.microsoft.com/en-us/41079210-829b-430e-93e9-0cf5e87ab9b1)|If the [MapTypeId](../Topic/MapTypeId%20Enumeration1.md) is birdseye, use the methods of the [Map Class](../Topic/Map%20Class3.md) to get information about the map view.|  
|[VEMap.GetCenter Method](http://msdn.microsoft.com/en-us/750ee0b4-2393-4554-80b6-867c6e575158)|Use the **getCenter** method of the [Map Class](../Topic/Map%20Class3.md).|  
|[VEMap.GetDirections Method](http://msdn.microsoft.com/en-us/6e777674-4be6-45ad-b8e3-4597ea98d08d)|Use the **calculateDirections** method of the [DirectionsManager Class](../Topic/DirectionsManager%20Class3.md).|  
|[VEMap.GetHeading Method](http://msdn.microsoft.com/en-us/39c2ecd0-d327-45c0-acce-4a17678838de)|Use the **getHeading** method of the [Map Class](../Topic/Map%20Class3.md).|  
|[VEMap.GetImageryMetadata Method](http://msdn.microsoft.com/en-us/0b4d3c57-89a2-4888-a823-5313af1d838a)|Use the [Bing Maps REST Services](../rest-services/bing-maps-rest-services.md) to retrieve imagery metadata as described in the [Get Imagery Metadata](../rest-services/get-imagery-metadata.md) topic.|  
|[VEMap.GetLeft Method](http://msdn.microsoft.com/en-us/70e2ffc5-00e2-439f-acfe-d92e2e3b3103)|Use the **getPageX** method of the [Map Class](../Topic/Map%20Class3.md).|  
|[VEMap.GetMapMode Method](http://msdn.microsoft.com/en-us/6063128c-c4a0-4253-bbf0-a7668d84d9d2)|3D is not supported. All available map types are found in the [MapTypeId Enumeration](../Topic/MapTypeId%20Enumeration1.md).|  
|[VEMap.GetMapStyle Method](http://msdn.microsoft.com/en-us/34840f07-bcf8-46c6-9448-08f92d1b6030)|Use the **getMapTypeId** method of the [Map Class](../Topic/Map%20Class3.md).|  
|[VEMap.GetMapView Method](http://msdn.microsoft.com/en-us/8f421e4c-5a45-4c72-930f-1ba1a6017519)|Use the methods of the [Map Class](../Topic/Map%20Class3.md) to return information about the current or target map view.|  
|[VEMap.GetPitch Method](http://msdn.microsoft.com/en-us/b5dfaad6-172f-4871-9554-86da0c5909fb)|3D is not supported.|  
|[VEMap.GetRoute Method](http://msdn.microsoft.com/en-us/9c458203-a333-47a5-89f6-75a71097dd33)|Use the **calculateDirections** method of the [DirectionsManager Class](../Topic/DirectionsManager%20Class3.md).|  
|[VEMap.GetShapeByID Method](http://msdn.microsoft.com/en-us/644df12f-e06f-4c04-9207-68096042287f)|Shapes and other objects on the map are items in the **entities** collection of the [Map Class](../Topic/Map%20Class3.md), which is an [EntityCollection](../Topic/EntityCollection%20Class1.md).|  
|[VEMap.GetShapeLayerByIndex Method](http://msdn.microsoft.com/en-us/cf345946-fea2-4519-b6f2-d303885146cb)|Shapes and other objects on the map are items in the **entities** collection of the [Map Class](../Topic/Map%20Class3.md), which is an [EntityCollection](../Topic/EntityCollection%20Class1.md). Use the **get** method of the [EntityCollection Class](../Topic/EntityCollection%20Class1.md) to return a shape by its index.|  
|[VEMap.GetShapeLayerCount Method](http://msdn.microsoft.com/en-us/f6552e7e-f6e1-4caa-b72f-aa342b071522)|Shapes and other objects on the map are items in the **entities** collection of the [Map Class](../Topic/Map%20Class3.md), which is an [EntityCollection](../Topic/EntityCollection%20Class1.md). Use the **getLength** method of the [EntityCollection Class](../Topic/EntityCollection%20Class1.md) to return the number of items in the collection.|  
|[VEMap.GetTileLayerByID Method](http://msdn.microsoft.com/en-us/479ce139-f605-4131-bea4-a7864fb435e6)|Tile layers and other objects on the map are items in the **entities** collection of the [Map Class](../Topic/Map%20Class3.md), which is an [EntityCollection](../Topic/EntityCollection%20Class1.md).|  
|[VEMap.GetTileLayerByIndex Method](http://msdn.microsoft.com/en-us/65fc5613-31c9-47b4-8fb6-0d5849687ae6)|Tile layers and other objects on the map are items in the **entities** collection of the [Map Class](../Topic/Map%20Class3.md), which is an [EntityCollection](../Topic/EntityCollection%20Class1.md). Use the **get** method of the [EntityCollection Class](../Topic/EntityCollection%20Class1.md) to return a tile layer by its index.|  
|[VEMap.GetTileLayerCount Method](http://msdn.microsoft.com/en-us/b33786fa-dbeb-4339-951f-09966c251e28)|Tile layers and other objects on the map are items in the **entities** collection of the [Map Class](../Topic/Map%20Class3.md), which is an [EntityCollection](../Topic/EntityCollection%20Class1.md). Use the **getLength** method of the [EntityCollection Class](../Topic/EntityCollection%20Class1.md) to return the number of items in the collection.|  
|[VEMap.GetTop Method](http://msdn.microsoft.com/en-us/7a3a84c0-7226-4363-9c17-804103312b09)|Use the **getPageY** method of the [Map Class](../Topic/Map%20Class3.md).|  
|[VEMap.GetVersion Method](http://msdn.microsoft.com/en-us/12d8f473-767e-4063-9cbf-0ab3fe89fec4)|Use the **getVersion** static method of the [Map Class](../Topic/Map%20Class3.md).|  
|[VEMap.GetZoomLevel Method](http://msdn.microsoft.com/en-us/37da8057-14ea-45e4-bbfd-732c204b58db)|Use the **getZoom** method of the [Map Class](../Topic/Map%20Class3.md).|  
|[VEMap.Hide3DNavigationControl Method](http://msdn.microsoft.com/en-us/7e1688ec-d339-4b0b-8af5-7dd72f4826c4)|3D is not supported.|  
|[VEMap.HideAllShapeLayers Method](http://msdn.microsoft.com/en-us/e4958ac1-7347-4d78-8e92-aaf2579d76c0)|Shapes and other objects on the map are items in the **entities** collection of the [Map Class](../Topic/Map%20Class3.md), which is an [EntityCollection](../Topic/EntityCollection%20Class1.md). Set the **visible** property of the [EntityCollectionOptions Object](../Topic/EntityCollectionOptions%20Object.md) to **false** using the **setOptions** method of the [EntityCollection Class](../Topic/EntityCollection%20Class1.md) to hide all shapes.|  
|[VEMap.HideBaseTileLayer Method](http://msdn.microsoft.com/en-us/b468dcdb-01dc-4dc6-96d5-5e99251d46a2)|Use the **setView** method of the [Map Class](../Topic/Map%20Class3.md) to set the **mapTypeId** property of the [ViewOptions Object](../Topic/ViewOptions%20Object2.md) to **mercator**.|  
|[VEMap.HideControl Method](http://msdn.microsoft.com/en-us/6ae26c12-5f9e-4e20-b68c-5a9f0a6c41bd)|Use the **getRootElement** method of the [Map Class](../Topic/Map%20Class3.md) to retrieve the map `div` to hide the control you added.|  
|[VEMap.HideDashboard Method](http://msdn.microsoft.com/en-us/118c6d22-2ab1-4140-b7df-167ed4d8ede8)|Use the **showDashboard** and **showMapTypeSelector** options of the [MapOptions Object](../Topic/MapOptions%20Object2.md) to customize the map navigation control.|  
|[VEMap.HideFindControl Method](http://msdn.microsoft.com/en-us/4599aef1-f9c3-45bf-b0a2-5c6a936f228b)|The find control is not supported.|  
|[VEMap.HideInfoBox Method](http://msdn.microsoft.com/en-us/80eec63c-bdbc-4798-8ef0-2e9ac17ed41d)|Set the **visible** property of the [InfoboxOptions Object](../Topic/InfoboxOptions%20Object1.md) to **false** using the **setOptions** method of the [Infobox Class](../Topic/Infobox%20Class1.md) to hide an info box.|  
|[VEMap.HideMiniMap Method](http://msdn.microsoft.com/en-us/1cb291a3-0324-4b6f-b984-1b334899591e)|The mini map, also known as the overview map, is not supported. Add a second smaller map to your HTML page to simulate the overview map.|  
|[VEMap.HideScalebar Method](http://msdn.microsoft.com/en-us/f1c23799-8303-4ff0-accc-e21968181e5b)|The scale bar cannot be hidden.|  
|[VEMap.HideTileLayer Method](http://msdn.microsoft.com/en-us/8fb01611-e2e3-4b56-bf56-e6bbeca3b750)|Set the **visible** property of the [TileLayerOptions Object](../Topic/TileLayerOptions%20Object1.md) to **false** using the **setOptions** method of the [TileLayer Class](../Topic/TileLayer%20Class2.md) to hide a tile layer.|  
|[VEMap.HideTrafficLegend Method](http://msdn.microsoft.com/en-us/da23f071-ef5e-4e2c-ac87-04b89356b2fb)|There is no traffic legend, but you can use the **hide** method of the [TrafficLayer Class (deprecated)](../Topic/TrafficLayer%20Class%20\(deprecated\).md) to hide traffic.|  
|[VEMap.Import3DModel Method](http://msdn.microsoft.com/en-us/2eb54b61-0b5c-4e78-a69c-3c03dd4d9c38)|Models are not supported.|  
|[VEMap.ImportShapeLayerData Method](http://msdn.microsoft.com/en-us/d7038b6c-671a-44ab-b048-90e491155fb3)|Data import is not supported.|  
|[VEMap.IncludePointInView Method](http://msdn.microsoft.com/en-us/d7a0de88-4159-4f5d-9f4d-47f46f85118b)|Use the **setView** method of the [Map Class](../Topic/Map%20Class3.md) to set the **bounds** of the map view to include a point.<br /><br /> map.setView({center: pointToInclude, bounds: new Microsoft.Maps.LocationRect.fromLocation(map.getCenter())})|  
|[VEMap.IsBirdseyeAvailable Method](http://msdn.microsoft.com/en-us/c57930d1-01e9-43f5-a22a-10824fb1a65b)|This functionality is not supported.|  
|[VEMap.LatLongToPixel Method](http://msdn.microsoft.com/en-us/c5e0aa97-3f30-4d19-891a-cb156e209d83)|Use the **tryLocationToPixel** method of the [Map Class](../Topic/Map%20Class3.md).|  
|[VEMap.LoadMap Method](http://msdn.microsoft.com/en-us/78792a1c-fc52-49d0-8932-7f6ae754583f)|Initialize a [Map Class](../Topic/Map%20Class3.md).|  
|[VEMap.LoadTraffic Method](http://msdn.microsoft.com/en-us/ee9965a8-b709-40c4-ace5-56279a144b2b)|Use the **show** method of the [TrafficLayer Class (deprecated)](../Topic/TrafficLayer%20Class%20\(deprecated\).md).|  
|[VEMap.Pan Method](http://msdn.microsoft.com/en-us/33319988-8d7a-49a4-8f76-ba072917bee6)|Use the **setView** method of the [Map Class](../Topic/Map%20Class3.md) to set the **centerOffset** property of the [ViewOptions Object](../Topic/ViewOptions%20Object2.md).<br /><br /> map.setView({center: map.getCenter(), centerOffset: new Microsoft.Maps.Point(10,10)});|  
|[VEMap.PanToLatLong Method](http://msdn.microsoft.com/en-us/3d294b12-0100-4e90-b62a-8507122316d2)|Use the **setView** method of the [Map Class](../Topic/Map%20Class3.md) to set the **center** property of the [ViewOptions Object](../Topic/ViewOptions%20Object2.md).|  
|[VEMap.PixelToLatLong Method](http://msdn.microsoft.com/en-us/a763ad29-005e-4378-9fa0-9b6326b25e7b)|Use the **tryPixelToLocation** method of the [Map Class](../Topic/Map%20Class3.md).|  
|[VEMap.RemoveCustomLayer Method](http://msdn.microsoft.com/en-us/0fcdf8ce-0caf-496d-aad5-19f5074b026e)|Custom layers are not supported.|  
|[VEMap.Resize Method](http://msdn.microsoft.com/en-us/be237d17-7b98-4038-978d-0d4123444b0f)|Set the **height** and **width** properties of the [MapOptions Object](../Topic/MapOptions%20Object2.md) using the **setOptions** method of the [Map Class](../Topic/Map%20Class3.md).|  
|[VEMap.Search Method](http://msdn.microsoft.com/en-us/37d650d2-aba0-4b02-bef3-167531cf4bbe)|Find a location by [address](../rest-services/find-a-location-by-address.md), [point](../rest-services/find-a-location-by-point.md), or [query](../rest-services/find-a-location-by-query.md) using the [Bing Maps REST Services](../rest-services/bing-maps-rest-services.md) and display it on the map as described in [Geocoding a Location](../Topic/Geocoding%20a%20Location.md).|  
|[VEMap.SetAltitude Method](http://msdn.microsoft.com/en-us/42cd2561-1396-41ae-9e9a-ab024a660ad6)|Set map view properties using the **setView** method of the [Map Class](../Topic/Map%20Class3.md).|  
|[VEMap.SetBirdseyeOrientation Method](http://msdn.microsoft.com/en-us/125b62fb-6e96-478f-a0a7-e55537df32c3)|Set map view properties using the **setView** method of the [Map Class](../Topic/Map%20Class3.md).|  
|[VEMap.SetBirdseyeScene Method](http://msdn.microsoft.com/en-us/3bbf2f97-6dab-46e5-9023-66a277a19857)|Set map view properties using the **setView** method of the [Map Class](../Topic/Map%20Class3.md).|  
|[VEMap.SetCenter Method](http://msdn.microsoft.com/en-us/e304cb20-9a09-4fdc-a74e-7eef8a3131ae)|Use the **setView** method of the [Map Class](../Topic/Map%20Class3.md) to set the **center** property of the [ViewOptions Object](../Topic/ViewOptions%20Object2.md).|  
|[VEMap.SetCenterAndZoom Method](http://msdn.microsoft.com/en-us/2778b7d1-3b7e-4518-87e0-e427f12a54c5)|Use the **setView** method of the [Map Class](../Topic/Map%20Class3.md) to set the **center** and **zoom** properties of the [ViewOptions Object](../Topic/ViewOptions%20Object2.md).|  
|[VEMap.SetClientToken Method](http://msdn.microsoft.com/en-us/af70cbf7-bab2-4f04-9ad3-4770e7181dad)|Client tokens are not supported.|  
|[VEMap.SetCredentials Method](http://msdn.microsoft.com/en-us/8e0d691c-05df-4022-83d4-0ca97cd4b914)|Use the **credentials** property of the [MapOptions Object](../Topic/MapOptions%20Object2.md) to set the map credentials. Your credentials are your Bing Maps Key. Information about getting a key is described in [Getting a Bing Maps Key](../getting-started/getting-a-bing-maps-key.md).|  
|[VEMap.SetDashboardSize Method](http://msdn.microsoft.com/en-us/7853fe7d-d5b4-472b-8b3b-167956a1e8a3)|Dashboard size modification is not supported.|  
|[VEMap.SetDefaultInfoBoxStyles Method](http://msdn.microsoft.com/en-us/85c31fcd-105c-4c5d-8dfc-b5774abc9d47)|Create a basic info box using the [Infobox Class](../Topic/Infobox%20Class1.md).|  
|[VEMap.SetFailedShapeRequest Method](http://msdn.microsoft.com/en-us/7ec59862-649c-41ea-9d5e-cd53d3ab7a27)|Due to implementation differences, there is not a need for corresponding functionality.|  
|[VEMap.SetHeading Method](http://msdn.microsoft.com/en-us/550ac0f8-a5df-4c6d-a937-ea2576916a44)|Use the **setView** method of the [Map Class](../Topic/Map%20Class3.md) to set the **heading** property of the [ViewOptions Object](../Topic/ViewOptions%20Object2.md).|  
|[VEMap.SetMapMode Method](http://msdn.microsoft.com/en-us/97f610ec-a667-4fe4-a581-4e1cb212b44f)|3D is not supported. All available map types are found in the [MapTypeId Enumeration](../Topic/MapTypeId%20Enumeration1.md).|  
|[VEMap.SetMapStyle Method](http://msdn.microsoft.com/en-us/370142af-d68c-4044-9243-d016e4ea558e)|Use the **setView** method of the [Map Class](../Topic/Map%20Class3.md) to set the **mapTypeId** property of the [ViewOptions Object](../Topic/ViewOptions%20Object2.md).|  
|[VEMap.SetMapView Method](http://msdn.microsoft.com/en-us/cadcc506-7000-43a8-a847-1f1a61e0c659)|Use the **setView** method of the [Map Class](../Topic/Map%20Class3.md) to set map view properties of the [ViewOptions Object](../Topic/ViewOptions%20Object2.md).|  
|[VEMap.SetMouseWheelZoomToCenter Method](http://msdn.microsoft.com/en-us/3e707edc-6ad3-462a-9f1b-5118c69aba11)|The mouse wheel always zooms to the cursor position on the screen.|  
|[VEMap.SetPitch Method](http://msdn.microsoft.com/en-us/475239a9-b28f-42de-b8a3-74f353213c94)|3D is not supported.|  
|[VEMap.SetPrintOptions Method](http://msdn.microsoft.com/en-us/29295763-9557-4ce4-81fd-42e370befc1d)|Printing is fully supported.|  
|[VEMap.SetScaleBarDistanceUnit Method](http://msdn.microsoft.com/en-us/6d3b75ac-03ad-4540-9fdf-a261a167c127)|Scale bar modification is not supported.|  
|[VEMap.SetShapesAccuracy Method](http://msdn.microsoft.com/en-us/e4c7a7ea-750b-4607-98f4-7231d05ff88a)|Due to implementation differences, there is not a need for corresponding functionality.|  
|[VEMap.SetShapesAccuracyRequestLimit Method](http://msdn.microsoft.com/en-us/72602e1d-5a87-42e2-b254-6a2ecd42851e)|Due to implementation differences, there is not a need for corresponding functionality.|  
|[VEMap.SetTileBuffer Method](http://msdn.microsoft.com/en-us/2060a58e-ce22-4d05-aea3-84126e713699)|Use the **setOptions** method of the [Map Class](../Topic/Map%20Class3.md) to set the **tileBuffer** property of the [MapOptions Object](../Topic/MapOptions%20Object2.md).|  
|[VEMap.SetTrafficLegendText Method](http://msdn.microsoft.com/en-us/a152fa71-b9fb-4891-8b3c-b5b9cd4d7ced)|There is no traffic legend, but use the **show** method of the [TrafficLayer Class (deprecated)](../Topic/TrafficLayer%20Class%20\(deprecated\).md) to display traffic.|  
|[VEMap.SetZoomLevel Method](http://msdn.microsoft.com/en-us/fa500dab-ce1a-434d-bb52-7e251b6627fd)|Use the **setView** method of the [Map Class](../Topic/Map%20Class3.md) to set the **zoom** property of the [ViewOptions Object](../Topic/ViewOptions%20Object2.md).|  
|[VEMap.Show3DBirdseye Method](http://msdn.microsoft.com/en-us/2d10546d-34b2-4682-b286-b79c571b9c0a)|Use the **setView** method of the [Map Class](../Topic/Map%20Class3.md)to set the **mapTypeId** property of the [ViewOptions Object](../Topic/ViewOptions%20Object2.md) to **birdseye**.|  
|[VEMap.Show3DNavigationControl Method](http://msdn.microsoft.com/en-us/4e2d1294-9214-4087-b6d9-977af9c17ae1)|3D is not supported.|  
|[VEMap.ShowAllShapeLayers Method](http://msdn.microsoft.com/en-us/ff584ae8-6f08-474c-bfe2-552377a8ee3d)|Shapes and other objects on the map are items in the **entities** collection of the [Map Class](../Topic/Map%20Class3.md), which is an [EntityCollection](../Topic/EntityCollection%20Class1.md). Set the **visible** property of the [EntityCollectionOptions Object](../Topic/EntityCollectionOptions%20Object.md) to **true** using the **setOptions** method of the [EntityCollection Class](../Topic/EntityCollection%20Class1.md) to show all shapes.|  
|[VEMap.ShowBaseTileLayer Method](http://msdn.microsoft.com/en-us/18b17bf3-3d4a-4aec-8e3a-dcb8eddb1b24)|By default the base tile layer is shown. If you have set the **mapTypeId** of the [ViewOptions Object](../Topic/ViewOptions%20Object2.md) to **mercator** to hide the base tiles, set the **mapTypeId** to another map type to show the base tiles again.|  
|[VEMap.ShowControl Method](http://msdn.microsoft.com/en-us/6c593255-d1d8-4922-98b6-61fd15e9f1e6)|Use the **getRootElement** method of the [Map Class](../Topic/Map%20Class3.md) to retrieve the map `div` to show a control you added.|  
|[VEMap.ShowDashboard Method](http://msdn.microsoft.com/en-us/440ca32a-b8e2-42b9-8f59-9a57d587b838)|Use the **showDashboard**, **showBreadcrumb**, and **showMapTypeSelector** options of the [MapOptions Object](../Topic/MapOptions%20Object2.md) to customize the map navigation control.|  
|[VEMap.ShowDisambiguationDialog Method](http://msdn.microsoft.com/en-us/dee6799b-afd7-4c90-9e79-be9fd810d5ff)|The disambiguation dialog is not supported.|  
|[VEMap.ShowFindControl Method](http://msdn.microsoft.com/en-us/5996441b-278f-441d-afd5-7b3194140863)|The find control is not supported.|  
|[VEMap.ShowInfoBox Method](http://msdn.microsoft.com/en-us/573f401a-2f1a-4b44-9a7f-f9e7c70e379e)|Add an info box to the map using the [Infobox Class](../Topic/Infobox%20Class1.md).|  
|[VEMap.ShowMessage Method](http://msdn.microsoft.com/en-us/b08ec4e9-d1a0-441d-9b77-fc71aee7c712)|Add a `div` to your HTML page to show a message.|  
|[VEMap.ShowMiniMap Method](http://msdn.microsoft.com/en-us/79adf44c-b3e1-4782-ac5b-d3664ac35fc1)|The mini map, also known as the overview map, is not supported. Add a second smaller map to your HTML page to simulate the overview map.|  
|[VEMap.ShowScalebar Method](http://msdn.microsoft.com/en-us/4636a77e-b586-43dd-92c1-e47d5e50e223)|Scale bar modification is not supported.|  
|[VEMap.ShowTileLayer Method](http://msdn.microsoft.com/en-us/3af812da-dbbe-430a-bdcf-a5bd7175162d)|Add a tile layer to the map using the [TileLayer Class](../Topic/TileLayer%20Class2.md).|  
|[VEMap.ShowTrafficLegend Method](http://msdn.microsoft.com/en-us/ccf568f8-c362-49cb-872b-50fd08616510)|There is no traffic legend, but use the **show** method of the [TrafficLayer Class (deprecated)](../Topic/TrafficLayer%20Class%20\(deprecated\).md) to display traffic.|  
|[VEMap.StartContinuousPan Method](http://msdn.microsoft.com/en-us/70546f59-83b9-4836-896c-13bd53ea73c8)|Use the Java Script **setTimeout** method and the **setView** method of the [Map Class](../Topic/Map%20Class3.md). Example code is found in the Appendix section at the end of this topic.|  
|[VEMap.ZoomIn Method](http://msdn.microsoft.com/en-us/6bca84f9-d273-4ab2-bbb9-1d70169d5ce2)|Use the **setView** method of the [Map Class](../Topic/Map%20Class3.md) to set the **zoom** property of the [ViewOptions Object](../Topic/ViewOptions%20Object2.md).|  
|[VEMap.ZoomOut Method](http://msdn.microsoft.com/en-us/965f23fc-4cfa-4854-98a8-a0a392589d1f)|Use the **setView** method of the [Map Class](../Topic/Map%20Class3.md) to set the **zoom** property of the [ViewOptions Object](../Topic/ViewOptions%20Object2.md).|  
  
## Appendix  
 The following code shows how to simulate continuous pan in [!INCLUDE[bmmc_product_name](../articles/includes/bmmc-product-name-md.md)].  
  
```  
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">  
<html>  
   <head>  
      <title></title>  
      <meta http-equiv="Content-Type" content="text/html; charset=utf-8">  
  
      <script type="text/javascript" src="http://ecn.dev.virtualearth.net/mapcontrol/mapcontrol.ashx?v=7.0"></script>  
  
      <script type="text/javascript">  
  
         var map = null;  
         var t = null;  
         var isPanning = false;  
  
         function GetMap()  
         {  
            // Initialize the map  
            map = new Microsoft.Maps.Map(document.getElementById("mapDiv"), {credentials:"Bing Maps Key"});   
  
         }  
  
         function StartPan()  
         {  
            if (!isPanning)  
            {  
                PanMap();  
                isPanning = true;  
            }  
         }  
  
         function PanMap()  
         {  
  
            map.setView({center: map.getCenter(), centerOffset: new Microsoft.Maps.Point(-10,0)});  
  
            t = setTimeout(PanMap, 200);  
  
         }  
  
         function EndPan()  
         {  
            clearTimeout(t);  
            isPanning = false;  
         }  
  
      </script>  
   </head>  
   <body onload="GetMap();">  
      <div id='mapDiv' style="position:relative; width:400px; height:400px;"></div>       
      <input type="button" value="Pan Map" onclick="StartPan()"/>    
      <input type="button" value="Stop Pan" onclick="EndPan()"/>  
   </body>  
</html>  
```  
  
## See Also  
 [Bing Maps AJAX Control, Version 6.3](http://msdn.microsoft.com/en-us/e3807b0c-5ad1-4bc1-bff0-7f4af0bad48d)   
 [Bing Maps AJAX Control, Version 7.0](../Topic/Bing%20Maps%20AJAX%20Control,%20Version%207.0.md)