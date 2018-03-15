---
title: "Pushpin Syntax and Icon Styles | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 959d6077-b25f-4418-a3bf-71b99c09aebc
caps.latest.revision: 22
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms:service: "bingmaps"
---
# Pushpin Syntax and Icon Styles
Pushpins identify locations on a map. You can specify an icon style and a label for a pushpin, in addition to its location.  
  
> [!NOTE]
>  You can specify up to 18 pushpins within a [Get a Static Map](../rest-services/get-a-static-map.md) URL that uses HTTP GET protocol. However, if you use the HTTP POST method option, you can specify up to 100 pushpins by inserting them into the request body. See the **HTTP POST Syntax** section below for information about how to format the pushpins in a request body. The [Get a Static Map](../rest-services/get-a-static-map.md) topic provides more details and an example.  
  
 The following table shows the syntax to use to specify a pushpin location.  
  
```  
pushpin=latitude,longitude;iconStyle;label  
```  
  
 You can use the alias `pp` if you do not want to spell out `pushpin`.  
  
 A latitude and a longitude are required. You can optionally specify an icon style and a label for the pushpin. A length of a label string is limited to three characters.  
  
 The following table shows the options for specifying a pushpin.  
  
|Description|Syntax|  
|-----------------|------------|  
|Specify a pushpin location.|latitude,longitude<br /><br /> **Example**: pushpin=47.620548,-122.34874|  
|Specify a pushpin location and an icon style.|latitude,longitude;iconStyle<br /><br /> **Example**: pushpin=47.620548,-122.34874;5|  
|Specify a pushpin location and a label.|latitude,longitude;;label **Note:**  The order of the syntax requires that if you specify a label without specifying an icon style, you must preserve the syntax and put two semi-colons between the coordinates and the label. <br /><br /> **Example**: pushpin=47.620548,-122.34874;;P10|  
|Specify a pushpin location, an icon style, and a label. A label can have up to three (3) characters.|latitude,longitude;iconStyle;label<br /><br /> **Example**: pushpin=47.620548,-122.34874;5;P10|  
  
## HTTP POST Syntax  
 If you use the HTTP POST method for specifying pushpins on a static map, you must include the pushpins in the body of the request.  
  
 When specifying multiple pushpins in the request body, you must the ampersand character (&) or a carriage return (\r\n) as a delimiter. Pushpins that follow a carriage return (appear on a new line) do not have ampersands.  
  
 The following examples show how to specify pushpins in the body of an HTTP POST request. For more information about this type of request, see [Get a Static Map](../rest-services/get-a-static-map.md).  
  
 **Example 1**  
  
```  
pp=38.889586530732335,-77.05010175704956;23;LMT\r\n  
pp=38.88772364638439,-77.0472639799118;7;KMT\r\n  
pp=38.890479451480054,-77.04744637012482;1;VMT\r\n  
pp=38.8896854931628,-77.03519403934479;45;WMT  
  
```  
  
 **Example 2**  
  
```  
pp=38.889586530732335,-77.05010175704956;23;LMT&pp=38.88772364638439,-77.0472639799118;7;KMT\r\n  
pp=38.890479451480054,-77.04744637012482;1;VMT&pp=38.8896854931628,-77.03519403934479;45;WMT  
  
```  
  
## Icon Styles  
 The following table shows the available pushpin icon styles.  
  
|IconStyle|Icon|  
|---------------|----------|  
|0|![5c74ad81&#45;b8be&#45;4674&#45;a0a5&#45;91bf2df38d55](../rest-services/media/5c74ad81-b8be-4674-a0a5-91bf2df38d55.png "5c74ad81-b8be-4674-a0a5-91bf2df38d55")|  
|1 **[default]**|![748904ec&#45;4ee4&#45;439a&#45;a692&#45;601a3bf7a239](../rest-services/media/748904ec-4ee4-439a-a692-601a3bf7a239.png "748904ec-4ee4-439a-a692-601a3bf7a239")|  
|2|![610e10d7&#45;b486&#45;4576&#45;abaa&#45;4a35b4adff48](../rest-services/media/610e10d7-b486-4576-abaa-4a35b4adff48.png "610e10d7-b486-4576-abaa-4a35b4adff48")|  
|3|![1a999390&#45;a22b&#45;4c76&#45;a6f0&#45;2efb53ccf4c7](../rest-services/media/1a999390-a22b-4c76-a6f0-2efb53ccf4c7.png "1a999390-a22b-4c76-a6f0-2efb53ccf4c7")|  
|4|![a7f9fc6f&#45;1215&#45;4b00&#45;98ea&#45;9b3ce24401c0](../rest-services/media/a7f9fc6f-1215-4b00-98ea-9b3ce24401c0.png "a7f9fc6f-1215-4b00-98ea-9b3ce24401c0")|  
|5|![83275ca6&#45;a731&#45;4af5&#45;b29c&#45;42324bed6455](../rest-services/media/83275ca6-a731-4af5-b29c-42324bed6455.png "83275ca6-a731-4af5-b29c-42324bed6455")|  
|6|![14d73593&#45;1c35&#45;4eef&#45;a544&#45;bedb9172092e](../rest-services/media/14d73593-1c35-4eef-a544-bedb9172092e.png "14d73593-1c35-4eef-a544-bedb9172092e")|  
|7|![f0ad0035&#45;d443&#45;45f3&#45;9ba0&#45;2f014134fdc0](../rest-services/media/f0ad0035-d443-45f3-9ba0-2f014134fdc0.png "f0ad0035-d443-45f3-9ba0-2f014134fdc0")|  
|8|![3714c528&#45;3b4c&#45;45f5&#45;9536&#45;77677f4d9c63](../rest-services/media/3714c528-3b4c-45f5-9536-77677f4d9c63.png "3714c528-3b4c-45f5-9536-77677f4d9c63")|  
|9|![f8ea8238&#45;819b&#45;4ba3&#45;8445&#45;5cf667fcf7bc](../rest-services/media/f8ea8238-819b-4ba3-8445-5cf667fcf7bc.png "f8ea8238-819b-4ba3-8445-5cf667fcf7bc")|  
|10|![0a4a9d6a&#45;8c16&#45;4401&#45;994c&#45;0ea86f6db8b2](../rest-services/media/0a4a9d6a-8c16-4401-994c-0ea86f6db8b2.png "0a4a9d6a-8c16-4401-994c-0ea86f6db8b2")|  
|11|![c62f5134&#45;da4a&#45;4495&#45;877e&#45;a6aaa2badcec](../rest-services/media/c62f5134-da4a-4495-877e-a6aaa2badcec.png "c62f5134-da4a-4495-877e-a6aaa2badcec")|  
|12|![22594e72&#45;b742&#45;47c1&#45;8b16&#45;16969593d73d](../rest-services/media/22594e72-b742-47c1-8b16-16969593d73d.png "22594e72-b742-47c1-8b16-16969593d73d")|  
|13|![e6259b02&#45;fff8&#45;46ca&#45;8a08&#45;ef0003ec5a46](../rest-services/media/e6259b02-fff8-46ca-8a08-ef0003ec5a46.png "e6259b02-fff8-46ca-8a08-ef0003ec5a46")|  
|14|![20ab02d8&#45;0be0&#45;4d74&#45;a070&#45;109cb548ed6d](../rest-services/media/20ab02d8-0be0-4d74-a070-109cb548ed6d.png "20ab02d8-0be0-4d74-a070-109cb548ed6d")|  
|15|![2472e5ef&#45;50e2&#45;4c32&#45;bbb8&#45;4ced383ea673](../rest-services/media/2472e5ef-50e2-4c32-bbb8-4ced383ea673.png "2472e5ef-50e2-4c32-bbb8-4ced383ea673")|  
|16|![f6f25ac9&#45;b6cf&#45;4554&#45;91f0&#45;dc68318e2aa1](../rest-services/media/f6f25ac9-b6cf-4554-91f0-dc68318e2aa1.png "f6f25ac9-b6cf-4554-91f0-dc68318e2aa1")|  
|17|![c999f081&#45;c6a2&#45;4ba2&#45;a522&#45;42c44cecd57b](../rest-services/media/c999f081-c6a2-4ba2-a522-42c44cecd57b.png "c999f081-c6a2-4ba2-a522-42c44cecd57b")|  
|18|![d9abfbdd&#45;f4d4&#45;4587&#45;ba5c&#45;92dc86642738](../rest-services/media/d9abfbdd-f4d4-4587-ba5c-92dc86642738.png "d9abfbdd-f4d4-4587-ba5c-92dc86642738")|  
|19|![f313363e&#45;8e84&#45;4fec&#45;b8da&#45;b3ad1ddc7731](../rest-services/media/f313363e-8e84-4fec-b8da-b3ad1ddc7731.png "f313363e-8e84-4fec-b8da-b3ad1ddc7731")|  
|20|![792d281f&#45;7696&#45;4574&#45;befc&#45;6abb33349438](../rest-services/media/792d281f-7696-4574-befc-6abb33349438.png "792d281f-7696-4574-befc-6abb33349438")|  
|21|![517c88d7&#45;17c8&#45;4f74&#45;89b3&#45;95fd0b28061c](../rest-services/media/517c88d7-17c8-4f74-89b3-95fd0b28061c.png "517c88d7-17c8-4f74-89b3-95fd0b28061c")|  
|22|![016673a3&#45;0282&#45;4dd2&#45;95a9&#45;59395a50f6e7](../rest-services/media/016673a3-0282-4dd2-95a9-59395a50f6e7.png "016673a3-0282-4dd2-95a9-59395a50f6e7")|  
|23|![76fee352&#45;3881&#45;4f27&#45;8957&#45;9b1daf1b33b3](../rest-services/media/76fee352-3881-4f27-8957-9b1daf1b33b3.png "76fee352-3881-4f27-8957-9b1daf1b33b3")|  
|24|![dc992382&#45;ce01&#45;4fa6&#45;9444&#45;2708c7089c31](../rest-services/media/dc992382-ce01-4fa6-9444-2708c7089c31.png "dc992382-ce01-4fa6-9444-2708c7089c31")|  
|25|![29127350&#45;aeee&#45;45ae&#45;86d8&#45;ae1b1401bc1a](../rest-services/media/29127350-aeee-45ae-86d8-ae1b1401bc1a.png "29127350-aeee-45ae-86d8-ae1b1401bc1a")|  
|26|![242afc4c&#45;742f&#45;4337&#45;ad5c&#45;890b043ab649](../rest-services/media/242afc4c-742f-4337-ad5c-890b043ab649.png "242afc4c-742f-4337-ad5c-890b043ab649")|  
|27|![6cfcd96c&#45;fa3a&#45;41bc&#45;95ae&#45;a312887c15d7](../rest-services/media/6cfcd96c-fa3a-41bc-95ae-a312887c15d7.png "6cfcd96c-fa3a-41bc-95ae-a312887c15d7")|  
|28|![71d658fe&#45;bbe6&#45;4d5b&#45;a003&#45;31168a4df81f](../rest-services/media/71d658fe-bbe6-4d5b-a003-31168a4df81f.png "71d658fe-bbe6-4d5b-a003-31168a4df81f")|  
|29|![2c751486&#45;1ded&#45;421c&#45;be12&#45;cd235576e1ce](../rest-services/media/2c751486-1ded-421c-be12-cd235576e1ce.png "2c751486-1ded-421c-be12-cd235576e1ce")|  
|30|![e1304c66&#45;6e00&#45;4b81&#45;8534&#45;847b9329cc34](../rest-services/media/e1304c66-6e00-4b81-8534-847b9329cc34.png "e1304c66-6e00-4b81-8534-847b9329cc34")|  
|31|![90196075&#45;92c2&#45;4d1c&#45;a8f4&#45;eebfd681099b](../rest-services/media/90196075-92c2-4d1c-a8f4-eebfd681099b.png "90196075-92c2-4d1c-a8f4-eebfd681099b")|  
|32|![5f14de64&#45;bb5f&#45;4410&#45;8909&#45;225d95885205](../rest-services/media/5f14de64-bb5f-4410-8909-225d95885205.png "5f14de64-bb5f-4410-8909-225d95885205")|  
|33|![564bed6d&#45;cb69&#45;40f2&#45;88c0&#45;082bc2503f55](../rest-services/media/564bed6d-cb69-40f2-88c0-082bc2503f55.png "564bed6d-cb69-40f2-88c0-082bc2503f55")|  
|34|![54d50e0c&#45;5425&#45;4cb1&#45;bbdf&#45;8c3da904b2ce](../rest-services/media/54d50e0c-5425-4cb1-bbdf-8c3da904b2ce.png "54d50e0c-5425-4cb1-bbdf-8c3da904b2ce")|  
|35|![fcefc81e&#45;0d88&#45;4cc9&#45;97ee&#45;dccc26b7ac77](../rest-services/media/fcefc81e-0d88-4cc9-97ee-dccc26b7ac77.jpg "fcefc81e-0d88-4cc9-97ee-dccc26b7ac77")|  
|36|![4e781e20&#45;4767&#45;4cb5&#45;ae23&#45;a25ae58cab88](../rest-services/media/4e781e20-4767-4cb5-ae23-a25ae58cab88.png "4e781e20-4767-4cb5-ae23-a25ae58cab88")|  
|37|![Pushpin Icon Style 37](../rest-services/media/vewsiconstyle-37.jpg "Pushpin Icon Style 37")|  
|38|![Pushpin Icon Style 38](../rest-services/media/vewsiconstyle-38.jpg "Pushpin Icon Style 38")|  
|39|![Pushpin Icon Style 39](../rest-services/media/vewsiconstyle-39.jpg "Pushpin Icon Style 39")|  
|40|![Pushpin Icon Style 40](../rest-services/media/vewsiconstyle-40.jpg "Pushpin Icon Style 40")|  
|41|![Pushpin Icon Style 41](../rest-services/media/vewsiconstyle-41.jpg "Pushpin Icon Style 41")|  
|42|![Pushpin Icon Style 42](../rest-services/media/vewsiconstyle-42.jpg "Pushpin Icon Style 42")|  
|43|![Pushpin Icon Style 43](../rest-services/media/vewsiconstyle-43.jpg "Pushpin Icon Style 43")|  
|44|![Pushpin Icon Style 44](../rest-services/media/vewsiconstyle-44.jpg "Pushpin Icon Style 44")|  
|45|![Pushpin Icon Style 45](../rest-services/media/vewsiconstyle-45.jpg "Pushpin Icon Style 45")|  
|46|![Pushpin Icon Style 46](../rest-services/media/vewsiconstyle-46.jpg "Pushpin Icon Style 46")|  
|47|![Pushpin Icon Style 47](../rest-services/media/vewsiconstyle-47.jpg "Pushpin Icon Style 47")|  
|48|![Pushpin Icon Style 48](../rest-services/media/vewsiconstyle-48.jpg "Pushpin Icon Style 48")|  
|49|![Pushpin Icon Style 49](../rest-services/media/vewsiconstyle-49.jpg "Pushpin Icon Style 49")|  
|50|![Pushpin Icon Style 50](../rest-services/media/vewsiconstyle-50.jpg "Pushpin Icon Style 50")|  
|51|![Pushpin Icon Style 51](../rest-services/media/vewsiconstyle-51.jpg "Pushpin Icon Style 51")|  
|52|![Pushpin Icon Style 52](../rest-services/media/vewsiconstyle-52.jpg "Pushpin Icon Style 52")|  
|53|![Pushpin Icon Style 53](../rest-services/media/vewsiconstyle-53.jpg "Pushpin Icon Style 53")|  
|54|![Pushpin Icon Style 54](../rest-services/media/vewsiconstyle-54.jpg "Pushpin Icon Style 54")|  
|55|![Pushpin Icon Style 55](../rest-services/media/vewsiconstyle-55.jpg "Pushpin Icon Style 55")|  
|56|![Pushpin Icon Style 56](../rest-services/media/vewsiconstyle-56.jpg "Pushpin Icon Style 56")|  
|57|![Pushpin Icon Style 57](../rest-services/media/vewsiconstyle-57.jpg "Pushpin Icon Style 57")|  
|58|![Pushpin Icon Style 58](../rest-services/media/vewsiconstyle-58.jpg "Pushpin Icon Style 58")|  
|59|![Pushpin Icon Style 59](../rest-services/media/vewsiconstyle-59.jpg "Pushpin Icon Style 59")|  
|60|![Pushpin Icon Style 60](../rest-services/media/vewsiconstyle-60.jpg "Pushpin Icon Style 60")|  
|61|![Pushpin Icon Style 61](../rest-services/media/vewsiconstyle-61.jpg "Pushpin Icon Style 61")|  
|62|![Pushpin Icon Style 62](../rest-services/media/vewsiconstyle-62.jpg "Pushpin Icon Style 62")|  
|63|![Pushpin Icon Style 63](../rest-services/media/vewsiconstyle-63.jpg "Pushpin Icon Style 63")|  
|64|![Pushpin Icon Style 64](../rest-services/media/vewsiconstyle-64.jpg "Pushpin Icon Style 64")|  
|65|![Pushpin Icon Style 65](../rest-services/media/vewsiconstyle-65.jpg "Pushpin Icon Style 65")|  
|66|![Pushpin Icon Style 66](../rest-services/media/vewsiconstyle-66.jpg "Pushpin Icon Style 66")|  
|67|![Pushpin Icon Style 67](../rest-services/media/vewsiconstyle-67.jpg "Pushpin Icon Style 67")|  
|68|![Pushpin Icon Style 68](../rest-services/media/vewsiconstyle-68.jpg "Pushpin Icon Style 68")|  
|69|![Pushpin Icon Style 69](../rest-services/media/vewsiconstyle-69.jpg "Pushpin Icon Style 69")|  
|70|![Pushpin Icon Style 70](../rest-services/media/vewsiconstyle-70.jpg "Pushpin Icon Style 70")|  
|71|![Pushpin Icon Style 71](../rest-services/media/vewsiconstyle-71.jpg "Pushpin Icon Style 71")|  
|72|![Pushpin Icon Style 72](../rest-services/media/vewsiconstyle-72.jpg "Pushpin Icon Style 72")|  
|73|![Pushpin Icon Style 73](../rest-services/media/vewsiconstyle-73.jpg "Pushpin Icon Style 73")|  
|74|![Pushpin Icon Style 74](../rest-services/media/vewsiconstyle-74.jpg "Pushpin Icon Style 74")|  
|75|![Pushpin Icon Style 75](../rest-services/media/vewsiconstyle-75.jpg "Pushpin Icon Style 75")|  
|76|![Pushpin Icon Style 76](../rest-services/media/vewsiconstyle-76.jpg "Pushpin Icon Style 76")|  
|77|![Pushpin Icon Style 77](../rest-services/media/vewsiconstyle-77.jpg "Pushpin Icon Style 77")|  
|78|![Pushpin Icon Style 78](../rest-services/media/vewsiconstyle-78.jpg "Pushpin Icon Style 78")|  
|79|![Pushpin Icon Style 79](../rest-services/media/vewsiconstyle-79.jpg "Pushpin Icon Style 79")|  
|80|![Pushpin Icon Style 80](../rest-services/media/vewsiconstyle-80.jpg "Pushpin Icon Style 80")|  
|81|![Pushpin Icon Style 81](../rest-services/media/vewsiconstyle-81.jpg "Pushpin Icon Style 81")|  
|82|![Pushpin Icon Style 82](../rest-services/media/vewsiconstyle-82.jpg "Pushpin Icon Style 82")|  
|83|![Pushpin Icon Style 83](../rest-services/media/vewsiconstyle-83.jpg "Pushpin Icon Style 83")|  
|84|![Pushpin Icon Style 84](../rest-services/media/vewsiconstyle-84.jpg "Pushpin Icon Style 84")|  
|85|![Pushpin Icon Style 85](../rest-services/media/vewsiconstyle-85.jpg "Pushpin Icon Style 85")|  
|86|![Pushpin Icon Style 86](../rest-services/media/vewsiconstyle-86.jpg "Pushpin Icon Style 86")|  
|87|![Pushpin Icon Style 87](../rest-services/media/vewsiconstyle-87.jpg "Pushpin Icon Style 87")|  
|88|![Pushpin Icon Style 88](../rest-services/media/vewsiconstyle-88.jpg "Pushpin Icon Style 88")|  
|89|![Pushpin Icon Style 89](../rest-services/media/vewsiconstyle-89.jpg "Pushpin Icon Style 89")|  
|90|![Pushpin Icon Style 90](../rest-services/media/vewsiconstyle-90.jpg "Pushpin Icon Style 90")|  
|91|![Pushpin Icon Style 91](../rest-services/media/vewsiconstyle-91.jpg "Pushpin Icon Style 91")|  
|92|![Pushpin Icon Style 92](../rest-services/media/vewsiconstyle-92.jpg "Pushpin Icon Style 92")|  
|93|![Pushpin Icon Style 93](../rest-services/media/vewsiconstyle-93.jpg "Pushpin Icon Style 93")|  
|94|![Pushpin Icon Style 94](../rest-services/media/vewsiconstyle-94.jpg "Pushpin Icon Style 94")|  
|95|![Pushpin Icon Style 95](../rest-services/media/vewsiconstyle-95.jpg "Pushpin Icon Style 95")|  
|96|![Pushpin Icon Style 96](../rest-services/media/vewsiconstyle-96.jpg "Pushpin Icon Style 96")|  
|97|![Pushpin Icon Style 97](../rest-services/media/vewsiconstyle-97.jpg "Pushpin Icon Style 97")|  
|98|![Pushpin Icon Style 98](../rest-services/media/vewsiconstyle-98.jpg "Pushpin Icon Style 98")|  
|99|![Pushpin Icon 99](../rest-services/media/vewsiconstyle-99.jpg "Pushpin Icon 99")|  
|100|![Pushpin Icon 100](../rest-services/media/vewsiconstyle-100.jpg "Pushpin Icon 100")|  
|101|![Pushpin Icon 101](../rest-services/media/vewsiconstyle-101.jpg "Pushpin Icon 101")|  
|102|![Pushpin Icon 102](../rest-services/media/vewsiconstyle-102.jpg "Pushpin Icon 102")|  
|103|![Pushpin Icon 103](../rest-services/media/vewsiconstyle-103.jpg "Pushpin Icon 103")|  
|104|![Pushpin Icon 104](../rest-services/media/vewsiconstyle-104.jpg "Pushpin Icon 104")|  
|105|![Pushpin Icon 105](../rest-services/media/vewsiconstyle-105.jpg "Pushpin Icon 105")|  
|106|![Pushpin Icon 106](../rest-services/media/vewsiconstyle-106.jpg "Pushpin Icon 106")|  
|107|![Pushpin Icon 107](../rest-services/media/vewsiconstyle-107.jpg "Pushpin Icon 107")|  
|108|![Pushpin Icon 108](../rest-services/media/vewsiconstyle-108.jpg "Pushpin Icon 108")|  
|109|![Pushpin Icon 109](../rest-services/media/vewsiconstyle-109.jpg "Pushpin Icon 109")|  
|110|![Pushpin Icon 110](../rest-services/media/vewsiconstyle-110.jpg "Pushpin Icon 110")|  
|111|![Pushpin Icon 111](../rest-services/media/vewsiconstyle-111.jpg "Pushpin Icon 111")|  
|112|![Pushpin Icon 112](../rest-services/media/vewsiconstyle-112.jpg "Pushpin Icon 112")|  
|113|![Pushpin Icon 113](../rest-services/media/vewsiconstyle-113.jpg "Pushpin Icon 113")|  
|114|![Pushpin Icon 14](../rest-services/media/vewsiconstyle-114.jpg "Pushpin Icon 14")|  
|115|![Pushpin Icon 115](../rest-services/media/vewsiconstyle-115.jpg "Pushpin Icon 115")|  
|116|![Pushpin Icon 116](../rest-services/media/vewsiconstyle-116.jpg "Pushpin Icon 116")|  
|117|![Pushpin Icon 117](../rest-services/media/vewsiconstyle-117.jpg "Pushpin Icon 117")|  
|118|![Pushpin Icon 118](../rest-services/media/vewsiconstyle-118.jpg "Pushpin Icon 118")|  
|119|![Pushpin Icon 119](../rest-services/media/vewsiconstyle-119-2.jpg "Pushpin Icon 119")|  
|120|![Pushpin Icon 20](../rest-services/media/vewsiconstyle-120.jpg "Pushpin Icon 20")|  
|121|![Pushpin Icon 121](../rest-services/media/vewsiconstyle-121-2.jpg "Pushpin Icon 121")|  
|122|![Pushpin Icon 122](../rest-services/media/vewsiconstyle-122.jpg "Pushpin Icon 122")|  
|123|![Pushpin Icon 123](../rest-services/media/vewsiconstyle-123.jpg "Pushpin Icon 123")|  
|124|![Pushpin Icon 124](../rest-services/media/vewsiconstyle-124.jpg "Pushpin Icon 124")|  
|125|![Pushpin Icon 125](../rest-services/media/vewsiconstyle-125.jpg "Pushpin Icon 125")|  
|126|![Pushpin Icon 126](../rest-services/media/vewsiconstyle-126.jpg "Pushpin Icon 126")|  
|127|![Pushpin Icon 127](../rest-services/media/vewsiconstyle-127.jpg "Pushpin Icon 127")|  
|128|![Pushpin Icon 128](../rest-services/media/vewsiconstyle-128.jpg "Pushpin Icon 128")|  
|129|![Pushpin Icon 129](../rest-services/media/vewsiconstyle-129.jpg "Pushpin Icon 129")|  
|130|![Pushpin Icon 130](../rest-services/media/vewsiconstyle-130.jpg "Pushpin Icon 130")|  
|131|![Pushpin Icon 131](../rest-services/media/vewsiconstyle-131.jpg "Pushpin Icon 131")|  
|132|![Pushpin Icon 132](../rest-services/media/vewsiconstyle-132.jpg "Pushpin Icon 132")|  
|133|![Pushpin Icon 133](../rest-services/media/vewsiconstyle-133.jpg "Pushpin Icon 133")|  
|134|![Pushpin Icon 134](../rest-services/media/vewsiconstyle-134.jpg "Pushpin Icon 134")|  
|135|![Pushpin Icon 135](../rest-services/media/vewsiconstyle-135.jpg "Pushpin Icon 135")|  
|136|![Pushpin Icon 136](../rest-services/media/vewsiconstyle-136.jpg "Pushpin Icon 136")|