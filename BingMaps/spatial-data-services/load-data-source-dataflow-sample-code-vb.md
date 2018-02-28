---
title: "Load Data Source Dataflow Sample Code (VB) | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 3533c946-4c5d-4e2d-935c-310e406b8a58
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# Load Data Source Dataflow Sample Code (VB)
The following Visual Basic code shows how to upload entity data to a data source by using the Load Data Source Dataflow. The code is provided in two parts. The first code sample creates a Load Data Source Dataflow job and monitors the job status. The second code sample provides general classes that support these operations.  
  
## Classes that upload spatial data and check the status of a Load Data Source Dataflow job  
  
```  
Imports System  
Imports System.Collections.Generic  
Imports System.Linq  
Imports System.Text  
Imports BingMapsMigrationCsExamples.Properties  
Imports System.IO  
Imports System.Net  
64  
Imports System.Xml  
Imports System.Threading  
Imports System.Runtime.Serialization  
Imports System.Runtime.Serialization.Json  
Imports BingMapsMigrationCsExamples  
  
Class SpatialDataUploading  
    Inherits ExamplesBase  
    #Region  
    Imports System.Xml  
    Imports System.Threading  
    Imports System.Runtime.Serialization  
    Imports System.Runtime.Serialization.Json  
    Imports BingMapsMigrationCsExamples  
  
    Class SpatialDataUploading  
        Inherits ExamplesBase  
        #Region "Spatial Data Upload"  
        ''' <summary>  
        ''' Bing Maps REST examples of uploading data to Spatial Data Services (SDS).  
        ''' </summary>  
        ''' <returns>The URL of the DataflowJob, with master key,  
        ''' that can be used to query status.</returns>  
  
        Public Function UploadSpatialData() As String  
            ' http://spatial.virtualearth.net/REST/v1/Dataflows/LoadDataSource?dataSourceName=MyShopsSample&loadOperation=complete&input=xml&output=xml&key=masterKey  
            ' Custom name of spatial data source created during upload.  
            Dim dataSourceName As String = "MyShopsSample"  
            ' Path to the spatial data input file to be uploaded.  
            Dim dataFilePath As String = ".\Data\SpatialDataUploadExampleData1.xml"  
            ' The master key used for uploading to Spatial Data Services.  
            ' This key should differ from your query key.  
            Dim bingMapsMasterKey As String = "TODO Replace with your Bing Maps Master Key."  
            ' Create the spatial data upload URL.  
            Dim queryStringBuilder As New StringBuilder()  
            queryStringBuilder.Append("dataSourceName=")  
            queryStringBuilder.Append(Uri.EscapeUriString(dataSourceName))  
            queryStringBuilder.Append("&loadOperation=complete")  
            ' Use xml input and output for the spatial data.  
            queryStringBuilder.Append("&input=xml")  
            queryStringBuilder.Append("&output=xml")  
            queryStringBuilder.Append("&key=")  
            queryStringBuilder.Append(Uri.EscapeUriString(bingMapsMasterKey))  
            Dim uriBuilder As New UriBuilder("http://spatial.virtualearth.net")  
            uriBuilder.Path = "/REST/v1/Dataflows/LoadDataSource"  
            uriBuilder.Query = queryStringBuilder.ToString()  
            Dim dataflowJobUrl As String = Nothing  
            Using dataStream As FileStream = File.OpenRead(dataFilePath)  
            Dim request As HttpWebRequest = DirectCast(WebRequest.Create(uriBuilder.Uri), HttpWebRequest)  
            '  
            ' The HTTP method must be 'POST'.  
            '  
            request.Method = "POST"  
            request.ContentType = "application/xml"  
            Using requestStream As Stream = request.GetRequestStream()  
            Dim buffer As Byte() = New Byte(16383) {}  
            Dim bytesRead As Integer = dataStream.Read(buffer, 0, buffer.Length)  
            While bytesRead > 0  
                requestStream.Write(buffer, 0, bytesRead)  
                bytesRead = dataStream.Read(buffer, 0, buffer.Length)  
            End While  
            End Using  
            ' Submit the HTTP request and check if the  
            ' job was created successfully.  
            Using response As HttpWebResponse = DirectCast(request.GetResponse(), HttpWebResponse)  
            '  
            ' If the job was created successfully, the status code should be  
            ' 201 (Created) and the 'Location' header should contain a URL  
            ' that defines the location of the new dataflow job. You use this  
            ' URL with the Bing Maps Key to query the status of your job.  
            '  
            If response.StatusCode <> HttpStatusCode.Created Then  
                Throw New Exception("An HTTP error status code was " + "encountered when creating the geocode job.")  
            End If  
            dataflowJobUrl = response.GetResponseHeader("Location")  
            If [String].IsNullOrEmpty(dataflowJobUrl) Then  
                Throw New Exception("The 'Location' header is " + "missing from the HTTP response " + "when creating a geocode job.")  
            End If  
            End Using  
            End Using  
            Console.WriteLine("Upload job location = " + dataflowJobUrl)  
            Dim jobStatusQueryUrl As String = String.Format("{0}?key={1}", dataflowJobUrl, Uri.EscapeUriString(bingMapsMasterKey))  
            Return jobStatusQueryUrl  
        End Function  
  
        ''' <summary>  
        ''' Bing Maps REST example of querying a  
        ''' Spatial Data Services DataflowJob status.  
        ''' Blocks the calling thread until the DataflowJob  
        ''' completes or until a timeout is reached.  
        ''' </summary>  
        ''' <param name="jobStatusQueryUrl">The URL used to query  
        66  
        ''' the upload job status.  
        ''' Must contain your Bing Maps Key  
        ''' as a query parameter.</param>  
        ''' <returns>The URL of the uploaded data flow.</returns>  
        ''' <exception cref="Exception">On upload  
        ''' error or timeout.</exception>  
  
        Public Function QueryDataflowJobStatus(ByVal jobStatusQueryUrl As String, ByVal timeoutInSeconds As Integer) As String  
            Dim dataSourceUrl As String = Nothing  
            Const secondsBetweenPolls As Integer = 5  
            Dim maxCount As Integer = timeoutInSeconds / secondsBetweenPolls  
            If maxCount < 1 Then  
                maxCount = 1  
            End If  
            For checkCounter As Integer = 0 To maxCount - 1  
                Console.WriteLine("Querying job status: " + jobStatusQueryUrl)  
                ' Check the job status by making a  
                ' request to the job status URL.  
                Dim jsonResponse As BingMapsRestV1.Response = GetJsonResponse(jobStatusQueryUrl)  
                Dim job As BingMapsRestV1.DataflowJob = TryCast(jsonResponse.ResourceSets(0).Resources(0), BingMapsRestV1.DataflowJob)  
                If job.Status = "Completed" Then  
                    For Each link As BingMapsRestV1.Link In job.Links  
                        If link.Role = "dataSource" Then  
                            ' There can be multiple data source  
                            ' links but for this example,  
                            ' we just use the first link.  
                            dataSourceUrl = link.Url  
                            Exit For  
                        End If  
                    Next  
                    Exit For  
                ElseIf job.Status = "Aborted" Then  
                    Throw New Exception("The spatial data upload " + "failed with status: " + job.Status + " Job location: " + jobStatusQueryUrl + " Error message: " + job.ErrorMessge)  
                End If  
                ' Job status is "Pending" or otherwise incomplete.  
                ' Wait to poll the job status again.  
                Thread.Sleep(secondsBetweenPolls * 1000)  
            Next  
            If String.IsNullOrEmpty(dataSourceUrl) Then  
                Throw New Exception("Timed out or otherwise failed to " + "find the dataSource link in the data flow job. " + " Job location: " + jobStatusQueryUrl)  
                67  
            End If  
            Return dataSourceUrl  
        End Function  
  
        #End Region  
    End Class  
```  
  
### Support Classes  
  
```  
Imports System  
Imports System.Collections.Generic  
Imports System.Windows.Media.Imaging  
Imports System.Text  
Imports System.Net  
Imports System.Xml  
Imports System.Runtime.Serialization.Json  
Imports BingMapsMigrationCsExamples.BingMapsRestV1  
Imports BingMapsMigrationCsExamples.Properties  
Imports BingMapsMigrationCsExamples.Helpers  
Imports BingMapsMigrationCsExamples  
  
''' <summary>  
''' Base class containing the functionality common for all examples.  
''' </summary>  
Public MustInherit Class ExamplesBase  
    #Region "Constants"  
        Private Shared BingMapsKey As String = "TODO Replace with your BingMapsKey"  
    #End Region  
  
    #Region "Static members"  
    ''' <summary>  
    ''' Send the request to the Bing Maps REST API  
    ''' and deserialize the JSON response.  
    ''' </summary>  
    Public Shared Function GetJsonResponse(ByVal requestUrl As String) As BingMapsRestV1.Response  
        Dim request As HttpWebRequest = TryCast(WebRequest.Create(requestUrl), HttpWebRequest)  
        Using response As HttpWebResponse = TryCast(request.GetResponse(), HttpWebResponse)  
        If response.StatusCode <> HttpStatusCode.OK Then  
            Throw New Exception([String].Format("Server error (HTTP {0}: {1}).", response.StatusCode, response.StatusDescription))  
        End If  
        Dim jsonSerializer As New DataContractJsonSerializer(GetType(BingMapsRestV1.Response))  
        Dim objResponse As Object = jsonSerializer.ReadObject(response.GetResponseStream())  
        Dim jsonResponse As BingMapsRestV1.Response = TryCast(objResponse, BingMapsRestV1.Response)  
        Return jsonResponse  
        End Using   
    End Function  
  
    ''' <summary>  
    ''' Send the request to the Bing Maps REST API and deserialize the XML response.  
    ''' </summary>  
    Public Shared Function GetXmlResponse(ByVal requestUrl As String) As XmlDocument  
        Dim request As HttpWebRequest = TryCast(WebRequest.Create(requestUrl), HttpWebRequest)  
        Using response As HttpWebResponse = TryCast(request.GetResponse(), HttpWebResponse)  
        If response.StatusCode <> HttpStatusCode.OK Then  
            Throw New Exception([String].Format("Server error (HTTP {0}: {1}).", response.StatusCode, response.StatusDescription))  
        End If  
        Dim xmlDoc As New XmlDocument()  
        xmlDoc.Load(response.GetResponseStream())  
        Return xmlDoc  
        End Using  
    End Function  
  
    #End Region  
  
    #Region "Instance members"  
        Protected imageLoader As New MapImageLoader()  
    #End Region  
End Class  
```