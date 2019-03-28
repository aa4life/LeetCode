class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        oneup = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        tenup = ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        hundred = ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        thousand = ["M", "MM", "MMM"]
        
        result = ""
        if num >= 1000:
            result += thousand[num//1000 -1]
            num = num % 1000
        
        if num >= 100:
            result += hundred[num//100 - 1]
            num = num % 100
        
        if num >= 10:
            result += tenup[num//10 - 1]
            num = num % 10
        
        if num >= 1:
            result += oneup[num - 1]
        
        return result