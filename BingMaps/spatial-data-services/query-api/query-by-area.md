---
title: "Query by Area | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 92dcfac8-a089-4bc4-921a-65c740956511
caps.latest.revision: 54
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Query by Area

Use the following URLs to search a data source for entity types that are within a specified area. You can use the [Query Options](../query-api/query-options.md) such and $filter and $select to further specify the entity information that would like to return. For example, you can search for all restaurants within 10 kilometers that serve Italian food and request that only the restaurant name and location information is returned.  
  
## Supported HTTP Methods  
 GET, HEAD  
  
## URL template  
  
> [!NOTE]
>  This template supports both HTTP and HTTPS protocols. URLs in the response use HTTPS protocol.  
>   
>  A query response can contain a maximum number of 200 results.  
  
 **Get information about entities by searching an area defined by a point or address and a distance.**  
  
 The distance specifies the maximum distance from the specified point to search. The maximum distance is 1000 kilometers.  
  
 You must specify the distance in kilometers between 0.16 and 1000 kilometers. The distance unit of miles is not supported.  
  
 You can return the distance from the point to each entity found in the search area by specifying `__Distance` as one of the $select query option values. For more information see the queryOption parameter description in the table below.  
  
 To search entities along a route, see [Query Near a Route](../query-api/query-near-route.md).  
  
 To search for entities by area and by property value, see [Query by Property](../query-api/query-by-property.md).  
  
 **Search using latitude, longitude and distance.**  
  
```url
http://spatial.virtualearth.net/REST/v1/data/accessId/dataSourceName/entityTypeName?spatialFilter=nearby(latitude,longitude,distance)&queryoption1&queryoption2&queryoptionN&jsonp=jsonCallBackFunction&jsonso=jsonState&isStaging=isStaging&key=queryKey  
```  
  
 **Search using an address string and distance.**  
  
```url
http://spatial.virtualearth.net/REST/v1/data/accessId/dataSourceName/entityTypeName?spatialFilter=nearby(addressString,distance)&queryoption1&queryoption2&queryoptionN&jsonp=jsonCallBackFunction&jsonso=jsonState&isStaging=isStaging&key=queryKey  
```  
  
 **Get information about nearby entities by searching an area defined by a bounding box.**  
  
 A bounding box defines an area using latitude and longitude pairs.  
  
```url
http://spatial.virtualearth.net/REST/v1/data/accessId/dataSourceName/entityTypeName?spatialFilter=bbox(southLatitude,westLongitude,northLatitude,eastLongitude)&queryOption1&queryOption2&queryOptionN&jsonp=jsonCallBackFunction&jsonso=jsonState&isStaging=isStaging&key=queryKey  
```  
  
 **Get information about nearby entities by searching an area defined by a geography type, such as a polygon or line string.**  
  
 Available geography objects are defined in [Geography Types](../data-source-management-api/load-data-source-dataflow/geography-types.md).  
  
```url
http://spatial.virtualearth.net/REST/v1/data/accessId/dataSourceName/entityTypeName?spatialFilter=intersects(geography)& queryOption1&queryOption2&queryOptionN&jsonp=jsonCallBackFunction&jsonso=jsonState&isStaging=isStaging&key=queryKey  
```  
  
### Template Parameters  
  
> [!NOTE]
>  Parameter names and values are not case-sensitive except for the queryKey parameter value.  
  
|Parameter|Description|Values|  
|---------------|-----------------|------------|  
|accessId|**Required**. A unique ID for the data source.|A string containing an ID that is part of the URL structure that identifies the data source.<br /><br /> **Example**: 20181f26d9e94c81acdf9496133d4f23|  
|dataSourceName|**Required** The name of the data source that you want to search.|A string that identifies the data source.<br /><br /> **Example**: FourthCoffeeSample|  
|entityTypeName|**Required** The entity type to search for.|The entity type of the data source.<br /><br /> **Example**: FourthCoffeeShops|  
|spatialFilter|**Required** The area you want to search. You can specify this area in three ways:<br /><br /> -   A latitude and longitude representing a point and a distance in kilometers from that point to search.<br />-   An address and distance in kilometers from the address to search.<br />-   A set of latitude and longitude pairs that create an area called a bounding box.<br />-   A geographical area defined by one of the geography types described in [Geography Types](../data-source-management-api/load-data-source-dataflow/geography-types.md).|**To define an area using a point and distance in kilometers**, use the following syntax:<br /><br /> spatialFilter=nearby(*latitude,longitude,distance or address,distance*)<br /><br /> where *latitude* and *longitude* and , *address* represents a location and the *distance* represents the maximum distance to search from that location. You must specify the distance in kilometers. The distance unit of miles is not supported.<br /><br /> **Examples**:<br /><br /> spatialFilter=nearby(47.6,-122.3,50.0)<br /><br /> spatialFilter=nearby('1 Microsoft Way,Redmond,WA 98052',50.0)<br /><br /> **To define an area using a bounding box**, use the following syntax:<br /><br /> spatialFilter=bbox(*South Latitude*, *West Longitude*, *North Latitude*, *East Longitude*)<br /><br /> where the latitude and longitude values define an area on the earth.<br /><br /> **Example**: spatialFilter=bbox(47.5,-122.4,47.7,-122.2)<br /><br /> To define an area using a geography description, use the following syntax:<br /><br /> spatialFilter=intersects('geography description')<br /><br /> The geography description can have a maximum of 200 points that must be within an area described by 10 degrees of latitude and 10 degrees of longitude.<br /><br /> **Example**: spatialFilter=intersects('POLYGON ((-112 42,-112 41,-123 41,-123 42,-112 42))')<br /><br /> **Note:**  The PointsOfInterest data source does not support the intersects and nearRoute filters.|  
|queryOption|**Optional**. Specifies query options, such as format and properties to display in the response. For more information about query options, see [Query Options](../query-api/query-options.md).|A set of query options. Each query option is specified as a single URL parameter. Query option examples include the ability to filter on property values ($filter), specify the format of response ($format) and order by a property value ($orderby). See [Query Options](../query-api/query-options.md) for a complete list.<br /><br /> The following example shows how to set both the $format and the $orderby query options in the URL.<br /><br /> `&$format=json&$orderby=ZipCode`<br /><br /> If you are using a spatial filters and you want to return the distance from the point to each entity (point and distance query) returned in the response or the distance from the center of a bounding box (bounding box query), you can add a custom value `__Distance` to the list of $select values as shown in the following examples.<br /><br /> **Examples**:<br /><br /> $select=AddressLine,City,PostalCode,__Distance<br /><br /> $select=*,\__Distance<br /><br /> When you specify `__Distance` as a $select value, the response returns a custom property element of type Edm:Double that is also named `__Distance`.<br /><br /> You can specify up to three (3) properties for the $orderby option. You cannot use the latitude or longitude properties to sort results. You can use __Distance as a $orderby value for bounding box searches only.<br /><br /> If the $orderby option is not specified as part of the request, the results are sorted as follows:<br /><br /> -   For searches using a point and distance: The results will be sorted by the distance of the entity from the specified point. If two results are at the same distance, they are sorted by the property that represents the entity ID. Results are returned in ascending order.<br />-   For searches using a bounding box or geography description: The results will be sorted by the property that represents the entity ID in ascending order.<br />-   If you want to return the intersection of each entity geography value with a specified geography, use the ‘intersection’ function.<br />     Example: $select=intersection('POLYGON ((-112 42,-112 41,-123 41,-123 42,-112 42))')<br /><br /> You cannot use the latitude or longitude properties to filter results by using the $filter query option.|  
|jsonp|**Optional.** Name of JSON callback function that is called when the response to the request is received. The JSON object provided in the response is passed to the callback function.|A string that contains the name of the callback function.<br /><br /> **Example**: jsonp=MyCallbackFunction|  
|jsonso|**Optional.** The state object to pass to the JSON callback function. You can use a state object to match a response with a specific call. This value is provided as the second parameter to the callback function provided in the JSONP parameter.|Any valid JavaScript string.<br /><br /> **Example**: jsonso=abc3144sd|  
|isStaging|**Optional.** Specifies to query the staged version of the data source instead of the published version.|A Boolean value.<br /><br /> -   0 or false**[default]**<br />-   1 or true<br /><br /> **Example**: isStaging=0|  
|queryKey|**Required**. The Bing Maps Key to use to access the data source.|The Bing Maps Keys that you can use for a data source are specified when the data source is created. For example, there may be a single query key you must use to query the data source or you may be able to use any Bing Maps Key. For more information about specifying query keys when a data source is created, see [Create a Load Data Source Job](../data-source-management-api/load-data-source-dataflow/create-a-load-data-source-job-and-input-entity-data.md).<br /><br /> **Example**: key=abc123def456ghi789abc123def456ghi789|  
  
## Response  

The response to this URL contains the results of the query.  
  
 If the $orderby query option is not specified as part of the request, the results are sorted as follows:  
  
-   For searches using a point and distance: The results will be sorted by the distance of the entity from the specified point. If two results are at the same distance, they are sorted by the property that is used as the entity ID. Results are returned in ascending order.  
  
-   For searches using a bounding box: The results will be sorted by the property that represents the entity ID in ascending order.  
  
 This URL supports the following response formats.  
  
-   Atom (application/atom + xml) [**default**]  
  
-   JSON (application/json)  
  
 When the output format is set to Atom, the response contains a collection of Atom entries that are part of an Atom feed. For more information about these Atom response formats, see [OData AtomPub Format](https://www.odata.org/developers/protocols/atom-format) and the Atom examples in the **Examples** section.  
  
 When the output format is JSON, the response format for both types of requests is a collection of JSON Entries in a “results” container. For more information about the JSON response format, see [OData: JavaScript Object Notation (JSON) Format](https://www.odata.org/developers/protocols/json-format) and the JSON examples in the **Examples** section.  
  
## Examples  

**EXAMPLE: Query a data source by specifying a bounding box.**  
  
 This example queries for coffee shops within an area defined by a bounding box (a pair of latitudes and longitudes).The $select and $top query options request the entity ID, latitude and longitude for the first three (3) entities that meet the search criteria.  
  
 **URL with Atom Response**  
  
```url
http://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops?spatialFilter=bbox(40.7801465817126,-74.46958923339845,40.88535150706938,-74.163070678710937)&$select=EntityID,Latitude,Longitude&$top=3&key=queryKey  
```  
  
```xml
<feed xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata" xmlns="http://www.w3.org/2005/Atom">  
  <title type="text" />  
  <id>uuid:d359c52a-63a7-469d-bad9-7b54baada637;id=45</id>  
  <rights type="text">© 2011 Microsoft and its suppliers. This API and any results cannot be used or accessed without Microsoft’s express written permission.</rights>  
  <updated>2011-01-11T01:55:58Z</updated>  
  <entry>  
    <id>https://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops('-7884')</id>  
    <title type="text" />  
    <updated>2011-01-11T01:55:58Z</updated>  
    <content type="application/xml">  
      <m:properties>  
        <d:EntityID>-7884</d:EntityID>  
        <d:Latitude m:type="Edm.Double">40.780329</d:Latitude>  
        <d:Longitude m:type="Edm.Double">-74.237863</d:Longitude>  
      </m:properties>  
    </content>  
  </entry>  
  <entry>  
    <id>https://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops('-7891')</id>  
    <title type="text" />  
    <updated>2011-01-11T01:55:58Z</updated>  
    <content type="application/xml">  
      <m:properties>  
        <d:EntityID>-7891</d:EntityID>  
        <d:Latitude m:type="Edm.Double">40.781604</d:Latitude>  
        <d:Longitude m:type="Edm.Double">-74.181775</d:Longitude>  
      </m:properties>  
    </content>  
  </entry>  
  <entry>  
    <id>https://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops('-7920')</id>  
    <title type="text" />  
    <updated>2011-01-11T01:55:58Z</updated>  
    <content type="application/xml">  
      <m:properties>  
        <d:EntityID>-7920</d:EntityID>  
        <d:Latitude m:type="Edm.Double">40.787240</d:Latitude>  
        <d:Longitude m:type="Edm.Double">-74.391041</d:Longitude>  
      </m:properties>  
    </content>  
  </entry>  
</feed>  
  
```  
  
 **URL with JSON Response**  
  
```url
http://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops?spatialFilter=bbox(40.7801465817126,-74.46958923339845,40.88535150706938,-74.163070678710937)&$select=EntityID,Latitude,Longitude&$top=3&$format=json&key=queryKey  
```  
  
```json
{  
   "d":{  
      "__copyright":"\u00a9 2011 Microsoft and its suppliers.  This API and any results cannot be used or accessed without Microsoft’s express written permission.",  
      "results":[  
         {  
            "__metadata":{  
               "uri":"https://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops('-7884')"  
            },  
            "EntityID":"-7884",  
            "Latitude":40.780329,  
            "Longitude":-74.237863  
         },  
         {  
            "__metadata":{  
               "uri":"https://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops('-7891')"  
            },  
            "EntityID":"-7891",  
            "Latitude":40.781604,  
            "Longitude":-74.181775  
         },  
         {  
            "__metadata":{  
               "uri":"https://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops('-7920')"  
            },  
            "EntityID":"-7920",  
            "Latitude":40.787240,  
            "Longitude":-74.391041  
         }  
      ]  
   }  
}  
```  
  
 **EXAMPLE: Query a data source by specifying a point and distance to search from that point.**  
  
 This example queries for coffee shops within an area defined by a point (latitude and longitude) and a distance from that point. The query returns the entity ID and the latitude and longitude of the first three (3) entities that meet the search criteria.  
  
 **URL with Atom Response**  
  
```url
http://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops?spatialFilter=nearby(40.83274904439099,-74.3163299560546935,5)&$select=EntityID,Latitude,Longitude,__Distance&$top=3&key=queryKey  
```  
  
```xml
<feed xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata" xmlns="http://www.w3.org/2005/Atom">  
  <title type="text" />  
  <id>uuid:d359c52a-63a7-469d-bad9-7b54baada637;id=46</id>  
  <rights type="text">© 2011 Microsoft and its suppliers. This API and any results cannot be used or accessed without Microsoft’s express written permission.</rights>  
  <updated>2011-01-11T02:03:34Z</updated>  
  <entry>  
    <id>https://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops('-8051')</id>  
    <title type="text" />  
    <updated>2011-01-11T02:03:34Z</updated>  
    <content type="application/xml">  
      <m:properties>  
        <d:EntityID>-8051</d:EntityID>  
        <d:Latitude m:type="Edm.Double">40.820685</d:Latitude>  
        <d:Longitude m:type="Edm.Double">-74.295683</d:Longitude>  
        <d:__Distance m:type="Edm.Double">2.19734068236095</d:__Distance>  
      </m:properties>  
    </content>  
  </entry>  
  <entry>  
    <id>https://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops('-8174')</id>  
    <title type="text" />  
    <updated>2011-01-11T02:03:34Z</updated>  
    <content type="application/xml">  
      <m:properties>  
        <d:EntityID>-8174</d:EntityID>  
        <d:Latitude m:type="Edm.Double">40.849513</d:Latitude>  
        <d:Longitude m:type="Edm.Double">-74.292831</d:Longitude>  
        <d:__Distance m:type="Edm.Double">2.72010344668636</d:__Distance>  
      </m:properties>  
    </content>  
  </entry>  
  <entry>  
    <id>https://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops('-8181')</id>  
    <title type="text" />  
    <updated>2011-01-11T02:03:34Z</updated>  
    <content type="application/xml">  
      <m:properties>  
        <d:EntityID>-8181</d:EntityID>  
        <d:Latitude m:type="Edm.Double">40.851404</d:Latitude>  
        <d:Longitude m:type="Edm.Double">-74.293720</d:Longitude>  
        <d:__Distance m:type="Edm.Double">2.81746736218219</d:__Distance>  
      </m:properties>  
    </content>  
  </entry>  
</feed>  
```  
  
 **URL with JSON Response**  
  
```url
http://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops?spatialFilter=nearby(40.83274904439099,-74.3163299560546935,5)&$filter&$select=EntityID,Latitude,Longitude,__Distance&$top=3&$format=json&key=queryKey  
```  
  
```json
{  
   "d":{  
      "__copyright":"\u00a9 2011 Microsoft and its suppliers.  This API and any results cannot be used or accessed without Microsoft’s express written permission.",  
      "results":[  
         {  
            "__metadata":{  
               "uri":"https://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops('-8051')"  
            },  
            "EntityID":"-8051",  
            "Latitude":40.820685,  
            "Longitude":-74.295683,  
            "__Distance":2.19740735412509  
         },  
         {  
            "__metadata":{  
               "uri":"https://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops('-8174')"  
            },  
            "EntityID":"-8174",  
            "Latitude":40.849513,  
            "Longitude":-74.292831.  
            "__Distance":2.72010344668636  
         },  
         {  
            "__metadata":{  
               "uri":"https://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops('-8181')"  
            },  
            "EntityID":"-8181",  
            "Latitude":40.851404,  
            "Longitude":-74.293720,  
            "__Distance":2.81746736218219  
         }  
      ]  
   }  
}  
```  
  
 **EXAMPLE: Query a data source by specifying a point and distance to search and limit the results returned based on additional property values.**  
  
 This example queries for coffee shops within a given distance and uses the $filter property to further limit the results to coffee shops with wifi. The query returns the entity ID and the latitude and longitude of the first three (3) entities that meet the search criteria.  
  
 **URL with ATOM Response**  
  
```url
http://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops?spatialFilter=nearby(40.83274904439099,-74.3163299560546935,5)&$filter=IsWifiHotSpot%20eq%201&$select=DisplayName,Latitude,Longitude&$top=3&key=queryKey  
```  
  
```xml
<feed xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata" xmlns="http://www.w3.org/2005/Atom">  
  <title type="text" />  
  <id>uuid:9d7fa138-2948-4928-8e41-62a6c2daad08;id=1503</id>  
  <rights type="text">© 2011 Microsoft and its suppliers. This API and any results cannot be used or accessed without Microsoft’s express written permission.</rights>  
  <updated>2011-02-03T01:36:41Z</updated>  
  <entry>  
    <id>https://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops('-8080')</id>  
    <title type="text" />  
    <updated>2011-02-03T01:36:41Z</updated>  
    <content type="application/xml">  
      <m:properties>  
        <d:DisplayName>Fourth Coffee Store #8080, East Hanover, NJ, United States</d:DisplayName>  
        <d:Latitude m:type="Edm.Double">40.827191</d:Latitude>  
        <d:Longitude m:type="Edm.Double">-74.358151</d:Longitude>  
      </m:properties>  
    </content>  
  </entry>  
  <entry>  
    <id>https://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops('-8089')</id>  
    <title type="text" />  
    <updated>2011-02-03T01:36:41Z</updated>  
    <content type="application/xml">  
      <m:properties>  
        <d:DisplayName>Fourth Coffee Store #8077, East Hanover, NJ, United States</d:DisplayName>  
        <d:Latitude m:type="Edm.Double">40.826413</d:Latitude>  
        <d:Longitude m:type="Edm.Double">-74.360059</d:Longitude>  
      </m:properties>  
    </content>  
  </entry>  
  <entry>  
    <id>https://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops('-8089')</id>  
    <title type="text" />  
    <updated>2011-02-03T01:36:41Z</updated>  
    <content type="application/xml">  
      <m:properties>  
        <d:DisplayName>Fourth Coffee Store #8089, East Hanover, NJ, United States</d:DisplayName>  
        <d:Latitude m:type="Edm.Double" 40.828150</d:Latitude>  
        <d:Longitude m:type="Edm.Double>-74.364028</d:Longitude>  
      </m:properties>  
    </content>  
  </entry>  
</feed>  
  
```  
  
 **URL with JSON Response**  
  
```url
http://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops?spatialFilter=nearby(40.83274904439099,-74.3163299560546935,5)&$filter=IsWifiHotSpot%20eq%201&$select=DisplayName,Latitude,Longitude&$top=3&format=json&key=queryKey  
```  
  
```json
{  
   "d":{  
      "__copyright":"\u00a9 2011 Microsoft and its suppliers.  This API and any results cannot be used or accessed without Microsoft’s express written permission.",  
      "results":[  
         {  
            "__metadata":{  
               "uri":"https:\/\/spatial.virtualearth.net\/REST\/v1\/data\/20181f26d9e94c81acdf9496133d4f23\/FourthCoffeeSample\/FourthCoffeeShops('-8080')"  
            },  
            "DisplayName":"Fourth Coffee Store #8080, East Hanover, NJ, United States",  
            "Latitude":40.827191,  
            "Longitude:-74.358151         },  
         {  
            "__metadata":{  
               "uri":"https:\/\/spatial.virtualearth.net\/REST\/v1\/data\/20181f26d9e94c81acdf9496133d4f23\/FourthCoffeeSample\/FourthCoffeeShops('-8077')"  
            },  
            "DisplayName":"Fourth Coffee Store #8077, East Hanover, NJ, United States",  
            "Latitude":40.826413,  
            "Longitude":-74.360059  
         },  
         {  
            "__metadata":{  
               "uri":"https:\/\/spatial.virtualearth.net\/REST\/v1\/data\/20181f26d9e94c81acdf9496133d4f23\/FourthCoffeeSample\/FourthCoffeeShops('-8089')"  
            },  
            "DisplayName":"Fourth Coffee Store #8089, East Hanover, NJ, United States",  
            "Latitude":40.828150,  
            "Longitude":-74.364028  
         }  
      ]  
   }  
}  
```  
  
 **EXAMPLE: Query a data source by specifying a point and distance to search and return all entity properties and distance to each entity.**  
  
 This example queries for coffee shops within a given distance of a point with wifi. The query returns the complete set of entity properties and the distance for all the entities that meet the search criteria.  
  
```url
http://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops?spatialFilter=nearby('1 Microsoft Way Redmond WA 98052',5)&$filter=IsWifiHotSpot%20eq%201&$select=*,__Distance&key=queryKey  
```  
  
 **EXAMPLE: Query a data source for all entities that intersect with the specified POLYGON geography description and return the Entity ID and the intersection geography**  
  
 **URL with ATOM Response**  
  
```url
http://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c239ddf9496133d4f23/SampleDataSource/SampleEntityType?SpatialFilter=intersects('POLYGON((-112 42,-112 41,-123 41,-123 42,-112 42))'&$select=intersection('POLYGON((-112 42,-112 41,-123 41,-123 42,-112 42))'),EntityID&$top=2&key=queryKey  
```  
  
```xml
<?xml version="1.0" encoding="utf-8"?>  
<feed xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata" xmlns="http://www.w3.org/2005/Atom">  
  <title type="text"></title>  
  <id>uuid:a3900084-6586-4c9e-a0c0-a57f32279ea6;id=1499</id>  
  <rights type="text">© 2013 Microsoft and its suppliers.  This API and any results cannot be used or accessed without Microsoft's express written permission.</rights>  
  <updated>2013-09-13T23:04:24Z</updated>  
  <entry>  
    <id>https://spatial.virtualearth.net/REST/v1/data/8188bb678a2e4605b56f9b3a6fc8eaf0/NavteqGeom/NavteqGeomTest('1001199368')</id>  
    <title type="text"></title>  
    <updated>2013-09-13T23:04:24Z</updated>  
    <content type="application/xml">  
      <m:properties>  
        <d:__IntersectedGeom m:type="Edm.Geography">LINESTRING (-117.01828 41.00016, -117.01828 41.00000)</d:__IntersectedGeom>  
        <d:EntityID>1001199368</d:EntityID>  
      </m:properties>  
    </content>  
  </entry>  
  <entry>  
    <id>https://spatial.virtualearth.net/REST/v1/data/8188bb678a2e4605b56f9b3a6fc8eaf0/NavteqGeom/NavteqGeomTest('1001503020')</id>  
    <title type="text"></title>  
    <updated>2013-09-13T23:04:24Z</updated>  
    <content type="application/xml">  
      <m:properties>  
        <d:__IntersectedGeom m:type="Edm.Geography">POLYGON ((-120.87118 41.68966, -120.87053 41.7041, -120.89012 41.70441, -120.89027 41.68988, -120.87118 41.68966))</d:__IntersectedGeom>  
        <d:EntityID>1001503020</d:EntityID>  
      </m:properties>  
    </content>  
  </entry>  
</feed>  
```  
  
 **URL with JSON Response**  
  
```url
http://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c239ddf9496133d4f23/SampleDataSource/SampleEntityType?SpatialFilter=intersects('POLYGON((-112 42,-112 41,-123 41,-123 42,-112 42))'&$select=intersection('POLYGON((-112 42,-112 41,-123 41,-123 42,-112 42))'),EntityID&$top=2&$format=json&key=queryKey  
```  
  
```json
{  
   "d":{  
      "__copyright":"\u00a9 2013 Microsoft and its suppliers.  This API and any results cannot be used or accessed without Microsoft's express written permission.",  
      "results":[  
         {  
            "__metadata":{  
               "uri":"https:\/\/data.blmp2-test-br1.live-int.com\/REST\/v1\/data\/8188bb678a2e4605b56f9b3a6fc8eaf0\/NavteqGeom\/NavteqGeomTest('1001199368')"  
            },  
            "__IntersectedGeom":"LINESTRING (-117.01828 41.00016, -117.01828011091472 41.000000000000007)",  
            "EntityID":"1001199368"  
         },  
         {  
            "__metadata":{  
               "uri":"https:\/\/spatial.virtualearth.net\/REST\/v1\/data\/8188bb678a2e4605b56f9b3a6fc8eaf0\/NavteqGeom\/NavteqGeomTest('1001503020')"  
            },  
            "__IntersectedGeom":"POLYGON ((-120.87118 41.68966, -120.87053 41.7041, -120.89012 41.70441, -120.89027 41.68988, -120.87118 41.68966))",  
            "EntityID":"1001503020"  
         }  
      ]  
   }  
}  
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
 [Query by ID](../query-api/query-by-id.md)   
 [Query by Property](../query-api/query-by-property.md)
