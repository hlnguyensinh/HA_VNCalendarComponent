from datetime import date, timedelta, datetime

from .vnlunar import VNLunar
from .const import TIME_ZONE

####--------------------------------------------------------------------


class VNLunarCache:

    def __init__(self, timeZone: int = TIME_ZONE) -> None:
        self.timeZone = timeZone

        self.cache = {}

        self.clsLunar = VNLunar()

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

            lunar = self.clsLunar.convertSolar2Lunar(
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


####--------------------------------------------------------------------

# from datetime import datetime

# clsLunarCache = VNLunarCache()
# clsLunarCache.preload([2022,2023,2024,2025,2026,2027,2028,2029])
# print(clsLunarCache.buildYear(2026))
# print(clsLunarCache.get(now.day, now.month, now.year))
# print(clsLunarCache.get_month(now.month, now.year))
# print(clsLunarCache.get_year(now.year))
# print(clsLunarCache.today())
# print(clsLunarCache.cleanup())
