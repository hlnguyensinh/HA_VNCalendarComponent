from datetime import date, timedelta, datetime

from .vnlunarextra import VNLunarExtra
from .const import TIME_ZONE

####--------------------------------------------------------------------


class VNLunarCache:

    def __init__(self, timeZone: int = TIME_ZONE) -> None:
        self.timeZone = timeZone

        self.cache = {}

        self.clsLunar = VNLunarExtra()
        self.thoithancache = self.clsLunar.getThoiThan()

    def buildYear(self, year: int) -> dict:
        data = {}

        start = date(year, 1, 1)
        end = date(year, 12, 31)
        delta = timedelta(days=1)

        d = start

        while d <= end:
            dd = d.day
            mm = d.month
            yy = d.year

            lunar = self.clsLunar.getLunarDay(
                dd,
                mm,
                yy,
                self.timeZone,
            )

            key_day = f"{yy}-{mm:02d}-{dd:02d}"
            key_month = f"{yy}-{mm:02d}"

            # init month dict nếu chưa có
            if key_month not in data:
                data[key_month] = {}

            data[key_month][key_day] = lunar

            d += delta

        self.cache[year] = data

        self.cleanup(year)

        return data

    def get(self, dd: int, mm: int, yy: int) -> dict:
        yearMap = self.cache.get(yy, {})

        if not yearMap:
            yearMap = self.buildYear(yy)

        key_day = f"{yy}-{mm:02d}-{dd:02d}"
        key_month = f"{yy}-{mm:02d}"

        return yearMap[key_month][key_day]

    def get_month(self, mm: int, yy: int) -> dict:
        yearMap = self.cache.get(yy, {})

        if not yearMap:
            yearMap = self.buildYear(yy)

        key_month = f"{yy}-{mm:02d}"

        return yearMap[key_month]

    def get_year(self, yy: int) -> dict:
        yearMap = self.cache.get(yy, {})

        if not yearMap:
            yearMap = self.buildYear(yy)

        return yearMap

    def today(self) -> dict:
        now = datetime.now()

        return self.get(now.day, now.month, now.year)

    def preload(self, years: list) -> None:
        for y in years:
            self.buildYear(y)

    def clear(self, year: int) -> None:
        self.cache.pop(year, None)

    def clearAll(self) -> None:
        self.cache.clear()

    def keep3cache(self, viewingyear: int) -> None:
        current_year = datetime.now().year
        viewingyear = viewingyear if viewingyear > 1900 else current_year

        keep_years = {
            current_year - 1,
            current_year,
            current_year + 1,
            viewingyear - 1,
            viewingyear,
            viewingyear + 1,
        }

        for year in list(self.cache.keys()):
            if year not in keep_years:
                self.clear(year)

    def cleanup(self, viewingyear: int) -> None:
        trigger = 6

        lencached = len(self.cache)

        if lencached > trigger:
            print(f"before: ", lencached)
            self.keep3cache(viewingyear)
            lencached = len(self.cache)
            print(f"after: ", lencached)

    def get_current_hour_chi(self) -> str | None:
        now = datetime.now()

        current_minutes = now.hour * 60 + now.minute

        for chi, time_range in self.thoithancache.items():
            start, end = time_range.split("-")

            sh, sm = map(int, start.split(":"))
            eh, em = map(int, end.split(":"))

            start_minutes = sh * 60 + sm
            end_minutes = eh * 60 + em

            # handle crossing midnight (Tý hour)
            if end_minutes < start_minutes:
                if current_minutes >= start_minutes or current_minutes < end_minutes:
                    return chi
            else:
                if current_minutes >= start_minutes and current_minutes < end_minutes:
                    return chi

        return None

    def is_current_good_hour(self, goodhours: list) -> bool:
        current_chi = self.get_current_hour_chi()

        return any(item["name"] == current_chi for item in goodhours)

    def get_current_hour_info(self, dd: int, mm: int, yy: int) -> dict:
        dayinfo = self.get(dd, mm, yy)

        hour = self.get_current_hour_chi()

        return {
            "goodhours": dayinfo.get("goodHours", []),
            "hour": hour,
            "range": self.thoithancache.get(hour),
            "isgoodhour": self.is_current_good_hour(dayinfo.get("goodHours", [])),
        }

    def get_current_hour_info_today(self) -> dict:
        dayinfo = self.today()

        hour = self.get_current_hour_chi()

        return {
            "goodhours": dayinfo.get("goodHours", []),
            "hour": hour,
            "range": self.thoithancache.get(hour),
            "isgoodhour": self.is_current_good_hour(dayinfo.get("goodHours", [])),
        }

    def getThoiThan(self) -> dict:
        return self.thoithancache


####--------------------------------------------------------------------

# from datetime import datetime

# clsLunarCache = VNLunarCache()

# clsLunarCache.preload([2022,2023,2024,2025,2026,2027,2028,2029])
# print(clsLunarCache.buildYear(2026))
# print(clsLunarCache.today())
# print(clsLunarCache.cleanup())

# now = datetime.now()
# testday = clsLunarCache.get(now.day, now.month, now.year)
# print(clsLunarCache.get_month(now.month, now.year))
# print(clsLunarCache.get_year(now.year))
# print(testday)
# print(clsLunarCache.get_current_hour_info(2,5,2026))
# print(clsLunarCache.get_current_hour_info(now.day, now.month, now.year))
