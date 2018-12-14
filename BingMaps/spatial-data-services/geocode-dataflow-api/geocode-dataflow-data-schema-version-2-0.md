---
title: "Geocode Dataflow Data Schema - Version 2.0 | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: d1a904ed-0e24-443e-906b-26ce0d8275e0
caps.latest.revision: 8
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Geocode Dataflow Data Schema - Version 2.0

The Geocode Dataflow API data schema version 2.0 is an update to the data schema and builds upon version 1.0 by adding all the location information returned by the [REST Services Locations API](https://msdn.microsoft.com/en-us/library/ff701715.aspx). Like version 1.0, version 2.0 supports the following formats for uploading and downloading spatial data:  
  
-   Text files with values separated by comma, tab, or pipe (&#124;) characters.  
  
-   XML  
  
 This topic describes version 2.0 of the spatial data schema for the Geocode Dataflow API. Text file and the XML schema definitions are provided along with descriptions of the fields. For examples of input and output spatial data in all formats, see [Sample Input and Output v2.0](../geocode-dataflow-api/geocode-dataflow-sample-input-and-output-data-version-2-0.md).  
  
## Text File Schema  
 The following text file schema shows how the input and output values for the Geocode Dataflow are organized in a text file. Note that there are GeocodeRequest, GeocodeResponse, and ReverseGeocodeRequest values. The Geocode Request fields define location information to geocode. The ReverseGeocodeRequest fields provide latitude and longitude information to reverse geocode. The GeocodeReponse fields are populated with the processed output data.  
  
 When you use version 2.0 of the schema with text file input, you can choose the fields that want to provide and those that you want return by specifying them in the input file after the heading information. An example is provided below and in [Sample Input and Output v2.0](../geocode-dataflow-api/geocode-dataflow-sample-input-and-output-data-version-2-0.md).  
  
 The following fields can be used in text files. Definitions are provided below.  
  
```text
Id  
GeocodeRequest/Culture  
GeocodeRequest/Query  
GeocodeRequest/Address/AddressLine  
GeocodeRequest/Address/AdminDistrict  
GeocodeRequest/Address/CountryRegion   
GeocodeRequest/Address/AdminDistrict2  
GeocodeRequest/Address/FormattedAddress  
GeocodeRequest/Address/Locality  
GeocodeRequest/Address/PostalCode  
GeocodeRequest/Address/PostalTown  
GeocodeRequest/ConfidenceFilter/MinimumConfidence  
ReverseGeocodeRequest/IncludeEntityTypes  
ReverseGeocodeRequest/Location/Latitude  
ReverseGeocodeRequest/Location/Longitude  
GeocodeResponse/Address/AddressLine  
GeocodeResponse/Address/AdminDistrict  
GeocodeResponse/Address/CountryRegion  
GeocodeResponse/Address/AdminDistrict2  
GeocodeResponse/Address/FormattedAddress  
GeocodeResponse/Address/Locality  
GeocodeResponse/Address/PostalCode  
GeocodeResponse/Address/PostalTown  
GeocodeResponse/Address/Neighborhood  
GeocodeResponse/Address/Landmark  
GeocodeResponse/Confidence  
GeocodeResponse/Name  
GeocodeResponse/EntityType  
GeocodeResponse/MatchCodes  
GeocodeResponse/Point/Latitude  
GeocodeResponse/Point/Longitude  
GeocodeResponse/BoundingBox/SouthLatitude  
GeocodeResponse/BoundingBox/WestLongitude  
GeocodeResponse/BoundingBox/NorthLatitude  
GeocodeResponse/BoundingBox/EastLongitude  
GeocodeResponse/QueryParseValues  
GeocodeResponse/GeocodePoints  
StatusCode  
FaultReason  
TraceId  
  
```  
  
 The following input and output examples show how version 2.0 of the schema is used with text files. Note that to use version 2.0 of the schema, you must set the version to 2.0 on the first line of the input file. For version 2.0, empty values are provided for any input or output data that is not provided. For more text file examples, see [Sample Input and Output v2.0](../geocode-dataflow-api/geocode-dataflow-sample-input-and-output-data-version-2-0.md).  
  
 **Example Text File Input**  
  
```csv
Bing Spatial Data Services, 2.0  
Id, GeocodeRequest/Culture, GeocodeRequest/Query, GeocodeRequest/Address/AddressLine, GeocodeRequest/Address/AdminDistrict, GeocodeRequest/Address/CountryRegion, GeocodeRequest/Address/AdminDistrict2, GeocodeRequest/Address/FormattedAddress, GeocodeRequest/Address/Locality, GeocodeRequest/Address/PostalCode, GeocodeRequest/Address/PostalTown, GeocodeRequest/ConfidenceFilter/MinimumConfidence,ReverseGeocodeRequest/IncludeEntityTypes, ReverseGeocodeRequest/Location/Latitude, ReverseGeocodeRequest/Location/Longitude, GeocodeResponse/Address/AddressLine, GeocodeResponse/Address/AdminDistrict, GeocodeResponse/Address/CountryRegion, GeocodeResponse/Address/AdminDistrict2, GeocodeResponse/Address/FormattedAddress, GeocodeResponse/Address/Locality, GeocodeResponse/Address/PostalCode, GeocodeResponse/Address/PostalTown, GeocodeResponse/Address/Neighborhood, GeocodeResponse/Address/Landmark, GeocodeResponse/Confidence, GeocodeResponse/Name, GeocodeResponse/EntityType, GeocodeResponse/MatchCodes, GeocodeResponse/Point/Latitude, GeocodeResponse/Point/Longitude, GeocodeResponse/BoundingBox/SouthLatitude, GeocodeResponse/BoundingBox/WestLongitude,GeocodeResponse/BoundingBox/NorthLatitude,GeocodeResponse/BoundingBox/EastLongitude, GeocodeResponse/QueryParseValues, GeocodeResponse/GeocodePoints, StatusCode, FaultReason, TraceId  
1,en-US,,One Microsoft Way,WA,,,,Redmond,98052  
2,en-gb,,,,,,,,,,High,"Neighborhood,PopulatedPlace",53.77848387,-1.719561517  
3,en-US,One Microsoft Way, Redmond, Wa  
```  
  
 **Example Text File Output**  
  
```csv
Bing Spatial Data Services, 2.0  
Id, GeocodeRequest/Culture, GeocodeRequest/Query, GeocodeRequest/Address/AddressLine, GeocodeRequest/Address/AdminDistrict, GeocodeRequest/Address/CountryRegion, GeocodeRequest/Address/AdminDistrict2, GeocodeRequest/Address/FormattedAddress, GeocodeRequest/Address/Locality, GeocodeRequest/Address/PostalCode, GeocodeRequest/Address/PostalTown, GeocodeRequest/ConfidenceFilter/MinimumConfidence,ReverseGeocodeRequest/IncludeEntityTypes, ReverseGeocodeRequest/Location/Latitude, ReverseGeocodeRequest/Location/Longitude, GeocodeResponse/Address/AddressLine, GeocodeResponse/Address/AdminDistrict, GeocodeResponse/Address/CountryRegion, GeocodeResponse/Address/AdminDistrict2, GeocodeResponse/Address/FormattedAddress, GeocodeResponse/Address/Locality, GeocodeResponse/Address/PostalCode, GeocodeResponse/Address/PostalTown, GeocodeResponse/Address/Neighborhood, GeocodeResponse/Address/Landmark, GeocodeResponse/Confidence, GeocodeResponse/Name, GeocodeResponse/EntityType, GeocodeResponse/MatchCodes, GeocodeResponse/Point/Latitude, GeocodeResponse/Point/Longitude, GeocodeResponse/BoundingBox/SouthLatitude, GeocodeResponse/BoundingBox/WestLongitude,GeocodeResponse/BoundingBox/NorthLatitude,GeocodeResponse/BoundingBox/EastLongitude, GeocodeResponse/QueryParseValues, GeocodeResponse/GeocodePoints, StatusCode, FaultReason, TraceId  
1,en-US,,One Microsoft Way,WA,,,,Redmond,98052,,,,,,1 Microsoft Way,WA,United States,King Co.,"1 Microsoft Way, Redmond, WA 98052",Redmond,98052,,,,High,"1 Microsoft Way, Redmond, WA 98052",Address,Good,47.6401305198669,-122.129731848836,47.6362678022963,-122.137375102026,47.6439932374376,-122.122088595645,,"[{""Longitude"":""47.6401305198669"",""Latitude"":""-122.129731848836"",""UsageTypes"":""Display"",""Type"":""Point"",""CalculationMethod"":""InterpolationOffset""},{""Longitude"":""47.6401546597481"",""Latitude"":""-122.129788175225"",""UsageTypes"":""Route"",""Type"":""Point"",""CalculationMethod"":""Interpolation""}]",Success,,"87898b72f9ba4de2bd29b7c877057eff"  
2,en-gb,,,,,,,,,,High,"Neighborhood,PopulatedPlace",53.77848387,-1.719561517,,England,United Kingdom,Bradford,"Bradford, Bradford",Bradford,,,,,High,"Bradford, Bradford",PopulatedPlace,Good,53.7957305908203,-1.75831997394562,53.6730422973633,-2.08797454833984,53.9155082702637,-1.42381429672241, ,,"[{""Longitude"":""53.7957305908203"",""Latitude"":""-1.75831997394562"",""UsageTypes"":""Display"",""Type"":""Point"",""CalculationMethod"":""Rooftop""}]",Success,,"0d5354c0a8494a6692a0cedbca748a85"  
3,en-US,One Microsoft Way,Redmond,Wa,,,,,,,,,,,1 Microsoft Way,WA,United States,King Co.,"1 Microsoft Way, Redmond, WA 98052",Redmond,98052,,,,High,"1 Microsoft Way, Redmond, WA 98052",Address,Good,47.6401305198669,-122.129731848836,47.6362678022963,-122.137375102026,47.6439932374376,-122.122088595645,"[{""Property"":""AddressLine"",""Value"":""One Microsoft Way""}]","[{""Longitude"":""47.6401305198669"",""Latitude"":""-122.129731848836"",""UsageTypes"":""Display"",""Type"":""Point"",""CalculationMethod"":""InterpolationOffset""},{""Longitude"":""47.6401546597481"",""Latitude"":""-122.129788175225"",""UsageTypes"":""Route"",""Type"":""Point"",""CalculationMethod"":""Interpolation""}]",Success,,"67f66d7c628f4c27a0287a049d10c5e7"  
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
                        <xs:attribute name="Latitude" type="xs:double" use="required" />  
                        <xs:attribute name="Longitude" type="xs:double" use="required" />  
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
                        <xs:attribute name="AdminDistrict2" type="xs:string" use="optional" />  
                        <xs:attribute name="FormattedAddress" type="xs:string" use="optional" />  
                        <xs:attribute name="Locality" type="xs:string" use="optional" />  
                        <xs:attribute name="PostalCode" type="xs:string" use="optional" />  
                        <xs:attribute name="Landmark" type="xs:string" use="optional" />  
                        <xs:attribute name="Neighborhood" type="xs:string" use="optional" />  
                      </xs:complexType>  
                    </xs:element>  
                    <xs:element maxOccurs="unbounded" name="GeocodePoint">  
                      <xs:complexType>  
                        <xs:attribute name="CalculationMethod" type="xs:string" use="required" />  
                        <xs:attribute name="Latitude" type="xs:double" use="required" />  
                        <xs:attribute name="Longitude" type="xs:double" use="required" />  
                        <xs:attribute name="Type" type="xs:string" use="required" />  
                        <xs:attribute name="UsageTypes" type="xs:string" use="required" />  
                      </xs:complexType>  
                    </xs:element>  
                    <xs:element minOccurs="0" maxOccurs="unbounded" name="QueryParseValue">  
                      <xs:complexType>  
                        <xs:attribute name="Property" type="xs:string" use="required" />  
                        <xs:attribute name="Value" type="xs:string" use="required" />  
                      </xs:complexType>  
                    </xs:element>  
                    <xs:element minOccurs="0" maxOccurs="1" name="BoundingBox">  
                      <xs:complexType>  
                        <xs:attribute name="SouthLatitude" type="xs:double" use="required" />  
                        <xs:attribute name="WestLongitude" type="xs:double" use="required" />  
                        <xs:attribute name="NorthLatitude" type="xs:double" use="required" />  
                        <xs:attribute name="EastLongitude" type="xs:double" use="required" />  
                      </xs:complexType>  
                    </xs:element>  
                    <xs:element minOccurs="0" maxOccurs="1" name="Point">  
                      <xs:complexType>  
                        <xs:attribute name="Latitude" type="xs:double" use="required" />  
                        <xs:attribute name="Longitude" type="xs:double" use="required" />  
                      </xs:complexType>  
                    </xs:element>  
                  </xs:sequence>  
                  <xs:attribute name="Name" type="xs:string" use="optional" />  
                  <xs:attribute name="EntityType" type="xs:string" use="optional" />  
                  <xs:attribute name="Confidence" type="xs:string" use="optional" />  
                  <xs:attribute name="MatchCodes" type="xs:string" use="optional" />  
                </xs:complexType>  
              </xs:element>  
                <xs:element minOccurs="0" maxOccurs="1" name="StatusCode" type="xs:string" />  
                <xs:element minOccurs="0" maxOccurs="1" name="FaultReason" type="xs:string" />  
              <xs:element minOccurs="0" maxOccurs="1" name="TraceId" type="xs:string" />  
            </xs:sequence>  
            <xs:attribute name="Id" type="xs:string" use="required" />  
          </xs:complexType>  
        </xs:element>  
      </xs:sequence>  
        <xs:attribute name="Version" type="xs:decimal" use="required" />  
    </xs:complexType>  
  </xs:element>  
</xs:schema>  
```  
  
 The following input and output examples show how the schema is used for XML files. Note that you must specify `Version="2.0"` at the GeocodeFeed level when you use version 2.0 of the schema. For a more detailed XML example, see [Sample Input and Output v2.0](../geocode-dataflow-api/geocode-dataflow-sample-input-and-output-data-version-2-0.md).  
  
 **Example XML Input**  
  
```xml
<?xml version="1.0" encoding="utf-8"?>  
<GeocodeFeed xmlns="http://schemas.microsoft.com/search/local/2010/5/geocode" Version="2.0">  
  <GeocodeEntity Id="001" xmlns="http://schemas.microsoft.com/search/local/2010/5/geocode">  
    <GeocodeRequest Culture="en-US" IncludeNeighborhood="1">  
      <Address AddressLine="1 Microsoft Way" AdminDistrict="WA" Locality="Redmond" PostalCode="98052" />  
    </GeocodeRequest>  
  </GeocodeEntity>  
  <GeocodeEntity Id="002" xmlns="http://schemas.microsoft.com/search/local/2010/5/geocode">  
    <GeocodeRequest IncludeNeighborhood="1" MaxResults="2" Query="Kings Road">  
      <ConfidenceFilter MinimumConfidence="Medium"/>  
    </GeocodeRequest>  
  </GeocodeEntity>  
  <GeocodeEntity Id="003" xmlns="http://schemas.microsoft.com/search/local/2010/5/geocode">  
    <ReverseGeocodeRequest Culture="en-US" IncludeNeighborhood="1" MaxResults="5" IncludeEntityTypes="Neighborhood">  
      <Location Longitude="-122.11871" Latitude="47.673099"/>  
      <ConfidenceFilter MinimumConfidence="High"/>  
    </ReverseGeocodeRequest>  
  </GeocodeEntity>  
  <GeocodeEntity Id="004" xmlns="http://schemas.microsoft.com/search/local/2010/5/geocode">  
    <ReverseGeocodeRequest Culture="en-US" IncludeNeighborhood="1" MaxResults="5" IncludeEntityTypes="Neighborhood">  
      <Location Longitude="-122.11871" Latitude="47.673099"/>  
      <ConfidenceFilter MinimumConfidence="High"/>  
    </ReverseGeocodeRequest>  
  </GeocodeEntity>  
</GeocodeFeed>  
  
```  
  
 **Example XML Output**  
  
```xml
<?xml version="1.0" encoding="utf-8"?>  
<GeocodeFeed Version="2.0" xmlns="http://schemas.microsoft.com/search/local/2010/5/geocode" >  
  <GeocodeEntity Id="001">  
    <GeocodeRequest Culture="en-US" IncludeNeighborhood="true">  
      <Address AddressLine="1 Microsoft Way" AdminDistrict="WA" Locality="Redmond" PostalCode="98052" />  
    </GeocodeRequest>  
    <GeocodeResponse Name="1 Microsoft Way, Redmond, WA 98052" EntityType="Address" Confidence="High" MatchCodes="Good">  
      <Address AddressLine="1 Microsoft Way" AdminDistrict="WA" CountryRegion="United States" AdminDistrict2="King Co." FormattedAddress="1 Microsoft Way, Redmond, WA 98052" Locality="Redmond" PostalCode="98052" />  
      <GeocodePoint CalculationMethod="InterpolationOffset" Latitude="47.6401305198669" Longitude="-122.129731848836" Type="Point" UsageTypes="Display" />  
      <GeocodePoint CalculationMethod="Interpolation" Latitude="47.6401546597481" Longitude="-122.129788175225" Type="Point" UsageTypes="Route" />  
      <BoundingBox SouthLatitude="47.6362678022963" WestLongitude="-122.137375102026" NorthLatitude="47.6439932374376" EastLongitude="-122.122088595645" />  
      <Point Latitude="47.6401305198669" Longitude="-122.129731848836" />  
    </GeocodeResponse>  
    <StatusCode>Success</StatusCode>  
    <TraceId>73ed21b4a4734676a3ae2d5d63e5b974</TraceId>  
  </GeocodeEntity>  
  <GeocodeEntity Id="002">  
    <GeocodeRequest IncludeNeighborhood="true" MaxResults="2" Query="Kings Road">  
      <ConfidenceFilter MinimumConfidence="Medium" />  
    </GeocodeRequest>  
    <GeocodeResponse Name="Kings Road Park, ID" EntityType="Park" Confidence="High" MatchCodes="Good">  
      <Address AdminDistrict="ID" CountryRegion="United States" AdminDistrict2="Canyon Co." FormattedAddress="Kings Road Park, ID" Locality="Nampa" Landmark="Kings Road Park" />  
      <GeocodePoint CalculationMethod="Rooftop" Latitude="43.5681953430176" Longitude="-116.528587341309" Type="Point" UsageTypes="Display" />  
      <BoundingBox SouthLatitude="43.5670738220215" WestLongitude="-116.530143737793" NorthLatitude="43.5693168640137" EastLongitude="-116.527038574219" />  
      <Point Latitude="43.5681953430176" Longitude="-116.528587341309" />  
    </GeocodeResponse>  
    <GeocodeResponse Name="Kings Park, Australia" EntityType="Park" Confidence="High" MatchCodes="Good">  
      <Address AdminDistrict="QLD" CountryRegion="Australia" FormattedAddress="Kings Park, Australia" Locality="Brisbane" Landmark="Kings Park" />  
      <GeocodePoint CalculationMethod="Rooftop" Latitude="-27.4164142608643" Longitude="152.942535400391" Type="Point" UsageTypes="Display" />  
      <BoundingBox SouthLatitude="-27.417537689209" WestLongitude="152.941268920898" NorthLatitude="-27.4152927398682" EastLongitude="152.943786621094" />  
      <Point Latitude="-27.4164142608643" Longitude="152.942535400391" />  
    </GeocodeResponse>  
    <StatusCode>Success</StatusCode>  
    <TraceId>4888f2dacb964c7ab381456d172281f5</TraceId>  
  </GeocodeEntity>  
  <GeocodeEntity Id="003">  
    <GeocodeRequest Culture="en-US" IncludeNeighborhood="true" MaxResults="5" Query="Seattle Space Needle" IncludeQueryParse="true" />  
    <GeocodeResponse Name="Space Needle, WA" EntityType="LandmarkBuilding" Confidence="High" MatchCodes="Good">  
      <Address AdminDistrict="WA" CountryRegion="United States" AdminDistrict2="King Co." FormattedAddress="Space Needle, WA" Locality="Seattle" Landmark="Space Needle" />  
      <GeocodePoint CalculationMethod="Rooftop" Latitude="47.619930267334" Longitude="-122.348670959473" Type="Point" UsageTypes="Display" />  
      <QueryParseValue Property="Locality" Value="Seattle" />  
      <QueryParseValue Property="Landmark" Value="Space Needle" />  
      <BoundingBox SouthLatitude="47.6193733215332" WestLongitude="-122.350967407227" NorthLatitude="47.6216163635254" EastLongitude="-122.347640991211" />  
      <Point Latitude="47.619930267334" Longitude="-122.348670959473" />  
    </GeocodeResponse>  
    <StatusCode>Success</StatusCode>  
    <TraceId>858ecbd4dd06407ea1fd55b3e482f317</TraceId>  
  </GeocodeEntity>  
  <GeocodeEntity Id="004">  
    <ReverseGeocodeRequest Culture="en-US" IncludeEntityTypes="Neighborhood" IncludeNeighborhood="true" MaxResults="5">  
      <Location Latitude="47.673099" Longitude="-122.11871" />  
      <ConfidenceFilter MinimumConfidence="High" />  
    </ReverseGeocodeRequest>  
    <GeocodeResponse Name="Anderson Park, WA" EntityType="Neighborhood" Confidence="High" MatchCodes="Ambiguous, Good">  
      <Address AdminDistrict="WA" CountryRegion="United States" AdminDistrict2="King Co." FormattedAddress="Anderson Park, WA" Locality="Redmond" Neighborhood="Anderson Park" />  
      <GeocodePoint CalculationMethod="Rooftop" Latitude="47.6732406616211" Longitude="-122.118690490723" Type="Point" UsageTypes="Display" />  
      <BoundingBox SouthLatitude="47.6442702786285" WestLongitude="-122.176023680315" NorthLatitude="47.7022110446136" EastLongitude="-122.061357301131" />  
      <Point Latitude="47.6732406616211" Longitude="-122.118690490723" />  
    </GeocodeResponse>  
    <StatusCode>Success</StatusCode>  
    <TraceId>3201a709a1a749d1a88f5d0952ee41ae</TraceId>  
  </GeocodeEntity>  
</GeocodeFeed>  
  
```  
  
## Data Schema Definitions  
 The following table provides descriptions of the fields in the spatial data schema. Field values are not case-sensitive.  
  
|Field|Operation|Values|  
|-----------|---------------|------------|  
|GeocodeFeed|XML container|The container for all geocode entity data when you use XML format.  You must specify version=2.0 for the GeocodeFeed if you want to use version 2.0 of the schema.|  
|GeocodeEntity|XML container|The container for all location entity data.|  
|GeocodeRequest|XML container|The container for geocode request data and options.|  
|ReverseGeocodeRequest|XML container|The container for reverse-geocode data and options.|  
|Version||Specifies the version of the schema to use. For XML, this value is set on the GeoFeed element. If it is not set, version 1.0 is the default. 2.0 as part of the first line of the file to specify the schema version (Bing Spatial Data Services, 2.0).|  
|Id|Geocode Request|A string that contains the ID of location entity data.<br /><br /> **Example**: 1|  
|Culture|Geocode Request<br /><br /> Reverse Geocode Request|A string specifying the culture.<br /><br /> **Example**: en-us [**default**]|  
|Query|Geocode Request|A query string that contains address information to geocode.<br /><br /> **Example**: 1600 Pennsylvania Ave NW Washington DC|  
|MaxResults|Geocode Request<br /><br /> Reverse Geocode Request|An integer from 1 to 20 specifying the maximum number of results to return.<br /><br /> This option is available with XML requests only.|  
|IncludeNeighborhood|Geocode Request<br /><br /> Reverse Geocode Request|A boolean value (true&#124;false or1&#124;0) that specifies whether to return neighborhood information in the address.<br /><br /> **Example**: Kiniski Gardens|  
|IncludeQueryParse|Geocode Request|A boolean value (true&#124;false or1&#124;0) that specifies whether to return parsing information.|  
|QueryParseValue|Geocode Response|One or more property-value query-parse pairs.<br /><br /> **Example**: \<QueryParseValue Property="Landmark" Value="Space Needle" />|  
|IncludeEntityTypes|Geocode Request<br /><br /> Reverse Geocode Request|A list of `POI Entity Types` to return. This parameter is only available when you are reverse-geocoding, and only returns a geocoded address if the entity type for that address is one of the entity types you specified.<br /><br /> For a list of entity types, see [Location and Area Types](../../rest-services/common-parameters-and-types/location-and-area-types.md).|  
|Address.AddressLine|Geocode Request<br /><br /> Geocode Response|A string specifying the street line of an address. The AddressLine property is the most precise, official line for an address relative to the postal agency that services the area specified by the Locality, PostalTown, or PostalCode properties.<br /><br /> **Example**: 1 Microsoft Way|  
|Address.AdminDistrict|Geocode Request<br /><br /> Geocode Response|A string specifying the subdivision name within the country or region for an address. This element is also commonly treated as the first order administrative subdivision; but in some cases, it is the second, third, or fourth order subdivision within a country, a dependency, or a region.<br /><br /> **Example**: WA|  
|Address.CountryRegion|Geocode Request<br /><br /> Geocode Response|A string specifying the country or region name of an address.<br /><br /> **Example**: US|  
|Address.District|Geocode Request|A string specifying the higher level administrative subdivision used in some countries or regions.|  
|Address.FormattedAddress|Geocode Response|A string that contains a full formatted address<br /><br /> **Note**: Do not use this field as a geocode request value. This field is used in the response.|  
|Address.Locality|Geocode Request<br /><br /> Geocode Response|A string specifying the populated place for the address. This commonly refers to a city, but may refer to a suburb or a neighborhood in certain countries.<br /><br /> **Example**: Seattle|  
|Address.PostalCode|Geocode Request<br /><br /> Geocode Response|A string specifying the post code, postal code, or ZIP Code of an address.<br /><br /> **Example**: 98178|  
|Address.PostalTown|Geocode Request|A string specifying the postal city of an address.|  
|Address.Neighborhood|Geocode Response|A string specifying the neighborhood for an address.|  
|Address.Landmark|Geocode Response|A string specifying a landmark associated with an address.|  
|ConfidenceFilter.MinimumConfidence|Geocode Request<br /><br /> Reverse Geocode Request|A string specifying the minimum confidence required for the result.<br /><br /> The following are possible confidence values:<br /><br /> -   Low<br />-   Medium<br />-   High<br /><br /> **Example**: High|  
|Location.Latitude<br /><br /> Location.Longitude|Reverse Geocode Request|A set of double values representing degrees of latitude and longitude.<br /><br /> Valid range of latitude values: [-90, +90]<br /><br /> **Example**: 47.673099<br /><br /> Valid range of longitude values: [-180, +180]<br /><br /> **Example**: -122.11871|  
|Confidence|Geocode Response|A string specifying the confidence of the result.<br /><br /> The following are possible confidence values:<br /><br /> -   Low<br />-   Medium<br />-   High|  
|Name|Geocode Response|A string specifying the display name for the response.<br /><br /> **Example**: 16552 NE 74th St, Redmond, WA 98052-7804|  
|EntityType|GeocodeResponse|A list of geographic `Entity Types` associated with a location, such as Address, PopulatedPlace and Neighborhood.<br /><br /> For a list of entity types, see [Location and Area Types](../../rest-services/common-parameters-and-types/location-and-area-types.md).<br /><br /> **Example**: PopulatedPlace|  
|MatchCodes|Geocode Response|A comma-separated list of one or more match code values that represent the geocoding level for each location in the response.<br /><br /> For example, a geocoded location with match codes of Good and Ambiguous means that more than one geocode location was found for the location information and that the geocode service did not have search up-hierarchy to find a match.<br /><br /> Similarly, a geocoded location with match codes of Ambiguous and UpHierarchy means that a geocode location could not be found that matched all of the location information, so the geocode service had to search up-hierarchy and found multiple matches at that level. An example of up an Ambiguous and UpHierarchy result is when you provide complete address information, but the geocode service cannot locate a match for the street address and instead returns information for more than one RoadBlock value.<br /><br /> The possible values are:<br /><br /> **Good**: The location has only one match or all returned matches are considered strong matches. For example, a query for New York returns several Good matches.<br /><br /> **Ambiguous**: The location is one of a set of possible matches. For example, when you query for the street address 128 Main St., the response may return two locations for 128 North Main St. and 128 South Main St. because there is not enough information to determine which option to choose.<br /><br /> **UpHierarchy**: The location represents a move up the geographic hierarchy. This occurs when a match for the location request was not found, so a less precise result is returned. For example, if a match for the requested address cannot be found, then a match code of UpHierarchy with a RoadBlock entity type may be returned.|  
|Point.Latitude,Point.Longitude|Geocode Response|A pair of double values that represent the location coordinates in degrees.|  
|BoundingBox.SouthLatitude, BoundingBox.EastLongitude, BoundingBox.NorthLatitude, BoundingBox.EastLongitude|Geocode Response|A set of geographical coordinates in degrees that define an area on the Earth that contains the location.|  
|QueryParseValue|Geocode Response|An address value that shows how a location query string was parsed. One or more query parse values for the following address values are returned when you set the IncludeQueryParse to true.<br /><br /> -   AddressLine<br />-   Locality<br />-   AdminDistrict<br />-   AdminDistrict2<br />-   PostalCode<br />-   CountryRegion<br />-   Landmark<br /><br /> **Text File (CSV, Pipe, Tab) Example**: This element has the following format in text files.<br /><br /> [{""Property"":""AddressLine"",""Value"":""One Microsoft Way""}]|  
|GeocodePoint|Geocode Response|A point associated with a geocoded address. There can be one or more geocode points associated with an address. For a list of fields, see **Geocode Point Fields** section below.|  
|StatusCode|Geocode Response|A string that provides information about the success of the operation.<br /><br /> **Examples**:<br /><br /> Success<br /><br /> BadRequest|  
|TraceId|Geocode Response|A unique ID for the geocode response.|  
|FaultReason|Geocode Response|Information about an error that occurred during the geocode dataflow job. This value is provided only for data that was not processed successfully.<br /><br /> **Example**: The Address.FormattedAddress property must not be specified because it is an output-only property.|  
  
 **Geocode Point Fields**  
  
 The following fields are provided for each geocode point returned in the response.  
  
|JSON|XML|Type|Description|  
|----------|---------|----------|-----------------|  
|point|Point|Point. For more information about the Point type, see [Location and Area Types](../../rest-services/common-parameters-and-types/location-and-area-types.md).|The latitude and longitude coordinates of the geocode point.|  
|calculationMethod|CalculationMethod|One of the following values:<br /><br /> -   Interpolation: The geocode point was matched to a point on a road using interpolation.<br />-   InterpolationOffset: The geocode point was matched to a point on a road using interpolation with an additional offset to shift the point to the side of the street.<br />-   ParcelCentroid: The geocode point was matched to the center of a parcel.<br />-   Rooftop: The geocode point was matched to the rooftop of a building.|The method that was used to compute the geocode point.|  
|usageTypes|usageTypes|One or more of the following values:<br /><br /> -   Display<br />-   Route|The best use for the geocode point.<br /><br /> Each geocode point is defined as a Route point, a Display point or both.<br /><br /> Use Route points if you are creating a route to the location. Use Display points if you are showing the location on a map. For example, if the location is a park, a Route point may specify an entrance to the park where you can enter with a car, and a Display point may be a point that specifies the center of the park.|  
  
 **Geocode Point format for Text (CSV, Pipe, Tab) files**  
  
 Geocode point data is provided as a JSON-formatted string for text files as shown in the following example.  
  
```json
[{""Longitude"":""47.6401305198669"",""Latitude"":""-122.129731848836"",""UsageTypes"":""Display"",""Type"":""Point"",""CalculationMethod"":""InterpolationOffset""},{""Latitude"":""47.6401546597481"",""Longitude"":""-122.129788175225"",""UsageTypes"":""Route"",""Type"":""Point"",""CalculationMethod"":""Interpolation""}]  
```