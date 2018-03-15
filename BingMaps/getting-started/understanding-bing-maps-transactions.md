---
title: "Understanding Bing Maps Transactions | Microsoft Docs"
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
When you use any [Bing Maps API](http://msdn.microsoft.com/en-us/library/dd877180.aspx) with a Bing Maps Key (you must have a [Bing Maps Account](http://www.bing.com/dev/maps)), transactions are recorded. Transactions track API usage and can be billable or non-billable. For example, using the [Bing Maps V8 Web Control](../v8-web-control/index.md) to show a map on a web page or geocoding an address using the [Bing Maps REST Services](http://msdn.microsoft.com/en-us/library/ff701713.aspx) are both billable transactions, while deleting a data source (a spatial database that you create using the [Bing Spatial Data Services](../spatial-data-services/index.md)) is not.  
  
 You can find descriptions of the transactions for each Bing Maps API in the tables below, and you can view transaction totals over time on the [Bing Maps Account Center](https://www.bingmapsportal.com). For more information, see [Viewing Usage Reports](../getting-started/understanding-bing-maps-transactions.md#viewusage). Note that it may take up to 24 hours for new transactions to appear.  
  
<a name="viewusage"></a>   
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

 A QPS (queries per second) report can be viewe by clicking on the **Traffic** tab.
  
## Billable versus non-billable transactions  
 Only billable transactions count towards the free-use limits for Basic keys, and Enterprise keys are only charged for billable transactions.  Non-billable transactions do not incur charges and do not count towards free-use limits. To determine if your application will qualify for free use and for more about licensing and transaction limits, [contact the licensing team](https://www.microsoft.com/maps/) or read the [Bing Maps Terms of Use](http://www.microsoft.com/maps/product/terms.html).  
  
<a name="sessionkey"></a>   
### Using Session IDs to make billable transactions non-billable  
 In the following description, Bing Maps services refer to Bing Maps REST Services and Bing Spatial Data Services<sup>1</sup>. Bing Maps controls refer to Bing Maps V8 Web Control, Bing Maps WPF Control, and Windows 10 UWP Map control.  
  
 Bing Maps service requests originating from a Bing Maps control that use a session ID instead of the Bing Maps key are non-billable up to 50 requests per session. The 51st transaction and every transaction thereafter will be billable. For example, if you make a Bing Maps REST Services request to geocode an address from the Bing Maps V8 web control and use the [Map.getCredentials](../v8-web-control/map-class.md) method to get the session ID for authentication, the resulting transaction is recorded as non-billable even though it is listed as a billable transaction in the table below.  
  
 You must use the Bing Maps Key that you used to load the map control to request a session ID. This session ID is only valid for the map control session. For the Bing Maps V8 web control, a session begins with the load of the map into a user’s browser and ends when the browser is closed or the user moves to a different page. Similarly for the WPF control, a session begins when the map control is loaded by the application and ends when the application is closed. Note that the Windows 10 UWP Map control does not provide access to session keys but instead provides native geocoding and routing functionalities which automatically make use of sessions. For more information about how to get a session ID from the Bing Maps Key, see [Using the REST Services with .NET](../rest-services/using-the-rest-services-with-net.md) and [Map Class](../v8-web-control/map-class.md). Note that if you make service requests with a Bing Maps Key instead of a session ID within the session, you will be charged for all billable requests.  
  
> [!NOTE]
>  <sup>1</sup> Bing Spatial Data Services transactions have two exceptions to free-use within sessions:  
>   
>  -   All Bing Spatial Data Services transactions become billable when you reach ten (10) million transactions within a year, even when you use a session ID.  
> -   Bing Spatial Data Services batch geocode transactions (Dataflow:BatchGeocode) become billable when you reach one (1) million batch geocode transactions within a year, even when you use a session ID.  
  
## Bing Maps Transactions by API  
 The following tables define transactions for all the APIs.  
  
### Map Control APIs (Web V8, WPF)  
  
|Category|Bing Maps API|Billable|Category Description|  
|--------------|-------------------|--------------|--------------------------|  
|AjaxSession-V8|Web Control|Yes|Any time a session that uses the Bing Maps Version 8.0 web control, is started with a valid Bing Maps Key, one (1) transaction is counted. A session begins with the load of the Bing Maps Web Control into a user’s browser and ends when the browser is closed or the user moves to a different page.<br /><br /> Anytime the Autosuggest Module is used without a map and a user selects a location suggestion from the menu one (1) transaction is counted.  When using the AutoSuggest Module, transactions are not logged for user key strokes or based on the number of location results that are returned in the Autosuggest menu.<br /><br /> All REST or Spatial Data<sup>2</sup> service requests that use a [session ID](../getting-started/understanding-bing-maps-transactions.md#sessionkey) are **not** billable when they are made from within a session.|  
|Win10-Native|Windows 10 UWP Map control|Yes|Any time an application session that the Windows 10 UWP Map control is started with a valid Bing Maps Key, one (1) transaction is counted. An application session begins with the load of the Windows 10 UWP Map control in an application and ends when the application is closed.|  
|WPFSession|WPF Control|Yes|Any time an application session is started and uses the Bing Maps WPF Control with a valid Bing Maps Key, one (1) transaction is counted. An application session begins with the load of the Bing Maps WPF Control by the application and ends when the application is closed.<br /><br /> All SOAP, REST or Spatial Data<sup>2</sup> service requests that use a [session ID](../getting-started/understanding-bing-maps-transactions.md#sessionkey) are **not** billable when they are made from within a session.|  
  
 <sup>2</sup>All Spatial Data Services requests over one (1) million per year are billable even when a session ID is used.  
  
### REST Services  
  
|Category|Bing Maps API|Billable|Category Description|  
|--------------|-------------------|--------------|--------------------------|  
|RESTLocations|REST Services|Yes<sup>3</sup>|Any time a [Locations](../rest-services/locations-api.md) URL request is made to geocode or reverse-geocode location data, one (1) transaction is counted.<br /><br /> Anytime the Autosuggest Module of the Bing Maps Version 8.0 web control is used and a user selects a location suggestion from the Autosuggest menu, one (1) transaction is logged.<br /><br /> Anytime a [Query API](../spatial-data-services/query-api.md) URL request is made with an address string that must be geocoded, one (1) transaction is counted.|  
|RESTElevations|REST Services|Yes<sup>3</sup>|Any time an [Elevations](../rest-services/elevations-api.md) URL request is made to get elevation data, one (1) transaction is counted.|  
|RESTImagery|REST Services|Yes<sup>3</sup>|Any time an [Imagery](../rest-services/imagery-api.md) URL request is made to get a static map, to get static map metadata or to get imagery metadata that contains a map tile URI, one (1) transaction is counted.|  
|RESTImagery-BasicMetadata|REST Services|No|Any time an [Imagery](../rest-services/imagery-api.md) URL request is made to get basic imagery metadata that does not contain a map tile URI, one (1) transaction is counted.|  
|RESTRoutes|REST Services|Yes<sup>3</sup>|Any time a [Routes](../rest-services/routes-api.md) URL request is made to find a route, one (1) transaction is counted.|  
|Route-DistanceMatrix|REST Services|Yes|Any time a synchronous [Distance Matrix](../rest-services/calculate-a-distance-matrix.md) request is made, one (1) transaction is counted for every two (2) cells calculated in the matrix.|  
|Route-DistanceMatrixAsync|REST Services|Yes|Any time an asynchronous [Distance Matrix](../rest-services/calculate-a-distance-matrix.md) request is made, one (1) transaction is counted for every two (2) cells calculated in the matrix.|  
|Route-DistanceMatrixAsyncCallback|REST Services|No|Any time the status of an asynchronous [Distance Matrix](../rest-services/calculate-a-distance-matrix.md) request is checked.|  
|Route-Isochrone|REST Services|Yes|Any time a synchronous [Isochrone](../rest-services/calculate-an-isochrone.md) request is made, one (1) transaction is counted.|  
|Route-IsochroneAsync|REST Services|Yes|Any time an asynchronous [Isochrone](../rest-services/calculate-an-isochrone.md) request is made, one (1) transaction is counted.|  
|Route-IsochroneAsyncCallback|REST Services|No|Any time the status of an asynchronous [Isochrone](../rest-services/calculate-an-isochrone.md) request is checked.|  
|Route-SnapToRoad|REST Services|Yes|Any time a synchronous [Snap to Road](../rest-services/snap-points-to-roads.md) request is made, one (1) transaction is counted.|  
|Route-SnapToRoadAsync|REST Services|Yes|Any time an asynchronous [Snap to Road](../rest-services/snap-points-to-roads.md) request is made, one (1) transaction is counted.|  
|Route-SnapToRoadAsyncCallback|REST Services|No|Any time the status of an asynchronous [Snap to Road](../rest-services/snap-points-to-roads.md) request is checked.|  
|Route-Truck|REST Services|Yes|Any time a synchronous [Truck Routing](../rest-services/calculate-a-truck-route.md) request is made, three (3) transactions are counted.|  
|Route-TruckAsync|REST Services|Yes|Any time an asynchronous [Truck Routing](../rest-services/calculate-a-truck-route.md) request is made, three (3) transactions are counted.|  
|Route-TruckAsyncCallback|REST Services|No|Any time the status of an asynchronous [Truck Routing](../rest-services/calculate-a-truck-route.md) request is checked.|  
|RESTTraffic|REST Services|Yes<sup>3</sup>|Any time a [Traffic](../rest-services/traffic-api.md) URL request is made to get traffic incident information, one (1) transaction is counted.|  
  
 <sup>3</sup>This transaction is not billable if the service request is made using a [session ID](../getting-started/understanding-bing-maps-transactions.md#sessionkey) from a Web or WPF Control session or from the AutoSuggest Module of the Web Control.  
  
### Spatial Data Services and Data Source Management using the Bing Maps Account Center  
  
|Category|Bing Maps API|Billable|Category Description|  
|--------------|-------------------|--------------|--------------------------|  
|Dataflow:BatchGeocode|Spatial Data Services|No<sup>4,6</sup>|Any time a request is made to [Create Job](../spatial-data-services/create-a-geocode-job-and-upload-data.md), a set of transactions equal to the number of total entities in the geocode request are counted.<br /><br /> Any time a data source is geocoded using the Bing Maps Dev Center, a set of transactions equal to the number of total entities in the geocode request are counted.|  
|Dataflow:Create|Spatial Data Services|No<sup>6</sup>|Any time a URL request is made to create a dataflow job to batch geocode entity data by using the [Create Job](../spatial-data-services/create-a-geocode-job-and-upload-data.md) API, one (1) transaction is counted.<br /><br /> Any time a URL request is made to stage, publish or rollback a data source by using the [Create a Load Data Source Job](../spatial-data-services/create-a-load-data-source-job-and-input-entity-data.md) API, one (1) transaction is counted.<br /><br /> Any time a data source is geocoded or published by using the Bing Maps Dev Center, one (1) transaction is counted.|  
|Dataflow:Get|Spatial Data Services|No<sup>6</sup>|Any time a URL request is made to [Get Job Status](../spatial-data-services/get-status-of-a-geocode-job.md), one (1) transaction is counted.<br /><br /> Any time a URL request is made to [Get Load Data Source Status](../spatial-data-services/get-load-data-source-status.md), one (1) transaction is counted.<br /><br /> Any time a URL request is made to [Get Download Data Source Job Status](../spatial-data-services/get-download-data-source-job-status.md), one (1) transaction is counted.<br /><br /> Any time a data source is geocoded or published by using the Bing Maps Dev Center, one (1) transaction is counted.|  
|Dataflow:Download|Spatial Data Services|No<sup>6</sup>|Any time a URL request is made to [Download Results](../spatial-data-services/download-geocode-job-results.md), one (1) transaction is counted.<br /><br /> Any time the geocoded results of non-published data source entity data are downloaded using the Bing Maps Dev Center, one (1) transaction is counted.<br /><br /> Note that if you download successful and failed results, these are two separate **Dataflow:Download** transactions.|  
|RESTSpatialDataService:GetAllMetadata|Spatial Data Services|No<sup>6</sup>|Any time a URL request is made to [Get Data Source Information](../spatial-data-services/get-data-source-information.md) that returns metadata for all data sources that are associated with a Bing Maps Account, one (1) transaction is counted.|  
|RESTSpatialDataService:GetDataSource|Spatial Data Services|No<sup>6</sup>|Any time a URL request is made to [Get Data Source Information](../spatial-data-services/get-data-source-information.md) that returns general information about one or more versions of a single data source, one (1) transaction is counted.|  
|RESTSpatialDataService:GetDataSourceMetadata|Spatial Data Services|No<sup>6</sup>|Any time a URL request is made to [Get Data Source Information](../spatial-data-services/get-data-source-information.md) that returns metadata for one or more versions of a single data source, one (1) transaction is counted.|  
|RESTSpatialDataService:<br /><br /> ListDataSources|Spatial Data Services|No<sup>6</sup>|Any time a URL request is made to [Get Data Source Information](../spatial-data-services/get-data-source-information.md) that returns general information about all data sources associated with a Bing Maps Account, one (1) transaction is counted.|  
|RESTSpatialDataService:DownloadDatasource|Spatial Data Services|No<sup>6</sup>|Any time a URL request is made to [Create a Download Job](../spatial-data-services/create-a-download-job.md), one (1) transaction is counted.<br /><br /> Any time a URL request is made to [Get Downloaded Data](../spatial-data-services/get-downloaded-data.md), one (1) transaction is counted.<br /><br /> Any time a published, staged or previous version of a data source is downloaded using the Bing Maps Dev Center, one (1) transaction is counted.|  
|RESTSpatialDataService:DeleteDataSource|Spatial Data Services|No<sup>6</sup>|Any time a URL request is made to [Delete a Data Source](../spatial-data-services/delete-a-data-source.md), one (1) transaction is counted.<br /><br /> Any time a data source is deleted using the Bing Maps Dev Center, one (1) transaction is counted.|  
|RESTSpatialDataService:SetDataSourcePublicOrPrivate|Spatial Data Services|No<sup>6</sup>|Any time a URL request is made to [Make a Data Source Public](../spatial-data-services/make-a-data-source-public.md), one (1) transaction is counted.|  
|RESTSpatialDataService:Query|Spatial Data Services|Yes<sup>5,6</sup>|Any time a [Query API](../spatial-data-services/query-api.md) URL request is made to query a data source, one (1) transaction is counted.<br /><br /> When a [Query by Area](../spatial-data-services/query-by-area.md) URL request is made with an address string that must be geocoded, one RESTLocations transaction is also counted.|  
|RESTSpatialDataService:Geodata|Spatial Data Services|No<sup>6</sup>|Any time a [Geodata API](../spatial-data-services/geodata-api.md) URL request is made to get boundary data, one (1) transaction is counted.<br /><br /> When a [Geodata API](../spatial-data-services/geodata-api.md) URL request is made with an address string that must be geocoded, one RESTLocations transaction is also counted.|  
  
 <sup>4</sup>Spatial Data Services batch geocode transactions are free up to one (1) million transactions per year for a Bing Maps account. After you reach one (1) million transactions in a year, these transactions become billable.  
  
 <sup>5</sup>This transaction is not billable if the service request is made using a [session ID](../getting-started/understanding-bing-maps-transactions.md#sessionkey) from an Web or WPF Control session, and the total number of Spatial Data Services transactions is less that ten (10) million per year for a Bing Maps account.  
  
 <sup>6</sup>Spatial Data Services requests become billable when you reach ten (10) million transactions within a year for a Bing Maps account even when a session ID is used.  
  
### Discontinued Map Control APIs (AJAX V7, Silverlight, Windows Store)  
  
|Category|Bing Maps API|Billable|Category Description|  
|--------------|-------------------|--------------|--------------------------|  
|AjaxSession|AJAX Control (DISCONTINUED)|Yes|Any time a session that uses Bing Maps Version 6.x or Version 7.0, is started with a valid Bing Maps Key, one (1) transaction is counted. A session begins with the load of the Bing Maps AJAX Control into a user’s browser and ends when the browser is closed or the user moves to a different page.|  
|WinStoreAppSession_JavaScript_V1<br /><br /> <br /><br /> WinStoreAppSession_JavaScript (for Windows 8 Beta and Preview versions)|Windows Store apps (DISCONTINUED)|Yes|Any time a session that uses Bing Maps SDK for Windows Store apps using JavaScript  is started with a valid Bing Maps Key, one (1) transaction is counted. A session begins with the load of the Bing Maps for JavaScript control into a user’s browser and ends when the browser is closed or the user moves to a different page.|  
|WinStoreAppSession_CSharp_VB_CPP_V1<br /><br /> <br /><br /> WinStoreAppSession_CSharp_VB_CPP (Windows 8 Beta and Preview versions)|Windows Store apps (DISCONTINUED)|Yes|Any time an application session that uses Bing Maps SDK for Windows Store apps for C#, C++, or Visual Basic  is started with a valid Bing Maps Key, one (1) transaction is counted. An application session begins with the load of Bing Maps for Windows Store apps for C#, C++, or Visual Basic control in an application and ends when the application is closed.|  
|SilverlightSession<br /><br /> <br /><br /> SilverlightSessionBeta (for beta release of the control)|Silverlight Control (DISCONTINUED)|Yes - SilverlightSession<br /><br /> <br /><br /> No – SilverlightSessionBeta|Any time a session that uses the Bing Maps Silverlight Control is started with a valid Bing Maps Key, one (1) transaction is counted. A session begins with the load of the Bing Maps Silverlight Control into a user’s browser and ends when the browser is closed or the user moves to a different page.|  
|WindowsPhoneSession_PublicApp|Silverlight Control for Windows Phone (DISCONTINUED)|No|Any time a session begins with the launch of an application that uses the Bing Maps Silverlight Control for Windows Phone, one (1) transaction is counted. This includes all map control interactions and map tile downloads that occur within the application and that use the same [session ID](../getting-started/understanding-bing-maps-transactions.md#sessionkey) until the application is closed.|  
|iOSSession|iOS Control (DISCONTINUED)|Yes|Any time an application session is started and uses the Bing Maps iOS Control with a valid Bing Maps Key, one (1) transaction is counted. An application session begins with the load of the Bing Maps iOS Control by the application and includes all Bing Maps iOS Control interactions until the application is closed.|  
  
### SOAP Services (Discontinued)  
  
|Category|Bing Maps API|Billable|Category Description|  
|--------------|-------------------|--------------|--------------------------|  
|WS: Geocode|SOAP Services|Yes<sup>7</sup>|Any time a request is made using the GeocodeServiceClient.Geocode Method  method, one (1) transaction is counted.|  
|WS: ReverseGeocode|SOAP Services|Yes<sup>7</sup>|Any time a request is made using the GeocodeServiceClient.ReverseGeocode Method, one (1) transaction is counted.|  
|WS: Get ImageryMetadata|SOAP Services|No|Any time a request is made using the ImageryServiceClient.GetImageryMetadata Method, one (1) transaction is counted.|  
|WS: GetMapUri|SOAP Services|Yes<sup>7</sup>|Any time a request is made using the ImageryServiceClient.GetMapUri Method, one (1) transaction is counted.|  
|WS: CalculateRoute|SOAP Services|Yes<sup>7</sup>|Any time a request is made using the RouteServiceClient.CalculateRoute Method  HYPERLINK "http://msdn.microsoft.com/en-us/library/cc981072.aspx" , one (1) transaction is counted.|  
|WS: CalculateRoutesFromMajorRoads|SOAP Services|Yes<sup>7</sup>|Any time a request is made using the RouteServiceClient.CalculateRoutesFromMajorRoads Method   and the   MajorRoutesOptions.ReturnRoutes Property  is set to **false**, one (1) transacation is counted.<br /><br /> Anytime a request is made using the RouteServiceClient.CalculateRoutesFromMajorRoads Method  and the   MajorRoutesOptions.ReturnRoutes Property  is set to **true**, one (1) transaction for the request and additional transactions for each returned route are counted.|  
|WS: Search|SOAP Services|Yes<sup>7</sup>|Any time a request is made using the SearchServiceClient.Search Method, one (1) transaction is counted.|  
|WS: PhotoSynthView|SOAP Services|Yes<sup>7</sup>|Any time a Synth associated with a Windows Live ID that corresponds to an enterprise Photosynth account is viewed, one (1) transaction is counted. Every Synth is associated with a Windows Live ID.|  
  
 <sup>7</sup>This transaction is not billable if the service request is made using a [session ID](../getting-started/understanding-bing-maps-transactions.md#sessionkey) from an AJAX Control, Silverlight Control, WPF Control, Windows Store app for JavaScript, or Windows Store app for C#, C++, or Visual Basic session.