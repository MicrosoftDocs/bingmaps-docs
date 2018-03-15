---
title: "Query API Sample Code (VB) | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: b7e1fbaa-d268-48ad-abc5-1a794461a4ec
caps.latest.revision: 5
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms:service: "bing-maps"
---
# Query API Sample Code (VB)
The following Visual Basic code provides examples of how to query a data source using the [Query API](../spatial-data-services/query-api.md).  
  
```  
Imports System  
Imports System.Net  
Imports System.Xml  
Imports Microsoft.VisualBasic  
''' <summary>  
''' Using the Spatial Data Services Query API to query the test data source FourthCoffeeSample  
''' </summary>  
Public Class SpatialDataQuerying  
  
    Private MyKey As String = "InsertYourBingMapsKey"  
  
    Private DataSourceID As String = "20181f26d9e94c81acdf9496133d4f23"  
  
#Region "Run the Queries"  
  
    ''' <summary>  
    ''' Run the Bing Spatial Data Query examples in this class.  
    ''' Requires the spatial data to already be uploaded.  
    ''' </summary>  
    Public Sub RunExampleQueries()  
        ExampleFindByAreaRadius()  
        ExampleFindByBoundingBox()  
        ExampleFindByProperty()  
        ExampleQueryByIdAtom()  
        ' ExampleQueryByIdJson();  
    End Sub  
#End Region  
  
#Region "Query By Area"  
    Public Sub ExampleFindByAreaRadius()  
        Console.WriteLine(vbLf & "ExampleFindByAreaRadius")  
  
        ' Find all previously uploaded MyShops entities located within  
        ' a certain radius around a point.  
        ' Custom name of spatial data source created during upload  
        Dim dataSourceName As String = "FourthCoffeeSample"  
        ' Name of entities in the data source  
        Dim dataEntityName As String = "FourthCoffeeShops"  
        ' Unique access ID assigned to your data source by Bing Maps  
        ' e.g. f8986xxxxxxxc844b  
        Dim accessId As String = DataSourceID  
        ' Your Bing Maps Spatial Data Services query key.  
        Dim bingMapsKey As String = MyKey  
        ' Coordinates of the point to search from.  
        Dim SearchLatitude As Double = 47.63674  
        Dim SearchLongitude As Double = -122.30413  
        ' Search radius  
        Dim Radius As Double = 3 ' km  
        ' Setup REST request to query our uploaded customer data  
        Dim requestUrl As String = String.Format("http://spatial.virtualearth.net/REST/v1/data/{0}/{1}/{2}" & "?spatialFilter=nearby({3},{4},{5})&key={6}", accessId, dataSourceName, dataEntityName, SearchLatitude, SearchLongitude, Radius, MyKey)  
        ' Send the request and get back an XML response.  
        Dim response As XmlDocument = GetXmlResponse(requestUrl)  
        ' Display each entity's info.  
        ProcessEntityElements(response)  
    End Sub  
#End Region  
  
#Region "Helper Methods"  
  
    Public Shared Function GetXmlResponse(ByVal requestUrl As String) As XmlDocument  
        Try  
            Dim request As HttpWebRequest = TryCast(WebRequest.Create(requestUrl), HttpWebRequest)  
            Dim response As HttpWebResponse = TryCast(request.GetResponse(), HttpWebResponse)  
  
            Dim xmlDoc As New XmlDocument()  
            xmlDoc.Load(response.GetResponseStream())  
            Return (xmlDoc)  
  
        Catch e As Exception  
            Console.WriteLine(e.Message)  
  
            Console.Read()  
            Return Nothing  
        End Try  
    End Function  
  
    ''' <summary>  
    ''' Display each "entry" in the Bing Spatial Data Services Atom (XML) response.  
    ''' </summary>>  
    Private Sub ProcessEntityElements(ByVal response As XmlDocument)  
        Dim entryElements As XmlNodeList = response.GetElementsByTagName("entry")  
        For i As Integer = 0 To entryElements.Count - 1  
            Dim element As XmlElement = CType(entryElements(i), XmlElement)  
            Dim contentElement As XmlElement = CType(element.GetElementsByTagName("content")(0), XmlElement)  
            Dim propElement As XmlElement = CType(contentElement.GetElementsByTagName("m:properties")(0), XmlElement)  
            Dim nameElement As XmlNode = propElement.GetElementsByTagName("d:Name")(0)  
            If nameElement Is Nothing Then  
                Throw New Exception("Name not found")  
            End If  
            Dim latElement As XmlNode = propElement.GetElementsByTagName("d:Latitude")(0)  
            If latElement Is Nothing Then  
                Throw New Exception("Latitude not found")  
            End If  
            Dim longElement As XmlNode = propElement.GetElementsByTagName("d:Longitude")(0)  
            If longElement Is Nothing Then  
                Throw New Exception("Longitude not found")  
            End If  
            Dim name As String = nameElement.InnerText  
            Dim latitude As Double = 0  
            Double.TryParse(latElement.InnerText, latitude)  
            Dim longitude As Double = 0  
            Double.TryParse(longElement.InnerText, longitude)  
            Console.WriteLine("Coordinates of '{0}': {1}, {2}", name, latitude, longitude)  
        Next i  
    End Sub  
#End Region  
  
#Region "Query by Property"  
    Public Sub ExampleFindByProperty()  
        Console.WriteLine(vbLf & "ExampleFindByProperty")  
        ' Find all previously uploaded MyShops entities that accept  
        ' online orders.  
        ' Custom name of spatial data source created during upload  
        Dim dataSourceName As String = "FourthCoffeeSample"  
        ' Name of entities in the data source  
        Dim dataEntityName As String = "FourthCoffeeShops"  
        ' Unique access ID assigned to your data source by Bing Maps  
        ' e.g. f8986xxxxxxxc844b  
        Dim accessId As String = DataSourceID  
        ' Your Bing Maps Spatial Data Services query key.  
        Dim bingMapsKey As String = MyKey  
        ' Setup REST request to query our uploaded customer data  
        Dim requestUrl As String = String.Format("http://spatial.virtualearth.net/REST/v1/data/{0}/{1}/{2}" & "?$filter=AcceptsOnlineOrders Eq True&key={3}", accessId, dataSourceName, dataEntityName, MyKey)  
        ' Send the request and get back an XML response.  
        Dim response As XmlDocument = GetXmlResponse(requestUrl)  
        ' Display each entity's info.  
        ProcessEntityElements(response)  
    End Sub  
#End Region  
  
#Region "Query by Bounding Box"  
    Public Sub ExampleFindByBoundingBox()  
        Console.WriteLine(vbLf & "ExampleFindByBoundingBox")  
        ' Find all previously uploaded MyShops entities located within  
        ' the specified bounding box.  
        ' Custom name of spatial data source created during upload  
        Dim dataSourceName As String = "FourthCoffeeSample"  
        ' Name of entities in the data source  
        Dim dataEntityName As String = "FourthCoffeeShops"  
        ' Unique access ID assigned to your data source by Bing Maps  
        ' e.g. f8986xxxxxxxc844b  
        Dim accessId As String = DataSourceID  
        ' Your Bing Maps Spatial Data Services query key.  
        Dim bingMapsKey As String = MyKey  
        ' Coordinates of the bounding box's corners  
        Dim lat1 As Double = 47.612476759406583  
        Dim long1 As Double = -122.3237670214032  
        Dim lat2 As Double = 47.682391560800767  
        Dim long2 As Double = -122.27996173131822  
        ' Setup REST request to query our uploaded customer data  
        Dim requestUrl As String = String.Format("http://spatial.virtualearth.net/REST/v1/data/{0}/{1}/{2}" & "?spatialFilter=bbox({3},{4},{5},{6})&key={7}", accessId, dataSourceName, dataEntityName, lat1, long1, lat2, long2, MyKey)  
        ' Send the request and get back an XML response.  
        Dim response As XmlDocument = GetXmlResponse(requestUrl)  
        ' Display each entity's info.  
        ProcessEntityElements(response)  
    End Sub  
#End Region  
  
#Region "Query By ID"  
    ''' <summary>  
    ''' Query by ID using ATOM protocol  
    ''' </summary>  
    Public Sub ExampleQueryByIdAtom()  
        Console.WriteLine(vbLf & "ExampleQueryByIdAtom")  
        ' http://spatial.virtualearth.net/REST/v1/data/accessId/dataSourceName/entityTypeName('entityId')?key=queryKey  
        ' http://spatial.virtualearth.net/REST/v1/data/f8986xxxxxxxc844b/MyShopsSample/MyShops('1')?key=queryKey  
        ' Custom name of spatial data source created during upload  
        Dim dataSourceName As String = "FourthCoffeeSample"  
        ' Name of entities in the data source  
        Dim dataEntityName As String = "FourthCoffeeShops"  
        ' Unique access ID assigned to your data source by Bing Maps  
        ' e.g. f8986xxxxxxxc844b  
        Dim accessId As String = DataSourceID  
        ' ID of the entity to search for  
        Dim entityId As Integer = -22067  
        ' Your Bing Maps Spatial Data Services query key.  
        Dim bingMapsKey As String = MyKey  
        Dim requestUrl As String = String.Format("http://spatial.virtualearth.net" & "/REST/v1/data/{0}/{1}/{2}('{3}')?key={4}", accessId, dataSourceName, dataEntityName, entityId, MyKey)  
        ' By default, the Spatial Data API returns  
        ' data responses in Atom (xml) format.  
        Dim xmlResponse As XmlDocument = GetXmlResponse(requestUrl)  
        ' Select the first shop data in the xml results.  
        Dim nsmgr As New XmlNamespaceManager(xmlResponse.NameTable)  
        nsmgr.AddNamespace("a", "http://www.w3.org/2005/Atom")  
        nsmgr.AddNamespace("m", "http://schemas.microsoft.com/ado/2007/08/dataservices/metadata")  
        nsmgr.AddNamespace("d", "http://schemas.microsoft.com/ado/2007/08/dataservices")  
        Dim firstShopNode As XmlNode = xmlResponse.SelectSingleNode("//a:entry/a:content/m:properties", nsmgr)  
        ' Extract result data from the xml nodes.  
        Dim retrievedEntityId As Integer = Integer.Parse(firstShopNode.SelectSingleNode("d:EntityID", nsmgr).FirstChild.Value)  
        Dim postalCode As String = firstShopNode.SelectSingleNode("d:PostalCode", nsmgr).FirstChild.Value  
        Dim latitude As Double = Double.Parse(firstShopNode.SelectSingleNode("d:Latitude", nsmgr).FirstChild.Value)  
        Dim longitude As Double = Double.Parse(firstShopNode.SelectSingleNode("d:Longitude", nsmgr).FirstChild.Value)  
        Console.WriteLine(String.Format("Found EntityID {0} Postal Code: {1} Lat,Lon:  ({2},{3})", retrievedEntityId, postalCode, latitude, longitude))  
    End Sub  
  
#End Region ';  
  
End Class  
  
```