---
title: "Get All Public Data Sources | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 92267a62-b90e-46a2-81d4-dc37cdcbfad9
caps.latest.revision: 4
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Get All Public Data Sources
Use the following URL to get a list of all data sources that are public. This includes data sources owned and managed by Microsoft and any data source that was created with a Bing Maps Key and made public using the [Make a Data Source Public](../data-source-management-api/make-public-data-source.md) API.  
  
## Supported HTTP Methods  
 GET  
  
## Response  
 This URL supports the following response formats.  
  
-   JSON: **application/json**  
  
-   XML: **application/xml**  
  
## URL Templates  
 **Get a list of all public data sources.**  
  
```  
http://spatial.virtualearth.net/REST/v1/data/$GetPublicDataSourceList?$format=format&key=anyBingMapsKey  
```  
  
## Template Parameters  
 Parameter names and values are not case-sensitive except for the key parameter value.  
  
|Parameter|Description|Values|  
|---------------|-----------------|------------|  
|format|Type of output response.|One of the following values:<br /><br /> -   atom<br />-   json|  
  
## Examples  
 **EXAMPLE: Get all publicly available data sources.**  
  
 **URL with XML Response**  
  
```  
HYPERLINK "http://spatial.virtualearth.net/REST/v1/data/$GetPublicDataSourceList?$format=atom&key=" http://spatial.virtualearth.net/REST/v1/data/$GetPublicDataSourceList?$format=atom&key=anyBingMapsKey  
```  
  
```  
<?xml version="1.0" encoding="utf-8"?>  
<app:service xmlns:app="http://www.w3.org/2007/app" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:bsi="http://schemas.microsoft.com/bing/spatial/2010/11/odata">  
  <bsi:copyright>© 2013 Microsoft and its suppliers.  This API and any results cannot be used or accessed without Microsoft's express written permission.</bsi:copyright>  
  <app:workspace bsi:uploaded="2012-07-16T07:42:30Z" bsi:updated="2012-07-16T07:46:05Z" bsi:isPublic="true">  
    <atom:title>MyPublicDataSource</atom:title>  
    <atom:disclaimer>This data source is not owned by Microsoft. All changes made to this data source are made by the data source owner and are not the responsibility of Microsoft.</atom:disclaimer>  
    <app:collection app:href="https:// spatial.virtualearth.net /REST/v1/data/20181f26d9e94987cdf9496133d4f23/MyPublicDataSource/CoffeeShops">  
      <atom:title>CoffeeShops</atom:title>  
    </app:collection>  
  </app:workspace>  
  <app:workspace bsi:uploaded="2013-09-13T05:55:01Z" bsi:updated="2013-09-13T06:04:48Z" bsi:isPublic="true">  
    <atom:title>NavteqNA</atom:title>  
    <atom:disclaimer>This data source is owned and managed by Microsoft.</atom:disclaimer>  
    <app:collection app:href="http://spatial.virtualearth.net/REST/v1/data/f22876ec257b474b82fe2ffcb8393150/NavteqNA/NavteqPOIs">  
      <atom:title>NavteqPOIs</atom:title>  
    </app:collection>  
  </app:workspace>  
</app:service>  
```  
  
 **URL with JSON Response**  
  
```  
{  
  "d": {  
    "Copyright": "\u00a9 2013 Microsoft and its suppliers.  This API and any results cannot be used or accessed without Microsoft's express written permission.",  
    "DataSources": [  
      {  
        "Name": "FourthCoffeeSample",  
        "Disclaimer": "This data source is not owned by Microsoft. All changes made to this data source are made by the data source owner and are not the responsibility of Microsoft.",  
        "IsPublic": true,  
        "Uploaded": "Mon, 16 Jul 2012 07:42:30 GMT",  
        "Updated": "Mon, 16 Jul 2012 07:46:05 GMT",  
        "EntitySets": [  
          "FourthCoffeeShops"  
        ]  
      },  
      {  
        "Name": "NavteqNA",  
        "Disclaimer": "This data source is owned and managed by Microsoft.",  
        "IsPublic": true,  
        "Uploaded": "Fri, 13 Sep 2013 05:55:01 GMT",  
        "Updated": "Fri, 13 Sep 2013 06:04:48 GMT",  
        "EntitySets": [  
          "NavteqPOIs"  
        ]  
     }  
}  
```