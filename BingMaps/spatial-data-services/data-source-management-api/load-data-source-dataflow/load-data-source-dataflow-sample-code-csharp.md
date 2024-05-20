---
title: "Load Data Source Dataflow Sample Code (C#) | Microsoft Docs"
description: C# sample code demonstrating how to upload entity data to a data source using the Load Data Source Dataflow API
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 0152ca75-a176-4e61-a8fa-cbd010c1c734
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Load Data Source Dataflow Sample Code (C#)

[!INCLUDE [bing-maps-spatial-data-service-data-source-management-api-retirement](../../includes/bing-maps-spatial-data-service-data-source-management-api-retirement.md)]

The following C# code shows how to upload entity data to a data source by using the Load Data Source Dataflow. The code is provided in two parts. The first code sample creates a Load Data Source Dataflow job and monitors the job status. The second code sample provides general classes that support these operations.  
  
## Classes that upload spatial data and check the status of a Load Data Source Dataflow job  
  
```csharp 
using System;  
using System.IO;  
using System.Net;  
using System.Text;  
using System.Threading;  
using BingMapsCsExamples.Properties;  
namespace BingMapsCsExamples.Examples.Phase2  
{  
  class SpatialDataUploading: ExamplesBase  
  {  
  
    /// <summary>   
    /// Upload spatial data to Bing Spatial Data Services   
    /// and wait for job completion (or timeout).   
    /// </summary>  
    public void UploadSpatialDataAndWaitForCompletion()  
    {  
      Console.WriteLine("Uploading spatial data...");  
      string statusUrl = UploadSpatialData();  
      Console.WriteLine("Spatial DataflowJob status URL: " + statusUrl);  
      Console.WriteLine("Waiting for job completion...");  
      string location = QueryDataflowJobStatus(statusUrl, 180);  
      Console.WriteLine("Spatial Data location: " + statusUrl);  
    }  
  
    /// <summary>   
    /// Bing Maps REST examples of uploading data to Spatial Data Services (SDS).   
    /// </summary>   
    /// <returns>The URL of the DataflowJob, with master key,   
    /// that can be used to query status.</returns>   
    public string UploadSpatialData()  
    {  
      // http://spatial.virtualearth.net/REST/v1/Dataflows/LoadDataSource?dataSourceName=MyShopsSample&loadOperation=complete&input=xml&output=xml&key=masterKey   
  
      // Custom name of spatial data source created during upload.   
      string dataSourceName = "MyShopsSample";  
      // Path to the spatial data input file to be uploaded.   
      string dataFilePath = @".\Data\SpatialDataUploadExampleData1.xml";  
      // The master key used for uploading to Spatial Data Services.   
      // This key should differ from your query key.   
      string bingMapsMasterKey = Settings.Default.BingMapsMasterKey;  
      // Create the spatial data upload URL.   
      StringBuilder queryStringBuilder = new StringBuilder();  
      queryStringBuilder.Append("dataSourceName=");  
      queryStringBuilder.Append(Uri.EscapeUriString(dataSourceName));  
      queryStringBuilder.Append("&loadOperation=complete");  
      // Use xml input and output for the spatial data.   
      // You could use any of: xml, csv, tab, or pipe.   
      queryStringBuilder.Append("&input=xml");  
      queryStringBuilder.Append("&output=xml");  
      queryStringBuilder.Append("&key=");  
      queryStringBuilder.Append(Uri.EscapeUriString(bingMapsMasterKey));  
      UriBuilder uriBuilder = new UriBuilder("http://spatial.virtualearth.net");  
      uriBuilder.Path = "/REST/v1/Dataflows/LoadDataSource";  
      uriBuilder.Query = queryStringBuilder.ToString();  
      // Create the request object. HttpWebRequest request = (HttpWebRequest)WebRequest.Create(uriBuilder.Uri);   
      // The HTTP method must be 'POST'.  
      request.Method = "POST";  
      request.ContentType = "application/xml";  
      // Write the request body with the   
      // spatial data XML file contents (schema and data).   
      using(FileStream dataStream = File.OpenRead(dataFilePath))  
      {  
        using(Stream requestStream = request.GetRequestStream())  
        {  
          byte[] buffer = new byte[16384];  
          int bytesRead = dataStream.Read(buffer, 0, buffer.Length);  
          while (bytesRead > 0)  
          {  
            requestStream.Write(buffer, 0, bytesRead);  
            bytesRead = dataStream.Read(buffer, 0, buffer.Length);  
          }  
        }  
      }  
      string dataflowJobUrl = null;  
  
      // Submit the HTTP request and check if the   
      // job was created successfully.   
      using(HttpWebResponse response = (HttpWebResponse)request.GetResponse())  
      {  
        // // If the job was created successfully, the status code should be   
        // 201 (Created) and the 'Location' header should contain a URL   
        // that defines the location of the new dataflow job. You use this   
        // URL with the Bing Maps Key to query the status of your job.   
        //   
        if (response.StatusCode != HttpStatusCode.Created)  
          throw new Exception("An HTTP error status code was " +   
            "encountered when creating the geocode job.");  
        dataflowJobUrl = response.GetResponseHeader("Location");  
        if (String.IsNullOrEmpty(dataflowJobUrl))  
          throw new Exception("The 'Location' header is " +   
            "missing from the HTTP response " + "when creating a geocode job.");  
      }  
      string jobStatusQueryUrl = string.Format("{0}?key={1}", dataflowJobUrl,  
        Uri.EscapeUriString(bingMapsMasterKey));  
      Console.WriteLine("Upload job location = " + dataflowJobUrl);  
  
      return jobStatusQueryUrl;  
    }  
  
    /// <summary>   
    /// Bing Maps REST example of querying a   
    /// Spatial Data Services DataflowJob status.   
    /// Blocks the calling thread until the DataflowJob   
    /// completes or until a timeout is reached.   
    /// </summary>   
    /// <param name="jobStatusQueryUrl">The URL used to query   
    /// the upload job status.   
    /// Must contain your Bing Maps Key   
    /// as a query parameter.</param>   
    /// <returns>The URL of the uploaded data flow.</returns>   
    /// <exception cref="Exception">On upload   
    /// error or timeout.</exception>   
    public string QueryDataflowJobStatus(string jobStatusQueryUrl, int  
      timeoutInSeconds)  
    {  
      // int timeoutInSeconds = 120;   
      string dataSourceUrl = null;  
      const int secondsBetweenPolls = 5;  
      int maxCount = timeoutInSeconds / secondsBetweenPolls;  
      if (maxCount < 1)  
      {  
        maxCount = 1;  
      }  
      for (int checkCounter = 0; checkCounter < maxCount; ++checkCounter)  
      {  
        Console.WriteLine("Querying job status: " + jobStatusQueryUrl);  
        // Check the job status by making a   
        // request to the job status URL.   
        BingMapsRestV1.Response jsonResponse = GetJsonResponse  
          (jobStatusQueryUrl);  
        BingMapsRestV1.DataflowJob job =  
          jsonResponse.ResourceSets[0].Resources[0] as  
          BingMapsRestV1.DataflowJob;  
        if (job.Status == "Completed")  
        {  
          foreach (BingMapsRestV1.Link link in job.Links)  
          {  
            if (link.Role == "dataSource")  
            {  
  
              // There can be multiple data source   
              // links but for this example,   
              // we just use the first link.  
              dataSourceUrl = link.Url;  
              break;  
            }  
          }  
          break;  
        }  
        else if (job.Status == "Aborted")  
        {  
          throw new Exception("The spatial data upload " +   
            "failed with status: " + job.Status + " Job location: " +  
            jobStatusQueryUrl + " Error message: " + job.ErrorMessge);  
        }  
        // Job status is "Pending" or otherwise incomplete.   
        // Wait to poll the job status again.   
        Thread.Sleep(secondsBetweenPolls * 1000);  
      }  
      if (string.IsNullOrEmpty(dataSourceUrl))  
      {  
        throw new Exception("Timed out or otherwise failed to " +   
          "find the dataSource link in the data flow job. " + " Job location: "  
          + jobStatusQueryUrl);  
      }  
      return dataSourceUrl;  
    }  
  }  
}  
```  
  
### Support Classes  
  
```csharp
using System;  
using System.IO;  
using System.Net;  
using System.Runtime.Serialization.Json;  
using System.Xml;  
using BingMapsCsExamples.Helpers;  
using BingMapsCsExamples.Properties;  
namespace BingMapsCsExamples.Examples  
{  
  
  /// <summary> /// Base class containing functionality common across the examples,   
  /// such as JSON and XML response processing.   
  /// </summary> public abstract class ExamplesBase  
  
  {  
    #region Static members   
    /// <summary>   
    /// Your Bing Maps Key. You can either replace the value   
    /// here or you can add a Settings value to your project.   
    /// </summary> protected static string BingMapsKey = Settings.Default.BingMapsKey;   
    /// <summary> /// Send the request to the Bing Maps REST API   
    /// and deserialize the JSON response.   
    /// </summary>   
    public static BingMapsRestV1.Response GetJsonResponse(string requestUrl)  
    {  
      System.Diagnostics.Trace.WriteLine("Request URL (JSON): " + requestUrl);  
      HttpWebRequest request = WebRequest.Create(requestUrl)as HttpWebRequest;  
      using(HttpWebResponse response = request.GetResponse()as HttpWebResponse)  
      {  
        if (response.StatusCode != HttpStatusCode.OK)  
          throw new Exception(String.Format("Server error (HTTP {0}: {1}).",  
            response.StatusCode, response.StatusDescription));  
        DataContractJsonSerializer jsonSerializer = new  
          DataContractJsonSerializer(typeof(BingMapsRestV1.Response));  
        object objResponse = jsonSerializer.ReadObject  
          (response.GetResponseStream());  
        BingMapsRestV1.Response jsonResponse = objResponse as  
          BingMapsRestV1.Response;  
        return jsonResponse;  
      }  
    }  
  
    /// <summary>   
    /// Send the request to the Bing Maps REST API and deserialize the XML response.   
    /// </summary>   
    public static XmlDocument GetXmlResponse(string requestUrl)  
    {  
      System.Diagnostics.Trace.WriteLine("Request URL (XML): " + requestUrl);  
      HttpWebRequest request = WebRequest.Create(requestUrl)as HttpWebRequest;  
      using(HttpWebResponse response = request.GetResponse()as HttpWebResponse)  
      {  
        if (response.StatusCode != HttpStatusCode.OK)  
          throw new Exception(String.Format("Server error (HTTP {0}: {1}).",  
            response.StatusCode, response.StatusDescription));  
        XmlDocument xmlDoc = new XmlDocument();  
        xmlDoc.Load(response.GetResponseStream());  
        TraceXmlDocument(xmlDoc);  
        return xmlDoc;  
      }  
    }  
  
    /// <summary>   
    /// Write an XML document to Diagnostics.Trace.   
    /// </summary>   
    private static void TraceXmlDocument(XmlDocument xmlDoc)  
    {  
      StringWriter sw = new StringWriter();  
      XmlTextWriter xw = new XmlTextWriter(sw);  
      xmlDoc.WriteTo(xw);  
      System.Diagnostics.Trace.WriteLine(sw.ToString());  
    }  
  
    #endregion   
  }  
  
}  
```