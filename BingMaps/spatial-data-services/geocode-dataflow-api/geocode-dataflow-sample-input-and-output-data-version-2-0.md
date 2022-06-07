---
title: "Geocode Dataflow Sample Input and Output Data Version 2.0 | Microsoft Docs"
description: "Examples of input and output data for version 2.0 of the Geocode Dataflow that demonstrates files in XML format and sets of values separated by pipe (|), comma, or tab characters."
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 95547b63-25d5-4019-9bc8-b307b0f660b4
caps.latest.revision: 4
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Geocode Dataflow Sample Input and Output Data Version 2.0

The following examples show sample input and output data for version 2.0 of the Geocode Dataflow. The input data can be provided in an XML format or as sets of values separated by pipe (&#124;), comma, or tab characters. The output data is provided in the same format as the input data. The data in these examples contains location data to geocode and latitude and longitude pairs to reverse geocode. For information about the data schema, see [Data Schema  v2.0](../geocode-dataflow-api/geocode-dataflow-data-schema-version-2-0.md).  
  
 The input data must use UTF-8 encoding.  
  
## XML Example  
  
### Input  
  
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
    <GeocodeRequest Culture="en-US" Query="Seattle Space Needle" IncludeNeighborhood="1" IncludeQueryParse="true" MaxResults="5" >  
    </GeocodeRequest>  
  </GeocodeEntity>  
  <GeocodeEntity Id="004" xmlns="http://schemas.microsoft.com/search/local/2010/5/geocode">  
    <GeocodeRequest Culture="en-US" Query="">  
      <Address AddressLine="" AdminDistrict="" />  
    </GeocodeRequest>  
  </GeocodeEntity>  
  <GeocodeEntity Id="005" xmlns="http://schemas.microsoft.com/search/local/2010/5/geocode">  
    <ReverseGeocodeRequest Culture="en-US" IncludeNeighborhood="1" MaxResults="5" IncludeEntityTypes="Neighborhood">  
      <Location Longitude="-122.11871" Latitude="47.673099"/>  
      <ConfidenceFilter MinimumConfidence="High"/>  
    </ReverseGeocodeRequest>  
  </GeocodeEntity>  
  <GeocodeEntity Id="006" xmlns="http://schemas.microsoft.com/search/local/2010/5/geocode" >  
    <ReverseGeocodeRequest Culture="en-ca">  
      <Location Longitude="-113.403092450204" Latitude="53.4802172766598"/>  
    </ReverseGeocodeRequest>  
  </GeocodeEntity>  
  <GeocodeEntity Id="007"  xmlns="http://schemas.microsoft.com/search/local/2010/5/geocode" >  
    <ReverseGeocodeRequest IncludeNeighborhood="1" MaxResults="5" IncludeEntityTypes="Neighborhood,PopulatedPlace">  
      <Location Longitude="-122.12934" Latitude="47.64054"/>  
    </ReverseGeocodeRequest>  
  </GeocodeEntity>  
</GeocodeFeed>  
  
```  
  
### Successful Output  
 The following is an example list of locations that were geocoded successfully.  
  
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
  <GeocodeEntity Id="005">  
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
    <TraceId>3201a709a1a749d1a88f5d0952ee41ae|LTSM002101|02.00.82.300|LTSMSNVM002006, LTSMSNVM001478</TraceId>  
  </GeocodeEntity>  
  <GeocodeEntity Id="006">  
    <ReverseGeocodeRequest Culture="en-ca">  
      <Location Latitude="53.4802172766598" Longitude="-113.403092450204" />  
    </ReverseGeocodeRequest>  
    <GeocodeResponse Name="448 Kirkpatrick Cres NW, Edmonton, AB T6L, Canada" EntityType="Address" Confidence="Medium" MatchCodes="Good">  
      <Address AddressLine="448 Kirkpatrick Cres NW" AdminDistrict="AB" CountryRegion="Canada" AdminDistrict2="Alberta" FormattedAddress="448 Kirkpatrick Cres NW, Edmonton, AB T6L, Canada" Locality="Edmonton" PostalCode="T6L" />  
      <GeocodePoint CalculationMethod="Interpolation" Latitude="53.4802203" Longitude="-113.4031111" Type="Point" UsageTypes="Display, Route" />  
      <BoundingBox SouthLatitude="53.4790962" WestLongitude="-113.4050001" NorthLatitude="53.4813445" EastLongitude="-113.4012221" />  
      <Point Latitude="53.4802203" Longitude="-113.4031111" />  
    </GeocodeResponse>  
    <StatusCode>Success</StatusCode>  
    <TraceId>94e6029cf3a5422496033678cbb7862b</TraceId>  
  </GeocodeEntity>  
  <GeocodeEntity Id="007">  
    <ReverseGeocodeRequest IncludeEntityTypes="Neighborhood,PopulatedPlace" IncludeNeighborhood="true" MaxResults="5">  
      <Location Latitude="47.64054" Longitude="-122.12934" />  
    </ReverseGeocodeRequest>  
    <GeocodeResponse Name="Redmond, WA" EntityType="PopulatedPlace" Confidence="High" MatchCodes="Good">  
      <Address AdminDistrict="WA" CountryRegion="United States" AdminDistrict2="King Co." FormattedAddress="Redmond, WA" Locality="Redmond" />  
      <GeocodePoint CalculationMethod="Rooftop" Latitude="47.6785583496094" Longitude="-122.130989074707" Type="Point" UsageTypes="Display" />  
      <BoundingBox SouthLatitude="47.6257362365723" WestLongitude="-122.245330810547" NorthLatitude="47.7296524047852" EastLongitude="-121.995613098145" />  
      <Point Latitude="47.6785583496094" Longitude="-122.130989074707" />  
    </GeocodeResponse>  
    <StatusCode>Success</StatusCode>  
    <TraceId>3f8922f29c474bf19e372b7cab716ef9</TraceId>  
  </GeocodeEntity>  
</GeocodeFeed>  
```  
  
### Error Output  
 The following location was not geocoded successfully.  
  
```xml
<?xml version="1.0" encoding="utf-8"?>  
<GeocodeFeed Version="2.0" xmlns="http://schemas.microsoft.com/search/local/2010/5/geocode" >  
  <GeocodeEntity Id="004">  
    <GeocodeRequest Culture="en-US">  
      <Address />  
    </GeocodeRequest>  
    <StatusCode>BadRequest</StatusCode>  
    <FaultReason>To geocode a location, you must specify at least one address field.</FaultReason>  
    <TraceId>2f2a8ea2402842198b6d9d6a62b03eeb</TraceId>  
  </GeocodeEntity>  
</GeocodeFeed>  
  
```  
  
## Pipe (&#124;) Example  
  
### Input  
  
```text
Bing Spatial Data Services, 2.0  
Id| GeocodeRequest/Culture| GeocodeRequest/Query| GeocodeRequest/Address/AddressLine| GeocodeRequest/Address/AdminDistrict| GeocodeRequest/Address/CountryRegion| GeocodeRequest/Address/AdminDistrict2| GeocodeRequest/Address/FormattedAddress| GeocodeRequest/Address/Locality| GeocodeRequest/Address/PostalCode| GeocodeRequest/Address/PostalTown| GeocodeRequest/ConfidenceFilter/MinimumConfidence|ReverseGeocodeRequest/IncludeEntityTypes| ReverseGeocodeRequest/Location/Latitude| ReverseGeocodeRequest/Location/Longitude| GeocodeResponse/Address/AddressLine| GeocodeResponse/Address/AdminDistrict| GeocodeResponse/Address/CountryRegion| GeocodeResponse/Address/AdminDistrict2| GeocodeResponse/Address/FormattedAddress| GeocodeResponse/Address/Locality| GeocodeResponse/Address/PostalCode| GeocodeResponse/Address/PostalTown| GeocodeResponse/Address/Neighborhood| GeocodeResponse/Address/Landmark| GeocodeResponse/Confidence| GeocodeResponse/Name| GeocodeResponse/EntityType| GeocodeResponse/MatchCodes| GeocodeResponse/Point/Latitude| GeocodeResponse/Point/Longitude| GeocodeResponse/BoundingBox/EastLongitude| GeocodeResponse/BoundingBox/NorthLatitude| GeocodeResponse/BoundingBox/WestLongitude| GeocodeResponse/BoundingBox/SouthLatitude| GeocodeResponse/QueryParseValues| GeocodeResponse/GeocodePoints| StatusCode| FaultReason| TraceId  
1|en-US||One Microsoft Way|WA||||Redmond|98052  
2|en-gb||||||||||High|Neighborhood,PopulatedPlace|53.77848387|-1.719561517  
3|en-US|One Microsoft Way, Redmond, Wa  
4|en-gb  
```  
  
### Successful Output  
 The following locations were geocoded successfully.  
  
```text
Bing Spatial Data Services, 2.0  
Id| GeocodeRequest/Culture| GeocodeRequest/Query| GeocodeRequest/Address/AddressLine| GeocodeRequest/Address/AdminDistrict| GeocodeRequest/Address/CountryRegion| GeocodeRequest/Address/AdminDistrict2| GeocodeRequest/Address/FormattedAddress| GeocodeRequest/Address/Locality| GeocodeRequest/Address/PostalCode| GeocodeRequest/Address/PostalTown| GeocodeRequest/ConfidenceFilter/MinimumConfidence|ReverseGeocodeRequest/IncludeEntityTypes| ReverseGeocodeRequest/Location/Latitude| ReverseGeocodeRequest/Location/Longitude| GeocodeResponse/Address/AddressLine| GeocodeResponse/Address/AdminDistrict| GeocodeResponse/Address/CountryRegion| GeocodeResponse/Address/AdminDistrict2| GeocodeResponse/Address/FormattedAddress| GeocodeResponse/Address/Locality| GeocodeResponse/Address/PostalCode| GeocodeResponse/Address/PostalTown| GeocodeResponse/Address/Neighborhood| GeocodeResponse/Address/Landmark| GeocodeResponse/Confidence| GeocodeResponse/Name| GeocodeResponse/EntityType| GeocodeResponse/MatchCodes| GeocodeResponse/Point/Latitude| GeocodeResponse/Point/Longitude| GeocodeResponse/BoundingBox/EastLongitude| GeocodeResponse/BoundingBox/NorthLatitude| GeocodeResponse/BoundingBox/WestLongitude| GeocodeResponse/BoundingBox/SouthLatitude| GeocodeResponse/QueryParseValues| GeocodeResponse/GeocodePoints| StatusCode| FaultReason| TraceId  
2|en-US||One Microsoft Way|WA||||Redmond|98052||||||1 Microsoft Way|WA|United States|King Co.|1 Microsoft Way, Redmond, WA 98052|Redmond|98052||||High|1 Microsoft Way, Redmond, WA 98052|Address|Good|47.6401305198669|-122.129731848836|-122.122088595645|47.6439932374376|-122.137375102026|47.6362678022963||[{"Longitude":"47.6401305198669","Latitude":"-122.129731848836","UsageTypes":"Display","Type":"Point","CalculationMethod":"InterpolationOffset"},{"Longitude":"47.6401546597481","Latitude":"-122.129788175225",  
"UsageTypes":"Route","Type":"Point","CalculationMethod":"Interpolation"}]|Success||"f72191c2a684402d9e29c95a03a91568 "  
3|en-gb||||||||||High|Neighborhood,PopulatedPlace|53.77848387|-1.719561517||England|United Kingdom|Bradford|Bradford, Bradford|Bradford|||||High|Bradford, Bradford|PopulatedPlace|Good|53.7957305908203|-1.75831997394562|-1.42381429672241|53.9155082702637|-2.08797454833984|53.6730422973633||[{"Longitude":"53.7957305908203","Latitude":"-1.75831997394562","UsageTypes":"Display","Type":"Point","CalculationMethod":"Rooftop"}]|Success||"9b425d0d2a3a4767ad15fb6329a3db1a"  
1|en-US||16630 Redmond Way|WA||||Redmond|98052||||||16630 Redmond Way|WA|United States|King Co.|16630 Redmond Way, Redmond, WA 98052|Redmond|98052||||High|16630 Redmond Way, Redmond, WA 98052|Address|Good|47.6732978820801|-122.118576049805|-122.110927940615|47.6771605996508|-122.126224158995|47.6694351645094||[{"Longitude":"47.6732978820801","Latitude":"-122.118576049805","UsageTypes":"Display","Type":"Point","CalculationMethod":"Parcel"},{"Longitude":"47.6730766296387","Latitude":"-122.118644714355","UsageTypes":"Route","Type":"Point","CalculationMethod":"Interpolation"}]|Success||"59cf9e78596c4cab91ffa84154444a11"  
4|en-US|One Microsoft Way, Redmond, Wa|||||||||||||1 Microsoft Way|WA|United States|King Co.|1 Microsoft Way, Redmond, WA 98052|Redmond|98052||||High|1 Microsoft Way, Redmond, WA 98052|Address|Good|47.6401305198669|-122.129731848836|-122.122088595645|47.6439932374376|-122.137375102026|47.6362678022963|[{"Property":"AddressLine","Value":"One Microsoft Way"},{"Property":"Locality","Value":"Redmond"},{"Property":"AdminDistrict","Value":"Wa"}]|[{"Longitude":"47.6401305198669","Latitude":"-122.129731848836","UsageTypes":"Display","Type":"Point","CalculationMethod":"InterpolationOffset"},{"Longitude":"47.6401546597481","Latitude":"-122.129788175225","UsageTypes":"Route","Type":"Point","CalculationMethod":"Interpolation"}]|Success||"528e63c4ad54477dab2d70835832a284"  
```  
  
### Error Output  
 The following location was not geocoded successfully.  
  
```text
Bing Spatial Data Services, 2.0  
Id| GeocodeRequest/Culture| GeocodeRequest/Query| GeocodeRequest/Address/AddressLine| GeocodeRequest/Address/AdminDistrict| GeocodeRequest/Address/CountryRegion| GeocodeRequest/Address/AdminDistrict2| GeocodeRequest/Address/FormattedAddress| GeocodeRequest/Address/Locality| GeocodeRequest/Address/PostalCode| GeocodeRequest/Address/PostalTown| GeocodeRequest/ConfidenceFilter/MinimumConfidence|ReverseGeocodeRequest/IncludeEntityTypes| ReverseGeocodeRequest/Location/Latitude| ReverseGeocodeRequest/Location/Longitude| GeocodeResponse/Address/AddressLine| GeocodeResponse/Address/AdminDistrict| GeocodeResponse/Address/CountryRegion| GeocodeResponse/Address/AdminDistrict2| GeocodeResponse/Address/FormattedAddress| GeocodeResponse/Address/Locality| GeocodeResponse/Address/PostalCode| GeocodeResponse/Address/PostalTown| GeocodeResponse/Address/Neighborhood| GeocodeResponse/Address/Landmark| GeocodeResponse/Confidence| GeocodeResponse/Name| GeocodeResponse/EntityType| GeocodeResponse/MatchCodes| GeocodeResponse/Point/Latitude| GeocodeResponse/Point/Longitude| GeocodeResponse/BoundingBox/EastLongitude| GeocodeResponse/BoundingBox/NorthLatitude| GeocodeResponse/BoundingBox/WestLongitude| GeocodeResponse/BoundingBox/SouthLatitude| GeocodeResponse/QueryParseValues| GeocodeResponse/GeocodePoints| StatusCode| FaultReason| TraceId  
5|en-gb||||||||||||||||||||||||||||||||||||BadRequest|To geocode a location, you must specify at least one address field.|"8e16af3752454e56aa71eed6ddb70534"  
```  
  
## Tab Example  
  
> [!NOTE]
>  In the following examples, a tab character is represented by an arrow: `->`.  
  
### Input  
  
```text
Bing Spatial Data Services, 2.0  
Id-> GeocodeRequest/Culture-> GeocodeRequest/Query-> GeocodeRequest/Address/AddressLine-> GeocodeRequest/Address/AdminDistrict-> GeocodeRequest/Address/CountryRegion-> GeocodeRequest/Address/AdminDistrict2-> GeocodeRequest/Address/FormattedAddress-> GeocodeRequest/Address/Locality-> GeocodeRequest/Address/PostalCode-> GeocodeRequest/Address/PostalTown->GeocodeRequest/ConfidenceFilter/MinimumConfidence->ReverseGeocodeRequest/IncludeEntityTypes-> ReverseGeocodeRequest/Location/Latitude-> ReverseGeocodeRequest/Location/Longitude-> GeocodeResponse/Address/AddressLine-> GeocodeResponse/Address/AdminDistrict-> GeocodeResponse/Address/CountryRegion-> GeocodeResponse/Address/AdminDistrict2-> GeocodeResponse/Address/FormattedAddress-> GeocodeResponse/Address/Locality-> GeocodeResponse/Address/PostalCode-> GeocodeResponse/Address/PostalTown-> GeocodeResponse/Address/Neighborhood-> GeocodeResponse/Address/Landmark-> GeocodeResponse/Confidence-> GeocodeResponse/Name-> GeocodeResponse/EntityType-> GeocodeResponse/MatchCodes-> GeocodeResponse/Point/Latitude-> GeocodeResponse/Point/Longitude-> GeocodeResponse/BoundingBox/EastLongitude-> GeocodeResponse/BoundingBox/NorthLatitude-> GeocodeResponse/BoundingBox/WestLongitude-> GeocodeResponse/BoundingBox/SouthLatitude-> GeocodeResponse/QueryParseValues-> GeocodeResponse/GeocodePoints-> StatusCode-> FaultReason-> TraceId  
1->en-US->->One Microsoft Way->WA->->->->Redmond->98052->->->  
2->en-gb->->->->->->->->->->High->Neighborhood,PopulatedPlace->53.77848387->-1.719561517  
3->en-US->One Microsoft Way, Redmond, Wa  
4->en-gb  
```  
  
### Successful Output  
 The locations were geocoded successfully.  
  
```text
Bing Spatial Data Services, 2.0  
Id-> GeocodeRequest/Culture-> GeocodeRequest/Query-> GeocodeRequest/Address/AddressLine-> GeocodeRequest/Address/AdminDistrict-> GeocodeRequest/Address/CountryRegion-> GeocodeRequest/Address/AdminDistrict2-> GeocodeRequest/Address/FormattedAddress-> GeocodeRequest/Address/Locality-> GeocodeRequest/Address/PostalCode-> GeocodeRequest/Address/PostalTown->GeocodeRequest/ConfidenceFilter/MinimumConfidence->ReverseGeocodeRequest/IncludeEntityTypes-> ReverseGeocodeRequest/Location/Latitude-> ReverseGeocodeRequest/Location/Longitude-> GeocodeResponse/Address/AddressLine-> GeocodeResponse/Address/AdminDistrict-> GeocodeResponse/Address/CountryRegion-> GeocodeResponse/Address/AdminDistrict2-> GeocodeResponse/Address/FormattedAddress-> GeocodeResponse/Address/Locality-> GeocodeResponse/Address/PostalCode-> GeocodeResponse/Address/PostalTown-> GeocodeResponse/Address/Neighborhood-> GeocodeResponse/Address/Landmark-> GeocodeResponse/Confidence-> GeocodeResponse/Name-> GeocodeResponse/EntityType-> GeocodeResponse/MatchCodes-> GeocodeResponse/Point/Latitude-> GeocodeResponse/Point/Longitude-> GeocodeResponse/BoundingBox/EastLongitude-> GeocodeResponse/BoundingBox/NorthLatitude-> GeocodeResponse/BoundingBox/WestLongitude-> GeocodeResponse/BoundingBox/SouthLatitude-> GeocodeResponse/QueryParseValues-> GeocodeResponse/GeocodePoints-> StatusCode-> FaultReason-> TraceId  
1->en-US->->One Microsoft Way->WA->->->->Redmond->98052->->->->->->1 Microsoft Way->WA->United States->King Co.->1 Microsoft Way, Redmond, WA 98052->Redmond->98052->->->->High->1 Microsoft Way, Redmond, WA 98052->Address->Good->47.6401305198669->-122.129731848836->-122.122088595645->47.6439932374376->-122.137375102026->47.6362678022963->->[{"Longitude":"47.6401305198669","Latitude":"-122.129731848836","UsageTypes":"Display","Type":"Point","CalculationMethod":"InterpolationOffset"},{"Longitude":"47.6401546597481","Latitude":"-122.129788175225","UsageTypes":"Route","Type":"Point","CalculationMethod":"Interpolation"}]->Success->->b1f7542aeb32475c896a7891bfe70a4a  
2->en-gb->->->->->->->->->->High->Neighborhood,PopulatedPlace->53.77848387->-1.719561517->->England->United Kingdom->Bradford->Bradford, Bradford->Bradford->->->->->High->Bradford, Bradford->PopulatedPlace->Good->53.7957305908203->-1.75831997394562->-1.42381429672241->53.9155082702637->-2.08797454833984->53.6730422973633->->[{"Longitude":"53.7957305908203","Latitude":"-1.75831997394562","UsageTypes":"Display","Type":"Point","CalculationMethod":"Rooftop"}]->Success->->0338ba3ca2d64e02aecd2206d0983827  
3->en-US->One Microsoft Way, Redmond, Wa->->->->->->->->->->->->->1 Microsoft Way->WA->United States->King Co.->1 Microsoft Way, Redmond, WA 98052->Redmond->98052->->->->High->1 Microsoft Way, Redmond, WA 98052->Address->Good->47.6401305198669->-122.129731848836->-122.122088595645->47.6439932374376->-122.137375102026->47.6362678022963->[{"Property":"AddressLine","Value":"One Microsoft Way"},{"Property":"Locality","Value":"Redmond"},{"Property":"AdminDistrict","Value":"Wa"}]->[{"Longitude":"47.6401305198669","Latitude":"-122.129731848836","UsageTypes":"Display","Type":"Point","CalculationMethod":"InterpolationOffset"},{"Longitude":"47.6401546597481","Latitude":"-122.129788175225","UsageTypes":"Route","Type":"Point","CalculationMethod":"Interpolation"}]->Success->->11c795f502ad40c683312e5aeabda09e  
```  
  
### Error Output  
 The following location was not geocoded successfully.  
  
```text
Bing Spatial Data Services, 2.0  
Id-> GeocodeRequest/Culture-> GeocodeRequest/Query-> GeocodeRequest/Address/AddressLine-> GeocodeRequest/Address/AdminDistrict-> GeocodeRequest/Address/CountryRegion-> GeocodeRequest/Address/AdminDistrict2-> GeocodeRequest/Address/FormattedAddress-> GeocodeRequest/Address/Locality-> GeocodeRequest/Address/PostalCode-> GeocodeRequest/Address/PostalTown->GeocodeRequest/ConfidenceFilter/MinimumConfidence->ReverseGeocodeRequest/IncludeEntityTypes-> ReverseGeocodeRequest/Location/Latitude-> ReverseGeocodeRequest/Location/Longitude-> GeocodeResponse/Address/AddressLine-> GeocodeResponse/Address/AdminDistrict-> GeocodeResponse/Address/CountryRegion-> GeocodeResponse/Address/AdminDistrict2-> GeocodeResponse/Address/FormattedAddress-> GeocodeResponse/Address/Locality-> GeocodeResponse/Address/PostalCode-> GeocodeResponse/Address/PostalTown-> GeocodeResponse/Address/Neighborhood-> GeocodeResponse/Address/Landmark-> GeocodeResponse/Confidence-> GeocodeResponse/Name-> GeocodeResponse/EntityType-> GeocodeResponse/MatchCodes-> GeocodeResponse/Point/Latitude-> GeocodeResponse/Point/Longitude-> GeocodeResponse/BoundingBox/EastLongitude-> GeocodeResponse/BoundingBox/NorthLatitude-> GeocodeResponse/BoundingBox/WestLongitude-> GeocodeResponse/BoundingBox/SouthLatitude-> GeocodeResponse/QueryParseValues-> GeocodeResponse/GeocodePoints-> StatusCode-> FaultReason-> TraceId  
5->en-gb->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->BadRequest->To geocode a location, you must specify at least one address field.->4e9f3b476f7f4e0388ccc69d36ffe422  
```  
  
## CSV (Comma-separate value) Example  
  
### Input  
  
```csv
Bing Spatial Data Services, 2.0  
Id, GeocodeRequest/Culture, GeocodeRequest/Query, GeocodeRequest/Address/AddressLine, GeocodeRequest/Address/AdminDistrict, GeocodeRequest/Address/CountryRegion, GeocodeRequest/Address/AdminDistrict2, GeocodeRequest/Address/FormattedAddress, GeocodeRequest/Address/Locality, GeocodeRequest/Address/PostalCode, GeocodeRequest/Address/PostalTown, GeocodeRequest/ConfidenceFilter/MinimumConfidence,ReverseGeocodeRequest/IncludeEntityTypes, ReverseGeocodeRequest/Location/Latitude, ReverseGeocodeRequest/Location/Longitude, GeocodeResponse/Address/AddressLine, GeocodeResponse/Address/AdminDistrict, GeocodeResponse/Address/CountryRegion, GeocodeResponse/Address/AdminDistrict2, GeocodeResponse/Address/FormattedAddress, GeocodeResponse/Address/Locality, GeocodeResponse/Address/PostalCode, GeocodeResponse/Address/PostalTown, GeocodeResponse/Address/Neighborhood, GeocodeResponse/Address/Landmark, GeocodeResponse/Confidence, GeocodeResponse/Name, GeocodeResponse/EntityType, GeocodeResponse/MatchCodes, GeocodeResponse/Point/Latitude, GeocodeResponse/Point/Longitude, GeocodeResponse/BoundingBox/EastLongitude, GeocodeResponse/BoundingBox/NorthLatitude, GeocodeResponse/BoundingBox/WestLongitude, GeocodeResponse/BoundingBox/SouthLatitude, GeocodeResponse/QueryParseValues, GeocodeResponse/GeocodePoints, StatusCode, FaultReason, TraceId  
1,en-US,,One Microsoft Way,WA,,,,Redmond,98052  
2,en-gb,,,,,,,,,,High,"Neighborhood,PopulatedPlace",53.77848387,-1.719561517  
3,en-US,One Microsoft Way, Redmond, Wa  
4,en-gb  
```  
  
### Successful Output  
 The following is an example list of locations that were geocoded successfully.  
  
```csv
Bing Spatial Data Services, 2.0  
Id, GeocodeRequest/Culture, GeocodeRequest/Query, GeocodeRequest/Address/AddressLine, GeocodeRequest/Address/AdminDistrict, GeocodeRequest/Address/CountryRegion, GeocodeRequest/Address/AdminDistrict2, GeocodeRequest/Address/FormattedAddress, GeocodeRequest/Address/Locality, GeocodeRequest/Address/PostalCode, GeocodeRequest/Address/PostalTown, GeocodeRequest/ConfidenceFilter/MinimumConfidence,ReverseGeocodeRequest/IncludeEntityTypes, ReverseGeocodeRequest/Location/Latitude, ReverseGeocodeRequest/Location/Longitude, GeocodeResponse/Address/AddressLine, GeocodeResponse/Address/AdminDistrict, GeocodeResponse/Address/CountryRegion, GeocodeResponse/Address/AdminDistrict2, GeocodeResponse/Address/FormattedAddress, GeocodeResponse/Address/Locality, GeocodeResponse/Address/PostalCode, GeocodeResponse/Address/PostalTown, GeocodeResponse/Address/Neighborhood, GeocodeResponse/Address/Landmark, GeocodeResponse/Confidence, GeocodeResponse/Name, GeocodeResponse/EntityType, GeocodeResponse/MatchCodes, GeocodeResponse/Point/Latitude, GeocodeResponse/Point/Longitude, GeocodeResponse/BoundingBox/EastLongitude, GeocodeResponse/BoundingBox/NorthLatitude, GeocodeResponse/BoundingBox/WestLongitude, GeocodeResponse/BoundingBox/SouthLatitude, GeocodeResponse/QueryParseValues, GeocodeResponse/GeocodePoints, StatusCode, FaultReason, TraceId  
1,en-US,,One Microsoft Way,WA,,,,Redmond,98052,,,,,,1 Microsoft Way,WA,United States,King Co.,"1 Microsoft Way, Redmond, WA 98052",Redmond,98052,,,,High,"1 Microsoft Way, Redmond, WA 98052",Address,Good,47.6401305198669,-122.129731848836,-122.122088595645,47.6439932374376,-122.137375102026,47.6362678022963,,"[{""Longitude"":""47.6401305198669"",""Latitude"":""-122.129731848836"",""UsageTypes"":""Display"",""Type"":""Point"",""CalculationMethod"":""InterpolationOffset""},{""Latitude"":""47.6401546597481"",""Longitude"":""-122.129788175225"",""UsageTypes"":""Route"",""Type"":""Point"",""CalculationMethod"":""Interpolation""}]",Success,,"87898b72f9ba4de2bd29b7c877057eff"  
2,en-gb,,,,,,,,,,High,"Neighborhood,PopulatedPlace",53.77848387,-1.719561517,,England,United Kingdom,Bradford,"Bradford, Bradford",Bradford,,,,,High,"Bradford, Bradford",PopulatedPlace,Good,53.7957305908203,-1.75831997394562,-1.42381429672241,53.9155082702637,-2.08797454833984,53.6730422973633,,"[{""Latitude"":""53.7957305908203"",""Longitude"":""-1.75831997394562"",""UsageTypes"":""Display"",""Type"":""Point"",""CalculationMethod"":""Rooftop""}]",Success,,"0d5354c0a8494a6692a0cedbca748a85"  
3,en-US,One Microsoft Way,Redmond,Wa,,,,,,,,,,,1 Microsoft Way,WA,United States,King Co.,"1 Microsoft Way, Redmond, WA 98052",Redmond,98052,,,,High,"1 Microsoft Way, Redmond, WA 98052",Address,Good,47.6401305198669,-122.129731848836,-122.122088595645,47.6439932374376,-122.137375102026,47.6362678022963,"[{""Property"":""AddressLine"",""Value"":""One Microsoft Way""}]","[{""Latitude"":""47.6401305198669"",""Longitude"":""-122.129731848836"",""UsageTypes"":""Display"",""Type"":""Point"",""CalculationMethod"":""InterpolationOffset""},{""Latitude"":""47.6401546597481"",""Longitude"":""-122.129788175225"",""UsageTypes"":""Route"",""Type"":""Point"",""CalculationMethod"":""Interpolation""}]",Success,,"67f66d7c628f4c27a0287a049d10c5e7"  
```  
  
### Error Output  
 The following is an example list of locations that were not geocoded successfully.  
  
```csv
Bing Spatial Data Services, 2.0  
Id, GeocodeRequest/Culture, GeocodeRequest/Query, GeocodeRequest/Address/AddressLine, GeocodeRequest/Address/AdminDistrict, GeocodeRequest/Address/CountryRegion, GeocodeRequest/Address/AdminDistrict2, GeocodeRequest/Address/FormattedAddress, GeocodeRequest/Address/Locality, GeocodeRequest/Address/PostalCode, GeocodeRequest/Address/PostalTown, GeocodeRequest/ConfidenceFilter/MinimumConfidence,ReverseGeocodeRequest/IncludeEntityTypes, ReverseGeocodeRequest/Location/Latitude, ReverseGeocodeRequest/Location/Longitude, GeocodeResponse/Address/AddressLine, GeocodeResponse/Address/AdminDistrict, GeocodeResponse/Address/CountryRegion, GeocodeResponse/Address/AdminDistrict2, GeocodeResponse/Address/FormattedAddress, GeocodeResponse/Address/Locality, GeocodeResponse/Address/PostalCode, GeocodeResponse/Address/PostalTown, GeocodeResponse/Address/Neighborhood, GeocodeResponse/Address/Landmark, GeocodeResponse/Confidence, GeocodeResponse/Name, GeocodeResponse/EntityType, GeocodeResponse/MatchCodes, GeocodeResponse/Point/Latitude, GeocodeResponse/Point/Longitude, GeocodeResponse/BoundingBox/EastLongitude, GeocodeResponse/BoundingBox/NorthLatitude, GeocodeResponse/BoundingBox/WestLongitude, GeocodeResponse/BoundingBox/SouthLatitude, GeocodeResponse/QueryParseValues, GeocodeResponse/GeocodePoints, StatusCode, FaultReason, TraceId  
5,en-gb,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,BadRequest,"To geocode a location, you must specify at least one address field.",e459b7b9ea1446cda80197f1569df669  
```