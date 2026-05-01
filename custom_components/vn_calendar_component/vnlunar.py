import math

from .const import TIME_ZONE

####--------------------------------------------------------------------


class VNLunar:
    PI = math.pi

    CAN = [
        "Giáp",
        "Ất",
        "Bính",
        "Đinh",
        "Mậu",
        "Kỷ",
        "Canh",
        "Tân",
        "Nhâm",
        "Quý",
    ]

    CHI = [
        "Tý",
        "Sửu",
        "Dần",
        "Mão",
        "Thìn",
        "Tỵ",
        "Ngọ",
        "Mùi",
        "Thân",
        "Dậu",
        "Tuất",
        "Hợi",
    ]

    SOLAR_TERM_EMOJI = [
        # 🌸 Xuân
        ["Xuân phân", "🌸"],
        ["Thanh minh", "🌿"],
        ["Cốc vũ", "🌧️"],
        # ☀️ Hạ
        ["Lập hạ", "🌱"],
        ["Tiểu mãn", "🌾"],
        ["Mang chủng", "🌾"],
        ["Hạ chí", "☀️"],
        ["Tiểu thử", "🌤️"],
        ["Đại thử", "🔥"],
        # 🍂 Thu
        ["Lập thu", "🍃"],
        ["Xử thử", "🌬️"],
        ["Bạch lộ", "💧"],
        ["Thu phân", "🍂"],
        ["Hàn lộ", "❄️"],
        ["Sương giáng", "🌫️"],
        # ❄️ Đông
        ["Lập đông", "🌨️"],
        ["Tiểu tuyết", "❄️"],
        ["Đại tuyết", "☃️"],
        ["Đông chí", "🌙"],
        ["Tiểu hàn", "🥶"],
        ["Đại hàn", "🧊"],
        # 🌱 Cuối đông → xuân
        ["Lập xuân", "🌱"],
        ["Vũ thủy", "🌧️"],
        ["Kinh trập", "⚡"],
    ]

    HOANG_DAO = [
        ["Hắc đạo", "⚡"],
        ["Hoàng đạo", "🍀"],
    ]

    HOANG_DAO_TABLE = {
        1: ["Tý", "Sửu", "Tỵ", "Mùi"],
        2: ["Dần", "Mão", "Mùi", "Dậu"],
        3: ["Thìn", "Tỵ", "Dậu", "Hợi"],
        4: ["Ngọ", "Mùi", "Hợi", "Sửu"],
        5: ["Thân", "Dậu", "Sửu", "Mão"],
        6: ["Tuất", "Hợi", "Mão", "Tỵ"],
        7: ["Tý", "Sửu", "Tỵ", "Mùi"],
        8: ["Dần", "Mão", "Mùi", "Dậu"],
        9: ["Thìn", "Tỵ", "Dậu", "Hợi"],
        10: ["Ngọ", "Mùi", "Hợi", "Sửu"],
        11: ["Thân", "Dậu", "Sửu", "Mão"],
        12: ["Tuất", "Hợi", "Mão", "Tỵ"],
    }

    BUDDHA_EVENTS = {
        "1-1": ["Di Lặc Bồ Tát"],
        "8-2": ["Phật Thích Ca xuất gia"],
        "15-2": ["Phật Thích Ca nhập Niết Bàn"],
        "19-2": ["Quan Âm đản sinh"],
        "21-2": ["Phổ Hiền Bồ Tát"],
        "16-3": ["Phật Thích Ca đản sinh (Nam tông)"],
        "4-4": ["Văn Thù Bồ Tát"],
        "8-4": ["Phật Thích Ca đản sinh (Bắc tông)"],
        "15-4": ["Phật Thích Ca thành đạo"],
        "13-6": ["Quan Âm thành đạo"],
        "15-7": ["Vu Lan (Ullambana)"],
        "19-6": ["Quan Âm thành đạo"],
        "30-7": ["Địa Tạng Vương Bồ Tát"],
        "22-9": ["Dược Sư Phật"],
        "19-9": ["Quan Âm xuất gia"],
        "8-12": ["Phật Thích Ca thành đạo"],
    }

    VEG_DAY = [1, 15]

    def INT(self, d: float) -> int:
        return math.floor(d)

    def jdFromDate(self, dd: int, mm: int, yy: int) -> int:
        a = self.INT((14 - mm) / 12)
        y = yy + 4800 - a
        m = mm + 12 * a - 3

        jd = (
            dd
            + self.INT((153 * m + 2) / 5)
            + 365 * y
            + self.INT(y / 4)
            - self.INT(y / 100)
            + self.INT(y / 400)
            - 32045
        )
        if jd < 2299161:
            jd = dd + self.INT((153 * m + 2) / 5) + 365 * y + self.INT(y / 4) - 32083

        return jd

    def jdToDate(self, jd: int) -> list:
        if jd > 2299160:
            a = jd + 32044
            b = self.INT((4 * a + 3) / 146097)
            c = a - self.INT((b * 146097) / 4)
        else:
            b = 0
            c = jd + 32082

        d = self.INT((4 * c + 3) / 1461)
        e = c - self.INT((1461 * d) / 4)
        m = self.INT((5 * e + 2) / 153)
        day = e - self.INT((153 * m + 2) / 5) + 1
        month = m + 3 - 12 * self.INT(m / 10)
        year = b * 100 + d - 4800 + self.INT(m / 10)

        return [day, month, year]

    def NewMoon(self, k: int) -> float:
        T = k / 1236.85
        T2 = T * T
        T3 = T2 * T
        dr = self.PI / 180
        Jd1 = 2415020.75933 + 29.53058868 * k + 0.0001178 * T2 - 0.000000155 * T3
        Jd1 = Jd1 + 0.00033 * math.sin((166.56 + 132.87 * T - 0.009173 * T2) * dr)
        M = 359.2242 + 29.10535608 * k - 0.0000333 * T2 - 0.00000347 * T3
        Mpr = 306.0253 + 385.81691806 * k + 0.0107306 * T2 + 0.00001236 * T3
        F = 21.2964 + 390.67050646 * k - 0.0016528 * T2 - 0.00000239 * T3
        C1 = (0.1734 - 0.000393 * T) * math.sin(M * dr) + 0.0021 * math.sin(2 * dr * M)
        C1 = C1 - 0.4068 * math.sin(Mpr * dr) + 0.0161 * math.sin(dr * 2 * Mpr)
        C1 = C1 - 0.0004 * math.sin(dr * 3 * Mpr)
        C1 = C1 + 0.0104 * math.sin(dr * 2 * F) - 0.0051 * math.sin(dr * (M + Mpr))
        C1 = (
            C1 - 0.0074 * math.sin(dr * (M - Mpr)) + 0.0004 * math.sin(dr * (2 * F + M))
        )
        C1 = (
            C1
            - 0.0004 * math.sin(dr * (2 * F - M))
            - 0.0006 * math.sin(dr * (2 * F + Mpr))
        )
        C1 = (
            C1
            + 0.001 * math.sin(dr * (2 * F - Mpr))
            + 0.0005 * math.sin(dr * (2 * Mpr + M))
        )

        if T < -11:
            deltat = (
                0.001
                + 0.000839 * T
                + 0.0002261 * T2
                - 0.00000845 * T3
                - 0.000000081 * T * T3
            )
        else:
            deltat = -0.000278 + 0.000265 * T + 0.000262 * T2

        JdNew = Jd1 + C1 - deltat

        return JdNew

    def SunLongitude(self, jdn: float) -> float:
        T = (jdn - 2451545.0) / 36525
        T2 = T * T
        dr = self.PI / 180
        M = 357.5291 + 35999.0503 * T - 0.0001559 * T2 - 0.00000048 * T * T2
        L0 = 280.46645 + 36000.76983 * T + 0.0003032 * T2
        DL = (1.9146 - 0.004817 * T - 0.000014 * T2) * math.sin(dr * M)
        DL = (
            DL
            + (0.019993 - 0.000101 * T) * math.sin(dr * 2 * M)
            + 0.00029 * math.sin(dr * 3 * M)
        )
        L = L0 + DL
        L = L * dr
        L = L - self.PI * 2 * self.INT(L / (self.PI * 2))
        return L

    def getSunLongitude(self, dayNumber: int, timeZone: int) -> int:
        return self.INT(
            (self.SunLongitude(dayNumber - 0.5 - timeZone / 24) / self.PI) * 6
        )

    def getNewMoonDay(self, k: int, timeZone: int) -> int:
        return self.INT(self.NewMoon(k) + 0.5 + timeZone / 24)

    def getLunarMonth11(self, yy: int, timeZone: int) -> int:
        # off = jdFromDate(31, 12, yy) - 2415021.076998695;
        off = self.jdFromDate(31, 12, yy) - 2415021
        k = self.INT(off / 29.530588853)
        nm = self.getNewMoonDay(k, timeZone)
        sunLong = self.getSunLongitude(nm, timeZone)
        if sunLong >= 9:
            nm = self.getNewMoonDay(k - 1, timeZone)

        return nm

    def getLeapMonthOffset(self, a11: float, timeZone: int) -> int:
        k = self.INT((a11 - 2415021.076998695) / 29.530588853 + 0.5)

        last = 0
        i = 1
        arc = self.getSunLongitude(self.getNewMoonDay(k + i, timeZone), timeZone)

        while True:
            last = arc

            i += 1

            arc = self.getSunLongitude(
                self.getNewMoonDay(k + i, timeZone),
                timeZone,
            )

            if arc == last or i >= 14:
                break

        return i - 1

    def canChiYear(self, lunarYear: int) -> str:
        return self.CAN[(lunarYear + 6) % 10] + " " + self.CHI[(lunarYear + 8) % 12]

    def canChiMonth(self, lunarYear: int, lunarMonth: int) -> str:
        yearCan = (lunarYear + 6) % 10
        canIndex = (yearCan * 2 + lunarMonth + 1) % 10
        chiIndex = (lunarMonth + 1) % 12

        return self.CAN[canIndex] + " " + self.CHI[chiIndex]

    def canChiDay(self, jd: int) -> str:
        return self.CAN[(jd + 9) % 10] + " " + self.CHI[(jd + 1) % 12]

    def canChiDayFromSolar(self, dd: int, mm: int, yy: int) -> str:
        jd = self.jdFromDate(dd, mm, yy)
        return self.canChiDay(jd)

    def solarTerm(self, jd: int, timeZone: int) -> list:
        L = self.SunLongitude(jd - 0.5 - timeZone / 24)
        degree = (L * 180) / self.PI

        index = self.INT(degree / 15)
        return self.SOLAR_TERM_EMOJI[index]

    def solarTermFromSolar(self, dd: int, mm: int, yy: int, timeZone: int) -> list:
        jd = self.jdFromDate(dd, mm, yy)
        return self.solarTerm(jd, timeZone)

    def dayType(self, lunarMonth: int, dayCanChi: str) -> list:
        chi = dayCanChi.split(" ")[1]

        goodlist = self.HOANG_DAO_TABLE.get(lunarMonth, [])

        return self.HOANG_DAO[1] if chi in goodlist else self.HOANG_DAO[0]

    def isVegDay(self, lunarDay: int) -> bool:
        return True if lunarDay in self.VEG_DAY else False

    def buddhaEvents(self, lunarDay: int, lunarMonth: int) -> list:
        events = self.BUDDHA_EVENTS.get(str(lunarDay) + "-" + str(lunarMonth), [])
        return events

    def convertSolar2Lunar(self, dd: int, mm: int, yy: int, timeZone: int) -> dict:
        dayNumber = self.jdFromDate(dd, mm, yy)

        k = self.INT((dayNumber - 2415021.076998695) / 29.530588853)
        monthStart = self.getNewMoonDay(k + 1, timeZone)

        if monthStart > dayNumber:
            monthStart = self.getNewMoonDay(k, timeZone)

        a11 = self.getLunarMonth11(yy, timeZone)
        b11 = a11

        if a11 >= monthStart:
            lunarYear = yy
            a11 = self.getLunarMonth11(yy - 1, timeZone)
        else:
            lunarYear = yy + 1
            b11 = self.getLunarMonth11(yy + 1, timeZone)

        lunarDay = dayNumber - monthStart + 1
        diff = self.INT((monthStart - a11) / 29)

        lunarLeap = 0
        lunarMonth = diff + 11
        leapMonthDiff = 0

        if b11 - a11 > 365:
            leapMonthDiff = self.getLeapMonthOffset(a11, timeZone)
            if diff >= leapMonthDiff:
                lunarMonth = diff + 10
                if diff == leapMonthDiff:
                    lunarLeap = 1

        if lunarMonth > 12:
            lunarMonth = lunarMonth - 12

        if lunarMonth >= 11 and diff < 4:
            lunarYear -= 1

        return {
            "solar": {
                "day": dd,
                "month": mm,
                "year": yy,
            },
            "lunar": {
                "day": lunarDay,
                "month": lunarMonth,
                "year": lunarYear,
                "leap": True if lunarLeap else False,
                "canchi": {
                    "year": self.canChiYear(lunarYear),
                    "month": self.canChiMonth(lunarYear, lunarMonth),
                    "day": self.canChiDay(dayNumber),
                },
                "events": self.buddhaEvents(lunarDay, lunarMonth),
            },
            "timezone": timeZone,
            "solarTerm": self.solarTerm(dayNumber, timeZone),
            "dayType": self.dayType(lunarMonth, self.canChiDay(dayNumber)),
            "isVeg": self.isVegDay(lunarDay),
        }

    def convertLunar2Solar(
        self,
        lunarDay: int,
        lunarMonth: int,
        lunarYear: int,
        lunarLeap: int,
        timeZone: int,
    ) -> list:
        #  off, leapOff, leapMonth, monthStart;
        if lunarMonth < 11:
            a11 = self.getLunarMonth11(lunarYear - 1, timeZone)
            b11 = self.getLunarMonth11(lunarYear, timeZone)
        else:
            a11 = self.getLunarMonth11(lunarYear, timeZone)
            b11 = self.getLunarMonth11(lunarYear + 1, timeZone)

        k = self.INT(0.5 + (a11 - 2415021.076998695) / 29.530588853)
        off = lunarMonth - 11

        if off < 0:
            off += 12

        if b11 - a11 > 365:
            leapOff = self.getLeapMonthOffset(a11, timeZone)
            leapMonth = leapOff - 2
            if leapMonth < 0:
                leapMonth += 12

            if lunarLeap != 0 and lunarMonth != leapMonth:
                return [0, 0, 0]
            elif lunarLeap != 0 or off >= leapOff:
                off += 1

        monthStart = self.getNewMoonDay(k + off, timeZone)
        return self.jdToDate(monthStart + lunarDay - 1)

    def get_lunar_from_solar(
        self, day: int, month: int, year: int, timezone: int = TIME_ZONE
    ):
        return self.convertSolar2Lunar(
            day,
            month,
            year,
            timezone,
        )


####--------------------------------------------------------------------

# from datetime import datetime

# now = datetime.now()
# clsLunar = VNLunar()

# print(clsLunar.convertSolar2Lunar(now.day, now.month, now.year, 7))
# print(clsLunar.convertSolar2Lunar(2, 4, 2026, 7))
# print(clsLunar.convertLunar2Solar(13, 3, 2026, 0, 7))
