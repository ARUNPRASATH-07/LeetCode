class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #Intalizing the array of 26 places and dict
        
        anagram_map = {}  #to define what will be inside the dict
        for s in strs:
            ch = [0] * 26
            for i in s:
                
                ch[ord(i) - ord('a')] +=1 # 80 - 80 = 0 keeping the value in the array at 0th index
                #key is generated but it is mutable in array so we have to use tuple
            key = tuple(ch)
            #Hashmap is introduced here to keep the values in the respective key
            if key not in anagram_map:
                 anagram_map[key] = []
            anagram_map[key].append(s)
        return list(anagram_map.values())