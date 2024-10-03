class Solution:
    def romanToInt(self, s: str) -> int:
    
    # Dictionary to map Roman numerals to their respective values
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
        total = 0  # Initialize the total sum
        prev_value = 0  # To track the value of the previous Roman numeral character
    
    # Iterate over the string in reverse order
        for char in reversed(s):
            value = roman_dict[char]
        
        # If the current value is smaller than the previous one, subtract it
            if value < prev_value:
                total -= value
            else:
                total += value  # Otherwise, add it to the total
        
                prev_value = value  # Update the previous value to current one