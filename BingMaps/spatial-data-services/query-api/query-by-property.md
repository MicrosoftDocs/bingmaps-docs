---
title: "Query by Property | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 1cf2d2a8-2c2d-47f9-81cd-b89adbe221bc
caps.latest.revision: 42
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Query by Property
Use the following URL to search a data source for one or more entities by specifying property values.  
  
## Supported HTTP Methods  
 GET, HEAD  
  
## URL template  
 This template supports both HTTP and HTTPS protocols. URLs in the response use HTTPS protocol.  
  
 A query response can contain a maximum number of 250 results.  
  
 **Query for one or more entities by specifying property values and a distance to search.**  
  
```  
http://spatial.virtualearth.net/REST/v1/data/accessId/dataSourceName  
/entityTypeName?spatialFilter=nearby(latitude,longitude,distance)&$filter=filterString&queryOption1&queryOption2&queryOptionN&jsonp=jsonCallBackFunction&jsonso=jsonState&isStaging=isStaging&key=queryKey  
```  
  
 **Query for one or more entities by specifying property values and a bounding box to search.**  
  
```  
http://spatial.virtualearth.net/REST/v1/data/accessId/dataSourceName  
/entityTypeName?bbox(southLatitude,westLongitude,northLatitude,eastLongitude)&$filter=filterString&queryOption1&queryOption2&queryOptionN&jsonp=jsonCallBackFunction&jsonso=jsonState&isStaging=isStaging&key=queryKey  
```  
  
 **Query for one or more entities by specifying property values and searching an area defined by a geography type, such as a polygon or line string.**  
  
 Available geography objects are defined in [Geography Types](../data-source-management-api/load-data-source-dataflow/geography-types.md).  
  
```  
http://spatial.virtualearth.net/REST/v1/data/accessId/dataSourceName/entityTypeName?spatialFilter=intersects(geography)&$filter=filterString&queryOption1&queryOption2&queryOptionN&jsonp=jsonCallBackFunction&jsonso=jsonState&isStaging=isStaging&key=queryKey  
```  
  
### Template Parameters  
  
> [!NOTE]
>  Parameter names and values are not case-sensitive except for the queryKey parameter value.  
  
|Parameter|Description|Values|  
|---------------|-----------------|------------|  
|accessId|**Required**. A unique ID for the data source.|A string containing and ID that is part of the URL structure that identifies the data source.<br /><br /> **Example**: 20181f26d9e94c81acdf9496133d4f23|  
|dataSourceName|**Required** The name of the data source that you want to search.|A string containing the data source name.<br /><br /> **Example**: FourthCoffeeSample|  
|entityTypeName|**Required** The entity type to search for.|The entity type of the data source.<br /><br /> **Example**: FourthCoffeeStores|  
|spatialFilter|**Required** The area you want to search. You can specify this area in three ways:<br /><br /> -   A latitude and longitude representing a point and a distance in kilometers to search from that point.<br />-   A set of latitude and longitude pairs that create an area called a bounding box.<br />-   A geographical area defined by one of the geography types described in<br />     [Geography Types](../data-source-management-api/load-data-source-dataflow/geography-types.md).|To define an area using a point and distance in kilometers, use the following syntax:<br /><br /> spatialFilter=nearby(*latitude*, *longitude*, *distance*)<br /><br /> where *latitude* and *longitude* represent a point on the Earth and the *distance* represents the maximum distance to search from that route. The distance must be between 0.15 and 400 kilometers. The distance unit of miles is not supported.<br /><br /> **Example**: spatialFilter=nearby(47.6,-122.3,50.0)<br /><br /> To define an area using a bounding box, use the following syntax:<br /><br /> spatialFilter=bbox(*South Latitude*, *West Longitude*, *North Latitude*, *East Longitude*)<br /><br /> where the latitude and longitude values define an area on the earth.<br /><br /> **Example**: spatialFilter=bbox(47.5,-122.4,47.7,-122.2)<br /><br /> To define an area using a geography description, use the following syntax:<br /><br /> spatialFilter=intersects('geography description')<br /><br /> The geography description can have a maximum of 200 points that must be within and area described by 10 degrees of latitude and 10 degrees of longitude.<br /><br /> **Example**: spatialFilter=intersects('POLYGON ((-112 42,-112 41,-123 41,-123 42,-112 42))')|  
|filterString|**Required**. The search condition based on property values.|A conditional expression that uses property values. An entity is returned when the expression is true for that entity’s values. This parameter is an [OData query option](http://www.odata.org/developers/protocols/uri-conventions#FilterSystemQueryOption). Currently, the Query API only supports logical operators.<br /><br /> **Example**: $filter=CountryRegion Eq 'Washington' and Employees Ge 10|  
|queryOptions|**Optional**. Options for this query. For more information about query options, see [Query Options](../query-api/query-options.md).|A set of query values. Each query value is specified as an individual URL parameter. The following example shows how to set both the $format and the $orderby query options in the URL.<br /><br /> `&$format=json&$orderby=ZipCode`<br /><br /> **Example**: $select=HoursOfOperation,IsWiFiHotSpot<br /><br /> If the $orderby option is not specified as part of the request, the results will be sorted by the property that represents the entity ID in ascending order. You can specify up to three (3) properties for the $orderby option. You cannot use the latitude or longitude properties to sort results.<br /><br /> You cannot use the latitude or longitude properties to filter results by using the $filter query option.|  
|jsonp|**Optional.** Name of JSON callback function that is called when the response to the request is received. The JSON object provided in the response is passed to the callback function.|A string that contains the name of the callback function.<br /><br /> **Example**: jsonp=MyCallbackFunction|  
|isStaging|**Optional.** Specifies to query the staged version of the data source instead of the published version.|A Boolean value.<br /><br /> -   0 or false**[default]**<br />-   1 or true<br /><br /> **Example**: isStaging=1|  
|jsonso|**Optional.** The state object to pass to the JSON callback function. You can use a state object to match a response with a specific call. This value is provided as the second parameter to the callback function provided in the JSONP parameter.|Any valid JavaScript string.<br /><br /> **Example**: jsonso=abc3144sd|  
|queryKey|**Required**. The Bing Maps Key to use to access the data source.|The Bing Maps Keys that you can use for a data source are specified when the data source is created. For example, there may be a single query key you must use to query the data source or you may be able to use any Bing Maps Key. For more information about specifying query keys when a data source is created, see [Create a Load Data Source Job](../data-source-management-api/load-data-source-dataflow/create-a-load-data-source-job-and-input-entity-data.md).<br /><br /> **Example**: key=abc123def456ghi789abc123def456ghi789|  
  
## Response  
 This URL supports the following response formats.  
  
 If the $orderby query option is not specified when you query for multiple entity IDs, the results will be sorted by the property that is used for the entity ID. Results are returned in ascending order.  
  
-   Atom (application/atom + xml) [default]  
  
-   JSON (application/json)  
  
 When the output format is set to Atom, the response contains a collection of Atom Entries is returned as part of an Atom feed. For more information about these Atom response formats, see [OData AtomPub Format](http://www.odata.org/developers/protocols/atom-format) and the Atom examples in the **Examples** section.  
  
 When the output format is JSON, the response format for both types of requests is a collection of JSON Entries in a “results” container. For more information about the JSON response format, see [OData: JavaScript Object Notation (JSON) Format](http://www.odata.org/developers/protocols/json-format) and the JSON examples in the **Examples** section.  
  
## Examples  
 **EXAMPLE: Get entities that meet specified filter conditions and order the results.**  
  
 This example queries for coffee shops in the city of Clearwater and returns information about whether they are WiFi hotspots. The entries are sorted in descending order so that shops that are WiFi hotspots are listed first.  
  
 **URL with Atom response**  
  
```  
 HYPERLINK "http://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23  
/FourthCoffeeSample/FourthCoffeeShops?spatialFilter=nearby(27.894007,-82.670776,2)&$filter=StoreType%20Eq" http://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23  
/FourthCoffeeSample/FourthCoffeeShops?spatialFilter=nearby(27.894007,-82.670776,2)&$filter=StoreType%20Eq%20'Coffee Shop'&$select=IsWiFiHotSpot&$orderby=IsWiFiHotSpot&key=queryKey  
```  
  
```  
<feed xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata" xmlns="http://www.w3.org/2005/Atom">  
  <title type="text" />  
  <id>uuid:876b2e49-e480-40b8-8282-9929ced06f7f;id=46</id>  
  <rights type="text">© 2011 Microsoft and its suppliers. This API and any results cannot be used or accessed without Microsoft’s express written permission.</rights>   
  <updated>2010-11-09T22:53:36Z</updated>  
  <entry>  
    <id>https://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops('-715')</id>  
    <title type="text" />  
    <updated>2010-11-09T22:53:36Z</updated>  
    <content type="application/xml">  
      <m:properties>  
        <d:IsWiFiHotSpot m:type="Edm.Boolean">1</d:IsWiFiHotSpot>  
      </m:properties>  
    </content>  
  </entry>  
  <entry>  
    <id>https://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops('-661')</id>  
    <title type="text" />  
    <updated>2010-11-09T22:53:36Z</updated>  
    <content type="application/xml">  
      <m:properties>  
        <d:IsWiFiHotSpot m:type="Edm.Boolean">0</d:IsWiFiHotSpot>  
      </m:properties>  
    </content>  
  </entry>  
  <entry>  
    <id>https://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops('-736')</id>  
    <title type="text" />  
    <updated>2010-11-09T22:53:36Z</updated>  
    <content type="application/xml">  
      <m:properties>  
        <d:IsWiFiHotSpot m:type="Edm.Boolean">0</d:IsWiFiHotSpot>  
      </m:properties>  
    </content>  
  </entry>  
  <entry>  
    <id>https://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops('-685')</id>  
    <title type="text" />  
    <updated>2010-11-09T22:53:36Z</updated>  
    <content type="application/xml">  
      <m:properties>  
        <d:IsWiFiHotSpot m:type="Edm.Boolean">0</d:IsWiFiHotSpot>  
      </m:properties>  
    </content>  
  </entry>  
  <entry>  
    <id>https://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops('-700')</id>  
    <title type="text" />  
    <updated>2010-11-09T22:53:36Z</updated>  
    <content type="application/xml">  
      <m:properties>  
        <d:IsWiFiHotSpot m:type="Edm.Boolean">0</d:IsWiFiHotSpot>  
      </m:properties>  
    </content>  
  </entry>  
</feed>  
  
```  
  
 **URL with JSON response**  
  
```  
 HYPERLINK "http://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf94961  
33d4f23/FourthCoffeeSample/FourthCoffeeShops?spatialFilter=nearby(27.894007,-82.670776,2)&$filter=StoreType%20Eq%20'Coffee" http://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf94961  
33d4f23/FourthCoffeeSample/FourthCoffeeShops?spatialFilter=nearby(27.894007,-82.670776,2)&$filter=StoreType%20Eq%20'Coffee Shop'&$select=IsWiFiHotSpot&$orderby=IsWiFiHotSpot&$format=json&key=queryKey  
```  
  
```  
{  
   "d":{  
      "__copyright":"\u00a9 2011 Microsoft and its suppliers.  This API and any results cannot be used or accessed without Microsoft’s express written permission.",  
      "results":[  
         {  
            "__metadata":{  
               "uri":"https://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops('-715')"  
            },  
            "IsWiFiHotSpot":true  
         },  
         {  
            "__metadata":{  
               "uri":"https://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops('-661')"  
            },  
            "IsWiFiHotSpot":false  
         },  
         {  
            "__metadata":{  
               "uri":"https://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops('-736')"  
            },  
            "IsWiFiHotSpot":false  
         },  
         {  
            "__metadata":{  
               "uri":"https://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops('-685')"  
            },  
            "IsWiFiHotSpot":false  
         },  
         {  
            "__metadata":{  
               "uri":"https://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops('-700')"  
            },  
            "IsWiFiHotSpot":false  
         }  
      ]  
   }  
}  
```  
  
 **EXAMPLE: Get entities using a wildcard search.**  
  
 This example queries for coffee shops that are near a location and that have a primary city value that begins with 'Clear'. The results show the display name, location and whether the location is accessible by a wheel chair.  
  
 **URL with Atom response**  
  
```  
http://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops?spatialFilter=nearby(27.894007,-82.670776,10)&$filter=StartsWith(PrimaryCity,'Clear')%20eq%20true&$orderby=IsWheelchairAccessible&$select=DisplayName,IsWheelChairAccessible,Latitude,Longitude&key=queryKey  
```  
  
```  
<?xml version="1.0" encoding="utf-8"?>  
<feed xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata" xmlns="http://www.w3.org/2005/Atom">  
  <title type="text"></title>  
  <id>uuid:721f67c8-3f6e-49d0-ba89-938fc4d83391;id=36</id>  
  <rights type="text">© 2012 Microsoft and its suppliers.  This API and any results cannot be used or accessed without Microsoft's express written permission.</rights>  
  <updated>2012-01-27T09:56:12Z</updated>  
  <entry>  
    <id>https://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops('-661')</id>  
    <title type="text"></title>  
    <updated>2012-01-27T09:56:12Z</updated>  
    <content type="application/xml">  
      <m:properties>  
        <d:DisplayName>Fourth Coffee Store #661, Clearwater, FL, United States</d:DisplayName>  
        <d:IsWheelchairAccessible m:type="Edm.Boolean">1</d:IsWheelchairAccessible>  
        <d:Latitude m:type="Edm.Double">27.894007</d:Latitude>  
        <d:Longitude m:type="Edm.Double">-82.670776</d:Longitude>  
      </m:properties>  
    </content>  
  </entry>  
  <entry>  
    <id>https://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops('-660')</id>  
    <title type="text"></title>  
    <updated>2012-01-27T09:56:12Z</updated>  
    <content type="application/xml">  
      <m:properties>  
        <d:DisplayName>Fourth Coffee Store #660, Clearwater, FL, United States</d:DisplayName>  
        <d:IsWheelchairAccessible m:type="Edm.Boolean">1</d:IsWheelchairAccessible>  
        <d:Latitude m:type="Edm.Double">27.893759</d:Latitude>  
        <d:Longitude m:type="Edm.Double">-82.667436</d:Longitude>  
      </m:properties>  
    </content>  
  </entry>  
  <entry>  
    <id>https://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops('-666')</id>  
    <title type="text"></title>  
    <updated>2012-01-27T09:56:12Z</updated>  
    <content type="application/xml">  
      <m:properties>  
        <d:DisplayName>Fourth Coffee Store #666, Clearwater, FL, United States</d:DisplayName>  
        <d:IsWheelchairAccessible m:type="Edm.Boolean">1</d:IsWheelchairAccessible>  
        <d:Latitude m:type="Edm.Double">27.899343</d:Latitude>  
        <d:Longitude m:type="Edm.Double">-82.715604</d:Longitude>  
      </m:properties>  
    </content>  
  </entry>  
  <entry>  
    <id>https://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops('-669')</id>  
    <title type="text"></title>  
    <updated>2012-01-27T09:56:12Z</updated>  
    <content type="application/xml">  
      <m:properties>  
        <d:DisplayName>Fourth Coffee Store #669, Clearwater, FL, United States</d:DisplayName>  
        <d:IsWheelchairAccessible m:type="Edm.Boolean">0</d:IsWheelchairAccessible>  
        <d:Latitude m:type="Edm.Double">27.916173</d:Latitude>  
        <d:Longitude m:type="Edm.Double">-82.733002</d:Longitude>  
      </m:properties>  
    </content>  
  </entry>  
  <entry>  
    <id>https://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops('-710')</id>  
    <title type="text"></title>  
    <updated>2012-01-27T09:56:12Z</updated>  
    <content type="application/xml">  
      <m:properties>  
        <d:DisplayName>Fourth Coffee Store #710, Clearwater, FL, United States</d:DisplayName>  
        <d:IsWheelchairAccessible m:type="Edm.Boolean">0</d:IsWheelchairAccessible>  
        <d:Latitude m:type="Edm.Double">27.960745</d:Latitude>  
        <d:Longitude m:type="Edm.Double">-82.719151</d:Longitude>  
      </m:properties>  
    </content>  
  </entry>  
</feed>  
  
```  
  
 **URL with JSON response**  
  
```  
http://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops?spatialFilter=nearby(27.894007,-82.670776,10)&$filter=StartsWith(PrimaryCity,'Clear')%20eq%20true&$orderby=IsWheelchairAccessible&$select=DisplayName,IsWheelChairAccessible,Latitude,Longitude&$format=json&key=queryKey  
```  
  
```  
{  
   "d":{  
      "__copyright":"\u00a9 2012 Microsoft and its suppliers.  This API and any results cannot be used or accessed without Microsoft's express written permission.",  
      "results":[  
         {  
            "__metadata":{  
               "uri":"https:\/\/spatial.virtualearth.net\/REST\/v1\/data\/20181f26d9e94c81acdf9496133d4f23\/FourthCoffeeSample\/FourthCoffeeShops('-661')"  
            },  
            "DisplayName":"Fourth Coffee Store #661, Clearwater, FL, United States",  
            "IsWheelchairAccessible":true,  
            "Latitude":27.894007,  
            "Longitude":-82.670776  
         },  
         {  
            "__metadata":{  
               "uri":"https:\/\/spatial.virtualearth.net\/REST\/v1\/data\/20181f26d9e94c81acdf9496133d4f23\/FourthCoffeeSample\/FourthCoffeeShops('-660')"  
            },  
            "DisplayName":"Fourth Coffee Store #660, Clearwater, FL, United States",  
            "IsWheelchairAccessible":true,  
            "Latitude":27.893759,  
            "Longitude":-82.667436  
         },  
         {  
            "__metadata":{  
               "uri":"https:\/\/spatial.virtualearth.net\/REST\/v1\/data\/20181f26d9e94c81acdf9496133d4f23\/FourthCoffeeSample\/FourthCoffeeShops('-666')"  
            },  
            "DisplayName":"Fourth Coffee Store #666, Clearwater, FL, United States",  
            "IsWheelchairAccessible":true,  
            "Latitude":27.899343,  
            "Longitude":-82.715604  
         },  
         {  
            "__metadata":{  
               "uri":"https:\/\/spatial.virtualearth.net\/REST\/v1\/data\/20181f26d9e94c81acdf9496133d4f23\/FourthCoffeeSample\/FourthCoffeeShops('-669')"  
            },  
            "DisplayName":"Fourth Coffee Store #669, Clearwater, FL, United States",  
            "IsWheelchairAccessible":false,  
            "Latitude":27.916173,  
            "Longitude":-82.733002  
         },  
         {  
            "__metadata":{  
               "uri":"https:\/\/spatial.virtualearth.net\/REST\/v1\/data\/20181f26d9e94c81acdf9496133d4f23\/FourthCoffeeSample\/FourthCoffeeShops('-710')"  
            },  
            "DisplayName":"Fourth Coffee Store #710, Clearwater, FL, United States",  
            "IsWheelchairAccessible":false,  
            "Latitude":27.960745,  
            "Longitude":-82.719151  
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
 [Query by Area](../query-api/query-by-area.m)   
 [Query by ID](../query-api/query-by-id.md)