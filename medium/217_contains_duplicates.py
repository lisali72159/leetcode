# Contains duplicates: Return true if there are duplicates in given array, else return false

def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]] = 1
            else:
                dict[nums[i]] += 1
                
                if dict[nums[i]] == 2:
                    return True
            
        return False 