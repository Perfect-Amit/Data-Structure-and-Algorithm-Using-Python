class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days=[31,28,31,30,31,30,31,31,30,31,30,31]
        def convert(date):
            m,d=map(int,date.split('-'))
            return sum(days[:m-1])+d
        a1=convert(arriveAlice)
        a2=convert(leaveAlice)
        b1=convert(arriveBob)
        b2=convert(leaveBob)
        return max(0,min(a2,b2)-max(a1,b1)+1)