x = "0.2S10(123)"

# Correcting index logic
index1 = x.find("(") - x.find(".") - 1  # Length of non-repeating decimal
index2 = x.find(")") - x.find("(") - 1  # Length of repeating decimal
# Fixing function to use the passed string
def function_get_decimal(string, char1, char2):
    start_index = string.find(char1) + 1
    end_index = string.find(char2)
    return string[start_index:end_index]

# Extracting non-repeating and repeating parts
substring = function_get_decimal(x, ".", "(")  # Non-repeating part
substring2 = function_get_decimal(x, "(", ")")  # Repeating part

decimal1 = int(substring)
decimal2 = int(substring2)

# Calculate numerator
decimal = pow(10, index2) * decimal1 + decimal2 - decimal1
left_ex = pow(10, index1 + index2) - pow(10, index1)

# Display the result
print(str(decimal) + "/" + str(left_ex))
