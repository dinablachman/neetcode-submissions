class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        start = 0
        stop = len(heights) - 1

        while (start < stop):
            height = min(heights[start], heights[stop])
            width = stop - start
            area = height * width
            if (area > max_area):
                max_area = area
            if (heights[start] < heights[stop]):
                start = start + 1
            elif (heights[start] > heights[stop]):
                stop = stop - 1
            else:
                start = start + 1
                stop = stop - 1
        
        return max_area