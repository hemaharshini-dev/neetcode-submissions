class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                mid = stack.pop()

                width = i - stack[-1] - 1 if stack else i
                area = heights[mid] * width

                max_area = max(max_area, area)

            stack.append(i)

        # Process remaining bars
        n = len(heights)

        while stack:
            mid = stack.pop()

            width = n - stack[-1] - 1 if stack else n
            area = heights[mid] * width

            max_area = max(max_area, area)

        return max_area