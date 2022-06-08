---
title: Get Data Source Information
titleSuffix: Microsoft Bing Maps
ms.date: 04/28/2022
ms.topic: article
ms.assetid: 9aea8125-9433-4956-a501-37773a4adee8
caps.latest.revision: 33
author: rbrundritt
ms.author: richbrun
manager: stevelom
ms.service: bing-maps
---

# Get Data Source Information

Use the following URLs to get information about one or more data sources.  
  
 You can view the query URL, master key, and query key for all data sources associated with a Bing Maps Account on [Bing Maps Account Center](https://www.bingmapsportal.com). For more information, see [Getting Data Source Information](https://msdn.microsoft.com/library/hh127034).  
  
## Supported HTTP Methods  

GET  
  
## URL templates  

 **Get information about all data sources that belong to a Bing Maps Account**.  
  
 The response returned by this URL is an AtomPub service document that contains the date and time that the each data source was last updated and the names of the data sources. When the `$format` query option is set to `atom`, which is the default value, the base URLs to use to query the data sources are also provided. For more information about the response and AtomPub service documents, see the **Response** and **Example** sections following the table of parameters.  
  
 The key parameter in this URL is set to any Bing Maps Key that belongs to the Bing Maps Account.  
  
```url
http://spatial.virtualearth.net/REST/v1/data?$format=formatQueryOption&key=anyKeyFromTheBingMapsAccount  
```  

**Get information about a specific data source.**  

To view data source information for the published data source and up to two (2) previous versions, set *showAllVersions* to true.  

The response returned by this URL is an AtomPub service document that contains the date and time that the data source was last updated and the name of the data source. When the `$format` query option is set to `atom`, which is the default value, the base URL to use to query the data source is also provided.  

The base part of the following URL with *accessID* and *dataSourceName* is returned when you create the data source. It is also returned when you request information for all data sources that belong to a Bing Maps Account. This base URL is unique for each data source and is used to get information about the datasource, such as entity types and properties. It is also used to query the data source. For more information about the response and AtomPub service documents, see the **Response** and **Example** sections following the table of parameters.  

The key parameter in this URL can be set to the data source master key or any Bing Maps Key that belongs to the same Bing Maps Account.  

```url
http://spatial.virtualearth.net/REST/v1/data/accessID/dataSourceName?$format=formatQueryOption&showAllVersions=showAllVerions&key=anyKeyFromTheBingMapsAccount  
```  
  
**Get the metadata for all data sources that belong to a Bing Maps Account**.  

The response returned by this URL is an OData Service Metadata Document, which describes the entity types and properties for all of the data sources that belong to a Bing Maps Account. For more information about the response and OData Service Metadata Documents, see the **Response** and **Example** sections following the table of parameters.  

The key parameter in this URL is set to any Bing Maps Key that belongs to the Bing Maps Account.  
  
```url
http://spatial.virtualearth.net/REST/v1/data/$metadata?key=anyKeyFromTheBingMapsAccount  
```  

**Get the metadata for a single data source.**  

To view data source metadata for the published data source and up to two (2) previous versions, set *showAllVersions* to true.  

The response returned by this URL is an OData Service Metadata Document, which describes the entity types and properties for the data source. For more information about the response and OData Service Metadata Documents, see the **Response** and **Example** sections following the table of parameters.  

The key parameter in this URL can be set to the data source master key or any Bing Maps Key that belongs to the same Bing Maps Account.  

```url
http://spatial.virtualearth.net/REST/v1/data/accessID/dataSourceName/$metadata?showAllVersions=showAllVersions&key=anyKeyFromTheBingMapsAccount  
```  

### Template Parameters  
  
> [!NOTE]
> Parameter names and values are not case-sensitive except for the key parameter value.  
  
|Parameter|Description|Values|  
|---------------|-----------------|------------|  
|accessId|**Required**. A unique ID for the data source.|A string containing and ID that is part of the URL structure that identifies the data source.<br /><br /> **Example**: a92dcfac8a0894bc4921ad5c74022623.|  
|dataSourceName|**Required** The name of the data source that you want to search.|A string that identifies the data source. The name is part of the URL structure that identifies the data source.<br /><br /> **Example**: FourthCoffeeSample|  
|entityTypeName|**Required** The entity type to search for in the data source.|A string that specifies the entity type for the data source.<br /><br /> **Example**: FourthCoffeeShops|  
|formatQueryOption|**Optional**. Specifies the format of the response. The supported formats are Atom and JSON.|One of the following values:<br /><br /> - atom **[default]**<br />- json<br /><br /> **Example**: $format=json|  
|showAllVersions|**Optional**. Shows data source information for the current data source and up to two (2) previous versions. This option is often used to get job IDs when you want to restore a previous version of the data source.|One of the following values:<br /><br /> - true: Show data source information for all versions.<br />- false **[default]**: Only show information for published data source.|  
|key|**Required**. A Bing Maps Key that belongs to the Bing Maps Account that manages the data source(s).|One of the Bing Maps Keys that is belongs to the Bing Maps Account that manages the data source(s).<br /><br /> If you are requesting information about a single data source, you can also use the data source master key.<br /><br /> **Example**: key=abc123def456ghi789abc123def456ghi789|  
  
## Response

These URLs supports the following response formats. You can specify the format to return by setting the $format query option. For more information, see [Query Options](../query-api/query-options.md).  
  
- Atom (application/atomsvc + xml) [**default**]
- JSON (application/json)  
  
> [!NOTE]
> You cannot request JSON format for your response when you request data source metadata.  

The response to the URLs that get information about one or more data sources that belong to a Bing Maps Account is an [Atom Publishing Protocol](https://www.ietf.org/rfc/rfc5023.txt) (AtomPub) service document. The AtomPub service document contains the data source information that you requested, that can be use to publish and edit web resources. For specific information about the JSON response format, see the [OData JSON Service Document](https://www.odata.org/documentation/odata-version-2-0/json-format) section of this document.

The response to the URL that gets metadata for a data source is an OData Service Metadata Document. This document describes the entity types and properties for that data source by using the Entity Data Model and the Conceptual Schema Data Language (CSDL). For more information, see [Service Metadata Document](https://www.odata.org/developers/protocols/overview#ServiceMetadataDocument) section of the [Open Data Protocol](https://www.odata.org/developers/protocols/overview).  

## Examples

**EXAMPLE: Get information on all data sources that belong to a Bing Maps Account**.  

The following example shows how to request information about all data sources that belong to a Bing Maps Account. The key parameter must be set to a Bing Maps Key that belongs to the Bing Maps Account.  
  
**URL with Atom Response**
  
```url
http://spatial.virtualearth.net/REST/v1/data?key=anyKeyFromTheBingMapsAccount  
```  
  
 The following response provides two unique URLs that represent two data sources that belong to a Bing Maps Account. You can use these URLs to query the data sources.  
  
```xml
<app:service xmlns:app="http://www.w3.org/2007/app"   
                  xmlns:atom="http://www.w3.org/2005/Atom"   
                  xmlns:bsi="http://schemas.microsoft.com/bing/spatial/2010/11/odata">  
  <bsi:copyright>© 2011 Microsoft and its suppliers.  This API and any results cannot be used or accessed without Microsoft’s express written permission.</bsi:copyright>  
  <app:workspace bsi:updated="2008-04-10T06:30:00-07:00" bsi:isPublic="true" >  
    <atom:title>FourthCoffeeSample</atom:title>  
    <app:collection app:href="https://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeStores">  
      <atom:title>FourthCoffeeStores</atom:title>  
    </app:collection>  
  </app:workspace>  
  <app:workspace bsi:updated="2008-04-10T06:30:00-07:00" bsi:isPublic="true" >  
    <atom:title>Transit</atom:title>  
    <app:collection app:href="https://spatial.virtualearth.net/REST/v1/data/123abc456deffed654cbc32131213411/Transit/Stops">  
      <atom:title>Stops</atom:title>  
    </app:collection>  
  </app:workspace>  
</app:service>  
  
```  
  
**URL with JSON Response**
  
```url
http://spatial.virtualearth.net/REST/v1/data?$format=json&key=anyKeyFromTheBingMapsAccount  
```  
  
```json
{  
   "d":{  
      "Copyright":"© 2011 Microsoft and its suppliers.  This API and any results cannot be used or accessed without Microsoft’s express written permission.",  
      "DataSources":[  
         {  
            "Name":"FourthCoffeeSample",  
            "IsPublic":"true",  
            "Updated":"Thu, 10 Apr 2008 13:30:00 GMT",  
            "EntitySets":[  
               "FourthCoffeeShops"  
            ]  
         },  
         {  
            "Name":"Transit",  
            "IsPublic":"true",  
            "Updated":"Thu, 10 Apr 2008 13:30:00 GMT",  
            "EntitySets":[  
               "Stops"  
            ]  
         }  
      ]  
   }  
}  
```  

**EXAMPLE: Get general information about a specific data source**.  

The following example shows how to request information for a specific data source including the three (3) previous versions. The key parameter must be set to the master key of the data source or any Bing Maps Key that belongs to the Bing Maps Account that contains the data source.  

**URL with Atom Response**

The following response provides a URL that you can use to query data source.  
  
```url
http://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample?showAllVersions=3&key=anyKeyFromTheBingMapsAccount  
```  
  
```xml
<?xml version="1.0" encoding="UTF-8"?>  
<app:service xmlns:bsi="http://schemas.microsoft.com/bing/spatial/2010/11/odata" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:app="http://www.w3.org/2007/app">  
  <bsi:copyright>© 2013 Microsoft and its suppliers. This API and any results cannot be used or accessed without Microsoft's express written permission.</bsi:copyright>  
    <app:workspace bsi:isStagingDataSource="false" bsi:isActive="true" bsi:isPublic="true" bsi:updated="2013-02-25T19:44:10Z">  
    <atom:title>FourthCoffeeSample</atom:title>  
    <atom:jobId>9cdf8b21033c474db7274ffe113f1f27</atom:jobId>  
    <app:collection app:href="https://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops">  
      <atom:title>FourthCoffeeShops</atom:title>  
    </app:collection>  
  </app:workspace><app:workspace bsi:isStagingDataSource="true" bsi:isActive="false" bsi:isPublic="false" bsi:uploaded="2013-02-22T19:51:58Z">  
    <atom:title>FourthCoffeeSample</atom:title>  
    <atom:jobId>f255f81b7a274022a2d6f000adf9a5b5</atom:jobId>  
    <app:collection app:href="https://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops">  
      <atom:title>FourthCoffeeShops</atom:title>  
    </app:collection>  
  </app:workspace><app:workspace bsi:isStagingDataSource="false" bsi:isActive="false" bsi:isPublic="true" bsi:updated="2013-02-25T19:42:20Z">  
    <atom:title>FourthCoffeeSample</atom:title>  
    <atom:jobId>60754ccac0cf40d391f1895e3652c1ba</atom:jobId>  
    <app:collection app:href="https://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops">  
      <atom:title>FourthCoffeeShops</atom:title>  
    </app:collection>  
  </app:workspace><app:workspace bsi:isStagingDataSource="false" bsi:isActive="false" bsi:isPublic="true" bsi:updated="2013-02-21T21:54:55Z">  
    <atom:title>FourthCoffeeSample</atom:title>  
    <atom:jobId>2c12f577f09f46b595d492ff9f80d4cc</atom:jobId>  
    <app:collection app:href="https://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops">  
      <atom:title>FourthCoffeeShops</atom:title>  
    </app:collection>  
  </app:workspace>  
</app:service>  
  
```  
  
**URL with JSON response**
  
```url
http://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample?$format=json&key=anyKeyFromTheBingMapsAccount  
```  
  
```json
{  
   "d":{  
      "Copyright":"© 2011 Microsoft and its suppliers.  This API and any results cannot be used or accessed without Microsoft’s express written permission.",  
      "Name":"FourthCoffeeSample",  
      "IsPublic":"true",  
      "Updated":"Thu, 10 Apr 2008 13:30:00 GMT",  
      "EntitySets":[  
         "FourthCoffeeShops"  
      ]  
   }  
}  
```  

**EXAMPLE: Get metadata for a specific data source**.  

The following example shows how to request metadata for a specific data source. Metadata includes the entity types for the data source and their corresponding properties. The key parameter must be set to the data source master key or to any Bing Maps Key that belongs to the Bing Maps Account that contains the data source.  

**URL with Atom Response**

Atom is the only supported response type when you request metadata.  
  
```url
http://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/$metadata?key=anyKeyFromTheBingMapsAccount  
```  
  
```xml
<edmx:Edmx xmlns:edmx="http://schemas.microsoft.com/ado/2007/06/edmx" xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata" Version="1.0">  
  <edmx:DataServices DataServiceVersion="1.0">  
    <Schema Namespace="FourthCoffeeSampleDataSource" xmlns="http://schemas.microsoft.com/ado/2008/09/edm">  
      <EntityType Name="FourthCoffeeShops">  
        <Key>  
          <PropertyRef Name="EntityID" />  
        </Key>  
        <Property Name="EntityID" Type="Edm.String" Nullable="false" MaxLength="2560" Unicode="true" FixedLength="false" />  
        <Property Name="Latitude" Type="Edm.Double"/>  
        <Property Name="Longitude" Type="Edm.Double"/>  
        <Property Name="AddressLine" Type="Edm.String" Nullable="true" MaxLength="2560" Unicode="true" FixedLength="false" />  
        <Property Name="PrimaryCity" Type="Edm.String" Nullable="true" MaxLength="2560" Unicode="true" FixedLength="false" />  
        <Property Name="Subdivision" Type="Edm.String" Nullable="true" MaxLength="2560" Unicode="true" FixedLength="false" />  
        <Property Name="PostalCode" Type="Edm.String" Nullable="true" MaxLength="2560" Unicode="true" FixedLength="false" />  
        <Property Name="Phone" Type="Edm.String" Nullable="true" MaxLength="2560" Unicode="true" FixedLength="false" />  
        <Property Name="SecondaryCity" Type="Edm.String" Nullable="true" MaxLength="2560" Unicode="true" FixedLength="false" />  
        <Property Name="CountryRegion" Type="Edm.String" Nullable="true" MaxLength="2560" Unicode="true" FixedLength="false" />  
        <Property Name="Name" Type="Edm.String" Nullable="true" MaxLength="2560" Unicode="true" FixedLength="false" />  
        <Property Name="DisplayName" Type="Edm.String" Nullable="true" MaxLength="2560" Unicode="true" FixedLength="false" />  
        <Property Name="Manager" Type="Edm.String" Nullable="true" MaxLength="2560" Unicode="true" FixedLength="false" />  
        <Property Name="StoreOpen" Type="Edm.String" Nullable="true" MaxLength="2560" Unicode="true" FixedLength="false" />  
        <Property Name="StoreType" Type="Edm.String" Nullable="true" MaxLength="2560" Unicode="true" FixedLength="false" />  
        <Property Name="SeatingCapacity" Type="Edm.Int64" Nullable="true" />  
        <Property Name="Open" Type="Edm.Int64" Nullable="true" />  
        <Property Name="Close" Type="Edm.Int64" Nullable="true" />  
        <Property Name="IsWiFiHotSpot" Type="Edm.Boolean" Nullable="true" />  
        <Property Name="IsWheelchairAccessible" Type="Edm.Boolean" Nullable="true" />  
        <Property Name="AcceptsOnlineOrders" Type="Edm.Boolean" Nullable="true" />  
        <Property Name="AcceptsCoffeeCards" Type="Edm.Boolean" Nullable="true" />  
        <Property Name="CreatedDate" Type="Edm.DateTime" Nullable="true" />  
        <Property Name="LastUpdatedDate" Type="Edm.DateTime" Nullable="true" />  
      </EntityType>  
    </Schema>  
    <Schema Namespace="FourthCoffeeSample" xmlns="http://schemas.microsoft.com/ado/2008/09/edm">  
      <EntityContainer Name="FourthCoffeeSampleContext" m:IsDefaultEntityContainer="true" IsPublic="true" JobID="20181f26d9e94c81acdf9496133d4fabc”>  
        <EntitySet Name="FourthCoffeeShops" EntityType="FourthCoffeeSampleDataSource.FourthCoffeeShops" />  
      </EntityContainer>  
    </Schema>  
  </edmx:DataServices>  
</edmx:Edmx>  
  
```  
  
## HTTP Status Codes  
  
> [!NOTE]
> For more details about these HTTP status codes, see [Status Codes and Error Handling](../status-codes-and-error-handling.md).  
  
When the request is successful, the following HTTP status code is returned.  
  
- 201  
  
When the request is not successful, the response returns one of the following errors.  
  
- 400
- 401
- 500
- 503
