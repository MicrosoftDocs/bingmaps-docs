---
title: "Geocode Dataflow Sample Code | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 48b41da1-8392-4e26-b17f-c1dbe0cf18ed
caps.latest.revision: 14
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Geocode Dataflow Sample Code
The following sample code uses the Geocode Dataflow to geocode spatial data.  
  
 **Notes:**  
  
-   The code uses the functionality included in Microsoft® .NET 2.0 and is written as a console application.  
  
-   The code accepts input data in any of the formats supported by the Geocode Dataflow. Examples of supported data formats are XML and CSV(comma-separated values). See [Create Job](../geocode-dataflow-api/create-a-geocode-job-and-upload-data.md) for more information about supported data formats.  
  
-   The code processes HTTP requests returned in XML format for version 1.0 of the Geocode Dataflow schema.  
  
-   The results of the geocode job are output to files named succeeded.txt and failed.txt.  
  
```csharp
using System;  
using System.IO;  
using System.Net;  
using System.Text;  
using System.Threading;  
using System.Xml;  
  
//This C# code sample shows how to geocode data using the Geocode Dataflow REST API.  
//For more information on this API, see the Bing Spatial Data Services SDK on MSDN:  
// http://msdn.microsoft.com/en-us/library/ff701734.aspx  
namespace GeocodeDataFlowExample  
{  
    //A summary of status information returned in the response when you check   
    // job status.   
    class DownloadDetails  
    {  
        public string jobStatus { get; set; }  
        public string suceededlink { get; set; }  
        public string failedlink { get; set; }  
  
    }  
  
    class Program  
    {  
        //Creates a geocode dataflow job and uploads spatial data to process.  
        //Parameters:   
        //   dataFilePath: The path to the file that contains the spatial data to geocode.  
        //   dataFormat: The format of the input data. Possible values are xml, csv, tab and pipe.  
        //   key: The Bing Maps Key to use for this job. The same key is used to get job status and download results.  
        //   description: Text that is used to describe the geocode dataflow job.   
        //Return value : A URL that defines the location of the geocode dataflow job that was created.  
        static string CreateJob(string dataFilePath, string dataFormat, string key, string description)  
        {  
            //Define parameters for the HTTP request  
            //  
            // The 'Content-Type' header of the HTTP Request must be "text/plain" or "application/xml"  
            // depending on the input data format.  
            //  
            string contentType = "text/plain";  
            if (dataFormat.Equals("xml", StringComparison.OrdinalIgnoreCase))  
                contentType = "application/xml";  
  
            StringBuilder queryStringBuilder = new StringBuilder();  
  
            //  
            // The 'input'(input format) and 'key' (Bing Maps Key) parameters are required.  
            //  
            queryStringBuilder.Append("input=").Append(Uri.EscapeUriString(dataFormat));  
            queryStringBuilder.Append("&");  
            queryStringBuilder.Append("key=").Append(Uri.EscapeUriString(key));  
  
            if (!String.IsNullOrEmpty(description))  
            {  
                //  
                // The 'description' parameter is optional.  
                //  
                queryStringBuilder.Append("&");  
                queryStringBuilder.Append("description=").Append(Uri.EscapeUriString(description));  
            }  
  
            //Build the HTTP URI that will upload and create the geocode dataflow job  
            UriBuilder uriBuilder = new UriBuilder("http://spatial.virtualearth.net");  
            uriBuilder.Path = "/REST/v1/dataflows/geocode";  
            uriBuilder.Query = queryStringBuilder.ToString();  
  
            //Include the data to geocode in the HTTP request  
            using (FileStream dataStream = File.OpenRead(dataFilePath))  
            {  
                HttpWebRequest request = (HttpWebRequest)WebRequest.Create(uriBuilder.Uri);  
  
                //  
                // The HTTP method must be 'POST'.  
                //  
                request.Method = "POST";  
                request.ContentType = contentType;  
  
                using (Stream requestStream = request.GetRequestStream())  
                {  
                    byte[] buffer = new byte[16384];  
                    int bytesRead = dataStream.Read(buffer, 0, buffer.Length);  
                    while (bytesRead > 0)  
                    {  
                        requestStream.Write(buffer, 0, bytesRead);  
  
                        bytesRead = dataStream.Read(buffer, 0, buffer.Length);  
                    }  
                }  
  
                //Submit the HTTP request and check if the job was created successfully.   
                using (HttpWebResponse response = (HttpWebResponse)request.GetResponse())  
                {  
                    //  
                    // If the job was created successfully, the status code should be  
                    // 201 (Created) and the 'Location' header should contain a URL  
                    // that defines the location of the new dataflow job. You use this   
                    // URL with the Bing Maps Key to query the status of your job.  
                    //  
                    if (response.StatusCode != HttpStatusCode.Created)  
                        throw new Exception ("An HTTP error status code was encountered when creating the geocode job.");  
  
                    string dataflowJobLocation = response.GetResponseHeader("Location");  
                    if (String.IsNullOrEmpty(dataflowJobLocation))  
                        throw new Exception ("The 'Location' header is missing from the HTTP response when creating a goecode job.");  
  
                    return dataflowJobLocation;  
                }  
            }  
        }  
  
        //Checks the status of a dataflow job and defines the URLs to use to download results when the job is completed.  
        //Parameters:   
        //   dataflowJobLocation: The URL to use to check status for a job.  
        //   key: The Bing Maps Key for this job. The same key is used to create the job and download results.    
        //Return value: A DownloadDetails object that contains the status of the geocode dataflow job (Completed, Pending, Aborted).  
        //              When the status is set to Completed, DownloadDetails also contains the links to download the results  
        static DownloadDetails CheckStatus(string dataflowJobLocation, string key)  
        {  
  
            DownloadDetails statusDetails = new DownloadDetails();  
            statusDetails.jobStatus = "Pending";  
  
            //Build the HTTP Request to get job status  
            UriBuilder uriBuilder = new UriBuilder(dataflowJobLocation + @"?key=" + key + "&output=xml");  
            HttpWebRequest request = (HttpWebRequest)WebRequest.Create(uriBuilder.Uri);  
  
            request.Method = "GET";  
  
            //Submit the request and read the response to get job status and to retrieve the links for   
            //  downloading the job results  
            //Note: The following conditional statements make use of the fact that the 'Status' field will    
            //  always appear after the 'Link' fields in the HTTP response.  
            using (HttpWebResponse response = (HttpWebResponse)request.GetResponse())  
            {  
  
                if (response.StatusCode != HttpStatusCode.OK)  
                    throw new Exception ("An HTTP error status code was encountered when checking job status.");  
  
                using (Stream receiveStream = response.GetResponseStream())  
                {  
                    XmlTextReader reader = new XmlTextReader(receiveStream);  
                    while (reader.Read())  
                    {  
                        if (reader.IsStartElement())  
                        {  
                            if (reader.Name.Equals("Status"))  
                            {  
                                //return job status  
                                statusDetails.jobStatus = reader.ReadString();  
  
                                return (statusDetails);  
                            }  
                            else if (reader.Name.Equals("Link"))  
                            {  
                                //Set the URL location values for retrieving   
                                // successful and failed job results  
                                reader.MoveToFirstAttribute();  
                                if (reader.Value.Equals("output"))  
                                {  
                                    reader.MoveToNextAttribute();  
                                    if (reader.Value.Equals("succeeded"))  
                                    {  
                                        statusDetails.suceededlink = reader.ReadString();  
  
                                    }  
                                    else if (reader.Value.Equals("failed"))  
                                    {  
                                        statusDetails.failedlink = reader.ReadString();  
                                    }  
                                }  
                            }  
                        }  
                    }  
  
                }  
  
            }  
            return (statusDetails);  
        }  
  
        //Downloads job results to files names Success.txt (successfully geocoded results) and   
        //   Failed.txt (info about spatial data that was not geocoded successfully).  
         //Parameters:   
        //   statusDetails: Inclues job status and the URLs to use to download all geocoded results.  
        //   key: The Bing Maps Key for this job. The same key is used to create the job and get job status.     
  
        static void DownloadResults(DownloadDetails statusDetails, string key)  
        {  
            //Write the results for data that was geocoded successfully to a file named Success.xml  
            if (statusDetails.suceededlink != null && !statusDetails.suceededlink.Equals(String.Empty))  
            {  
                //Create a request to download successfully geocoded data. You must add the Bing Maps Key to the   
                //  download location URL provided in the response to the job status request.  
                UriBuilder successUriBuilder = new UriBuilder(statusDetails.suceededlink + @"?key=" + key);  
                HttpWebRequest request1 = (HttpWebRequest)WebRequest.Create(successUriBuilder.Uri);  
  
                request1.Method = "GET";  
  
                using (HttpWebResponse response = (HttpWebResponse)request1.GetResponse())  
                {  
                    if (response.StatusCode != HttpStatusCode.OK)  
                        throw new Exception ("An HTTP error status code was encountered when downloading results.");  
  
                    using (Stream receiveStream = response.GetResponseStream())  
                    {  
                        StreamWriter successfile = new StreamWriter("Success.txt");  
                        using (StreamReader r = new StreamReader(receiveStream))  
                        {  
                            string line;  
                            while ((line = r.ReadLine()) != null)  
                            {  
                                successfile.WriteLine(line);  
                            }  
                        }  
                        successfile.Close();  
                    }  
  
                }  
            }  
  
            //If some spatial data could not be geocoded, write the error information to a file called Failed.xml  
            if (statusDetails.failedlink != null && !statusDetails.failedlink.Equals(String.Empty))  
            {  
                //Create an HTTP request to download error information. You must add the Bing Maps Key to the   
                //  download location URL provided in the response to the job status request.  
                UriBuilder failedUriBuilder = new UriBuilder(statusDetails.failedlink + @"?key=" + key);  
                HttpWebRequest request2 = (HttpWebRequest)WebRequest.Create(failedUriBuilder.Uri);  
  
                request2.Method = "GET";  
  
                using (HttpWebResponse response = (HttpWebResponse)request2.GetResponse())  
                {  
                    if (response.StatusCode != HttpStatusCode.OK)  
                        throw new Exception ("An HTTP error status code was encountered when downloading results.");  
  
                    using (Stream receiveStream = response.GetResponseStream())  
                    {  
                        StreamWriter failedfile = new StreamWriter("Failed.txt");  
                        using (StreamReader r = new StreamReader(receiveStream))  
                        {  
                            string line;  
                            while ((line = r.ReadLine()) != null)  
                            {  
                                failedfile.WriteLine(line);  
                             }  
                        }  
                        failedfile.Close();  
                    }  
  
                }  
            }  
        }  
  
        //  
        // Sample command-line:  
        // GeocodeDataFlowExample.exe <dataFilePath> <dataFormat> <key> [<description>]  
        //  
        // Where:  
        // <dataFilePath> is a path to the data file containing entities to geocode.  
        // <dataFormat> is one of these types: xml, csv, tab, pipe.  
        // <key> is a Bing Maps Key from http://www.bingmapsportal.com.  
        // <description> is an optional description for the dataflow job.  
        //  
  
        static void Main(string[] args)  
        {  
            string dataFilePath = args[0];  
            string dataFormat = args[1];  
            string key = args[2];  
            string description = null;  
  
            try  
            {  
  
                if (args.Length > 3)  
                    description = args[3];  
  
                string dataflowJobLocation = CreateJob(dataFilePath, dataFormat, key, description);  
                Console.WriteLine("Dataflow Job Location: {0}", dataflowJobLocation);  
  
                //Continue to check the dataflow job status until the job has completed  
                DownloadDetails statusDetails = new DownloadDetails();  
                do  
                {  
                    statusDetails = CheckStatus(dataflowJobLocation, key);  
                    Console.WriteLine("Dataflow Job Status: {0}", statusDetails.jobStatus);  
                    if (statusDetails.jobStatus== "Aborted")  
                        throw new Exception("Job was aborted due to an error.");  
                    Thread.Sleep(30000); //Get status every 30 seconds  
                }  
                while (statusDetails.jobStatus.Equals("Pending"));   
  
                //When the job is completed, get the results  
                //Two files are created to record the results:  
                //  Success.xml contains the data that was successfully geocoded  
                //  Failed.mxl contains the data that could not be geocoded  
  
                DownloadResults(statusDetails, key);  
  
            }  
  
            catch (Exception  e)  
            {  
                Console.WriteLine("Exception :" + e.Message);  
            }  
         }  
    }  
}  
  
```