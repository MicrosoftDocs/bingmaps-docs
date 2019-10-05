# Display flyout of pushpin

A Flyout is a simple panel that displays information over a map, often when an associated
[MapIcon](../map-control-api/MapIcon-class.md) is tapped.

## Examples

### Assigning flyout to pushpin

The following example shows how to set the flyout of a pushpin with a title.

**Java**

>```java
> MapFlyout flyout = new MapFlyout();
> flyout.setTitle("Test");
> flyout.setDescription("Sample description");
> icon.setFlyout(flyout);
>```

**Swift**

>```swift
> let flyout = MSMapFlyout()
> flyout.title = "Test"
> flyout.description = "Sample description"
> icon.flyout = flyout
>```

**Objective-C**

>```objectivec
> MSMapFlyout *flyout = [MSMapFlyout flyout];
> flyout.title = @"Test";
> flyout.description = @"Sample description";
> icon.flyout = flyout;
>```

### Hide and show flyout

The following example shows how to hide and show the flyout manually when a pushpin is tapped.

**Swift**

>```swift
> mapView.addUserDidTapHandler { (point:CGPoint, location:MSGeopoint?) -> Bool in
>    let tappedElements = self.mapView.findMapElements(atOffset: point)
>     if tappedElements.isEmpty {
>         for element in self.pinLayer.elements {
>             let icon = element as? MSMapIcon
>             icon?.flyout.hide()
>         }
>         return false
>     }
>     let altitude = self.mapView.mapCenter.altitudeReferenceSystem
>
>     let mapIcon = tappedElements.first as? MSMapIcon
>     if mapIcon == nil {
>         for element in self.pinLayer.elements {
>             let icon = element as? MSMapIcon
>             icon?.flyout.hide()
>         }
>         return false
>     }
>
>     if mapIcon!.flyout != nil {
>        mapIcon!.flyout.show()
>    }
>
>    return true
>}
>```
