---
title: "Using the REST Services with .NET | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: ded0b787-f21b-4e68-aee8-bfd091144aa2
caps.latest.revision: 10
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Using the REST Services with .NET
> [!IMPORTANT]
>  Update: Since writing this documentation the Bing Maps team has released an open source portable class library which makes it easy to access the Bing Maps REST services from any .NET application. You can find this library on GitHub              [here](https://github.com/Microsoft/BingMapsRESTToolkit/).  
  
 This article will describe how to interact with the Bing Maps REST Services APIs using .NET. This approach can be used with technologies such as Windows Store apps and Windows Presentation Foundation (WPF).  
  
 The Bing Maps REST Services are a set of RESTful web services that access collection of resources by using a URL and the HTTP GET and POST methods The size of REST responses tend to be significantly smaller than SOAP-based service responses, and reduce the amount of time it takes a client application to download the response data. This increase in efficiency becomes especially important when developing mobile applications.  
  
 Each Bing Maps REST Services request is made using a URI and additional query parameters that specify the information to return. Some REST Services APIs support HTTP POST requests that you can use when the query parameter data increases the URL length beyond browser limits. You can specify XML or JSON format for the response. A JSON response is typically 25%-40% smaller than an XML response, and will take less time for the client to download. This topic focuses on JSON responses only.  
  
## Making use of sessions  
 All Bing Maps REST Services require a Bing Maps Key. If you are using the Bing Maps REST Services with one of the Bing Maps controls, such as AJAX, WPF, Windows Store app SDK, you can use a Bing Maps key as a session key. A session key can be used for all requests to the Bing Maps REST Services. The benefit of using a session key is that you are billed for one transaction per session and all calls to the REST services within that session are non-billable. For more information about billed transactions, see [Viewing Bing Maps Usage Reports](http://msdn.microsoft.com/en-us/library/ff859477.aspx).  
  
 The following examples show how to create a session key from an instance of Bing Maps control using .NET.  
  
```csharp  
Map.CredentialsProvider.GetCredentials((c) =>  
{  
    string sessionKey = c.ApplicationId;  
  
    //Generate a request URL for the Bing Maps REST services.  
    //Use the session key in the request as the Bing Maps key  
});  
```  
  
```vb  
Map.CredentialsProvider.GetCredentials(  
        Function(c)  
            Dim sessionKey As String = c.ApplicationId  
            'Generate a request URL for the Bing Maps REST services.  
            'Use the session key in the request as the Bing Maps key  
            Return 0  
        End Function)  
```  
  
## Making the request  
  
> [!IMPORTANT]
>  The Response class is part of the data contracts for the Bing Maps REST services. The data contracts for the Bing Maps REST Services are quite large and have been included at the end of this topic. You must copy these data contract classes into your application.  
  
 To access the Bing Maps REST Services, you create a URL request and then submit the request using HTTP **GET** or **POST** protocol . When the response data is returned, you must serialize the data against a set of data contracts. The data contracts for the Bing Maps REST Services are quite large and have been included at the end of this topic. As the Bing Maps REST Services adds new functionality, these data contracts must be updated. A benefit of working with JSON serialization rather than XML serialization is that changes in the schema rarely cause issues for existing applications. For instance, if a new property is added to the Bing Maps REST Services, an application that uses the old data contracts can still process a response without errors; however, the new property will not be available. To get the new property, you must update the data contracts.  
  
 In order to make use of JSON serialization in .NET, use the DataContractJsonSerializer by referencing the following libraries in your project:  
  
-   System.Runtime.Serialization  
  
-   System.ServiceModel.Web  
  
 When you specify parameter data for a Bing Maps REST service request, it is a good practice to encode the parameter values. This becomes especially important when working with special characters. In the following code samples, we use the Uri class that encodes these parameters automatically.  
  
### HTTP GET Requests  
 The following example is a generic method that can be used to make GET requests with Bing Maps REST Services.  
  
```csharp  
private void GetResponse(Uri uri, Action<Response> callback)  
{  
    WebClient wc = new WebClient();  
    wc.OpenReadCompleted += (o, a) =>  
    {  
        if (callback != null)  
        {  
            DataContractJsonSerializer ser = new DataContractJsonSerializer(typeof(Response));  
            callback(ser.ReadObject(a.Result) as Response);  
        }  
    };  
    wc.OpenReadAsync(uri);  
}  
```  
  
```vb  
Private Sub GetResponse(uri As Uri, callback As Action(Of Response))  
    Dim wc As New WebClient()  
    AddHandler wc.OpenReadCompleted,  
        Function(o, a)  
            If callback IsNot Nothing Then  
               Dim ser As New DataContractJsonSerializer(GetType(Response))  
               callback(TryCast(ser.ReadObject(a.Result), Response))  
            End If  
           Return 0  
       End Function  
    wc.OpenReadAsync(uri)  
End Sub  
```  
  
### HTTP POST Requests  
 The following example is a generic method that can be used to make HTTP POST requests with Bing Maps REST Services for APIs that support HTTP POST protocol.  
  
```csharp  
private void GetPOSTResponse(Uri uri, string data, Action<Response> callback)  
{  
    HttpWebRequest request = (HttpWebRequest)HttpWebRequest.Create(uri);  
  
    request.Method = "POST";  
    request.ContentType = "text/plain;charset=utf-8";  
  
    System.Text.UTF8Encoding encoding = new System.Text.UTF8Encoding();  
    byte[] bytes = encoding.GetBytes(data);  
  
    request.ContentLength = bytes.Length;  
  
    using (Stream requestStream = request.GetRequestStream())  
    {  
        // Send the data.  
        requestStream.Write(bytes, 0, bytes.Length);  
    }  
  
    request.BeginGetResponse((x) =>  
    {  
        using (HttpWebResponse response = (HttpWebResponse)request.EndGetResponse(x))  
        {  
            if (callback != null)  
            {  
                DataContractJsonSerializer ser = new DataContractJsonSerializer(typeof(Response));  
                callback(ser.ReadObject(response.GetResponseStream()) as Response);  
            }  
        }  
    }, null);  
}  
```  
  
```vb  
Private Sub GetPOSTResponse(uri As Uri, data As String, callback As Action(Of Response))  
    Dim request As HttpWebRequest = DirectCast(HttpWebRequest.Create(uri), HttpWebRequest)  
  
    request.Method = "POST"  
    request.ContentType = "text/plain;charset=utf-8"  
  
    Dim encoding As New System.Text.UTF8Encoding()  
    Dim bytes As Byte() = encoding.GetBytes(data)  
  
    request.ContentLength = bytes.Length  
  
    Using requestStream As Stream = request.GetRequestStream()  
        ' Send the data.  
        requestStream.Write(bytes, 0, bytes.Length)  
    End Using  
  
    request.BeginGetResponse(  
        Function(x)  
            Using response As HttpWebResponse = DirectCast(request.EndGetResponse(x), HttpWebResponse)  
                If callback IsNot Nothing Then  
                    Dim ser As New DataContractJsonSerializer(GetType(Response))  
                    callback(TryCast(ser.ReadObject(response.GetResponseStream()), Response))  
                End If  
            End Using  
            Return 0  
        End Function, Nothing)  
End Sub  
```  
  
### Implementing a request  
 The following is an example of how to use the above generic methods to make an HTTP GET request to the Bing Maps REST Services. This example geocodes the address “1 Microsoft Way, Redmond, WA”.  
  
```csharp  
string key = "YOUR_BING_MAPS_KEY or SESSION_KEY";  
string query = "1 Microsoft Way, Redmond, WA";  
  
Uri geocodeRequest = new Uri(string.Format("http://dev.virtualearth.net/REST/v1/Locations?q={0}&key={1}", query, key));  
  
GetResponse(geocodeRequest, (x) =>  
{  
    Console.WriteLine(x.ResourceSets[0].Resources.Length + " result(s) found.");  
    Console.ReadLine();  
});  
```  
  
```vb  
Dim key As String = "YOUR_BING_MAPS_KEY or SESSION_KEY"  
Dim query As String = "1 Microsoft Way, Redmond, WA"  
  
Dim geocodeRequest As New Uri(String.Format("http://dev.virtualearth.net/REST/v1/Locations?q={0}&key={1}", query, key))  
  
GetResponse(geocodeRequest, Function(x)  
   Console.WriteLine(x.ResourceSets(0).Resources.Length + " result(s) found.")  
   Console.ReadLine()  
   Return 0  
End Function)  
```  
  
### Data Contracts  
 The data contracts for the Bing Maps REST Services are large but straight forward. All classes need to have a DataContract attribute, and all public properties that are to be serialized need to have a DataMember attribute, and both a getter and a setter in C#. See [JSON Data Contracts](../rest-services/json-data-contracts.md) for the latest set of contracts.  
  
## See Also  
 [Bing Maps REST Service Tips & Tricks](http://blogs.bing.com/maps/2013/02/14/bing-maps-rest-service-tips-tricks/)   
 [Geocoding With the Search Charm (Blog)](http://blogs.bing.com/maps/2013/06/20/geocoding-with-the-search-charm/)   
 [Geocoding with the Search Charm (Code)](https://code.msdn.microsoft.com/Geocoding-with-the-Search-b1dcbf8a)   
 [How to Share Maps Using the Share Charm in Windows Store Apps](http://blogs.msdn.com/b/rbrundritt/archive/2013/11/08/how-to-share-maps-using-the-share-charm-in-windows-store-apps.aspx)