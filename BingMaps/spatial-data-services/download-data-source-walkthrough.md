---
title: "Download Data Source Walkthrough | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: e2a1a875-80e8-43fd-80c0-ad603f87033a
caps.latest.revision: 9
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Download Data Source Walkthrough
Use the DataSourceDownload API to download entity data for a published data source.  
  
> [!NOTE]
>  Both HTTP and HTTPS protocols are supported.  
  
### Create the Download Data Source Job  
 To start the download process, create a DataSourceDownload URL request using the following format.  
  
```  
https://spatial.virtualearth.net/REST/v1/Dataflows/DataSourceDownload/accessId/DataSourceName?output=xml&key=DataSourceMasterKey  
```  
  
 When you make the download request, the response provides the ID and status of the download job, and a status URL. The status URL is specified in the `Link` element with the `role` attribute set to `self`.  The Link and status URL fields are highlighted in the following response example.  
  
 Note that the job status is set to Pending. Job status values include Pending, Completed and Aborted. The next section describes how to use the status URL to monitor job status and to get the location of the downloaded entity data.  
  
```  
<Response xmlns:xsi="https://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://schemas.microsoft.com/search/local/ws/rest/v1">  
  <Copyright>Copyright © 2011 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the  
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
        <DownloadJob>  
          <Id>e14b1d9bd65c4b9d99d267bbb8102ccf</Id>  
          <Link role="self">https://spatial.virtualearth.net/REST/v1/dataflows/DataSourceDownload/DataSourceName</Link>  
          <Description></Description>  
          <Status>Pending</Status>  
          <CreatedDate>2011-11-09T15:15:51.8326153-08:00</CreatedDate>  
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
  
## Check Job Status  
 To monitor the status of your download job, use the status URL described in the previous section with your data source master key.  
  
```  
https://spatial.virtualearth.net/REST/v1/dataflows/DataSourceDownload/DataSourceName?output=xml&key=DataSourceMasterKey  
```  
  
 When the status is set to `Completed`, a download URL appears in the response.  The download URL is specified as a `Link` field with the `role` attribute set to `output` and the `name` attribute set to `succeeded`.  
  
 The following response shows that the job is completed and specifies a download URL.  These fields are highlighted. The next section describes the download data and how to access it.  
  
```  
<Response xmlns:xsi="https://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://schemas.microsoft.com/search/local/ws/rest/v1">  
  <Copyright>Copyright © 2011 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the   
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
          <Link role="self">https://spatial.virtualearth.net/REST/v1/dataflows/DataSourceDownload/DataSourceName</Link>  
          <Link role="output" name="succeeded">https://spatial.virtualearth.net/REST/v1/dataflows/DataSourceDownload/DataSourceName/output/succeeded</Link>  
          <Description></Description>  
          <Status>Completed</Status>  
          <CreatedDate>2011-11-08T16:35:00.2429749-08:00</CreatedDate>  
          <CompletedDate>2011-11-08T16:44:00.9349209-08:00</CompletedDate>  
          <TotalEntityCount>2</TotalEntityCount>  
          <ProcessedEntityCount>0</ProcessedEntityCount>  
          <FailedEntityCount>0</FailedEntityCount>  
        </DataflowJob>  
      </Resources>  
    </ResourceSet>  
  </ResourceSets>  
</Response>  
```  
  
 If your job status is `Aborted`, then the job ended due to an error and an `ErrorMessage` element appears in the response and contains error information.  
  
## Get the downloaded data  
 To access the downloaded entity data, use the download URL described in the previous section with the data source master key.  
  
```  
https://spatial.virtualearth.net/REST/v1/dataflows/DataSourceDownload/DataSourceName/output/succeeded?key=DataSourceMasterKey  
```  
  
 The downloaded data includes the data schema and a set of entity data that matches that schema in XML format. XML is the only option for downloaded entity data.  
  
 The following sample data is an example of downloaded entity data.  
  
```  
<?xml version="1.0" encoding="UTF-8" ?>  
<MainRoot>  
  <xs:schema xmlns="" xmlns:xs="https://www.w3.org/2001/XMLSchema" xmlns:msdata="urn:schemas-microsoft-com:xml-msdata" id="DataSourceName">  
    <xs:element name="DataSourceName" msdata:IsDataSet="true" msdata:UseCurrentLocale="true">  
      <xs:complexType>  
        <xs:choice minOccurs="0" maxOccurs="unbounded">  
          <xs:element name="MyDataSourceEntityType">  
            <xs:complexType>  
              <xs:sequence>  
                <xs:element name="EntityID" type="xs:string" minOccurs="0"/>  
                <xs:element name="Latitude" type="xs:double" minOccurs="0"/>  
                <xs:element name="Longitude" type="xs:double" minOccurs="0"/>  
                <xs:element name="AddressLine" type="xs:string" minOccurs="0"/>  
                <xs:element name="Locality" type="xs:string" minOccurs="0"/>  
                <xs:element name="AdminDistrict" type="xs:string" minOccurs="0"/>  
                <xs:element name="CountryRegion" type="xs:string" minOccurs="0"/>  
                <xs:element name="PostalCode" type="xs:string" minOccurs="0"/>  
                <xs:element name="Confidence" type="xs:string" minOccurs="0"/>  
                <xs:element name="Phone" type="xs:string" minOccurs="0"/>  
                <xs:element name="Open" type="xs:long" minOccurs="0"/>  
                <xs:element name="Close" type="xs:long" minOccurs="0"/>  
                <xs:element name="IsWheelchairAccessible" type="xs:boolean" minOccurs="0" />  
              </xs:sequence>  
            </xs:complexType>  
          </xs:element>  
        </xs:choice>  
      </xs:complexType>  
      <xs:unique name="Constraint1" msdata:PrimaryKey="true">  
        <xs:selector xpath=".//MyDataSourceEntityType"/>  
        <xs:field xpath="EntityID"/>  
      </xs:unique>  
    </xs:element>  
  </xs:schema>  
  <MyDataSourceEntityType>  
    <EntityID>1</EntityID>  
    <Latitude>47.673302</Latitude>  
    <Longitude>-122.118576</Longitude>  
    <AddressLine>1 Microsoft Way</AddressLine>  
    <Locality>Redmond</Locality>  
    <AdminDistrict>WA</AdminDistrict>  
    <CountryRegion>United States</CountryRegion>  
    <PostalCode>98052</PostalCode>  
    <Confidence>High</Confidence>  
    <Phone>303-555-0188</Phone>  
    <Open>700</Open>  
    <Close>1800</Close>  
    <IsWheelchairAccessible>true</IsWheelchairAccessible>  
  </MyDataSourceEntityType>  
  <MyDataSourceEntityType>  
    <EntityID>2</EntityID>  
    <Latitude>34.023614</Latitude>  
    <Longitude>-118.28398</Longitude>  
    <AddressLine>W Jefferson Blvd</AddressLine>  
    <Locality>Los Angeles</Locality>  
    <AdminDistrict>CA</AdminDistrict>  
    <CountryRegion>United States</CountryRegion>  
    <PostalCode>90007</PostalCode>  
    <Confidence>Medium</Confidence>  
    <Phone>303-555-0188</Phone>  
    <Open>700</Open>  
    <Close>1800</Close>  
    <IsWheelchairAccessible>false</IsWheelchairAccessible>  
  </MyDataSourceEntityType>  
</MainRoot>  
```