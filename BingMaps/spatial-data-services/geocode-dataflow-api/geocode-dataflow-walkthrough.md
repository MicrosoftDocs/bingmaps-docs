---
title: "Geocode Dataflow Walkthrough | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 6cf02921-9035-48c2-a954-3d468565aea6
caps.latest.revision: 22
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Geocode Dataflow Walkthrough

The following steps show how to use  the Geocode Dataflow API and version 2.0 of the Geocode Dataflow data schema to geocode large sets of spatial data.  
  
## Uploading Your Spatial Data  
  
### Format the data  
 To create a job to geocode a set of spatial data using version 2.0 of the Geocode Dataflow schema, your input data must conform to the [Data Schema  v2.0](../geocode-dataflow-api/geocode-dataflow-data-schema-version-2-0.md) and be specified using XML format, or as text strings delimited by the comma, tab, or pipe (&#124;) character.  
  
 The following is an XML example that contains data to geocode. You can find examples in other formats in [Sample Input and Output v2.0](../geocode-dataflow-api/geocode-dataflow-sample-input-and-output-data-version-2-0.md).  
  
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
    <GeocodeEntity Id="006"  xmlns="http://schemas.microsoft.com/search/local/2010/5/geocode" >  
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
  
### Upload the data and create the geocode job  
 To geocode the data, upload the data and create a geocode job by using a REST URL and HTTP POST protocol. The following shows an example. For more information, see [Create Job](../geocode-dataflow-api/create-a-geocode-job-and-upload-data.md).  
  
> [!NOTE]
>  Both HTTP and HTTPS protocols are supported. The HTTPS protocol is recommended for geocode jobs that require you to secure your information.  
  
```url
http://spatial.virtualearth.net/REST/v1/Dataflows/Geocode?description=Geocode%20Demo&input=xml&output=xml&key=YourBingMapsKey  
```  
  
 When you make this request, the response includes a `DataflowJob` resource. This resource contains a set `Link` elements that define URLs. When you initiate a job, the response you receive contains a URL that you can use to get job status. After the job has completed, additional URLs are provided to download the geocoded results. The following response includes a URL for getting status as described in the next section. For more information about the `DataflowJob` resource, see [Response Data](../geocode-dataflow-api/geocode-dataflow-response-description.md).  
  
```xml
<Response xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://schemas.microsoft.com/search/local/ws/rest/v1">  
  <Copyright>Copyright © 2010 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the  
 content and any results may not be used, reproduced or transmitted in any manner without express written permission  
 from Microsoft Corporation.</Copyright>  
  <BrandLogoUri>http://spatial.virtualearth.net/Branding/logo_powered_by.png</BrandLogoUri>  
  <StatusCode>201</StatusCode>  
  <StatusDescription>Created</StatusDescription>  
  <AuthenticationResultCode>ValidCredentials</AuthenticationResultCode>  
  <TraceId>b1aae77f9b9145ffa87d97d7d405cffd</TraceId>  
  <ResourceSets>  
    <ResourceSet>  
      <EstimatedTotal>1</EstimatedTotal>  
      <Resources>  
        <DataflowJob>  
          <Id>e14b1d9bd65c4b9d99d267bbb8102ccf</Id>  
          <Link role="self">https://spatial.virtualearth.net/REST/v1/dataflows/geocode/e14b1d9bd65c4b9d99d267bbb8102ccf</Link>  
          <Description>Geocode Demo</Description>  
          <Status>Pending</Status>  
          <CreatedDate>2010-03-09T15:15:51.8326153-08:00</CreatedDate>  
          <CompletedDate xsi:nil="true" />  
          <TotalEntityCount>0</TotalEntityCount>  
          <ProcessedEntityCount>0</ProcessedEntityCount>  
          <FailedEntityCount>0</FailedEntityCount>  
        </DataflowJob>  
      </Resources>  
    </ResourceSet>  
  </ResourceSets>  
</Response>  
```  
  
## Checking Job Status  
 To find out the status of a geocode job, use the URL provided by `Link` element with the `role` attribute set to `self`. You must append the Bing Maps Key that you used to create the job to the URL to use it. For more information, see [Get Job Status](../geocode-dataflow-api/get-status-of-a-geocode-job.md).  
  
 Based on the example response above, you would make the following URL request to get job status. The job status is defined by the `Status` field. Continue to check status until it shows that the job has `Completed`. Then you can download the results as described in the next section.  
  
```url
https://spatial.virtualearth.net/REST/v1/dataflows/geocode/e14b1d9bd65c4b9d99d267bbb8102ccf?key=YourBingMapsKey  
```  
  
```xml
<Response xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://schemas.microsoft.com/search/local/ws/rest/v1">  
  <Copyright>Copyright © 2010 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the   
content and any results may not be used, reproduced or transmitted in any manner without express written permission   
from Microsoft Corporation.</Copyright>  
  <BrandLogoUri>http://spatial.virtualearth.net/Branding/logo_powered_by.png</BrandLogoUri>  
  <StatusCode>200</StatusCode>  
  <StatusDescription>OK</StatusDescription>  
  <AuthenticationResultCode>ValidCredentials</AuthenticationResultCode>  
  <TraceId>2a4fcb1fd1274497ab8ed84955012264</TraceId>  
  <ResourceSets>  
    <ResourceSet>  
      <EstimatedTotal>1</EstimatedTotal>  
      <Resources>  
        <DataflowJob>  
          <Id>e14b1d9bd65c4b9d99d267bbb8102ccf</Id>  
          <Link role="self">https://spatial.virtualearth.net/REST/v1/dataflows/geocode/e14b1d9bd65c4b9d99d267bbb8102ccf</Link>  
          <Link role="output" name="succeeded">https://spatial.virtualearth.net/REST/v1/dataflows/geocode/e14b1d9bd65c4b9d99d267bbb8102ccf/output/succeeded</Link>  
          <Link role="output" name="failed">https://spatial.virtualearth.net/REST/v1/dataflows/geocode/e14b1d9bd65c4b9d99d267bbb8102ccf/output/failed</Link>  
          <Description>Geocode Job 1</Description>  
          <Status>Completed</Status>  
          <CreatedDate>2010-03-08T16:35:00.2429749-08:00</CreatedDate>  
          <CompletedDate>2010-03-08T16:44:00.9349209-08:00</CompletedDate>  
          <TotalEntityCount>6</TotalEntityCount>  
          <ProcessedEntityCount>6</ProcessedEntityCount>  
          <FailedEntityCount>0</FailedEntityCount>  
        </DataflowJob>  
      </Resources>  
    </ResourceSet>  
  </ResourceSets>  
</Response>  
```  
  
 If your job status is `Aborted`, then the job ended due to an error and an `ErrorMessage` element appears in the response and contains error information.  
  
## Downloading Results  
 When the status of your job is `Completed`, you can download the results of the geocode job. The results are available for download for fourteen (14) calendar days. The `Link` URLs to use are identified by their `name` attribute and are set to `succeeded` and `failed`. A succeeded or failed Link URL only appears in the response if there is corresponding data to download. For example, if all the data was geocoded successfully, a failed Link URL does not appear. To download data, you must append the Bing Maps Key that you used to create the job to the download URLs.  
  
 The following show the download URLs and the geocoded data for this example.  
  
 **URL (name=succeeded)**  
  
```url
https://spatial.virtualearth.net/REST/v1/dataflows/geocode/e14b1d9bd65c4b9d99d267bbb8102ccf/output/succeeded?key={BingMapsKey}  
```  
  
 **Successful Geocode Results**  
  
```xml
<?xml version="1.0" encoding="utf-8"?>  
<GeocodeFeed Version="2.0" xmlns="http://schemas.microsoft.com/search/local/2010/5/geocode" >  
  <GeocodeEntity Id="010">  
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
    <TraceId>f2deda5c9fd04e41a3ead1907bcdd7d9</TraceId>  
  </GeocodeEntity>  
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
  
 **URL (name=failed)**  
  
```url
https://spatial.virtualearth.net/REST/v1/dataflows/geocode/e14b1d9bd65c4b9d99d267bbb8102ccf/output/failed?key={BingMapsKey}  
```  
  
 **Failed Geocode Results**  
  
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