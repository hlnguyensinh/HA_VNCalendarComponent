# Changelog

## [0.0.1] - 2026-04-25
- Initial release
- Lunar calendar display
- Solar terms
- Theme switching (day/night/full moon)

## [0.0.2] - 2026-04-26
- Update background links to github.
> Ex: /local/widget/vn_lunar_calendar/assets/whiteflower.jpg → https://raw.githubusercontent.com/hlnguyensinh/HA_VNLunarCalendar/main/assets/whiteflower.jpg

## [0.0.3] - 2026-04-27
- Hide vegetarian day icon to avoid overflowing the frame

## [0.0.4] - 2026-04-30
- Re-render calendar when a new date changes.
- For test:
	- Send JSON to input_text entity
	- Update vegegetarian status to input_boolean entity
	```
	entity_selected_lunar: input_text.your_input_text
	entity_isveg: input_boolean.your_input_boolean
	```
	
## [1.0.0] - 2026-05-01
- Release VN Calendar Component:
	- Sensor
	- Binary_sensor
- Auto detect and connect to VN Calendar Component (default), or run standalone if the component unavailable
- Add new entity to Update state of connected component:
	```
	entity_component: input_boolean.vn_lunar_connected
	```
	
## [1.1.0] - 2026-05-04

### Component:

#### Sensor & Binary sensor
| Name                     | Type          | Ex.Value  | Ex.Attribute                                                                              |
| ------------------------ | ------------- | --------- | ----------------------------------------------------------------------------------------- | 
| `vn_calendar_day_type`   | Sensor        | Hắc đạo   | {'dayType': ['Hắc đạo', '⚡'], 'goodhours': [{'name': 'Tý', 'time': '23:00-01:00'}, ...]} |
| `vn_calendar_today`      | Sensor        | 18/3/2026 | {"day": "Mậu Dần", "month": "Nhâm Thìn", "year": "Bính Ngọ", "events": [] }               |
| `vn_calendar_solar_term` | Sensor        | Cốc vũ    | {'solarTerm': ['Cốc vũ', '🌧️']}                                                           |
| `vn_calendar_good_hour`  | Binary_sensor | off       | {'hour': 'Ngọ', 'range': '11:00-13:00'}                                                   |
| `vn_calendar_veg_day`    | Binary_sensor | off       | None                                                                                      |

#### Services:
| Name               | Description                               |
| ------------------ | ----------------------------------------- |
| `good_hours`       | Get good hours in a day with current time |
| `good_hours_today` | Get good hours today with current time    |

### Frontend:
- Get good hours in a day with current time
- Get status "Hoàng đạo/Hắc đạo" realtime

| Name                   | Type          | Default | Description                |
| ---------------------- | ------------- | ------- | -------------------------- |
| `entity_hide_events`   | input_boolean | False   | Hide lunar events          |
| `entity_hide_goodday`  | input_boolean | True    | Hide good day              |
| `entity_hide_goodhour` | input_boolean | False   | Hide good hour             |
| `entity_hide_isveg`    | input_boolean | True    | Hide vegetarian day status |
| `entity_nobg`          | input_boolean | False   | Remove background          |
| `entity_readonly`      | input_boolean | False   | Disable click on calendar  |

- Example
```
- type: custom:vn-lunar-calendar
  entity_hide_events: input_boolean.vn_lunar_hide_events
  entity_hide_goodday: input_boolean.vn_lunar_hide_goodday
  entity_hide_goodhour: input_boolean.vn_lunar_hide_goodhour
  entity_hide_isveg: input_boolean.vn_lunar_hide_isveg
  entity_nobg: input_boolean.vn_lunar_nobg
  entity_readonly: input_boolean.vn_lunar_calendar_readonly
```

## [1.1.1] & [1.1.2] - 2026-05-04
- Update services.yaml
- Active vn_calendar_solar_term sensor
- Add new service:

| Service            | Description      |
| ------------------ | ---------------- |
| `get_zodiac_hours` | Get Zodiac hours |

## [1.2.0] - 2026-05-07
- Removed `entity_nobg`
- Change name `entity_component` → `entity_component_connected` (add '_connected')
- Change name `entity_hide_events` → `entity_hide_event` (remove 's')
- Add new `entity_theme`: choose theme for VN Lunar Calendar (ready support more theme), with values:
	- green
	- sample
	- standard (default)
- Add new `entity_use_component`: use component (True) or not (False)
- Add new `entity_textpanel`: useful for show entity's state, example: sensor.vn_calendar_day_type
- Add new `entity_theme_nocache`: no cache themes, turn on to re-design, turn off to get cache for improve performance

### Dynamic themes:
- Default "standard" theme, if you want to custom, please add file .js to ./themes/

### Summary:

| Name                         | Type          | Default value | Description                                   | ViewOnly |
| ---------------------------- | ------------- |:-------------:| --------------------------------------------- |:--------:| 
| `entity_use_component`       | input_boolean | True          | Use component                                 |          |
| `entity_component_connected` | input_boolean | N/A           | Get status component connection               | x        |
| `entity_theme`               | input_select  | standard      | Calendar Theme, other load file ./themes/*.js |          |
| `entity_hide_event`          | input_text    | False         | Hide lunar events tag                         |          |
| `entity_textpanel`           | any sensor    | N/A           | Show value (ex: sensor.vn_calendar_day_type)  |          |
| `entity_theme_nocache`       | input_boolean | False         | Not use theme cache                           |          |

## [1.2.1] - 2026-05-08
- Fix invalid manifest.json
- Fix HACS update/install issue

## [1.2.2] - 2026-05-11
- Update manifest.json, change "integration_type" from "entity" to "hub"