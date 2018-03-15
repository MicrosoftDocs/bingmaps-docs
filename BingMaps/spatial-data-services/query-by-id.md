---
title: "Query by ID | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: fdf59422-c11a-4363-bd90-5896edbff8a5
caps.latest.revision: 36
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Query by ID
Use the following URL to search a data source for one or more entities by entity ID. The property to use as the entity ID is specified in the data schema for the entity type. For more information, see [Data Schema and Sample Input](../spatial-data-services/load-data-source-data-schema-and-sample-input.md).  
  
## Supported HTTP Methods  
 GET, HEAD  
  
## URL template  
  
> [!NOTE]
>  This template supports both HTTP and HTTPS protocols. URLs in the response use HTTPS protocol.  
>   
>  A query response can contain a maximum number of 250 results.  
  
 **Query for a single entity by specifying the entity ID string.**  
  
```  
http://spatial.virtualearth.net/REST/v1/data/accessId/dataSourceName/entityTypeName(entityId)?jsonp=jsonCallBackFunction&jsonso=jsonState&isStaging=isStaging&key=queryKey  
```  
  
 **Query for multiple entities by specifying a list of entity ID strings.**  
  
 You can query for up to 50 entity ID strings with this URL.  
  
```  
http://spatial.virtualearth.net/REST/v1/data/accessId/dataSourceName/entityTypeName?$filter=entityId in (entityId1,entityId2,entityIdN)&queryoption1&  
queryoption2&queryoptionN&jsonp=jsonCallBackFunction&jsonso=jsonState&isStaging=isStaging&key=queryKey  
```  
  
### Template Parameters  
  
> [!NOTE]
>  Parameter names and values are not case-sensitive except for the queryKey parameter value.  
  
|Parameter|Description|Values|  
|---------------|-----------------|------------|  
|accessId|**Required**. A unique ID for the data source.|A string containing and ID that is part of the URL structure that identifies the data source.<br /><br /> **Example**: 20181f26d9e94c81acdf9496133d4f23|  
|dataSourceName|**Required** The name of the data source that you want to search.|A string that identifies the data source.<br /><br /> **Example**: FourthCoffeeSample|  
|entityTypeName|**Required** The entity type to search for.|A string that identifies the entity type of the data source.<br /><br /> **Example**: FourthCoffeeShops|  
|entityTypeName(entityTypeID)|**Required when searching for a single entity**. The entity type name and the entity ID string.|The entity type of the data source and the entity ID string to search for in the data source defined by using the following format:<br /><br /> *EntityTypeName*(*EntityIdString*)<br /><br /> **Example**: FourthCoffeeShops('4232')|  
|$filter=entityId in (*entityId1*, *entityId2*, *entityIdN*|**Required when searching for multiple entities.** A comma-separated list of entity ID strings to search for in the datasource.|A list of entity ID strings to search for in the data source. You can specify up to 50 entity ID strings.<br /><br /> **Example**: $filter=entityId in ('4024', '234', '8982')|  
|queryOptions|**Optional**. Options for this query. For more information about query options, see [Query Options](../spatial-data-services/query-options.md).|A set of query options. Each query option is specified as an individual URL parameter. The following example shows how to set both the $format and the $orderby query options in the URL.<br /><br /> `&$format=json&$orderby=ZipCode`<br /><br /> **Example**: $top=3<br /><br /> **Example**: $filter=ZipCode Eq '98052'<br /><br /> If the $orderby option is not specified as part of the request, the results will be sorted by the property that represents the entity ID. Results are returned in ascending order. You can specify up to three (3) properties for the $orderby option. You cannot use the latitude or longitude properties to sort results.<br /><br /> You cannot use the latitude or longitude properties to filter results by using the $filter query option.||  
|jsonp|**Optional.** Name of JSON callback function that is called when the response to the request is received. The JSON object provided in the response is passed to the callback function.|A string that contains the name of the callback function.<br /><br /> **Example**: jsonp=MyCallbackFunction|  
|jsonso|**Optional.** The state object to pass to the JSON callback function. You can use a state object to match a response with a specific call. This value is provided as the second parameter to the callback function provided in the JSONP parameter.|Any valid JavaScript string.<br /><br /> **Example**: jsonso=abc3144sd|  
|isStaging|**Optional.** Specifies to query the staged version of the data source instead of the published version.|A Boolean value.<br /><br /> -   0 or false**[default]**<br />-   1 or true<br /><br /> **Example**: isStaging=1|  
|queryKey|**Required**. The Bing Maps Key to use to access the data source.|The Bing Maps Keys that you can use for a data source are specified when the data source is created. For example, there may be a single query key you must use to query the data source or you may be able to use any Bing Maps Key. For more information about specifying query keys when a data source is created, see [Create a Load Data Source Job](../spatial-data-services/create-a-load-data-source-job-and-input-entity-data.md).<br /><br /> **Example**: key=20181f26d9e94c81acdf9496133d4f23|  
  
## Response  
 This URL supports the following response formats.  
  
 If the $orderby query option is not specified when you query for multiple entity IDs, the results will be sorted by the property that is used for the entity ID. Results are returned in ascending order.  
  
-   Atom (application/atom + xml) [**default**]  
  
-   JSON (application/json)  
  
 When the output format is set to Atom, the results are returned in the response as one or more Atom Entries. When information about a single entity is requested using the *entityTypeName*(*entityID*) format , a single Atom Entry is returned. When the $filter=entityId in (*entityId1*, *entityId2*, *entityIdN*) format is used to get entity information, a collection of Atom Entries is returned as part of an Atom feed. For more information about these Atom response formats, see [OData AtomPub Format](http://www.odata.org/developers/protocols/atom-format) and the Atom examples in the **Examples** section.  
  
 When the output format is JSON, the response format for both type of requests is a collection of JSON Entries in a “results” container. For more information about the JSON response format, see [OData: JavaScript Object Notation (JSON) Format](http://www.odata.org/developers/protocols/json-format) and the JSON examples in the **Examples** section.  
  
## Examples  
 **EXAMPLE: Get entity information by specifying the entity ID.**  
  
 This example returns all property information for the FourthCoffeeShops entity with an entity ID of '-22067'.  
  
 **URL with Atom Response**  
  
```  
http://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops('-22067')?key=queryKey  
```  
  
```  
<entry xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata" xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" xmlns="http://www.w3.org/2005/Atom">  
  <id>https://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops('-22067')</id>  
  <title type="text" />  
  <updated>2011-01-11T02:22:18Z</updated>  
  <content type="application/xml">  
    <m:properties>  
      <d:EntityID>-22067</d:EntityID>  
      <d:Latitude m:type="Edm.Double">57.003766</d:Latitude>  
      <d:Longitude m:type="Edm.Double">9.874434</d:Longitude>  
      <d:AddressLine>Løven</d:AddressLine>  
      <d:PrimaryCity>Aalborg</d:PrimaryCity>  
      <d:Subdivision>Nordjyllands Amt</d:Subdivision>  
      <d:PostalCode>9200</d:PostalCode>  
      <d:Phone>0800-XXXXX</d:Phone>  
      <d:SecondaryCity />  
      <d:CountryRegion>Danmark</d:CountryRegion>  
      <d:Name>Fourth Coffee Store #22067</d:Name>  
      <d:DisplayName>Fourth Coffee Store #22067, Aalborg, Nordjyllands Amt, Danmark</d:DisplayName>  
      <d:Manager>Alan Steiner</d:Manager>  
      <d:StoreOpen>Y</d:StoreOpen>  
      <d:StoreType>Drive-Thru</d:StoreType>  
      <d:SeatingCapacity m:type="Edm.Int64" m:null="true" />  
      <d:Open m:type="Edm.Int64">700</d:Open>  
      <d:Close m:type="Edm.Int64">1800</d:Close>  
      <d:IsWiFiHotSpot m:type="Edm.Boolean">0</d:IsWiFiHotSpot>  
      <d:IsWheelchairAccessible m:type="Edm.Boolean">0</d:IsWheelchairAccessible>  
      <d:AcceptsOnlineOrders m:type="Edm.Boolean">0</d:AcceptsOnlineOrders>  
      <d:AcceptsCoffeeCards m:type="Edm.Boolean">1</d:AcceptsCoffeeCards>  
      <d:CreatedDate m:type="Edm.DateTime">2010-11-03T00:00:00</d:CreatedDate>  
      <d:LastUpdatedDate m:type="Edm.DateTime">2010-11-03T23:31:36</d:LastUpdatedDate>  
    </m:properties>  
  </content>  
  <rights type="text">© 2011 Microsoft and its suppliers. This API and any results cannot be used or accessed without Microsoft’s express written permission.</rights>  
</entry>  
  
```  
  
 **URL with JSON Response**  
  
 The DateTime properties are specified in the JSON response by using the [ODATA JSON Serialization format for Edm.DateTime](http://www.odata.org/developers/protocols/json-format#PrimitiveTypes). This format uses the following formula:  
  
 "\\/Date(\<ticks>["+" &#124; "-" \<offset>)\\/"  
  
 where:  
  
 \<ticks> = number of milliseconds since midnight Jan 1, 1970  
  
 \<offset> = number of minutes to add or subtract  
  
```  
http://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops('-22067')?$format=json&key=queryKey  
```  
  
```  
{  
   "d":{  
      "__copyright":"\u00a9 2011 Microsoft and its suppliers.  This API and any results cannot be used or accessed without Microsoft’s express written permission.",  
      "__metadata":{  
         "uri":"https://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops('-22067')"  
      },  
      "EntityID":"-22067",  
      "Latitude":57.003766,  
      "Longitude":9.874434,  
      "AddressLine":"Løven",  
      "PrimaryCity":"Aalborg",  
      "Subdivision":"Nordjyllands Amt",  
      "PostalCode":"9200",  
      "Phone":"0800-XXXXX",  
      "SecondaryCity":"",  
      "CountryRegion":"Danmark",  
      "Name":"Fourth Coffee Store #22067",  
      "DisplayName":"Fourth Coffee Store #22067, Aalborg, Nordjyllands Amt, Danmark",  
      "Manager":"Alan Steiner",  
      "StoreOpen":"Y",  
      "StoreType":"Drive-Thru",  
      "SeatingCapacity":null,  
      "Open":700,  
      "Close":1800,  
      "IsWiFiHotSpot":false,  
      "IsWheelchairAccessible":false,  
      "AcceptsOnlineOrders":false,  
      "AcceptsCoffeeCards":true,  
      "CreatedDate":"\/Date(634181256403200000)\/",  
      "LastUpdatedDate":"\/Date(634182103363200000)\/"  
   }  
}  
```  
  
 **EXAMPLE: Get entity location information for two entity IDs**  
  
 This example returns location information for the FourthCoffeeShops entities with entity IDs of '-22067' and '-7891'.  
  
 **URL with Atom Response**  
  
```  
http://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops?$filter=entityId in('-22067','-7891')&$select=Latitude,Longitude,AddressLine,PrimaryCity,PostalCode&key=queryKey  
```  
  
```  
<feed xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata" xmlns="http://www.w3.org/2005/Atom">  
  <title type="text" />  
  <id>uuid:d359c52a-63a7-469d-bad9-7b54baada637;id=54</id>  
  <rights type="text">© 2011 Microsoft and its suppliers. This API and any results cannot be used or accessed without Microsoft’s express written permission.</rights>  
  <updated>2011-01-11T02:33:30Z</updated>  
  <entry>  
    <id>https://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops('-22067')</id>  
    <title type="text" />  
    <updated>2011-01-11T02:33:30Z</updated>  
    <content type="application/xml">  
      <m:properties>  
        <d:Latitude m:type="Edm.Double">57.003766</d:Latitude>  
        <d:Longitude m:type="Edm.Double">9.874434</d:Longitude>  
        <d:AddressLine>Løven</d:AddressLine>  
        <d:PrimaryCity>Aalborg</d:PrimaryCity>  
        <d:PostalCode>9200</d:PostalCode>  
      </m:properties>  
    </content>  
  </entry>  
  <entry>  
    <id>https://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops('-7891')</id>  
    <title type="text" />  
    <updated>2011-01-11T02:33:30Z</updated>  
    <content type="application/xml">  
      <m:properties>  
        <d:Latitude m:type="Edm.Double">40.781604</d:Latitude>  
        <d:Longitude m:type="Edm.Double">-74.181775</d:Longitude>  
        <d:AddressLine>148 Franklin St</d:AddressLine>  
        <d:PrimaryCity>Belleville</d:PrimaryCity>  
        <d:PostalCode>07109</d:PostalCode>  
      </m:properties>  
    </content>  
  </entry>  
</feed>  
  
```  
  
 **URL with JSON Response**  
  
```  
http://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops?$filter=entityId in('-22067','-7891')&$select=Latitude,Longitude,AddressLine,PrimaryCity,PostalCode&$format=json&key=queryKey  
```  
  
```  
{  
   "d":{  
      "__copyright":"\u00a9 2011 Microsoft and its suppliers.  This API and any results cannot be used or accessed without Microsoft’s express written permission.",  
      "results":[  
         {  
            "__metadata":{  
               "uri":"https://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops('-22067')"  
            },  
            "Latitude":57.003766,  
            "Longitude":9.874434,  
            "AddressLine":"Løven",  
            "PrimaryCity":"Aalborg",  
            "PostalCode":"9200"  
         },  
         {  
            "__metadata":{  
               "uri":"https://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops('-7891')"  
            },  
            "Latitude":40.781604,  
            "Longitude":-74.181775,  
            "AddressLine":"148 Franklin St",  
            "PrimaryCity":"Belleville",  
            "PostalCode":"07109"  
         }  
      ]  
   }  
}  
```  
  
## HTTP Status Codes  
  
> [!NOTE]
>  For more details about these HTTP status codes, see [Status Codes and Error Handling](../spatial-data-services/status-codes-and-error-handling.md).  
  
 When the request is successful, the following HTTP status code is returned.  
  
-   200  
  
 When the request is not successful, the response returns one of the following errors.  
  
-   400  
  
-   401  
  
-   500  
  
-   503  
  
## See Also  
 [Query by Area](../spatial-data-services/query-by-area.md)   
 [Query by Property](../spatial-data-services/query-by-property.md)