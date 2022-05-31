---
title: "Query Response Description | Microsoft Docs"
description: "This article describes query responses and shows sample responses for a Query API."
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 13733524-6632-434b-bedb-841856e94c61
caps.latest.revision: 11
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Query Response Description

When you query a data source using the Query API, the response returns a list of entities that met the query criteria. Information returned for each entity includes a [Query by ID](../query-api/query-by-id.md) URL that returns the complete information for that entity. Depending on the query options, all or a subset of the entity properties are also returned.  
  
 If a response format is not specified by using the `$format` query option, the results are returned in ATOM format. You can also set the `$format` parameter to `json` if you want to have the response returned in JSON format.  
  
 The data schema for the query is based on the [OData AtomPub Format](https://www.odata.org/developers/protocols/atom-format) for ATOM responses and the [OData: JavaScript Object Notation (JSON) Format](https://www.odata.org/developers/protocols/json-format) for JSON responses. More details and example responses for each type of query are found in the specific query topics.  
  
## Query API Response Examples

 The following examples show sample responses for a Query API. The property names, such as IsWiFiHotSpot, are the names assigned to these properties according to the data source schema.  
  
### ATOM Example  
  
```xml
<feed xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata" xmlns="http://www.w3.org/2005/Atom">  
  <title type="text" />  
  <id>uuid:876b2e49-e480-40b8-8282-9929ced06f7f;id=46</id>  
  <updated>2010-11-09T22:53:36Z</updated>  
  <entry>  
    <id>https://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops('-715')</id>  
    <title type="text" />  
    <updated>2010-11-09T22:53:36Z</updated>  
    <content type="application/xml">  
      <m:properties>  
        <d:IsWiFiHotSpot m:type="Edm.Boolean">1</d:IsWiFiHotSpot>  
        <d:LastUpdatedDate m:type="Edm.DateTime">2010-11-03T23:31:37</d:LastUpdatedDate>  
        <d:Geom m:type="Edm.Geography">POLYGON ((-121.9466 41.0133, -121.94579 41.01751, -121.94506 41.01595, -121.9466 41.0133))</d:Geom>  
        <d:__IntersectedGeom m:type="Edm.Geography">POLYGON ((-121.9466 41.0133, -121.94506 41.01595, -121.94579 41.01751, -121.9466 41.0133))</d:__IntersectedGeom>  
  
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
        <d:LastUpdatedDate m:type="Edm.DateTime">2010-11-03T00:00:00</d:LastUpdatedDate>  
      </m:properties>  
    </content>  
  </entry>  
</feed>  
  
```  
  
### JSON Example  
  
> [!NOTE]
>  The DateTime properties are specified in the JSON response by using the [ODATA JSON Serialization format for Edm.DateTime](https://www.odata.org/developers/protocols/json-format#PrimitiveTypes). This format uses the following formula:  
>   
>  "\\/Date(\<ticks>["+" &#124; "-" \<offset>)\\/"  
>   
>  where:  
>   
>  \<ticks> = number of milliseconds since midnight Jan 1, 1970  
>   
>  \<offset> = number of minutes to add or subtract  
  
```json
{  
   "d":{  
      "results":[  
         {  
            "__metadata":{  
               "uri":"https://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops('-715')"  
            },  
            "IsWiFiHotSpot":true  
            "LastUpdatedDate":"\/Date(634182103373200000)\/"  
         },  
         {  
            "__metadata":{  
               "uri":"https://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops('-661')"  
            },  
            "IsWiFiHotSpot":false  
            "LastUpdatedDate":"\/Date(634181256403200000)\/"  
         },  
      ]  
   }  
}  
```