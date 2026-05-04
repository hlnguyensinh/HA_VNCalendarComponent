# VN Lunar Calendar Component Sensors

## Details:

### Sensor

| Name                     | Type   | Ex.Value  | Ex.Attribute                                                                              | Description               |
| ------------------------ | ------ | --------- | ----------------------------------------------------------------------------------------- | ------------------------- |
| `vn_calendar_day_type`   | Sensor | Hắc đạo   | {'dayType': ['Hắc đạo', '⚡'], 'goodhours': [{'name': 'Tý', 'time': '23:00-01:00'}, ...]} | Today's Hoàng đạo/Hắc đạo |
| `vn_calendar_today`      | Sensor | 18/3/2026 | {"day": "Mậu Dần", "month": "Nhâm Thìn", "year": "Bính Ngọ", "events": [] }               | Today's lunar information |
| `vn_calendar_solar_term` | Sensor | Cốc vũ    | {'solarTerm': ['Cốc vũ', '🌧️']}                                                           | Solar term in year        |

---

### Binary Sensor

| Name                    | Type          | Ex.Value | Ex.Attribute                            | Description                       |
| ----------------------- | ------------- | -------- | --------------------------------------- | --------------------------------- |
| `vn_calendar_good_hour` | Binary_sensor | off      | {'hour': 'Ngọ', 'range': '11:00-13:00'} | Is good hour                      |
| `vn_calendar_veg_day`   | Binary_sensor | off      | None                                    | ON when today is a vegetarian day |

---
