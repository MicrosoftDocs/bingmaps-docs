
# Display flyout of pushpin

Flyout is a simple panel that display information over a map usually when associated [MapIcon](../map-control-api/MapIcon-class.md) is tapped.

## Examples

### Assigning flyout to pushpin

The following example shows how to set flyout of pushpin with title.

**Swift**

> ```swift
> let center = self.mapView.mapCenter
> let flyout = MSMapFlyout()
> flyout.frame = CGRect(x: 0, y: 0, width: 100, height: 50)
> flyout.backgroundColor = UIColor.blue
> let text = UILabel(frame: flyout.bounds)
> text.text = "Test"
> text.textAlignment = .center
> text.textColor = UIColor.white
> flyout.addSubview(text)
> let icon = MSMapIcon()
> icon.image = MSMapImage(uiImage:UIImage(named: "pushpin")!)
> icon.location = MSGeolocation(latitude: center.latitude, longitude: center.longitude, altitude: 0, altitudeReferenceSystem: .surface)
> icon.normalizedAnchorPoint = CGPoint(x:0.5, y:1.0)
> mElementLayer.elements.add(icon)
> icon.flyout = flyout
> ```

**Objective-C**

> ```objectivec
> MSGeolocation *center = self.mapView.mapCenter;
> MSMapFlyout *flyout = [MSMapFlyout flyout];
> flyout.frame = CGRectMake(0, 0, 100, 50);
> flyout.backgroundColor = [UIColor blueColor];
> UILabel *text = [[UILabel alloc] initWithFrame:flyout.bounds];
> text.text = @"Test";
> text.textAlignment = NSTextAlignmentCenter;
> text.textColor = [UIColor whiteColor];
> [flyout addSubview:text];
> MSMapIcon *icon = [MSMapIcon icon];
> icon.image = [MSMapImage imageWithUIImage:[UIImage imageNamed:@"pushpin"]];
> icon.location = [MSGeolocation geolocationWithLatitude:center.latitude
>                                           longitude:center.longitude
>                                            altitude:0
>                             altitudeReferenceSystem:MSMapAltitudeReferenceSystemSurface];
> icon.normalizedAnchorPoint = CGPointMake(0.5f, 1.0f);
> [mElementLayer.elements addMapElement:icon];
> icon.flyout = flyout;
> ```
