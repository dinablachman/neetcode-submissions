class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        water_levels = [0] * len(height)
        if (len(height) < 3):
            # 3 is min needed for trapping water
            return 0

        left_bar = 0
        right_bar = 0
        # left to right pass
        for i in range(len(height)):
            water_levels[i] = left_bar
            if(height[i] > left_bar):
                # update for the next pass
                left_bar = height[i]
        
        for j in range(len(height) - 1, -1, -1):
            water_levels[j] = min(water_levels[j], right_bar)
            if(height[j] > right_bar):
                # update for the next pass
                right_bar = height[j]
                
        for k in range(len(height)):
            total_water = total_water + max(0, water_levels[k] - height[k])  
    
        return total_water

