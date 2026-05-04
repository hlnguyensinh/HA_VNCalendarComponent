from .vnlunar import VNLunar

from .const import TIME_ZONE

####--------------------------------------------------------------------

class VNLunarExtra:
    
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

    THOI_THAN_HOUR = {
        "Tý": "23:00-01:00",
        "Sửu": "01:00-03:00",
        "Dần": "03:00-05:00",
        "Mão": "05:00-07:00",
        "Thìn": "07:00-09:00",
        "Tỵ": "09:00-11:00",
        "Ngọ": "11:00-13:00",
        "Mùi": "13:00-15:00",
        "Thân": "15:00-17:00",
        "Dậu": "17:00-19:00",
        "Tuất": "19:00-21:00",
        "Hợi": "21:00-23:00",
    }

    HOANG_DAO_HOUR_TABLE = {
        "Tý": ["Tý", "Sửu", "Mão", "Ngọ", "Thân", "Dậu"],
        "Sửu": ["Dần", "Mão", "Tỵ", "Thân", "Tuất", "Hợi"],
        "Dần": ["Tý", "Sửu", "Thìn", "Tỵ", "Mùi", "Tuất"],
        "Mão": ["Dần", "Mão", "Ngọ", "Mùi", "Dậu", "Tý"],
        "Thìn": ["Thìn", "Tỵ", "Thân", "Dậu", "Hợi", "Dần"],
        "Tỵ": ["Ngọ", "Mùi", "Tuất", "Hợi", "Sửu", "Thìn"],
        "Ngọ": ["Tý", "Sửu", "Mão", "Ngọ", "Thân", "Dậu"],
        "Mùi": ["Dần", "Mão", "Tỵ", "Thân", "Tuất", "Hợi"],
        "Thân": ["Tý", "Sửu", "Thìn", "Tỵ", "Mùi", "Tuất"],
        "Dậu": ["Dần", "Mão", "Ngọ", "Mùi", "Dậu", "Tý"],
        "Tuất": ["Thìn", "Tỵ", "Thân", "Dậu", "Hợi", "Dần"],
        "Hợi": ["Ngọ", "Mùi", "Tuất", "Hợi", "Sửu", "Thìn"],
    }

    def __init__(self, timeZone: int = TIME_ZONE) -> None:
        self.timeZone = timeZone

        self.clsLunar = VNLunar()

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
        jd = self.clsLunar.jdFromDate(dd, mm, yy)
        return self.canChiDay(jd)

    def solarTerm(self, jd: int, timeZone: int) -> list:
        L = self.clsLunar.SunLongitude(jd - 0.5 - timeZone / 24)
        degree = (L * 180) / self.clsLunar.PI

        index = self.clsLunar.INT(degree / 15)
        return self.SOLAR_TERM_EMOJI[index]

    def solarTermFromSolar(self, dd: int, mm: int, yy: int, timeZone: int) -> list:
        jd = self.clsLunar.jdFromDate(dd, mm, yy)
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
    
    def getThoiThan(self) -> dict:
        return self.THOI_THAN_HOUR
    
    def goodHours(self, dayCanChi: str) -> list:
        if not dayCanChi:
            return []

        parts = dayCanChi.split(" ")

        if len(parts) < 2:
            return []

        chi = parts[1]

        goodhours_table = self.HOANG_DAO_HOUR_TABLE.get(chi, [])

        return [
            {
                "name": hour,
                "time": self.THOI_THAN_HOUR.get(hour),
            }
            for hour in goodhours_table
        ]

    def getLunarDay(self, dd, mm, yy, timeZone) -> dict:
        dayinfo = self.clsLunar.convertSolar2Lunar(dd, mm, yy, timeZone)
        dayNumber = self.clsLunar.jdFromDate(dd, mm, yy)

        lunarDay = dayinfo[0];
        lunarMonth = dayinfo[1];
        lunarYear = dayinfo[2];
        lunarLeap = dayinfo[3];

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

            "timeZone": timeZone,
            "solarTerm": self.solarTerm(dayNumber, timeZone),
            "dayType": self.dayType(lunarMonth, self.canChiDay(dayNumber)),
            "isVeg": self.isVegDay(lunarDay),
            "goodHours": self.goodHours(self.canChiDay(dayNumber)),
        }

####--------------------------------------------------------------------

# from datetime import datetime

# now = datetime.now()
# clsLunar = VNLunarExtra()

# print(clsLunar.getLunarDay(now.day, now.month, now.year, 7))

# from datetime import datetime

# if __name__ == "__main__":
#     now = datetime.now()
#     clsLunar = VNLunar()