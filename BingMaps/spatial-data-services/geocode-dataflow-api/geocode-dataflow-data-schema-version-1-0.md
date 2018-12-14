---
title: "Geocode Dataflow Data Schema - Version 1.0 | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: ce4b9023-3f73-4a4c-b47b-31f2920c5402
caps.latest.revision: 29
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Geocode Dataflow Data Schema - Version 1.0
> [!NOTE]
>  If you are a new user, use the latest [version 2.0](../geocode-dataflow-api/geocode-dataflow-sample-input-and-output-data-version-2-0.md) of the data schema.  
  
 The Geocode Dataflow API supports the following formats for uploading and downloading spatial data:  
  
-   Text files with values separated by comma, tab, or pipe (&#124;) characters.  
  
-   XML  
  
 This topic describes the spatial data schema for version 1.0 the Geocode Dataflow API. Text file and the XML schema definitions are provided along with descriptions of the fields. For examples of input and output spatial data in all formats, see [Sample Input and Output v1.0](../geocode-dataflow-api/geocode-dataflow-sample-input-and-output-data-version-1-0.md).  
  
## Text File Schema  
 The following text file schema shows how the input and output values for the Geocode Dataflow are organized in a text file. Note that there are GeocodeRequest, GeocodeResponse, and ReverseGeocodeRequest values. The Geocode Request fields define location information to geocode. The ReverseGeocodeRequest fields provide latitude and longitude information to reverse geocode. The GeocodeResponse fields are populated with the processed output data. Each item of data must provide information or a blank entry for each of these fields. Descriptions of the fields are provided in the Data Schema Definitions section below.  
  
```text
GeocodeEntity/@Id  
GeocodeEntity/GeocodeRequest/@Culture  
GeocodeEntity/GeocodeRequest/@Query  
GeocodeEntity/GeocodeRequest/Address/@AddressLine  
GeocodeEntity/GeocodeRequest/Address/@AdminDistrict  
GeocodeEntity/GeocodeRequest/Address/@CountryRegion  
GeocodeEntity/GeocodeRequest/Address/@District  
GeocodeEntity/GeocodeRequest/Address/@FormattedAddress  
GeocodeEntity/GeocodeRequest/Address/@Locality  
GeocodeEntity/GeocodeRequest/Address/@PostalCode  
GeocodeEntity/GeocodeRequest/Address/@PostalTown  
GeocodeEntity/GeocodeRequest/ConfidenceFilter/@MinimumConfidence  
GeocodeEntity/GeocodeResponse/Address/@AddressLine  
GeocodeEntity/GeocodeResponse/Address/@AdminDistrict  
GeocodeEntity/GeocodeResponse/Address/@CountryRegion  
GeocodeEntity/GeocodeResponse/Address/@District  
GeocodeEntity/GeocodeResponse/Address/@FormattedAddress  
GeocodeEntity/GeocodeResponse/Address/@Locality  
GeocodeEntity/GeocodeResponse/Address/@PostalCode  
GeocodeEntity/GeocodeResponse/Address/@PostalTown  
GeocodeEntity/GeocodeResponse/RooftopLocation/@Latitude  
GeocodeEntity/GeocodeResponse/RooftopLocation/@Longitude  
GeocodeEntity/GeocodeResponse/InterpolatedLocation/@Latitude  
GeocodeEntity/GeocodeResponse/InterpolatedLocation/@Longitude  
GeocodeEntity/GeocodeResponse/@Confidence  
GeocodeEntity/GeocodeResponse/@DisplayName  
GeocodeEntity/GeocodeResponse/@EntityType  
GeocodeEntity/GeocodeResponse/@StatusCode  
GeocodeEntity/GeocodeResponse/@FaultReason  
GeocodeEntity/ReverseGeocodeRequest/Location/@Latitude  
GeocodeEntity/ReverseGeocodeRequest/Location/@Longitude  
```  
  
 The following two input values show an address to geocode and a latitude and longitude pair to reverse geocode. Note that both examples contain a value or blank space for each element in the text file schema.  
  
```csv
1,en-US,,16630 Redmond Way,WA,,,,Redmond,98052,,,,,,,,,,,,,,,,,,,,,,,,  
2,en-gb,,,,,,,,,,,,,,,,,,,,,,,,,,,,53.77848387,-1.719561517  
```  
  
## XML Schema  
 The following schema is the XML schema for spatial data. Descriptions of the fields are provided in the Data Schema Definitions section below.  
  
```xml
<?xml version="1.0" encoding="utf-8"?>  
<xs:schema attributeFormDefault="unqualified" elementFormDefault="qualified" targetNamespace="http://schemas.microsoft.com/search/local/2010/5/geocode" xmlns:xs="http://www.w3.org/2001/XMLSchema">  
  <xs:element name="GeocodeFeed">  
    <xs:complexType>  
      <xs:sequence>  
        <xs:element maxOccurs="unbounded" name="GeocodeEntity">  
          <xs:complexType>  
            <xs:sequence>  
              <xs:element minOccurs="0" maxOccurs="1" name="ReverseGeocodeRequest">  
                <xs:complexType>  
                  <xs:sequence>  
                    <xs:element minOccurs="1" maxOccurs="1" name="Location">  
                      <xs:complexType>  
                        <xs:attribute name="Latitude" type="xs:decimal" use="required" />  
                        <xs:attribute name="Longitude" type="xs:decimal" use="required" />  
                      </xs:complexType>  
                    </xs:element>  
                    <xs:element minOccurs="0" maxOccurs="1" name="ConfidenceFilter">  
                      <xs:complexType>  
                        <xs:attribute name="MinimumConfidence" type="xs:string" use="required" />  
                      </xs:complexType>  
                    </xs:element>  
                  </xs:sequence>  
                  <xs:attribute name="Culture" type="xs:string" use="optional" />  
                  <xs:attribute name="IncludeEntityTypes" type="xs:string" use="optional" />  
                  <xs:attribute name="IncludeNeighborhood" type="xs:boolean" use="optional" />  
                  <xs:attribute name="MaxResults" type="xs:unsignedByte" use="optional" />  
                </xs:complexType>  
              </xs:element>  
              <xs:element minOccurs="0" maxOccurs="1" name="GeocodeRequest">  
                <xs:complexType>  
                  <xs:sequence minOccurs="0">  
                    <xs:element minOccurs="0" maxOccurs="1" name="Address">  
                      <xs:complexType>  
                        <xs:attribute name="AddressLine" type="xs:string" use="optional" />  
                        <xs:attribute name="AdminDistrict" type="xs:string" use="optional" />  
                        <xs:attribute name="Locality" type="xs:string" use="optional" />  
                        <xs:attribute name="PostalCode" type="xs:string" use="optional" />  
<xs:attribute name="CountryRegion" type="xs:string" use="optional" />  
</xs:complexType>  
                    </xs:element>  
                    <xs:element minOccurs="0" maxOccurs="1" name="ConfidenceFilter">  
                      <xs:complexType>  
                        <xs:attribute name="MinimumConfidence" type="xs:string" use="required" />  
                      </xs:complexType>  
                    </xs:element>  
                  </xs:sequence>  
                  <xs:attribute name="Culture" type="xs:string" use="optional" />  
                  <xs:attribute name="IncludeQueryParse" type="xs:boolean" use="optional" />  
                  <xs:attribute name="IncludeNeighborhood" type="xs:boolean" use="optional" />  
                  <xs:attribute name="MaxResults" type="xs:unsignedByte" use="optional" />  
                  <xs:attribute name="Query" type="xs:string" use="optional" />  
                </xs:complexType>  
              </xs:element>  
              <xs:element minOccurs="0" maxOccurs="unbounded" name="GeocodeResponse">  
                <xs:complexType>  
                  <xs:sequence>  
                    <xs:element minOccurs="0" maxOccurs="1" name="Address">  
                      <xs:complexType>  
                        <xs:attribute name="AddressLine" type="xs:string" use="optional" />  
                        <xs:attribute name="AdminDistrict" type="xs:string" use="optional" />  
                        <xs:attribute name="CountryRegion" type="xs:string" use="optional" />  
                        <xs:attribute name="District" type="xs:string" use="optional" />  
                        <xs:attribute name="FormattedAddress" type="xs:string" use="optional" />  
                        <xs:attribute name="Locality" type="xs:string" use="optional" />  
                        <xs:attribute name="PostalCode" type="xs:string" use="optional" />  
                        <xs:attribute name="PostalTown" type="xs:string" use="optional" />  
                        <xs:attribute name="Neighborhood" type="xs:string" use="optional" />  
                      </xs:complexType>  
                    </xs:element>  
                    <xs:element minOccurs="0" maxOccurs="1" name="RooftopLocation">  
                      <xs:complexType>  
                        <xs:attribute name="Latitude" type="xs:decimal" use="required" />  
                        <xs:attribute name="Longitude" type="xs:decimal" use="required" />  
                      </xs:complexType>  
                    </xs:element>  
                    <xs:element minOccurs="0" maxOccurs="1" name="InterpolatedLocation">  
                      <xs:complexType>  
                        <xs:attribute name="Latitude" type="xs:decimal" use="required" />  
                        <xs:attribute name="Longitude" type="xs:decimal" use="required" />  
                      </xs:complexType>  
                    </xs:element>  
                    <xs:element minOccurs="0" maxOccurs="unbounded" name="QueryParseValue">  
                      <xs:complexType>  
                        <xs:attribute name="Property" type="xs:string" use="required" />  
                        <xs:attribute name="Value" type="xs:string" use="required" />  
                      </xs:complexType>  
                    </xs:element>  
                  </xs:sequence>  
                  <xs:attribute name="DisplayName" type="xs:string" use="optional" />  
                  <xs:attribute name="EntityType" type="xs:string" use="optional" />  
                  <xs:attribute name="Confidence" type="xs:string" use="optional" />  
                  <xs:attribute name="StatusCode" type="xs:string" use="required" />  
                  <xs:attribute name="FaultReason" type="xs:string" use="optional" />  
                </xs:complexType>  
              </xs:element>  
              <xs:element minOccurs="0" maxOccurs="1" name="DataQuality">  
                <xs:complexType>  
                  <xs:attribute name="feedAlias" type="xs:string" use="required" />  
                </xs:complexType>  
              </xs:element>  
            </xs:sequence>  
            <xs:attribute name="Id" type="xs:string" use="required" />  
          </xs:complexType>  
        </xs:element>  
      </xs:sequence>  
    </xs:complexType>  
  </xs:element>  
</xs:schema>  
```  
  
 The following two input values show a location to geocode and a latitude and longitude pair to reverse geocode.  
  
```xml
<GeocodeFeed>  
  <GeocodeEntity Id="001" xmlns="http://schemas.microsoft.com/search/local/2010/5/geocode">  
    <GeocodeRequest Culture="en-US">  
      <Address AddressLine="16630 Redmond Way" AdminDistrict="WA" Locality="Redmond" PostalCode="98052" />  
    </GeocodeRequest>  
  </GeocodeEntity>  
  <GeocodeEntity Id="012" xmlns="http://schemas.microsoft.com/search/local/2010/5/geocode">  
    <ReverseGeocodeRequest Culture="en-gb">  
     <Location Longitude="-1.71956151723862" Latitude="53.7784838676453"/>  
    </ReverseGeocodeRequest>  
  </GeocodeEntity>  
</GeocodeFeed>  
```  
  
## Data Schema Definitions

The following table provides descriptions of the fields in the spatial data schema. Field values are not case-sensitive.  
  
|Field|Operation|Values|  
|-----------|---------------|------------|  
|Id|Geocode Request|A string that contains the ID of a spatial data input value.<br /><br /> **Example**: 1|  
|Culture|Geocode Request|A string specifying the culture.<br /><br /> **Example**: en-us [**default**]|  
|Query|Geocode Request|A query string that contains address information to geocode.<br /><br /> **Example**: 1600 Pennsylvania Ave NW Washington DC|  
|MaxResults|Geocode Request<br /><br /> Geocode Response|An integer from 1 to 20 specifying the maximum number of results to return.|  
|IncludeNeighborhood|Geocode Request<br /><br /> Geocode Response|A boolean value (true&#124;false or1&#124;0) that specifies whether to return neighborhood information in the address.<br /><br /> **Example**: Kiniski Gardens|  
|IncludeQueryParse|Geocode Request<br /><br /> Geocode Response|A boolean value (true&#124;false or1&#124;0) that specifies whether to return parsing information.<br /><br /> This option is available with XML requests only.|  
|QueryParseValue|Geocode Response|One or more property-value query-parse pairs.<br /><br /> **Example**: \<QueryParseValue Property="Landmark" Value="Space Needle" />|  
|IncludeEntityTypes|Geocode Request<br /><br /> Geocode Response|A list of `POI Entity Types` to return. This parameter is only available when you are reverse-geocoding, and only returns a geocoded address if the entity type for that address is one of the entity types you specified.<br /><br /> For a list of entity types, see [Location and Area Types](../../rest-services/common-parameters-and-types/location-and-area-types.md).|  
|EntityType|Geocode Response|A string specifying the `entity type` of the location.<br /><br /> For a list of entity types, see [Location and Area Types](../../rest-services/common-parameters-and-types/location-and-area-types.md).<br /><br /> **Examples**:<br /><br /> Address<br /><br /> RoadBlock|  
|Address.AddressLine|Geocode Request<br /><br /> Geocode Response|A string specifying the street line of an address. The AddressLine property is the most precise, official line for an address relative to the postal agency that services the area specified by the Locality, PostalTown, or PostalCode properties.<br /><br /> **Example**: 1 Microsoft Way|  
|Address.AdminDistrict|Geocode Request<br /><br /> Geocode Response|A string specifying the subdivision name within the country or region for an address. This element is also commonly treated as the first order administrative subdivision; but in some cases, it is the second, third, or fourth order subdivision within a country, a dependency, or a region.<br /><br /> **Example**: WA|  
|Address.CountryRegion|Geocode Request<br /><br /> Geocode Response|A string specifying the country or region name of an address.<br /><br /> **Example**: US|  
|Address.District|Geocode Request|A string specifying the higher level administrative subdivision used in some countries or regions.|  
|Address.FormattedAddress|Geocode Response|A string that contains a full formatted address<br /><br /> **Note**: Do not use this field as a geocode request value. This field is used in the response.|  
|Address.Locality|Geocode Request<br /><br /> Geocode Response|A string specifying the populated place for the address. This commonly refers to a city, but may refer to a suburb or a neighborhood in certain countries.<br /><br /> **Example**: Seattle|  
|Address.Neighborhood|Geocode Response|A string specifying the neighborhood for the address.|  
|Address.PostalCode|Geocode Request<br /><br /> Geocode Response|A string specifying the post code, postal code, or ZIP Code of an address.<br /><br /> **Example**: 98178|  
|Address.PostalTown|Geocode Request|A string specifying the postal city of an address.|  
|ConfidenceFilter.MinimumConfidence|Geocode Request|A string specifying the minimum confidence required for the result.<br /><br /> The following are possible confidence values:<br /><br /> -   Low<br />-   Medium<br />-   High<br /><br /> **Example**: High|  
|Location.Latitude<br /><br /> Location.Longitude|Reverse Geocode Request|A set of double values representing degrees of latitude and longitude.<br /><br /> Valid range of latitude values: [-90, +90]<br /><br /> **Example**: 47.673099<br /><br /> Valid range of longitude values: [-180, +180]<br /><br /> **Example**: -122.11871|  
|RooftopLocation.Latitude<br /><br /> RooftopLocation.Longitude|Geocode Response|A pair of double values representing degrees of latitude and longitude that are associated with an address.|  
|InterpolatedLocation.Latitude<br /><br /> InterpolatedLocation.Longitude|Geocode Response|A pair of double values representing degrees of latitude and longitude that are the result of interpolating between two points.|  
|Confidence|Geocode Response|A string specifying the confidence of the result.<br /><br /> The following are possible confidence values:<br /><br /> -   Low<br />-   Medium<br />-   High|  
|DisplayName|Geocode Response|A string specifying the display name for the response.<br /><br /> **Example**: 16552 NE 74th St, Redmond, WA 98052-7804|
|StatusCode|Geocode Response|A string that provides information about the success of the operation.<br /><br /> **Examples**:<br /><br /> Success<br /><br /> BadRequest|  
|FaultReason|Geocode Response|Information about an error that occurred during the geocode dataflow job. This value is provided only for data that was not processed successfully.<br /><br /> **Example**: The Address.FormattedAddress property must not be specified because it is an output-only property.|