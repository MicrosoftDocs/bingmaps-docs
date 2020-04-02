---
title: "Query Near a Route | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: f3bd4e1f-906f-48ed-bf94-da41af613708
caps.latest.revision: 15
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Query Near a Route
Use the following URL to search a data source for entities that are within one (1) mile or 1.6 kilometers of a route. You can use the [Query Options](../query-api/query-options.md) such as $filter and $select to further specify the entity information that would like to return. For example, you can search the [Traffic Incident Data Source](../public-data-sources/traffic-incident-data-source.md) for all traffic incidents along a route and request that only the severity, description and location (latitude and longitude) be returned.  
  
For an example on how to get traffic incidents along a route on a map, see [Searching for Traffic Incidents Along a Route](https://docs.microsoft.com/en-us/bingmaps/v8-web-control/map-control-concepts/spatial-data-services-module-examples/query-api/along-a-route-search).  
  
## Supported HTTP Methods  
 GET, HEAD  
  
## URL template  
  
> [!NOTE]
>  This template supports both HTTP and HTTPS protocols. URLs in the response use HTTPS protocol.  
>   
>  A query response can contain a maximum number of 500 results.  
  
 **Get entities that are within one (1) mile or 1.6 kilometers of a route.**  
  
 Use the query options to specify the properties that you want to return and to provide other options such as the number of results to return.  
  
```url
http://spatial.virtualearth.net/REST/v1/data/accessId/dataSourceName/entityTypeName?spatialFilter=nearRoute(startRoute,endRoute)&avoid=avoid&optimize=optimize&distanceBeforeFirstTurn=distanceBeforeFirstTurn&heading=heading&travelMode=travelMode&queryoption1&queryoption2&queryoptionN&jsonp=jsonCallBackFunction&jsonso=jsonState&isStaging=isStaging&key=queryKey  
```  
  
### Template Parameters  
  
> [!NOTE]
>  Parameter names and values are not case-sensitive except for the queryKey parameter value.  
  
 **Query Parameters**  
  
|Parameter|Description|Values|  
|---------------|-----------------|------------|  
|accessId|**Required**. A unique ID for the data source.|A string containing an ID that is part of the URL structure that identifies the data source.<br /><br /> **Example**: 20181f26d9e94c81acdf9496133d4f23|  
|dataSourceName|**Required**. The name of the data source that you want to search.|A string that identifies the data source.<br /><br /> **Example**: FourthCoffeeSample|  
|entityTypeName|**Required** The entity type to search for.|The entity type of the data source.<br /><br /> **Example**: FourthCoffeeShops|  
|spatialFilter|**Required**. The start and end points of the route. You can specify the start and end points of the route in two ways.<br /><br /> -   A latitude and longitude.<br />-   An address.|To define a route and distance, use the following syntax:<br /><br /> spatialFilter=nearRoute(*latitude,longitude or address of route start*, *latitude,longitude or address of route end*)<br /><br /> **Example**: spatialFilter=nearRoute('47.62341,-122.33441', '47.63143,-122.57243')<br /><br /> **Note:**  NAVTEQNA, NAVTEQEU and PointsOfInterest data sources do not support the intersects and nearRoute filters.|  
|queryOption|**Optional**. Specifies query options, such as format and properties to display in the response. For more information about query options, see [Query Options](../query-api/query-options.md).|A set of query options. Each query option is specified as a single URL parameter. Query option examples include the ability to filter on property values ($filter), specify the format of response ($format) and order by a property value ($orderby). See [Query Options](../query-api/query-options.md) for a complete list.<br /><br /> The following example shows how to set both the $format and the $orderby query options in the URL.<br /><br /> `&$format=json&$orderby=ZipCode`<br /><br /> If you want to return the distance from the point to each entity returned in the response, you can add a custom value `__Distance` to the list of $select values as shown in the following example.<br /><br /> **Example**: $select=AddressLine,City,PostalCode,__Distance<br /><br /> When you specify `__Distance` as a $select value, the response returns a custom property element of type Edm:Double that is also named `__Distance`.<br /><br /> You can specify up to three (3) properties for the $orderby option. You cannot use the latitude or longitude properties to sort results.|  
|jsonp|**Optional.** Name of JSON callback function that is called when the response to the request is received. The JSON object provided in the response is passed to the callback function.|A string that contains the name of the callback function.<br /><br /> **Example**: jsonp=MyCallbackFunction.|  
|jsonso|**Optional.** The state object to pass to the JSON callback function. You can use a state object to match a response with a specific call. This value is provided as the second parameter to the callback function provided in the JSONP parameter.|Any valid JavaScript string.<br /><br /> **Example**: jsonso=abc3144sd|  
|isStaging|**Optional.** Specifies to query the staged version of the data source instead of the published version.|A Boolean value.<br /><br /> -   0 or false**[default]**<br />-   1 or true<br /><br /> **Example**: isStaging=1|  
|queryKey|**Required**. The Bing Maps Key to use to access the data source.|The Bing Maps Keys that you can use for a data source are specified when the data source is created. For example, there may be a single query key you must use to query the data source or you may be able to use any Bing Maps Key. For more information about specifying query keys when a data source is created, see [Create a Load Data Source Job](../data-source-management-api/load-data-source-dataflow/create-a-load-data-source-job-and-input-entity-data.md).<br /><br /> **Example**: key=abc123def456ghi789abc123def456ghi789|  
  
 **Route Parameters**  
  
|Parameter|Alias|Description|Values|  
|---------------|-----------|-----------------|------------|  
|avoid||**Optional.** Specifies the road types to minimize or avoid when the route is created for the driving travel mode.|A comma-separated list of values that limit the use of highways and toll roads in the route. In the definitions below, “highway” also refers to a “limited-access highway”.<br /><br /> If no values are specified, highways and tolls are allowed in the route.<br /><br /> -   highways: Avoids the use of highways  in the route.<br />-   tolls: Avoids the use of toll roads in the route.<br />-   minimizeHighways: Minimizes (tries to avoid) the use of highways in the route.<br />-   minimizeTolls: Minimizes (tries to avoid) the use of toll roads in the route. **Note:**  If you specify more than one option for a road type, then the most restrictive option is used. For example, if you set the avoid parameter to both highways and minimizeHighways, the highways option is used and all highways are avoided. <br /><br /> **Examples**:<br /><br /> avoid=highways<br /><br /> avoid=highways,tolls|  
|distanceBeforeFirstTurn|dbft|**Optional.** Specifies the distance before the first turn is allowed in the route. This option only applies to the driving travel mode.|An integer distance specified in meters. Use this parameter to make sure that the moving vehicle has enough distance to make the first turn.<br /><br /> **Examples**:<br /><br /> distanceBeforeFirstTurn=500<br /><br /> dbft=500|  
|heading|hd|**Optional.** Specifies the initial heading for the route.|An integer value between 0 and 359 that represents degrees from north where north is 0 degrees and the heading is specified clockwise from north. For example, setting the heading of 270 degrees creates a route that initially heads west.<br /><br /> **Example**:<br /><br /> heading=90|  
|optimize|optmz|**Optional.** Specifies what parameters to use to optimize the route on the map.|One of the following values:<br /><br /> -   distance: The route is calculated to minimize the distance. Traffic information is not used.<br />-   time **[default]**: The route is calculated to minimize the time. Traffic information is not used.<br />-   timeWithTraffic: The route is calculated to minimize the time and uses current traffic information.<br /><br /> **Example**: optimize=time|  
|travelMode||**Optional.** The mode of travel for the route.|One of the following values:<br /><br /> -   Driving **[default]**<br />-   Walking|  
  
## Response

The response to this URL contains the results of the query.  
  
 Results are returned in ascending order. If the $orderby query option is not specified as part of the request, the results are sorted as follows:  
  
1.  The results are sorted based on the distance from the start of the route.  
  
2.  The results are sorted by the distance from the closest route point.  
  
3.  The results are sorted based on entity ID.  
  
 This URL supports the following response formats.  
  
-   Atom (application/atom + xml) [**default**]  
  
-   JSON (application/json)  
  
 When the output format is set to Atom, the response contains a collection of Atom entries that are part of an Atom feed. For more information about these Atom response formats, see [OData AtomPub Format](https://www.odata.org/developers/protocols/atom-format) and the Atom examples in the **Examples** section.  
  
 When the output format is JSON, the response format for both types of requests is a collection of JSON Entries in a “results” container. For more information about the JSON response format, see [OData: JavaScript Object Notation (JSON) Format](https://www.odata.org/developers/protocols/json-format) and the JSON examples in the **Examples** section.  
  
## Examples

**EXAMPLE: Query a data source for entities near a route.**  
  
 The following example queries for coffee shops along a route between Webster, Texas and Kemah, Texas. Coffee shops within one (1) mile of the route are returned in the response. Because [FourthCoffeeSample Data Source](../public-data-sources/fourthcoffeesample.md) is a public data source, you can use any Bing Maps Key for the query key.  
  
 **URLs with ATOM Response**  
  
 Specifying address values  
  
```url
http://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops?spatialFilter=nearRoute('Webster,TX','Kemah,TX')&$select=EntityID,Latitude,Longitude,DisplayName,Phone&$top=3&key=queryKey  
```  
  
 Specifying latitude and longitude values  
  
```url
http://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops?spatialFilter=nearRoute('29.5386,-95.1194','29.5431,-95.01831')&$select=EntityID,Latitude,Longitude,DisplayName,Phone&$top=3&key=queryKey  
```  
  
```xml
<?xml version="1.0" encoding="utf-8"?>  
<feed xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata" xmlns="http://www.w3.org/2005/Atom">  
  <title type="text"></title>  
  <id>uuid:65a15ae6-c650-492a-9079-d942b919aa47;id=583534</id>  
  <rights type="text">© 2012 Microsoft and its suppliers.  This API and any results cannot be used or accessed without Microsoft's express written permission.</rights>  
  <updated>2012-01-24T23:36:03Z</updated>  
  <entry>  
    <id>https://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops('-946')</id>  
    <title type="text"></title>  
    <updated>2012-01-24T23:36:03Z</updated>  
    <content type="application/xml">  
      <m:properties>  
        <d:EntityID>-946</d:EntityID>  
        <d:Latitude m:type="Edm.Double">29.533064</d:Latitude>  
        <d:Longitude m:type="Edm.Double">-95.124686</d:Longitude>  
        <d:DisplayName>Fourth Coffee Store #946, Webster, TX, United States</d:DisplayName>  
        <d:Phone>            1-800-XXX-XXXX      </d:Phone>  
      </m:properties>  
    </content>  
  </entry>  
  <entry>  
    <id>https://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops('-951')</id>  
    <title type="text"></title>  
    <updated>2012-01-24T23:36:03Z</updated>  
    <content type="application/xml">  
      <m:properties>  
        <d:EntityID>-951</d:EntityID>  
        <d:Latitude m:type="Edm.Double">29.541998</d:Latitude>  
        <d:Longitude m:type="Edm.Double">-95.016876</d:Longitude>  
        <d:DisplayName>Fourth Coffee Store #951, Kemah, TX, United States</d:DisplayName>  
        <d:Phone>            1-800-XXX-XXXX      </d:Phone>  
      </m:properties>  
    </content>  
  </entry>  
  <entry>  
    <id>https://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops('-960')</id>  
    <title type="text"></title>  
    <updated>2012-01-24T23:36:03Z</updated>  
    <content type="application/xml">  
      <m:properties>  
        <d:EntityID>-960</d:EntityID>  
        <d:Latitude m:type="Edm.Double">29.566524</d:Latitude>  
        <d:Longitude m:type="Edm.Double">-95.060661</d:Longitude>  
        <d:DisplayName>Fourth Coffee Store #960, Seabrook, TX, United States</d:DisplayName>  
        <d:Phone>            1-800-XXX-XXXX      </d:Phone>  
      </m:properties>  
    </content>  
  </entry>  
</feed>  
  
```  
  
 **URLs with JSON Response**  
  
 Specifying address values  
  
```url
http://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops?spatialFilter=nearRoute('Webster,TX','Kemah,TX')&$select=EntityID,Latitude,Longitude,DisplayName,Phone&$top=3&$format=json&key=queryKey  
```  
  
 Specifying latitude and longitude values  
  
```url
http://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops?spatialFilter=nearRoute('29.5386,-95.1194','29.5431,-95.01831')&$select=EntityID,Latitude,Longitude,DisplayName,Phone&$format=json&$top=3&key=queryKey  
```  
  
```json
{  
   "d":{  
      "__copyright":"\u00a9 2012 Microsoft and its suppliers.  This API and any results cannot be used or accessed without Microsoft's express written permission.",  
      "results":[  
         {  
            "__metadata":{  
               "uri":"https:\/\/spatial.virtualearth.net\/REST\/v1\/data\/20181f26d9e94c81acdf9496133d4f23\/FourthCoffeeSample\/FourthCoffeeShops('-946')"  
            },  
            "EntityID":"-946",  
            "Latitude":29.533064,  
            "Longitude":-95.124686,  
            "DisplayName":"Fourth Coffee Store #946, Webster, TX, United States",  
            "Phone":"            1-800-XXX-XXXX      "  
         },  
         {  
            "__metadata":{  
               "uri":"https:\/\/spatial.virtualearth.net\/REST\/v1\/data\/20181f26d9e94c81acdf9496133d4f23\/FourthCoffeeSample\/FourthCoffeeShops('-951')"  
            },  
            "EntityID":"-951",  
            "Latitude":29.541998,  
            "Longitude":-95.016876,  
            "DisplayName":"Fourth Coffee Store #951, Kemah, TX, United States",  
            "Phone":"            1-800-XXX-XXXX      "  
         },  
         {  
            "__metadata":{  
               "uri":"https:\/\/spatial.virtualearth.net\/REST\/v1\/data\/20181f26d9e94c81acdf9496133d4f23\/FourthCoffeeSample\/FourthCoffeeShops('-960')"  
            },  
            "EntityID":"-960",  
            "Latitude":29.566524,  
            "Longitude":-95.060661,  
            "DisplayName":"Fourth Coffee Store #960, Seabrook, TX, United States",  
            "Phone":"            1-800-XXX-XXXX      "  
         }  
      ]  
   }  
}  
```  
  
 **EXAMPLE: Query a data source for entities near a route.**  
  
 The following example adds additional route parameters to the previous example that can affect the route.  
  
```url
http://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops?&spatialFilter=nearRoute('Webster,TX','Kemah,TX')&$select=EntityID,Latitude,Longitude&avoid=tolls&optimize=time&travelMode=driving&output=xml&key=queryKey  
```  
  
## HTTP Status Codes  
  
> [!NOTE]
>  For more details about these HTTP status codes, see [Status Codes and Error Handling](../status-codes-and-error-handling.md).  
  
 When the request is successful, the following HTTP status code is returned.  
  
-   200  
  
 When the request is not successful, the response returns one of the following errors.  
  
-   400  
  
-   401  
  
-   500  
  
-   503  
  
## See Also  
 [Query by Area](../query-api/query-by-area.md)   
 [Query by ID](../query-api/query-by-id.md)   
 [Query by Property](../query-api/query-by-property.md)
