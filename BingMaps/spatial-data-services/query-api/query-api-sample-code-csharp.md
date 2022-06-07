---
title: "Query API Sample Code (C#) | Microsoft Docs"
description: "The Query API Sample Code, written in C#, provides examples of how to query a data source using the Query API."
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: c36505f5-5534-4d12-88c8-5dd8fa698fb3
caps.latest.revision: 5
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Query API Sample Code (C#)

The following C# code provides examples of how to query a data source using the [Query API](../query-api/index.md).  
  
```csharp
using System;  
using System.Net;  
using System.Xml;  
namespace QueryAPIExamples  
{  
  /// <summary>  
  /// Using the Spatial Data Services Query API to query the test data source FourthCoffeeSample  
  /// </summary>  
  public class SpatialDataQuerying  
  {  
  
   string BingMapsKey = "InsertYourBngMapsKeyHere";  
  
   string DataSourceID = "20181f26d9e94c81acdf9496133d4f23";  
   static void Main()  
   {  
       SpatialDataQuerying queryTest = new SpatialDataQuerying();  
       queryTest.RunExampleQueries();  
       Console.ReadLine();  
  
   }  
  
   #region Run the Queries  
  
    /// <summary>  
    /// Run the Bing Spatial Data Query examples in this class.  
    /// Requires the spatial data to already be uploaded.  
    /// </summary>  
    public void RunExampleQueries()  
    {  
      ExampleFindByAreaRadius();  
      ExampleFindByBoundingBox();  
      ExampleFindByProperty();  
      ExampleQueryByIdAtom();  
     // ExampleQueryByIdJson();  
    }  
    #endregion   
  
    #region Query By Area  
    public void ExampleFindByAreaRadius()  
    {  
       Console.WriteLine("\nExampleFindByAreaRadius");  
  
      // Find all previously uploaded MyShops entities located within  
      // a certain radius around a point.  
      // Custom name of spatial data source created during upload  
      string dataSourceName = "FourthCoffeeSample";  
      // Name of entities in the data source  
      string dataEntityName = "FourthCoffeeShops";  
      // Unique access ID assigned to your data source by Bing Maps  
      // e.g. f8986xxxxxxxc844b  
      string accessId = DataSourceID;  
      // Your Bing Maps Spatial Data Services query key.  
      string bingMapsKey = BingMapsKey;  
      // Coordinates of the point to search from.  
      double SearchLatitude = 47.63674;  
      double SearchLongitude =  - 122.30413;  
      // Search radius  
      double Radius = 3; // km  
      // Setup REST request to query our uploaded customer data  
      string requestUrl = string.Format("http://spatial.virtualearth.net/REST/v1/data/{0}/{1}/{2}" +   
        "?spatialFilter=nearby({3},{4},{5})&key={6}",accessId,dataSourceName,  
        dataEntityName,SearchLatitude, SearchLongitude, Radius, bingMapsKey);  
      // Send the request and get back an XML response.  
      XmlDocument response = GetXmlResponse(requestUrl);  
      // Display each entity's info.  
      ProcessEntityElements(response);  
    }  
    #endregion   
  
    #region Helper Methods  
  
    public static XmlDocument GetXmlResponse(string requestUrl)  
    {  
        try  
        {  
            HttpWebRequest request = WebRequest.Create(requestUrl) as HttpWebRequest;  
            HttpWebResponse response = request.GetResponse() as HttpWebResponse;  
  
            XmlDocument xmlDoc = new XmlDocument();  
            xmlDoc.Load(response.GetResponseStream());  
            return (xmlDoc);  
  
        }  
        catch (Exception e)  
        {  
            Console.WriteLine(e.Message);  
  
            Console.Read();  
            return null;  
        }  
    }  
  
    /// <summary>  
    /// Display each "entry" in the Bing Spatial Data Services Atom (XML) response.  
    /// </summary>  
    /// <param name="entryElements"></param>  
    private void ProcessEntityElements(XmlDocument response)  
    {  
      XmlNodeList entryElements = response.GetElementsByTagName("entry");  
      for (int i = 0; i <= entryElements.Count - 1; i++)  
      {  
        XmlElement element = (XmlElement)entryElements[i];  
        XmlElement contentElement = (XmlElement)element.GetElementsByTagName(  
          "content")[0];  
        XmlElement propElement = (XmlElement)  
          contentElement.GetElementsByTagName("m:properties")[0];  
        XmlNode nameElement = propElement.GetElementsByTagName("d:Name")[0];  
        if (nameElement == null)  
          throw new Exception("Name not found");  
        XmlNode latElement = propElement.GetElementsByTagName("d:Latitude")[0];  
        if (latElement == null)  
          throw new Exception("Latitude not found");  
        XmlNode longElement = propElement.GetElementsByTagName("d:Longitude")  
          [0];  
        if (longElement == null)  
          throw new Exception("Longitude not found");  
        string name = nameElement.InnerText;  
        double latitude = 0;  
        Double.TryParse(latElement.InnerText, out latitude);  
        double longitude = 0;  
        Double.TryParse(longElement.InnerText, out longitude);  
        Console.WriteLine("Coordinates of '{0}': {1}, {2}", name, latitude,  
          longitude);  
      }  
    }  
    #endregion  
  
    #region Query by Property  
    public void ExampleFindByProperty()  
    {  
        Console.WriteLine("\nExampleFindByProperty");  
      // Find all previously uploaded MyShops entities that accept  
      // online orders.  
      // Custom name of spatial data source created during upload  
      string dataSourceName = "FourthCoffeeSample";  
      // Name of entities in the data source  
      string dataEntityName = "FourthCoffeeShops";  
      // Unique access ID assigned to your data source by Bing Maps  
      // e.g. f8986xxxxxxxc844b  
      string accessId = DataSourceID;  
      // Your Bing Maps Spatial Data Services query key.  
      string bingMapsKey = BingMapsKey;  
      // Setup REST request to query our uploaded customer data  
      string requestUrl = String.Format(  
        "http://spatial.virtualearth.net/REST/v1/data/{0}/{1}/{2}" +   
        "?$filter=AcceptsOnlineOrders Eq True&key={3}", accessId,  
        dataSourceName, dataEntityName, bingMapsKey);  
      // Send the request and get back an XML response.  
      XmlDocument response = GetXmlResponse(requestUrl);  
      // Display each entity's info.  
      ProcessEntityElements(response);  
    }  
    #endregion   
  
    #region Query by Bounding Box  
    public void ExampleFindByBoundingBox()  
    {  
        Console.WriteLine("\nExampleFindByBoundingBox");  
      // Find all previously uploaded MyShops entities located within  
      // the specified bounding box.  
      // Custom name of spatial data source created during upload  
        string dataSourceName = "FourthCoffeeSample";  
        // Name of entities in the data source  
        string dataEntityName = "FourthCoffeeShops";  
      // Unique access ID assigned to your data source by Bing Maps  
      // e.g. f8986xxxxxxxc844b  
      string accessId = DataSourceID;  
      // Your Bing Maps Spatial Data Services query key.  
      string bingMapsKey = BingMapsKey;  
      // Coordinates of the bounding box's corners  
      double lat1 = 47.61247675940658;  
      double long1 =  - 122.3237670214032;  
      double lat2 = 47.68239156080077;  
      double long2 =  - 122.27996173131822;  
      // Setup REST request to query our uploaded customer data  
      string requestUrl = String.Format(  
        "http://spatial.virtualearth.net/REST/v1/data/{0}/{1}/{2}" +   
        "?spatialFilter=bbox({3},{4},{5},{6})&key={7}", accessId,  
        dataSourceName, dataEntityName, lat1, long1, lat2, long2, bingMapsKey);  
      // Send the request and get back an XML response.  
      XmlDocument response = GetXmlResponse(requestUrl);  
      // Display each entity's info.  
      ProcessEntityElements(response);  
    }  
    #endregion   
  
    #region Query By ID  
    /// <summary>  
    /// Query by ID using ATOM protocol  
    /// </summary>  
    public void ExampleQueryByIdAtom()  
    {  
        Console.WriteLine("\nExampleQueryByIdAtom");  
      // http://spatial.virtualearth.net/REST/v1/data/accessId/dataSourceName/entityTypeName('entityId')?key=queryKey  
      // http://spatial.virtualearth.net/REST/v1/data/f8986xxxxxxxc844b/MyShopsSample/MyShops('1')?key=queryKey  
      // Custom name of spatial data source created during upload  
     string dataSourceName = "FourthCoffeeSample";  
      // Name of entities in the data source  
      string dataEntityName = "FourthCoffeeShops";  
      // Unique access ID assigned to your data source by Bing Maps  
      // e.g. f8986xxxxxxxc844b  
      string accessId = DataSourceID;  
      // ID of the entity to search for  
      int entityId = -22067;  
      // Your Bing Maps Spatial Data Services query key.  
      string bingMapsKey = BingMapsKey;  
      string requestUrl = string.Format("http://spatial.virtualearth.net" +   
        "/REST/v1/data/{0}/{1}/{2}('{3}')?key={4}", accessId, dataSourceName,  
        dataEntityName, entityId, bingMapsKey);  
      // By default, the Spatial Data API returns  
      // data responses in Atom (xml) format.  
      XmlDocument xmlResponse = GetXmlResponse(requestUrl);  
      // Select the first shop data in the xml results.  
      XmlNamespaceManager nsmgr = new XmlNamespaceManager(xmlResponse.NameTable);  
      nsmgr.AddNamespace("a", "http://www.w3.org/2005/Atom");  
      nsmgr.AddNamespace("m",   
        "http://schemas.microsoft.com/ado/2007/08/dataservices/metadata");  
      nsmgr.AddNamespace("d",   
        "http://schemas.microsoft.com/ado/2007/08/dataservices");  
      XmlNode firstShopNode = xmlResponse.SelectSingleNode(  
        "//a:entry/a:content/m:properties", nsmgr);  
      // Extract result data from the xml nodes.  
      int retrievedEntityId = int.Parse(firstShopNode.SelectSingleNode(  
        "d:EntityID", nsmgr).FirstChild.Value);  
      string postalCode = firstShopNode.SelectSingleNode(  
        "d:PostalCode", nsmgr).FirstChild.Value;  
      double latitude = double.Parse(firstShopNode.SelectSingleNode(  
        "d:Latitude", nsmgr).FirstChild.Value);  
      double longitude = double.Parse(firstShopNode.SelectSingleNode(  
        "d:Longitude", nsmgr).FirstChild.Value);  
      Console.WriteLine(string.Format("Found EntityID {0} Postal Code: {1} Lat,Lon:  ({2},{3})",   
          retrievedEntityId,postalCode, latitude, longitude));  
    }  
  
    #endregion;  
  
  }  
}  
  
```