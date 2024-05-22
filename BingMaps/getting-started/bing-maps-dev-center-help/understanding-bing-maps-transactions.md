---
title: "Understanding Bing Maps Transactions | Microsoft Docs"
description: "Describes how to understand Bing Maps transactions and provides a table that outlines Bing Maps transactions by API with category descriptions."
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 4bdf7358-a387-4193-8efa-6650b68ff82b
caps.latest.revision: 99
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Understanding Bing Maps Transactions

[!INCLUDE [bing-maps-enterprise-service-retirement](../../includes/bing-maps-enterprise-service-retirement.md)]

When you use any [Bing Maps API](../../rest-services/index.md) with a Bing Maps Key (you must have a [Bing Maps Account](https://www.bingmapsportal.com/)), transactions are recorded. Transactions track API usage and can be billable or non-billable. For example, using the [Bing Maps V8 Web Control](../../v8-web-control/index.md) to show a map on a web page or geocoding an address using the [Bing Maps REST Services](../../rest-services/index.md) are both billable transactions, while deleting a data source (a spatial database that you create using the [Bing Spatial Data Services](../../spatial-data-services/index.md)) is not.  
  
 You can find descriptions of the transactions for each Bing Maps API in the tables below, and you can view transaction totals over time on the [Bing Maps Account Center](https://www.bingmapsportal.com). For more information, see [Viewing Usage Reports](#viewing-usage-reports). Note that it may take up to 24 hours for new transactions to appear.  
  
## Viewing Usage Reports

 Follow these steps to view a transaction history for a Bing Maps Key and its associated applications.  
  
 **View usage report**  
  
1.  Sign in to the [Bing Maps Dev Center](https://www.bingmapsportal.com/).  
  
2.  Click **Usage Report** under **My account**.  
  
 **View usage report by key**  
  
1.  Sign in to the [Bing Maps Dev Center](https://www.bingmapsportal.com/).  
  
2.  Click **My Keys** under **My account**.  
  
3.  Click the **Usage Report** link next to the Bing Maps key you would like a report for.  
  
 **Additional Notes**  
  
 To change the range of dates for the report, use the options under the **Usage Period** field.  
  
 To export the data in the report, use the options under the **Export** field.  

## Billable versus non-billable transactions  

Only billable transactions count towards the free-use limits for Basic keys, and Enterprise keys are only charged for billable transactions.  Non-billable transactions do not incur charges and do not count towards free-use limits. To determine if your application will qualify for free use and for info about licensing and transaction limits, [please see the Bing Maps licensing page](https://www.microsoft.com/maps/licensing) and review the [Bing Maps Terms of Use](https://www.microsoft.com/maps/product/terms.html).
  
### Using Session IDs to make billable transactions non-billable

 In the following description, Bing Maps services refer to Bing Maps REST Services and Bing Spatial Data Services<sup>1</sup>. Bing Maps controls refer to Bing Maps V8 Web Control, Bing Maps WPF Control, and Windows 10 UWP Map control.  
  
Bing Maps service requests originating from a Bing Maps control that use a session ID instead of the Bing Maps key are non-billable up to 25 requests per session. The 26th transaction and every transaction thereafter will be billable. For example, if you make a Bing Maps REST Services request to geocode an address from the Bing Maps V8 web control and use the [Map.getCredentials](../../v8-web-control/map-control-api/map-class.md) method to get the session ID for authentication, the resulting transaction is recorded as non-billable even though it is listed as a billable transaction in the table below.  
  
 You must use the Bing Maps Key that you used to load the map control to request a session ID. This session ID is only valid for the map control session. For the Bing Maps V8 web control, a session begins with the load of the map into a user’s browser and ends when the browser is closed or the user moves to a different page. Similarly for the WPF control, a session begins when the map control is loaded by the application and ends when the application is closed. Note that the Windows 10 UWP Map control does not provide access to session keys but instead provides native geocoding and routing functionalities which automatically make use of sessions. For more information about how to get a session ID from the Bing Maps Key, see [Using the REST Services with .NET](../../rest-services/using-the-rest-services-with-net.md) and [Map Class](../../v8-web-control/map-control-api/map-class.md). Note that if you make service requests with a Bing Maps Key instead of a session ID within the session, you will be charged for all billable requests.  


## Bing Maps Transactions by API  
 The following tables define transactions for all the APIs.  
  
### Map Control APIs (Web V8, UWP, WPF, iOS, Android, Unity)  
  
|Category|Bing Maps API|Billable|Category Description|  
|--------------|-------------------|--------------|--------------------------|  
|iOS-Control|iOS Control|Yes|Any time a session is started and uses the Bing Maps iOS control with a valid Bing Maps Key, one (1) transaction is counted. A session begins with the load of the Bing Maps iOS control by the application and ends when the application is closed or the control is disposed. Panning, zooming, changing of the map type (i.e.: road, aerial, etc.) or overlaying data on the map within the session doesn't cause additional transactions to be accrued.<br /><br />Anytime the Map Services API is used without a map, one (1) transaction is counted. All REST service requests that originate from Map Services and use a session ID are not billable when they are made from within a session.|
|Android-Control|Android Control|Yes|Any time a session is started and uses the Bing Maps Android control with a valid Bing Maps Key, one (1) transaction is counted. A session begins with the load of the Bing Maps Android control by the application and ends when the application is closed or the control is disposed. Panning, zooming, changing of the map type (i.e.: road, aerial, etc.) or overlaying data on the map within the session doesn't cause additional transactions to be accrued.<br /><br />Anytime the Map Services API is used without a map, one (1) transaction is counted. All REST service requests that originate from Map Services and use a session ID are not billable when they are made from within a session.|
|Web-V8-Control (formerly AjaxSession-V8)|Web Control|Yes|Any time a session that uses the Bing Maps Version 8.0 web control, is started with a valid Bing Maps Key, one (1) transaction is counted. A session begins with the load of the Bing Maps Web Control into a user’s browser and ends when the browser is closed or the user moves to a different page. Panning, zooming, changing of the map type (i.e.: road, aerial, etc.) or overlaying data on the map within the session doesn't cause additional transactions to be accrued.<br /><br /> Anytime the Autosuggest Module is used without a map and a user selects a location suggestion from the menu one (1) transaction is counted.  When using the AutoSuggest Module, transactions are not logged for user key strokes or based on the number of location results that are returned in the Autosuggest menu.<br /><br /> All REST or Spatial Data<sup>2</sup> service requests that use a [session ID](#using-session-ids-to-make-billable-transactions-non-billable) are **not** billable when they are made from within a session.|  
|Win10-Control (formerly Win10-Native)|Windows 10 UWP Map control|Yes|Any time a session is started and uses the Windows 10 UWP Map control with a valid Bing Maps Key, one (1) transaction is counted. A session begins with the load of the Windows 10 UWP Map control in an application and ends when the application is closed or the control is disposed. Panning, zooming, changing of the map type (i.e.: road, aerial, etc.) or overlaying data on the map within the session doesn't cause additional transactions to be accrued.<br /><br />Anytime the Map Services API is used without a map, one (1) transaction is counted. All REST service requests that originate from Map Services and use a session ID are not billable when they are made from within a session.|  
|WPF-Control (formerly WPFSession)|WPF Control|Yes|Any time a session is started and uses the Bing Maps WPF control with a valid Bing Maps Key, one (1) transaction is counted. A session begins with the load of the Bing Maps WPF control by the application and ends when the application is closed or the control is disposed. Panning, zooming, changing of the map type (i.e.: road, aerial, etc.) or overlaying data on the map within the session doesn't cause additional transactions to be accrued.<br /><br /> All REST or Spatial Data<sup>2</sup> service requests that use a [session ID](#using-session-ids-to-make-billable-transactions-non-billable) are **not** billable when they are made from within a session.|
|Unity-Control (PREVIEW)|Unity Control|Yes|Any time an application session is started and uses a MapRenderer component and a MapSession component with a valid Bing Maps Key, one (1) transaction is counted. An application session begins with each initialization of a MapRenderer by the application and ends when the application is closed or the session expires. When a session expires and the application is still active, a new session is created and one (1) transaction is counted. Panning and zooming a MapRenderer doesn't cause additional transactions to be accrued. Any time the MapSession component's GetRegion API is called without a MapRenderer session already being active, one (1) transaction is counted. Any time a Map Service API is called, i.e.: MapLocationFinder, one (1) transaction is counted.|
  
<sup>2</sup>All Spatial Data Services requests over one (1) million per year are billable even when a session ID is used.  
  
### REST Services  
  
|Category|Bing Maps API|Billable|Category Description|  
|--------------|-------------------|--------------|--------------------------|  
|RESTAutosuggest| REST Services|Yes<sup>3</sup>|Any time ten (10) [Autosuggest](../../rest-services/autosuggest.md) URL requests are made to get suggested entity information, one (1) transaction is counted.|
|RESTElevations|REST Services|Yes<sup>3</sup>|Any time an [Elevations](../../rest-services/elevations/index.md) URL request is made to get elevation data, one (1) transaction is counted.|  
|RESTImagery|REST Services|Yes<sup>3</sup>|Any time an [Imagery](../../rest-services/imagery/index.md) URL request is made to get a static map, to get static map metadata or to get imagery metadata that contains a map tile URI, one (1) transaction is counted. <br /><br />Note: This transaction type has been superseded by the more specific RESTImagery-Metadata, RESTImagery-StaticMap and RESTImagery-StaticMapWithRoute transaction types.|
|RESTImagery-Metadata|REST Services|Yes<sup>3</sup>|Any time an [Imagery](../../rest-services/imagery/get-imagery-metadata.md) URL request is made to get imagery metadata that contains a map tile URI, one (1) transaction is counted.|
|RESTImagery-StaticMap|REST Services|Yes<sup>3</sup>|Any time an [Imagery](../../rest-services/imagery/get-a-static-map.md) URL request is made to get a static map, one (1) transaction is counted.|
|RESTImagery-StaticMapWithRoute|REST Services|Yes<sup>3</sup>|Any time an [Imagery](../../rest-services/imagery/get-a-static-map.md) URL request is made to get a static map, one (1) transaction is counted.|  
|RESTImagery-BasicMetadata|REST Services|No|Any time an [Imagery](../../rest-services/imagery/imagery-metadata.md) URL request is made to get basic imagery metadata that does not contain a map tile URI, one (1) transaction is counted.|  
|RESTLocalInsights| REST Services | Yes<sup>3</sup> | Any time a [Local Insights](../../rest-services/routes/local-insights.md) URL request is made, one (1) transaction is counted.|
|RESTLocalSearch| REST Services | Yes<sup>3</sup>| Any time a [Local Search](../../rest-services/locations/local-search.md) URL request is made, one (1) transaction is counted.|
|RESTLocationRecog|REST Services|Yes<sup>3</sup>| Any time a [Location Recognition](../../rest-services/locations/location-recognition.md) URL request is made to get location information about entities such as local businesses, natural points of interests, and a reverse geocoded address for a specified latitude and longitude coordinate, one (1) transaction is counted.|
|RESTLocations|REST Services|Yes<sup>3</sup>|Any time a [Locations](../../rest-services/locations/index.md) URL request is made to geocode or reverse-geocode location data, one (1) transaction is counted.<br /><br />Note: This transaction type has been superseded by the more specific RestLocations-Structured, RestLocations-Unstructured and RESTLocations-Reverse transaction types.|
|RestLocations-Structured|REST Services|Yes<sup>3</sup>|Any time a [Locations](../../rest-services/locations/find-a-location-by-address.md) URL request is made to geocode location data, one (1) transaction is counted.|
|RestLocations-Unstructured|REST Services|Yes<sup>3</sup>|Any time a [Locations](../../rest-services/locations/find-a-location-by-query.md) URL request is made to geocode location data, one (1) transaction is counted.|
|RESTLocations-Reverse|REST Services|Yes<sup>3</sup>|Any time a [Locations](../../rest-services/locations/find-a-location-by-point.md) URL request is made to reverse geocode location data, one (1) transaction is counted.|
|RESTRoutes|REST Services|Yes<sup>3</sup>|Any time a [Routes](../../rest-services/routes/index.md) URL request is made to find a route, one (1) transaction is counted.|
|RESTTimezone|REST Services|Yes<sup>3</sup>| Any time a [Time Zone](../../rest-services/timezone/index.md) URL request is made to retrieve a time zone for a location by point or query, convert a UTC datetime to a time zone, or retrieve information about IANA the Windows time zone standards, one (1) transaction is counted. |
|RESTTraffic|REST Services|Yes<sup>3</sup>|Any time a [Traffic](../../rest-services/traffic/index.md) URL request is made to get traffic incident information, one (1) transaction is counted.|
|Route-DistanceMatrix|REST Services|Yes|Any time a synchronous [Distance Matrix](../../rest-services/routes/calculate-a-distance-matrix.md) request is made, one (1) transaction is counted for every four (4) cells calculated in the matrix.|  
|Route-DistanceMatrixAsync|REST Services|Yes|Any time an asynchronous [Distance Matrix](../../rest-services/routes/calculate-a-distance-matrix.md) request is made, one (1) transaction is counted for every four (4) cells calculated in the matrix.|  
|Route-DistanceMatrixAsyncCallback|REST Services|No|Any time the status of an asynchronous [Distance Matrix](../../rest-services/routes/calculate-a-distance-matrix.md) request is checked.|  
|Route-Isochrone|REST Services|Yes<sup>3|Any time a synchronous [Isochrone](../../rest-services/routes/calculate-an-isochrone.md) request is made, one (1) transaction is counted.|  
|Route-IsochroneAsync|REST Services|Yes<sup>3|Any time an asynchronous [Isochrone](../../rest-services/routes/calculate-an-isochrone.md) request is made, one (1) transaction is counted.|  
|Route-IsochroneAsyncCallback|REST Services|No|Any time the status of an asynchronous [Isochrone](../../rest-services/routes/calculate-an-isochrone.md) request is checked.|
|Routes-OptimizeItinerary|REST Services|Yes|Any time a synchronous [Multi-Itinerary Optimization](../../rest-services/routes/optimized-itinerary.md) request is made, the number of transactions counted is based on the number of itineraryAgents multiplied by the number of itineraryItems in the request.|  
|Routes-OptimizeItineraryAsync|REST Services|Yes|Any time an asynchronous [Multi-Itinerary Optimization](../../rest-services/routes/optimized-itinerary.md) request is made, the number of transactions counted is based on the number of itineraryAgents multiplied by the number of itineraryItems in the request.|
|Routes-OptimizeItineraryAsyncCallback|REST Services|No|Any time the status of an asynchronous [Multi-Itinerary Optimization](../../rest-services/routes/optimized-itinerary.md) request is checked.|  
|Route-SnapToRoad|REST Services|Yes<sup>3|Any time a synchronous [Snap to Road](../../rest-services/routes/snap-points-to-roads.md) request is made, one (1) transaction is counted.|  
|Route-SnapToRoadAsync|REST Services|Yes<sup>3|Any time an asynchronous [Snap to Road](../../rest-services/routes/snap-points-to-roads.md) request is made, one (1) transaction is counted.|  
|Route-SnapToRoadAsyncCallback|REST Services|No|Any time the status of an asynchronous [Snap to Road](../../rest-services/routes/snap-points-to-roads.md) request is checked.|  
|Route-Truck|REST Services|Yes|Any time a synchronous [Truck Routing](../../rest-services/routes/calculate-a-truck-route.md) request is made, three (3) transactions are counted.|  
|Route-TruckAsync|REST Services|Yes|Any time an asynchronous [Truck Routing](../../rest-services/routes/calculate-a-truck-route.md) request is made, three (3) transactions are counted.|  
|Route-TruckAsyncCallback|REST Services|No|Any time the status of an asynchronous [Truck Routing](../../rest-services/routes/calculate-a-truck-route.md) request is checked.|
|GeospatialEndpoint|REST Services|No|Any time a [Geospatial Endpoint](../../articles/geospatial-endpoint-service.md) URL request is made, one (1) transaction is counted.|

 <sup>3</sup>This transaction is not billable if the service request is made using a [session ID](#using-session-ids-to-make-billable-transactions-non-billable) from a Web or WPF Control session or from the AutoSuggest Module of the Web Control.  

### Spatial Data Services and Data Source Management using the Bing Maps Account Center  
  
|Category|Bing Maps API|Billable|Category Description|  
|--------------|-------------------|--------------|--------------------------|  
|Dataflow:BatchGeocode|Spatial Data Services|Yes|Any time a request is made to [Create Job](../../spatial-data-services/geocode-dataflow-api/create-a-geocode-job-and-upload-data.md), a set of transactions equal to the number of total entities in the geocode request are counted.<br /><br /> Any time a data source is geocoded using the Bing Maps Dev Center, a set of transactions equal to the number of total entities in the geocode request are counted.<br /><br />Each row that is geocoded will generate one (1) transactions.|  
|Dataflow:Create|Spatial Data Services|No|Any time a URL request is made to create a dataflow job to batch geocode entity data by using the [Create Job](../../spatial-data-services/create-a-geocode-job-and-upload-data.md) API, one (1) transaction is counted.<br /><br /> Any time a URL request is made to stage, publish or rollback a data source by using the [Create a Load Data Source Job](../../spatial-data-services/data-source-management-api/load-data-source-dataflow/create-a-load-data-source-job-and-input-entity-data.md) API, one (1) transaction is counted.<br /><br /> Any time a data source is geocoded or published by using the Bing Maps Dev Center, one (1) transaction is counted.|  
|Dataflow:Get|Spatial Data Services|No|Any time a URL request is made to [Get Job Status](../../spatial-data-services/geocode-dataflow-api/get-status-of-a-geocode-job.md), one (1) transaction is counted.<br /><br /> Any time a URL request is made to [Get Load Data Source Status](../../spatial-data-services/data-source-management-api/load-data-source-dataflow/get-load-data-source-status.md), one (1) transaction is counted.<br /><br /> Any time a URL request is made to [Get Download Data Source Job Status](../../spatial-data-services/data-source-management-api/load-data-source-dataflow/get-load-data-source-status.md), one (1) transaction is counted.<br /><br /> Any time a data source is geocoded or published by using the Bing Maps Dev Center, one (1) transaction is counted.|  
|Dataflow:Download|Spatial Data Services|No|Any time a URL request is made to [Download Results](../../spatial-data-services/geocode-dataflow-api/download-geocode-job-results.md)], one (1) transaction is counted.<br /><br /> Any time the geocoded results of non-published data source entity data are downloaded using the Bing Maps Dev Center, one (1) transaction is counted.<br /><br /> Note that if you download successful and failed results, these are two separate **Dataflow:Download** transactions.|  
|RESTSpatialDataService:GetAllMetadata|Spatial Data Services|No|Any time a URL request is made to get [Get Data Source Information](../../spatial-data-services/data-source-management-api/get-data-source-information.md) that returns metadata for all data sources that are associated with a Bing Maps Account, one (1) transaction is counted.|  
|RESTSpatialDataService:GetDataSource|Spatial Data Services|No|Any time a URL request is made to [Get Data Source Information](../../spatial-data-services/data-source-management-api/get-data-source-information.md) that returns general information about one or more versions of a single data source, one (1) transaction is counted.|  
|RESTSpatialDataService:GetDataSourceMetadata|Spatial Data Services|No|Any time a URL request is made to [Get Data Source Information](../../spatial-data-services/data-source-management-api/get-data-source-information.md) that returns metadata for one or more versions of a single data source, one (1) transaction is counted.|  
|RESTSpatialDataService:<br /><br /> ListDataSources|Spatial Data Services|No|Any time a URL request is made to [Get Data Source Information](../../spatial-data-services/data-source-management-api/get-data-source-information.md) that returns general information about all data sources associated with a Bing Maps Account, one (1) transaction is counted.|  
|RESTSpatialDataService:DownloadDatasource|Spatial Data Services|No|Any time a URL request is made to [Create a Download Job](../../spatial-data-services/data-source-management-api/download-data-source-dataflow/create-a-download-job.md), one (1) transaction is counted.<br /><br /> Any time a URL request is made to [Get Downloaded Data](../../spatial-data-services/data-source-management-api/download-data-source-dataflow/get-downloaded-data.md), one (1) transaction is counted.<br /><br /> Any time a published, staged or previous version of a data source is downloaded using the Bing Maps Dev Center, one (1) transaction is counted.|  
|RESTSpatialDataService:DeleteDataSource|Spatial Data Services|No|Any time a URL request is made to [Delete a Data Source](../../spatial-data-services/data-source-management-api/delete-data-source.md), one (1) transaction is counted.<br /><br /> Any time a data source is deleted using the Bing Maps Dev Center, one (1) transaction is counted.|  
|RESTSpatialDataService:SetDataSourcePublicOrPrivate|Spatial Data Services|No|Any time a URL request is made to [Make a Data Source Public](../../spatial-data-services/data-source-management-api/make-public-data-source.md), one (1) transaction is counted.|  
|RESTSpatialDataService:Query|Spatial Data Services|Yes<sup>4</sup>|Any time a [Query API](../../spatial-data-services/query-api/index.md) URL request is made to query a data source, one (1) transaction is counted.<br /><br /> When a [Query by Area](../../spatial-data-services/query-api/query-by-area.md) URL request is made with an address string that must be geocoded, one RESTLocations transaction is also counted.|  
|RESTSpatialDataService:Geodata|Spatial Data Services|Yes|Any time a [Geodata API](../../spatial-data-services/geodata-api.md) URL request is made to get boundary data, one (1) transaction is counted.<br /><br /> When a [Geodata API](../../spatial-data-services/geodata-api.md) URL request is made with an address string that must be geocoded, one RESTLocations transaction is also counted.|  
|RESTSpatialDataService:QueryPointsOfInterest|Spatial Data Services|Yes<sup>4</sup>|Any time a [Query API](../../spatial-data-services/query-api/index.md) URL request is made to query the [PointsOfInterest](../../spatial-data-services/public-data-sources/pointsofinterest.md) data source, one (1) transaction is counted.<br /><br /> When a [Query by Area](../../spatial-data-services/query-api/query-by-area.md) URL request is made with an address string that must be geocoded, one RESTLocations transaction is also counted.| 

<sup>4</sup>This transaction is not billable if the service request is made using a [session ID](#using-session-ids-to-make-billable-transactions-non-billable) from an Web or WPF Control session.

### Discontinued Map Control APIs (AJAX V7, Silverlight, Windows Store)  
  
|Category|Bing Maps API|Billable|Category Description|  
|--------------|-------------------|--------------|--------------------------|  
|Web-Control (formerly AjaxSession)|AJAX Control (DISCONTINUED)|Yes|Any time a session that uses Bing Maps Version 6.x or Version 7.0, is started with a valid Bing Maps Key, one (1) transaction is counted. A session begins with the load of the Bing Maps AJAX Control into a user’s browser and ends when the browser is closed or the user moves to a different page.|  
|WinStoreAppSession_JavaScript_V1<br /><br /> <br /><br /> WinStoreAppSession_JavaScript (for Windows 8 Beta and Preview versions)|Windows Store apps (DISCONTINUED)|Yes|Any time a session that uses Bing Maps SDK for Windows Store apps using JavaScript  is started with a valid Bing Maps Key, one (1) transaction is counted. A session begins with the load of the Bing Maps for JavaScript control into a user’s browser and ends when the browser is closed or the user moves to a different page.|  
|WinStoreAppSession_CSharp_VB_CPP_V1<br /><br /> <br /><br /> WinStoreAppSession_CSharp_VB_CPP (Windows 8 Beta and Preview versions)|Windows Store apps (DISCONTINUED)|Yes|Any time an application session that uses Bing Maps SDK for Windows Store apps for C#, C++, or Visual Basic  is started with a valid Bing Maps Key, one (1) transaction is counted. An application session begins with the load of Bing Maps for Windows Store apps for C#, C++, or Visual Basic control in an application and ends when the application is closed.|  
|SilverlightSession<br /><br /> <br /><br /> SilverlightSessionBeta (for beta release of the control)|Silverlight Control (DISCONTINUED)|Yes - SilverlightSession<br /><br /> <br /><br /> No – SilverlightSessionBeta|Any time a session that uses the Bing Maps Silverlight Control is started with a valid Bing Maps Key, one (1) transaction is counted. A session begins with the load of the Bing Maps Silverlight Control into a user’s browser and ends when the browser is closed or the user moves to a different page.|  
|WindowsPhoneSession_PublicApp|Silverlight Control for Windows Phone (DISCONTINUED)|No|Any time a session begins with the launch of an application that uses the Bing Maps Silverlight Control for Windows Phone, one (1) transaction is counted. This includes all map control interactions and map tile downloads that occur within the application and that use the same [session ID](#using-session-ids-to-make-billable-transactions-non-billable) until the application is closed.|  
|iOSSession|iOS Control (DISCONTINUED)|Yes|Any time an application session is started and uses the Bing Maps iOS Control with a valid Bing Maps Key, one (1) transaction is counted. An application session begins with the load of the Bing Maps iOS Control by the application and includes all Bing Maps iOS Control interactions until the application is closed.| 
  
### SOAP Services (Discontinued)  
  
|Category|Bing Maps API|Billable|Category Description|  
|--------------|-------------------|--------------|--------------------------|  
|WS: Geocode|SOAP Services|Yes<sup>5</sup>|Any time a request is made using the GeocodeServiceClient.Geocode Method  method, one (1) transaction is counted.|  
|WS: ReverseGeocode|SOAP Services|Yes<sup>5</sup>|Any time a request is made using the GeocodeServiceClient.ReverseGeocode Method, one (1) transaction is counted.|  
|WS: Get ImageryMetadata|SOAP Services|No|Any time a request is made using the ImageryServiceClient.GetImageryMetadata Method, one (1) transaction is counted.|  
|WS: GetMapUri|SOAP Services|Yes<sup>5</sup>|Any time a request is made using the ImageryServiceClient.GetMapUri Method, one (1) transaction is counted.|  
|WS: CalculateRoute|SOAP Services|Yes<sup>5</sup>|Any time a request is made using the [RouteServiceClient.CalculateRoute Method](https://msdn.microsoft.com/library/cc981072.aspx) , one (1) transaction is counted.|  
|WS: CalculateRoutesFromMajorRoads|SOAP Services|Yes<sup>5</sup>|Any time a request is made using the RouteServiceClient.CalculateRoutesFromMajorRoads Method   and the   MajorRoutesOptions.ReturnRoutes Property  is set to **false**, one (1) transacation is counted.<br /><br /> Anytime a request is made using the RouteServiceClient.CalculateRoutesFromMajorRoads Method  and the   MajorRoutesOptions.ReturnRoutes Property  is set to **true**, one (1) transaction for the request and additional transactions for each returned route are counted.|  
|WS: Search|SOAP Services|Yes<sup>5</sup>|Any time a request is made using the SearchServiceClient.Search Method, one (1) transaction is counted.|  
|WS: PhotoSynthView|SOAP Services|Yes<sup>5</sup>|Any time a Synth associated with a Windows Live ID that corresponds to an enterprise Photosynth account is viewed, one (1) transaction is counted. Every Synth is associated with a Windows Live ID.|  
  
 <sup>5</sup>This transaction is not billable if the service request is made using a [session ID](#using-session-ids-to-make-billable-transactions-non-billable) from an AJAX Control, Silverlight Control, WPF Control, Windows Store app for JavaScript, or Windows Store app for C#, C++, or Visual Basic session.
