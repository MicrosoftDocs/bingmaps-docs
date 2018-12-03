---
title: "Geocode Dataflow Sample Input and Output Data Version 1.0 | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 888cbf5b-c96a-4c7a-847f-83f96154a6d8
caps.latest.revision: 14
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Geocode Dataflow Sample Input and Output Data Version 1.0
> [!NOTE]
>  If you are a new user, see [Sample Input and Output v2.0](../geocode-dataflow-api/geocode-dataflow-sample-input-and-output-data-version-2-0.md) to learn how to use the latest [version 2.0](../geocode-dataflow-api/geocode-dataflow-sample-input-and-output-data-version-2-0.md) of the data schema.  
  
 The following examples show sample input and output data for version 1.0 of the Geocode Dataflow. The input data can be provided in an XML format or as sets of values separated by pipe (&#124;), comma, or tab characters. The output data is provided in the same format as the input data. The data in these examples contains location data to geocode and latitude and longitude pairs to reverse geocode. For information about the version 1.0 data schema, see [Data Schema v1.0](../geocode-dataflow-api/geocode-dataflow-data-schema-version-1-0.md).  
  
 The input data must use UTF-8 encoding.  
  
## XML Example  
  
### Input  
  
```xml
<?xml version="1.0" encoding="utf-8"?>  
<GeocodeFeed xmlns="http://schemas.microsoft.com/search/local/2010/5/geocode">  
  <GeocodeEntity Id="001" xmlns="http://schemas.microsoft.com/search/local/2010/5/geocode">  
    <GeocodeRequest Culture="en-US" IncludeNeighborhood="1">  
      <Address AddressLine="One Microsoft Way" AdminDistrict="WA" Locality="Redmond" PostalCode="98052" />  
    </GeocodeRequest>  
  </GeocodeEntity>  
  <GeocodeEntity Id="002" xmlns="http://schemas.microsoft.com/search/local/2010/5/geocode">  
    <GeocodeRequest Culture="en-US" Query="Seattle Space Needle" IncludeNeighborhood="1" IncludeQueryParse="true" >  
    </GeocodeRequest>  
  </GeocodeEntity>  
  <GeocodeEntity Id="003" xmlns="http://schemas.microsoft.com/search/local/2010/5/geocode">  
    <GeocodeRequest Culture="en-US" Query="Ccs-PMV, VE" IncludeNeighborhood="1" IncludeQueryParse="true" MaxResults="5">  
    </GeocodeRequest>  
  </GeocodeEntity>  
  <GeocodeEntity Id="004" xmlns="http://schemas.microsoft.com/search/local/2010/5/geocode" MaxResults="2">  
    <GeocodeRequest Culture="en-US" Query="Greenwich">  
      <Address AddressLine="" AdminDistrict="" />  
    </GeocodeRequest>  
  </GeocodeEntity>  
  <GeocodeEntity Id="005" xmlns="http://schemas.microsoft.com/search/local/2010/5/geocode">  
    <GeocodeRequest Culture="en-US" Query="">  
      <Address AddressLine="" AdminDistrict="" />  
    </GeocodeRequest>  
  </GeocodeEntity>  
  <GeocodeEntity Id="006" xmlns="http://schemas.microsoft.com/search/local/2010/5/geocode">  
    <ReverseGeocodeRequest Culture="en-US" IncludeNeighborhood="1" MaxResults="5" IncludeEntityTypes="Neighborhood,PopulatedPlace">  
      <Location Longitude="-122.11871" Latitude="47.673099"/>  
      <ConfidenceFilter MinimumConfidence="High"/>  
    </ReverseGeocodeRequest>  
  </GeocodeEntity>  
  </GeocodeFeed>  
  
```  
  
### Successful Output  
 The locations were geocoded successfully.  
  
```xml
<GeocodeFeed xmlns="http://schemas.microsoft.com/search/local/2010/5/geocode">  
  
  <GeocodeEntity xmlns="http://schemas.microsoft.com/search/local/2010/5/geocode" Id="001">  
    <GeocodeRequest Culture="en-US" IncludeNeighborhood="true">  
      <Address AddressLine="One Microsoft Way" AdminDistrict="WA" Locality="Redmond" PostalCode="98052"/>  
    </GeocodeRequest>  
    <GeocodeResponse DisplayName="1 Microsoft Way, Redmond, WA 98052" EntityType="Address" Confidence="High" StatusCode="Success">  
      <Address AddressLine="1 Microsoft Way" AdminDistrict="WA" CountryRegion="United States" District="King Co." FormattedAddress="1 Microsoft Way, Redmond, WA 98052" Locality="Redmond"PostalCode="98052"/>  
      <InterpolatedLocation Latitude="47.6400493830442" Longitude="-122.129796892405"/>  
    </GeocodeResponse>  
    <DataQuality feedAlias="geofeed1"/>  
  </GeocodeEntity>  
  
  <GeocodeEntity xmlns="http://schemas.microsoft.com/search/local/2010/5/geocode" Id="006">  
    <ReverseGeocodeRequest IncludeEntityTypes="Neighborhood,PopulatedPlace" Culture="en-US" IncludeNeighborhood="true" MaxResults="5">  
      <Location Latitude="47.673099" Longitude="-122.11871"/>  
      <ConfidenceFilter MinimumConfidence="High"/>  
    </ReverseGeocodeRequest>  
    <GeocodeResponse DisplayName="Redmond, WA" EntityType="PopulatedPlace" Confidence="High" StatusCode="Success">  
      <Address AdminDistrict="WA" CountryRegion="United States" District="King Co." FormattedAddress="Redmond, WA" Locality="Redmond"/>  
      <RooftopLocation Latitude="47.678581237793" Longitude="-122.131576538086"/>  
    </GeocodeResponse>  
    <DataQuality feedAlias="geofeed1"/>  
  </GeocodeEntity>  
  
  <GeocodeEntity xmlns="http://schemas.microsoft.com/search/local/2010/5/geocode" Id="002">  
    <GeocodeRequest Culture="en-US" IncludeNeighborhood="true" Query="Seattle Space Needle" IncludeQueryParse="true"/>  
    <GeocodeResponse DisplayName="Space Needle, WA" EntityType="LandmarkBuilding" Confidence="High" StatusCode="Success">  
      <Address AdminDistrict="WA" CountryRegion="United States" District="King Co." FormattedAddress="Space Needle, WA" Locality="Seattle"/>  
      <RooftopLocation Latitude="47.619930267334" Longitude="-122.348670959473"/>  
      <QueryParseValue Property="Landmark" Value="Seattle Space Needle"/>  
    </GeocodeResponse>  
    <DataQuality feedAlias="geofeed1"/>  
  </GeocodeEntity>  
  
  <GeocodeEntity xmlns="http://schemas.microsoft.com/search/local/2010/5/geocode" Id="004" MaxResults="2">  
    <GeocodeRequest Culture="en-US" Query="Greenwich">  
      <Address/>  
    </GeocodeRequest>  
    <GeocodeResponse DisplayName="Greenwich, CT" EntityType="PopulatedPlace" Confidence="High" StatusCode="Success">  
      <Address AdminDistrict="CT" CountryRegion="United States" District="Fairfield Co." FormattedAddress="Greenwich, CT" Locality="Greenwich"/>  
      <RooftopLocation Latitude="41.0642509460449" Longitude="-73.6397705078125"/>  
    </GeocodeResponse>  
    <DataQuality feedAlias="geofeed1"/>  
  </GeocodeEntity>  
  
  <GeocodeEntity xmlns="http://schemas.microsoft.com/search/local/2010/5/geocode" Id="003">  
    <GeocodeRequest Culture="en-US" IncludeNeighborhood="true" MaxResults="5" Query="Ccs-PMV, VE" IncludeQueryParse="true"/>  
    <GeocodeResponse DisplayName="Del Caribe International Airport, Venezuela" EntityType="Airport" Confidence="High" StatusCode="Success">  
      <Address AdminDistrict="New Sparta" CountryRegion="Venezuela" FormattedAddress="Del Caribe International Airport, Venezuela" Locality="Díaz"/>  
      <RooftopLocation Latitude="10.9168796539307" Longitude="-63.9689712524414"/>  
      <QueryParseValue Property="Landmark" Value="Ccs-PMV"/>  
      <QueryParseValue Property="CountryRegion" Value="VE"/>  
    </GeocodeResponse>  
    <DataQuality feedAlias="geofeed1"/>  
  </GeocodeEntity>  
  
</GeocodeFeed>  
  
```  
  
### Error Output  

The following location was not geocoded successfully.  
  
```xml
<?xml version="1.0" encoding="utf-8"?>  
<GeocodeFeed xmlns="http://schemas.microsoft.com/search/local/2010/5/geocode" >  
  <GeocodeEntity Id="005" xmlns="http://schemas.microsoft.com/search/local/2010/5/geocode">  
    <GeocodeRequest Culture="en-US">  
      <Address />  
    </GeocodeRequest>  
    <GeocodeResponse StatusCode="BadRequest" FaultReason="To geocode a location, you must specify at least one address field." />  
  </GeocodeEntity>  
</GeocodeFeed>  
  
```  
  
## XML Unstructured Query Input Example

For XML input data, you can also geocode an address without specifying its distinct address parts. The following example shows an unstructured query request.  
  
```xml
<GeocodeFeed >  
  <GeocodeEntity Id="001" xmlns="http://schemas.microsoft.com/search/local/2010/5/geocode">  
    <GeocodeRequest Culture="en-ca" Query=457 Kirkpatrick Crescent NW Edmonton Alberta, Canada T6L">  
    </GeocodeRequest>  
  </GeocodeEntity>  
</GeocodeFeed>  
```  
  
## Pipe (&#124;) Example  
  
### Input  
  
```text
1|en-US||16630 Redmond Way|WA|USA|||Redmond|98052||||||||||||||||||||||  
2|en-US||16552 NE 74th St|WA||||Redmond|||High||||||||||||||||||||||  
3|en-US|Seattle Space Needle||||||||||||||||||||||||||||  
4|en-US|||||||||||||||||||||||||||||  
5|en-US||W Jefferson Blvd|CA||||Los Angeles|90007||||||||||||||||||||||||  
6|en-US|||CA||||Los angeles|||||||||||||||||||||||||  
7|en-ca|Montreal Canada||||||||||||||||||||||||||||  
8|en-CA||444 Kirkpatrick Cres NW|AB|Canada|||Edmonton||||||||||||||||||||||||  
9|en-gb|BD4 9JB||||||||||||||||||||||||||||  
10|en-us||||||||||||||||||||||||||||47.673099|-122.11871  
11|en-ca||||||||||||||||||||||||||||53.48021728|-113.4030925  
12|en-gb||||||||||||||||||||||||||||53.77848387|-1.719561517  
```  
  
### Successful Output  
 The following is an example list of locations that were geocoded successfully.  
  
```text
1|en-US||16630 Redmond Way|WA|USA|||Redmond|98052|||16630 Redmond Way|WA|United States||16630 Redmond Way, Redmond, WA 98052-4434|Redmond|98052-4434||47.673302|-122.118576|47.673099|-122.11871|High|16630 Redmond Way, Redmond, WA 98052-4434|Address|Success|||  
2|en-US||16552 NE 74th St|WA||||Redmond|||High|16552 NE 74th St|WA|United States||16552 NE 74th St, Redmond, WA 98052-7804|Redmond|98052-7804||||47.670211|-122.119581|High|16552 NE 74th St, Redmond, WA 98052-7804|Address|Success|||  
3|en-US|Seattle Space Needle|||||||||||Washington|United States||Space Needle, WA|Seattle|||47.620495|-122.34931|||High|Space Needle, WA|LandmarkBuilding|Success|||  
5|en-US||W Jefferson Blvd|CA||||Los Angeles|90007|||W Jefferson Blvd|CA|United States||W Jefferson Blvd, Los Angeles, CA 90007|Los Angeles|90007||||34.0236140484618|-118.28398661223|High|W Jefferson Blvd, Los Angeles, CA 90007|RoadBlock|Success|||  
6|en-US|||CA||||Los angeles|||||California|United States||Los Angeles, CA|Los Angeles|||34.0532901138067|-118.245009407401|||High|Los Angeles, CA|PopulatedPlace|Success|||  
7|en-ca|Montreal Canada|||||||||||Quebec|Canada||Montreal, QC|Montreal|||45.5122858285904|-73.5543867945671|||High|Montreal, QC|PopulatedPlace|Success|||  
8|en-CA||444 Kirkpatrick Cres NW|AB|Canada|||Edmonton||||444 Kirkpatrick Crescent NW|AB|Canada||444 Kirkpatrick Crescent NW, Edmonton, AB T6L|Edmonton|T6L||||53.4802172766598|-113.403092450204|High|444 Kirkpatrick Crescent NW, Edmonton, AB T6L|Address|Success|||  
9|en-gb|BD4 9JB||||||||||||United Kingdom||BD4 9JB, United Kingdom||BD4 9JB||53.7784838676453|-1.71956151723862|||High|BD4 9JB, United Kingdom|Postcode1|Success|||  
10||||||||||||16630 Redmond Way|WA|United States||16630 Redmond Way, Redmond, WA 98052-4434|Redmond|98052-4434||47.673302|-122.118576|||High|16630 Redmond Way, Redmond, WA 98052-4434|Address|Success||47.673099|-122.11871  
11||||||||||||457 Kirkpatrick Crescent NW|Alberta|Canada||457 Kirkpatrick Crescent NW, Edmonton Alberta, Canada|Edmonton|T6L||||53.4802068024874|-113.403086364269|Medium|457 Kirkpatrick Crescent NW, Edmonton Alberta, Canada|Address|Success||53.48021728|-113.4030925  
12||||||||||||Fern Street|England|United Kingdom||Fern Street, Bradford BD4 9, United Kingdom|Bradford|BD4 9||||53.7784677743912|-1.71975195407867|Medium|Fern Street, Bradford BD4 9, United Kingdom|Address|Success||53.77848387|-1.719561517  
```  
  
### Error Output  
 The following is an example list of locations that were not geocoded successfully.  
  
`
4|en-US||||||||||||||||||||||||||BadRequest|Either Query or Address must be specified.|| `  
  
## Tab Example  
  
> [!NOTE]
>  In the following examples, a tab character is represented by an arrow: `->`.  
  
### Input  
  
```text
1->en-US->->16630 Redmond Way->WA->USA->->->Redmond->98052->->->->->->->->->->->->->->->->->->->->->->->->  
2->en-US->->16552 NE 74th St->WA->->->->Redmond->->->High->->->->->->->->->->->->->->->->->->->->->->  
3->en-US->Seattle Space Needle->->->->->->->->->->->->->->->->->->->->->->->->->->->->  
4->en-US->->->->->->->->->->->->->->->->->->->->->->->->->->->->->  
5->en-US->->W Jefferson Blvd->CA->->->->Los Angeles->90007->->->->->->->->->->->->->->->->->->->->->->->->  
6->en-US->->->CA->->->->Los angeles->->->->->->->->->->->->->->->->->->->->->->->->->  
7->en-ca->Montreal Canada->->->->->->->->->->->->->->->->->->->->->->->->->->->->  
8->en-CA->->444 Kirkpatrick Cres NW->AB->Canada->->->Edmonton->->->->->->->->->->->->->->->->->->->->->->->->  
9->en-gb->BD4 9JB->->->->->->->->->->->->->->->->->->->->->->->->->->->->  
10->en-us->->->->->->->->->->->->->->->->->->->->->->->->->->->->47.673099->-122.11871  
11->en-ca->->->->->->->->->->->->->->->->->->->->->->->->->->->->53.48021728->-113.4030925  
12->en-gb->->->->->->->->->->->->->->->->->->->->->->->->->->->->53.77848387->-1.719561517  
```  
  
### Successful Output  
 The following is an example list of locations that were geocoded successfully.  
  
```text
1->en-US->->16630 Redmond Way->WA->USA->->->Redmond->98052->->->16630 Redmond Way->WA->United States->->16630 Redmond Way, Redmond, WA 98052-4434->Redmond->98052-4434->->47.673302->-122.118576->47.673099->-122.11871->High->16630 Redmond Way, Redmond, WA 98052-4434->Address->Success->->->  
2->en-US->->16552 NE 74th St->WA->->->->Redmond->->->High->16552 NE 74th St->WA->United States->->16552 NE 74th St, Redmond, WA 98052-7804->Redmond->98052-7804->->->->47.670211->-122.119581->High->16552 NE 74th St, Redmond, WA 98052-7804->Address->Success->->->  
3->en-US->Seattle Space Needle->->->->->->->->->->->Washington->United States->->Space Needle, WA->Seattle->->->47.620495->-122.34931->->->High->Space Needle, WA->LandmarkBuilding->Success->->->  
5->en-US->->W Jefferson Blvd->CA->->->->Los Angeles->90007->->->W Jefferson Blvd->CA->United States->->W Jefferson Blvd, Los Angeles, CA 90007->Los Angeles->90007->->->->34.0236140484618->-118.28398661223->High->W Jefferson Blvd, Los Angeles, CA 90007->RoadBlock->Success->->->  
6->en-US->->->CA->->->->Los angeles->->->->->California->United States->->Los Angeles, CA->Los Angeles->->->34.0532901138067->-118.245009407401->->->High->Los Angeles, CA->PopulatedPlace->Success->->->  
7->en-ca->Montreal Canada->->->->->->->->->->->Quebec->Canada->->Montreal, QC->Montreal->->->45.5122858285904->-73.5543867945671->->->High->Montreal, QC->PopulatedPlace->Success->->->  
8->en-CA->->444 Kirkpatrick Cres NW->AB->Canada->->->Edmonton->->->->444 Kirkpatrick Crescent NW->AB->Canada->->444 Kirkpatrick Crescent NW, Edmonton, AB T6L->Edmonton->T6L->->->->53.4802172766598->-113.403092450204->High->444 Kirkpatrick Crescent NW, Edmonton, AB T6L->Address->Success->->->  
9->en-gb->BD4 9JB->->->->->->->->->->->->United Kingdom->->BD4 9JB, United Kingdom->->BD4 9JB->->53.7784838676453->-1.71956151723862->->->High->BD4 9JB, United Kingdom->Postcode1->Success->->->  
10->->->->->->->->->->->->16630 Redmond Way->WA->United States->->16630 Redmond Way, Redmond, WA 98052-4434->Redmond->98052-4434->->47.673302->-122.118576->->->High->16630 Redmond Way, Redmond, WA 98052-4434->Address->Success->->47.673099->-122.11871  
11->->->->->->->->->->->->457 Kirkpatrick Crescent NW->Alberta->Canada->->457 Kirkpatrick Crescent NW, Edmonton Alberta, Canada->Edmonton->T6L->->->->53.4802068024874->-113.403086364269->Medium->457 Kirkpatrick Crescent NW, Edmonton Alberta, Canada->Address->Success->->53.48021728->-113.4030925  
12->->->->->->->->->->->->Fern Street->England->United Kingdom->->Fern Street, Bradford BD4 9, United Kingdom->Bradford->BD4 9->->->->53.7784677743912->-1.71975195407867->Medium->Fern Street, Bradford BD4 9, United Kingdom->Address->Success->->53.77848387->-1.719561517  
  
```  
  
### Error Output  
 The following is an example list of locations that were not geocoded successfully.  
  
```text
4->en-US->->->->->->->->->->->->->->->->->->->->->->->->->->BadRequest->Either Query or Address must be specified.->->->->->->->->->->->->->->->->->->->->->BadRequest->The Address.FormattedAddress property must not be specified as it is an output-only property.->->  
```  
  
## CSV (comma-separated-value) Example  
  
### Input  
  
```csv
1,en-US,,16630 Redmond Way,WA,USA,,,Redmond,98052,,,,,,,,,,,,,,,,,,,,,,  
2,en-US,,16552 NE 74th St,WA,,,,Redmond,,,High,,,,,,,,,,,,,,,,,,,,,,  
3,en-US,Seattle Space Needle,,,,,,,,,,,,,,,,,,,,,,,,,,,,  
4,en-US,,,,,,,,,,,,,,,,,,,,,,,,,,,,,  
5,en-US,,W Jefferson Blvd,CA,,,,Los Angeles,90007,,,,,,,,,,,,,,,,,,,,,,,,  
6,en-US,,,CA,,,,Los angeles,,,,,,,,,,,,,,,,,,,,,,,,,  
7,en-ca,Montreal Canada,,,,,,,,,,,,,,,,,,,,,,,,,,,,  
8,en-CA,,444 Kirkpatrick Cres NW,AB,Canada,,,Edmonton,,,,,,,,,,,,,,,,,,,,,,,,  
9,en-gb,BD4 9JB,,,,,,,,,,,,,,,,,,,,,,,,,,,,  
10,en-us,,,,,,,,,,,,,,,,,,,,,,,,,,,,47.673099,-122.11871  
11,en-ca,,,,,,,,,,,,,,,,,,,,,,,,,,,,53.48021728,-113.4030925  
12,en-gb,,,,,,,,,,,,,,,,,,,,,,,,,,,,53.77848387,-1.719561517  
```  
  
### Successful Output  
 The following is an example list of locations that were geocoded successfully.  
  
```csv
1,en-US,,16630 Redmond Way,WA,USA,,,Redmond,98052,,,16630 Redmond Way,WA,United States,,"16630 Redmond Way, Redmond, WA 98052-4434",Redmond,98052-4434,,47.673302,-122.118576,47.673099,-122.11871,High,"16630 Redmond Way, Redmond, WA 98052-4434",Address,Success,,,  
2,en-US,,16552 NE 74th St,WA,,,,Redmond,,,High,16552 NE 74th St,WA,United States,,"16552 NE 74th St, Redmond, WA 98052-7804",Redmond,98052-7804,,,,47.670211,-122.119581,High,"16552 NE 74th St, Redmond, WA 98052-7804",Address,Success,,,  
3,en-US,Seattle Space Needle,,,,,,,,,,,Washington,United States,,"Space Needle, WA",Seattle,,,47.620495,-122.34931,,,High,"Space Needle, WA",LandmarkBuilding,Success,,,  
5,en-US,,W Jefferson Blvd,CA,,,,Los Angeles,90007,,,W Jefferson Blvd,CA,United States,,"W Jefferson Blvd, Los Angeles, CA 90007",Los Angeles,90007,,,,34.0236140484618,-118.28398661223,High,"W Jefferson Blvd, Los Angeles, CA 90007",RoadBlock,Success,,,  
6,en-US,,,CA,,,,Los angeles,,,,,California,United States,,"Los Angeles, CA",Los Angeles,,,34.0532901138067,-118.245009407401,,,High,"Los Angeles, CA",PopulatedPlace,Success,,,  
7,en-ca,Montreal Canada,,,,,,,,,,,Quebec,Canada,,"Montreal, QC",Montreal,,,45.5122858285904,-73.5543867945671,,,High,"Montreal, QC",PopulatedPlace,Success,,,  
8,en-CA,,444 Kirkpatrick Cres NW,AB,Canada,,,Edmonton,,,,444 Kirkpatrick Crescent NW,AB,Canada,,"444 Kirkpatrick Crescent NW, Edmonton, AB T6L",Edmonton,T6L,,,,53.4802172766598,-113.403092450204,High,"444 Kirkpatrick Crescent NW, Edmonton, AB T6L",Address,Success,,,  
9,en-gb,BD4 9JB,,,,,,,,,,,,United Kingdom,,"BD4 9JB, United Kingdom",,BD4 9JB,,53.7784838676453,-1.71956151723862,,,High,"BD4 9JB, United Kingdom",Postcode1,Success,,,  
10,,,,,,,,,,,,16630 Redmond Way,WA,United States,,"16630 Redmond Way, Redmond, WA 98052-4434",Redmond,98052-4434,,47.673302,-122.118576,,,High,"16630 Redmond Way, Redmond, WA 98052-4434",Address,Success,,47.673099,-122.11871  
11,,,,,,,,,,,,457 Kirkpatrick Crescent NW,Alberta,Canada,,"457 Kirkpatrick Crescent NW, Edmonton Alberta, Canada",Edmonton,T6L,,,,53.4802068024874,-113.403086364269,Medium,"457 Kirkpatrick Crescent NW, Edmonton Alberta, Canada",Address,Success,,53.48021728,-113.4030925  
12,,,,,,,,,,,,Fern Street,England,United Kingdom,,"Fern Street, Bradford BD4 9, United Kingdom",Bradford,BD4 9,,,,53.7784677743912,-1.71975195407867,Medium,"Fern Street, Bradford BD4 9, United Kingdom",Address,Success,,53.77848387,-1.719561517  
```  
  
### Error Output  
 The following is an example list of locations that were not geocoded successfully.  
  
```csv
4,en-US,,,,,,,,,,,,,,,,,,,,,,,,,,BadRequest,Either Query or Address must be specified.,,  
```