---
title: "Events Class | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 05fd0a56-4e95-4184-ba3e-b51903fd0e0e
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms:service: "bing-maps"
---
# Events Class
Events can be added and removed by using the methods available through the `Microsoft.Maps.Events` class. The Events class has the following static methods available.

Name                                                                                            | Type      | Description
----------------------------------------------------------------------------------------------- | --------- | ------------------------
`addHandler(target:object, eventName:string, handler:function) `                                   | object    | Attaches the handler for the event that is thrown by the target. Use the return object to remove the handler using the removeHandler method. 
`addOne(target:object, eventName:string, handler:function)`                                                                                          |           | Attaches the handler for the event that is thrown by the target, but only triggers the handler the first once after being attached. 
`addThrottledHandler(target:object, eventName:string, handler:function, throttleInterval:number)` | object    | Attaches the handler for the event that is thrown by the target, where the minimum interval between events (in milliseconds) is specified as a parameter. 
`hasHandler(target:object, eventName:string)`                                                     | boolean   | Checks if the target has any attached event handler.
`invoke(target:object, evenName:string,args:object)`                                              |           | Invokes an event on the target. This causes all handlers for the specified event name to be called.
`removeHandler(handlerId: object)`                                                                |           | Detaches the specified handler from the event. The **handlerId** is returned by the `addHandler` and `addThrottledHandler` methods.

The following code sample demonstrates how to add and remove events. The target is the object you want to add the event to (i.e. the map), the eventName is the name of the event to attach as a string, and the handler is a callback function that is called when the event is triggered. When an event is added, the addHandler method returns an object (handlerId). This object can be passed to the removeHandler method later to detach the event from the target object.

```
//Attach an event
var handlerId = Microsoft.Maps.Events.addHandler(target, 'eventName', handler);

//Remove an event
Microsoft.Maps.Events.removeHandler(handlerId);
```

## See Also

* [Event Examples](../v8-web-control/event-examples.md)