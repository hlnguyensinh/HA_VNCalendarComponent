[![HACS](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/hacs/integration)

# VN Lunar Calendar Component for Home Assistant

<p align="center">
  <img src="https://img.shields.io/github/v/release/hlnguyensinh/HA_VNCalendarComponent?style=for-the-badge" />
  <img src="https://img.shields.io/github/stars/hlnguyensinh/HA_VNCalendarComponent?style=for-the-badge" />
  <img src="https://img.shields.io/github/license/hlnguyensinh/HA_VNCalendarComponent?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Home%20Assistant-Custom%20Card-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Built%20with-ChatGPT-orange?style=for-the-badge" />
</p>

<p align="center">
A modern Vietnamese Lunar Calendar integration for Home Assistant.
</p>

Supports:

- Vietnamese lunar date conversion
- Can Chi (Heavenly Stem & Earthly Branch)
- Solar Terms (Tiết Khí)
- Vegetarian days (Ngày Chay)
- Buddhist events
- Hoàng Đạo / Hắc Đạo day classification
- Fast yearly cache engine
- Lovelace swipe calendar UI
- Sensors, binary sensors, and services

---

# Features

## Lunar Calendar Engine

- Solar → Lunar conversion
- Leap lunar month support
- Can Chi for:
    - Year
    - Month
    - Day
- Solar Terms (24 Tiết Khí)
- Hoàng Đạo / Hắc Đạo
- Vegetarian day detection
- Buddhist event lookup

---

## Home Assistant Integration

### Services

| Service     | Description                      |
| ----------- | -------------------------------- |
| `today`     | Get today's lunar information    |
| `get_day`   | Get lunar info of a specific day |
| `get_month` | Get full month lunar data        |
| `get_year`  | Get full year lunar data         |

---

## Sensors

### Sensor

| Entity                     | Description               |
| -------------------------- | ------------------------- |
| `sensor.vn_calendar_today` | Today's lunar information |

---

### Binary Sensor

| Entity                              | Description                       |
| ----------------------------------- | --------------------------------- |
| `binary_sensor.vn_calendar_veg_day` | ON when today is a vegetarian day |

---

## Setup:

- HACS -> Custom repositories:
    - Repository: `https://github.com/hlnguyensinh/HA_VNCalendarComponent`
    - Type: `Integration`

- Settings -> Devices & services -> Add integration -> VN Lunar Calendar Component

## Lovelace Calendar Card

### Features

- Swipe month navigation
- Solar + Lunar day display
- Today highlight
- Sunday highlight
- Vegetarian day markers
- Event markers
- Responsive layout
- Smooth animation
- Auto cache preload
- Frontend fallback mode

---

# Installation

## HACS (Recommended)

### Add Custom Repository

Repository type:

```txt
Integration
```

Repository URL:

```txt
https://github.com/hlnguyensinh/HA_VNCalendarComponent
```

Then:

1. Install integration
2. Restart Home Assistant
3. Add integration from:

```txt
Settings → Devices & Services
```

---

## Manual Installation

Copy:

```txt
custom_components/vn_calendar_component
```

into:

```txt
/config/custom_components/
```

Restart Home Assistant.

---

# Configuration

## Add Integration

Go to:

```txt
Settings → Devices & Services → Add Integration
```

Search:

```txt
VN Lunar Calendar Component
```

---

# Lovelace Card

### Resource

- Setup from HACS: _(Recommend)_
    - HACS -> Custom repositories
        - Repository: https://github.com/hlnguyensinh/HA_VNLunarCalendar/releases/latest/download/vn_lunar_calendar.js
        - Type: Dashboard

- Or manual

```yaml
url: /local/vn_lunar_calendar.js
type: module
```

---

### Example Card

```yaml
type: custom:vn-lunar-calendar
```

---

# Services

## today

### Example

```yaml
service: vn_calendar_component.today
```

---

## get_day

### Example

```yaml
service: vn_calendar_component.get_day
data:
    day: 2
    month: 4
    year: 2026
response_variable: lunar
```

---

## Example Response

```json
{
    "solar": {
        "day": 2,
        "month": 4,
        "year": 2026
    },
    "lunar": {
        "day": 15,
        "month": 2,
        "year": 2026,
        "leap": false,
        "canchi": {
            "year": "Bính Ngọ",
            "month": "Tân Mão",
            "day": "Bính Ngọ"
        },
        "events": ["Phật Thích Ca nhập Niết Bàn"]
    },
    "timezone": 7,
    "solarTerm": ["Xuân phân", "🌸"],
    "dayType": ["Hắc đạo", "⚡"],
    "isVeg": true
}
```

---

# Frontend Fallback Mode

If the backend integration is unavailable, the Lovelace card automatically switches to frontend-only lunar calculation mode.

This ensures:

- Calendar still works
- No blank UI
- Offline calculation support

---

# Cache System

The integration includes a high-performance yearly cache engine.

## Features

- Year-based cache
- Automatic preload
- Smart cleanup strategy
- Shared runtime cache via `hass.data`
- Fast month rendering

---

# Project Structure

```txt
custom_components/
└── vn_calendar_component/
    ├── __init__.py
    ├── manifest.json
    ├── config_flow.py
    ├── const.py
    ├── sensor.py
    ├── binary_sensor.py
    ├── services.yaml
    ├── coordinator.py
    ├── lunar.py
    ├── lunarcache.py
    └── translations/
```

---

# Roadmap

Planned features:

- Moon phase
- Multiple timezone support
- Calendar events entity
- Festival database
- Astrology information
- WebSocket realtime updates
- Multi-language support
- Theme presets
- Mobile optimized layout

---

# Credits

Lunar conversion algorithm inspired by:

- Hồ Ngọc Đức lunar calendar algorithm
- Traditional Vietnamese lunar calendar system
- Developer: **Nguyen Sinh**
- AI Support: ChatGPT (OpenAI)

---

# License

MIT License

---

# Screenshots

## Demo

<img src="https://raw.githubusercontent.com/hlnguyensinh/HA_VNLunarCalendar/main/screenshots/demo_day.gif" width="300" alt="VN Lunar Calendar - Day" />
<img src="https://raw.githubusercontent.com/hlnguyensinh/HA_VNLunarCalendar/main/screenshots/demo_night.gif" width="300" alt="VN Lunar Calendar - Night" />
<img src="https://raw.githubusercontent.com/hlnguyensinh/HA_VNLunarCalendar/main/screenshots/demo_night2.gif" width="300" alt="VN Lunar Calendar - Night 2" />

---

# Support

If you find this project useful:

- Star the repository
- Report issues
- Suggest new features
- Contribute improvements

---

# Author

VN Lunar Calendar for Home Assistant
