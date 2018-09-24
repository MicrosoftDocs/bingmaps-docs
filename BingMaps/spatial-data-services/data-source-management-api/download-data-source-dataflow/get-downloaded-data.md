---
title: "Get Downloaded Data | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 56e9e140-3b14-44b1-adbf-c3a73bb2822b
caps.latest.revision: 6
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Get Downloaded Data
A download URL is returned in the job status response when download job has completed. Use this download URL to access the downloaded entity data.  
  
 Your job has completed when the `Status` field in the response is set to `Completed`. The download URL is specified as an XML `Link` value, or as part of a JSON `links` collection. These links have a `role` attribute set to `output` and the `name` attribute and set to `succeeded`.  
  
 **XML**  
  
```  
<Link role="output" name="succeeded">https://spatial.virtualearth.net/REST/v1/dataflows/Download/MyDataSourceName/output/succeeded</Link>  
  
```  
  
 **JSON**  
  
```  
"links":[  
      {  
         "name":"succeeded",  
         "role":"output",  
         "url":"https:\/\/spatial.virtualearth.net\/REST\/v1\/dataflows\/DataSourceDownload\/MyDataSourceName\/output\/succeeded"  
      }  
]  
  
```  
  
 To download the entity data, you must add the master key for the data source to the download URL.  
  
```  
https://spatial.virtualearth.net/REST/v1/dataflows/DataSourceDownload/MyDataSourceName/output/succeeded?key=DataSourceMasterKey  
```  
  
 **Example of Downloaded Entity Data**  
  
 The following shows and example of downloaded entity data.  
  
```  
<?xml version="1.0" encoding="UTF-8" ?>  
<MainRoot>  
  <xs:schema xmlns="" xmlns:xs="https://www.w3.org/2001/XMLSchema" xmlns:msdata="urn:schemas-microsoft-com:xml-msdata" id="MyDataSourceName">  
    <xs:element name="MyDataSourceName" msdata:IsDataSet="true" msdata:UseCurrentLocale="true">  
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
</MainRoot>  
```  
  
 For information about the Download Data Source data schema, see [Response Data](../../data-source-management-api/download-data-source-dataflow/download-data-source-dataflow-response-description.md).  
  
 For a step-by-step description of how use the Download Data Source Dataflow, see [Walkthrough](../../data-source-management-api/download-data-source-dataflow/download-data-source-walkthrough.md).