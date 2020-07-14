class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        if hour == 12:
            hour = 0
        newHour = hour * 30
        newMinutes = minutes * 6
        hourCalc = newHour + (minutes / 2)
        res = abs(hourCalc - newMinutes)
        if res > 180:
            dif = res - 180
            res = res - (dif * 2)
        return res

# One liner I did not come up with
# return min(abs(30*hour-5.5*minutes),360-abs(30*hour-5.5*minutes))