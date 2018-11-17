class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        slist = sentence.split()
        result = ""
        for s in slist:
            for root in dict:
                if s.startswith(root):
                    s = root
            result += s + " "
        
        return result[:-1]