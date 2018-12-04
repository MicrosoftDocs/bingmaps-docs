---
title: "Load Data Source Data Schema and Sample Input | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: fef02eeb-4aad-4a17-becb-aa8108215e75
caps.latest.revision: 46
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Load Data Source Data Schema and Sample Input
You must provide a data schema and a set of input data to create a data source when you use the [Create a Load Data Source Job](../../data-source-management-api/load-data-source-dataflow/create-a-load-data-source-job-and-input-entity-data.md) URL. The data schema describes the entity type for the data source. The set of input data must validate against the schema. The data schema and input data are provided together when you create a LoadDataSource job to create or update a data source. You can provide a data schema and input data in XML format or as text with values separated by comma, tab or pipe(&#124;) characters. Before using this API, review the data limits defined in [Geocode and Data Source Limits](../../geocode-and-data-source-limits.md).  
  
 The input data format for an incremental update to a data source is the same as the format for creating a data source. The incremental update input data must include the data schema currently in use by the data source and the entity data to overwrite existing entries or to create new ones. If the entity ID of a set of entity data matches an entity ID in the data source, the entity data is replaced by the new data. If the entity ID does not exist, a new entity is created.  
  
## Data Schema  
 The data schema defines the name and attributes of the entity type to use for the new data source. If you are using XML to format your input data, you must provide an XSLT data schema. If you providing your input as values separated by comma, tab or pipe (&#124;) characters, you must provide a text data schema. Example schemas and input are provided in the **Example Schema and Entity Data** section below.  
  
 You must specify an entity ID and include latitude and longitude properties in your schema. The following sections describe how to specify the entity ID.  
  
 If you are using XML format, you can use [System.Data.Dataset](https://msdn.microsoft.com/en-us/library/system.data.dataset.aspx) to generate the data schema, primary key information and the input data.  
  
 The Bing Spatial Data Services only supports UTF-8 encoded input data.  
  
 For some helpful tips about creating the data schema and entity data, see [Helpful Tips for Entity Data](../../data-source-management-api/load-data-source-dataflow/helpful-tips-for-entity-data.md).  
  
### Entity ID  
 A data source requires an entity ID that is unique for every entity in the data source. Your data schema must specify one of the entity properties to be this entity ID. The following examples show how to specify a property named `ShopID` as the entity ID in your data schema. The data type of the entity ID property must be a string and all entity ID values must have a maximum length of 50 characters.  
  
#### Defining an entity ID in an XML schema  
 When you use XML to format your data, add the following entity ID declaration to the XSLT schema.  
  
```xml
<xs:unique name="Constraint1" msdata:PrimaryKey="true">  
  <xs:selector xpath=".//DataSourceName" />  
  <xs:field xpath="EntityIDStringProperty" />  
</xs:unique>  
  
```  
  
 The following XSLT example specifies the ShopID property as the entity ID for the FourthCoffeeShops data source.  
  
```xml
<xs:unique name="Constraint1" msdata:PrimaryKey="true">  
  <xs:selector xpath=".//FourthCoffeeShops" />  
  <xs:field xpath="ShopID" />  
</xs:unique>  
```  
  
#### Defining an entity ID in a text data schema  
 When you use a text format for your data, use the following property declaration for the entity ID property in the data schema.  
  
 *PropertyName*(Edm.String,primaryKey)  
  
 The following example specifies the ShopID property as the entity ID.  
  
 `ShopID(Edm.String,primaryKey)`  
  
### Version string  
 If you are using a text format for your input data, you must insert the following text data schema version information at the beginning of the data schema. Currently, the only text data schema version is 1.0.  
  
`Bing Spatial Data Services, 1.0, FourthCoffeeShops`  
  
### Location properties  
 Your data schema must include a location object that specifies the entity location. This object can be a latitude and longitude pair or a geographical object..  
  
 Supported geographical objects are SQL Server geography types, such as a line string or polygon. A geographical value must be specified using the [well-known text (WKT)](https://en.wikipedia.org/wiki/Well-known_text) format. For a list of supported geographical types, see [Geography Types](../../data-source-management-api/load-data-source-dataflow/geography-types.md).  
  
 The data schema must include a set of latitude and longitude properties or at most one geography property. You can also include both.  
  
> [!NOTE]
>  Note that geography types are only supported when you upload data sources using the Bing Spatial Data Services. You cannot upload data sources with geographical types using  the Bing Maps Dev Center.  
  
 The following rules apply when specifying location properties in the data schema:  
  
-   If the data schema contains latitude and longitude properties only (no geography property), you must specify latitude and longitude values for each entity.  
  
-   If the data schema contains a geography property only (no latitude and longitude), you must specify geography values for each entity. In addition, latitude and longitude values are calculated for you during upload using the [SqlGeometry.STCentroid](http://technet.microsoft.com/en-us/library/microsoft.sqlserver.types.sqlgeometry.stcentroid.aspx) method, and are stored as part of the entity data.  
  
-   If the data schema includes latitude, longitude and geography properties, only the geography property value must be specified. Latitude and longitude values are optional, and if they are not specified, the latitude and longitude values are calculated during upload using the [SqlGeometry.STCentroid](http://technet.microsoft.com/en-us/library/microsoft.sqlserver.types.sqlgeometry.stcentroid.aspx) method.  
  
 Note that if latitude and longitude are not included in the data schema or you do not provide values for these properties, latitude and longitude values are still calculated for you so that you can use all Query API methods. For example, if you query for entities within 10 kilometers of a location, the latitude and longitude of each entity is used to determine if the entity is within the distance limit. Whether you include them in the data schema or note, latitude and longitude properties are always available to you for use in queries or to return in response data.  
  
 **Latitude, Longitude and Elevation Types**  
  
 The following table shows the available properties for defining a point on the Earth and their corresponding types.  
  
|||||  
|-|-|-|-|  
|**Attribute**|**Description**|**Input Data Type**|**OData Data Type**|  
|Latitude|The latitude of the entity location.|double|Edm.Double|  
|Longitude|The longitude of the entity location.|double|Edm.Double|  
|Elevation|The elevation of the entity location.|double|Edm.Double|  
  
 **Geography Types**  
  
 For a complete description of supported geographical objects, see [Geography Types](../../data-source-management-api/load-data-source-dataflow/geography-types.md).  
  
### More about entity properties and data types  
 You can have a total of 350 properties in your schema.  The latitude and longitude properties do not count towards this maximum.  
  
 You must use the XML data types in an XML data schema. If you use one of the delimited formats for your data and data schema (values separated by commas, tabs or pipe (&#124;) characters), you must use the OData types in the data schema. Descriptions of OData types are found in the [OData Protocol Overview](https://www.odata.org/developers/protocols/overview).  
  
 The following table shows the supported data types for the data schema. These data types map to a set of OData types that are used by the data source.  
  
|XML Data Type|OData Type|  
|-------------------|----------------|  
|string|Edm.String<br /><br /> The maximum string length is 2560 characters.|  
|long|Edm.Int64|  
|Boolean|Edm.Boolean|  
|double|Edm.Double|  
|dateTime|Edm.DateTime|  
|anyType|Edm.Geography<br /><br /> The maximum number of points for any geography type is 100,000.|  
  
### Property name requirements  
 Property names must meet the following requirements:  
  
-   The property name can have up to 50 characters.  
  
-   The property name must contain alphanumeric characters and underscores (_) only.  
  
-   The first character of the property name must be a letter or an underscore.  
  
-   The property name cannot start with a two underscores (__).  
  
-   Property names are case-insensitive.  
  
## Example data schema with entity data  
 The following examples show how to define a data schema and entity data that conforms to that data schema. The [Create a Load Data Source Job](../../data-source-management-api/load-data-source-dataflow/create-a-load-data-source-job-and-input-entity-data.md) URL requires that the schema and the input data be provided together in the load data source request. XML and text file examples are provided. The data schema and input data must use UTF-8 encoding.  
  
### XML data schema and input data  
  
> [!IMPORTANT]
>  The XML root node (FourthCoffeeSampleData in this example) must have a different name than the \<xs:element> tag that sets the msdata:IsDataSet attribute (FourthCoffeeSample in this example).  
  
 In addition to other characters, such as a comma and hyphen (-), you can also use the pipe (&#124;) character in XML entity values.  
  
```xml
<?xml version="1.0" encoding="UTF-8"?>  
<FourthCoffeeSampleData>  
  <xs:schema id="FourthCoffeeSample" xmlns="" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:msdata="urn:schemas-microsoft-com:xml-msdata">  
    <xs:element name="FourthCoffeeSample" msdata:IsDataSet="true" msdata:UseCurrentLocale="true">  
      <xs:complexType>  
        <xs:choice minOccurs="0" maxOccurs="unbounded">  
          <xs:element name="FourthCoffeeShops">  
            <xs:complexType>  
              <xs:sequence>  
                <xs:element name="AddressLine" type="xs:string" minOccurs="0" />  
                <xs:element name="Locality" type="xs:string" minOccurs="0" />  
                <xs:element name="AdminDistrict" type="xs:string" minOccurs="0" />  
                <xs:element name="CountryRegion" type="xs:string" minOccurs="0" />  
                <xs:element name="PostalCode" type="xs:string" minOccurs="0" />  
                <xs:element name="Phone" type="xs:string" minOccurs="0" />  
                <xs:element name="Manager" type="xs:string" minOccurs="0" />  
                <xs:element name="StoreOpen" type="xs:string" minOccurs="0" />  
                <xs:element name="StoreType" type="xs:string" minOccurs="0" />  
                <xs:element name="Name" type="xs:string" minOccurs="0" />  
                <xs:element name="DisplayName" type="xs:string" minOccurs="0" />  
                <xs:element name="EntityID" type="xs:string" />  
                <xs:element name="Longitude" type="xs:double" minOccurs="0" />  
                <xs:element name="Latitude" type="xs:double" minOccurs="0" />  
                <xs:element name="StoreLayout" type="xs:anyType" minOccurs="0" />  
                <xs:element name="IsWiFiHotSpot" type="xs:boolean" minOccurs="0" />  
                <xs:element name="IsWheelchairAccessible" type="xs:boolean" minOccurs="0" />  
                <xs:element name="AcceptsOnlineOrders" type="xs:boolean" minOccurs="0" />  
                <xs:element name="AcceptsCoffeeCards" type="xs:boolean" minOccurs="0" />  
                <xs:element name="Open" type="xs:long" minOccurs="0" />  
                <xs:element name="Close" type="xs:long" minOccurs="0" />  
                <xs:element name="CreatedDate" msdata:DateTimeMode="Utc" type="xs:dateTime" minOccurs="0" />  
                <xs:element name="LastUpdatedDate" msdata:DateTimeMode="Utc" type="xs:dateTime" minOccurs="0" />  
              </xs:sequence>  
            </xs:complexType>  
          </xs:element>  
        </xs:choice>  
      </xs:complexType>  
      <xs:unique name="Constraint1" msdata:PrimaryKey="true">  
        <xs:selector xpath=".//FourthCoffeeShops" />  
        <xs:field xpath="EntityID" />  
      </xs:unique>  
    </xs:element>  
  </xs:schema>  
  <FourthCoffeeShops>  
    <AddressLine>Løven</AddressLine>  
    <Locality>Aalborg</Locality>  
    <AdminDistrict>Nordjyllands Amt</AdminDistrict>  
    <CountryRegion>Danmark</CountryRegion>  
    <PostalCode>9200</PostalCode>  
    <Phone>303-555-0188</Phone>  
    <Manager>Alan Steiner | Pannarat Pattanapitakkul</Manager>  
    <StoreOpen>Y</StoreOpen>  
    <StoreType>Drive-Thru</StoreType>  
    <Name>Fourth Coffee Store #22067</Name>  
    <DisplayName>Fourth Coffee Store #22067, Aalborg, Nordjyllands Amt, Danmark</DisplayName>  
    <EntityID>-22067</EntityID>  
    <Longitude>9.87443416667</Longitude>  
    <Latitude>57.00376611111</Latitude>  
    <StoreLayout>POLYGON((9.86445 57.13876,9.89266 57.13876, 9.89266 56.94234,9.86445 56.94234,9.86445 57.13876))</StoreLayout>  
    <IsWiFiHotSpot>false</IsWiFiHotSpot>  
    <IsWheelchairAccessible>false</IsWheelchairAccessible>  
    <AcceptsOnlineOrders>false</AcceptsOnlineOrders>  
    <AcceptsCoffeeCards>true</AcceptsCoffeeCards>  
    <Open>700</Open>  
    <Close>1800</Close>  
    <CreatedDate>2010-11-11T01:19:36.4350494Z</CreatedDate>  
    <LastUpdatedDate>2010-11-16T01:19:36.4350494Z</LastUpdatedDate>  
  </FourthCoffeeShops>  
  <FourthCoffeeShops>  
    <AddressLine>1 Microsoft Way</AddressLine>  
    <Locality>Redmond</Locality>  
    <AdminDistrict>WA</AdminDistrict>  
    <CountryRegion>United States</CountryRegion>  
    <PostalCode>8600</PostalCode>  
    <Phone>425-555-0111</Phone>  
    <Manager>Phil Spencer</Manager>  
    <StoreOpen>Y</StoreOpen>  
    <StoreType>Coffee Shop</StoreType>  
    <Name>Fourth Coffee Store #22066</Name>  
    <DisplayName>Fourth Coffee Store #22066, Redmond, WA United States</DisplayName>  
    <EntityID>-22066</EntityID>  
    <Longitude>-122.1293731033802</Longitude>  
    <Latitude>47.640568390488625</Latitude>  
    <IsWiFiHotSpot>true</IsWiFiHotSpot>  
    <IsWheelchairAccessible>true</IsWheelchairAccessible>  
    <AcceptsOnlineOrders>true</AcceptsOnlineOrders>  
    <AcceptsCoffeeCards>true</AcceptsCoffeeCards>  
    <Open>1000</Open>  
    <Close>2000</Close>  
    <CreatedDate>2010-11-11T01:19:36.4350494Z</CreatedDate>  
    <LastUpdatedDate>2010-11-16T01:19:36.4350494Z</LastUpdatedDate>  
  </FourthCoffeeShops>  
</FourthCoffeeSampleData>  
  
```  
  
### Text data schema and input separated by commas (CSV)  
  
```csv
Bing Spatial Data Services, 1.0, FourthCoffeeShops  
Phone(Edm.String),EntityID(Edm.String,primaryKey),Longitude(Edm.Double),Latitude(Edm.Double),StoreLayout(Edm.Geography),CountryRegion(Edm.String),Open(Edm.Int64),Close(Edm.Int64)  
303-555-0188,-22067,9.87443416667,57.00376611111,"POLYGON((9.86445 57.13876,9.89266 57.13876,9.89266 56.94234,9.86445 56.94234,9.86445 57.13876))",Danmark,700,1800  
425-555-0111,-22066,9.54552166667,56.16946722222,,Danmark,1000,2000  
```  
  
### Text data schema and input separated by tabs  
 In the following example, a tab character is represented by an arrow: ->.  
  
```csv
Bing Spatial Data Services, 1.0, FourthCoffeeShops  
Phone(Edm.String)->EntityID(Edm.String,primaryKey)->Longitude(Edm.Double)->Latitude(Edm.Double)->StoreLayout(Edm.Geography)->CountryRegion(Edm.String)->Open(Edm.Int64)->Close(Edm.Int64)  
303-555-0188->-22067->9.87443416667->57.00376611111->POLYGON((9.86445 57.13876,9.89266 57.13876,9.89266 56.94234,9.86445 56.94234,9.86445 57.13876))->Danmark->700->1800  
425-555-0111->-22066->9.54552166667->56.16946722222->->Danmark->1000->2000  
```  
  
### Text data schema and input separated by pipe characters (&#124;)  
  
```csv
Bing Spatial Data Services, 1.0, FourthCoffeeShops  
Phone(Edm.String)|EntityID(Edm.String,primaryKey)|Longitude(Edm.Double)|Latitude(Edm.Double)|StoreLayout(Edm.Geography)|CountryRegion(Edm.String)|Open(Edm.Int64)|Close(Edm.Int64)  
303-555-0188|-22067|9.87443416667|57.00376611111|POLYGON((9.86445 57.13876,9.89266 57.13876,9.89266 56.94234,9.86445 56.94234,9.86445 57.13876))|Danmark|700|1800  
425-555-0111|-22066|9.54552166667|56.16946722222||Danmark|1000|2000  
```