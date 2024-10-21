def function_a(x):
    try:
        result = (2 * x - 1) / (x + 3)
        return result
    except ZeroDivisionError:
        raise ValueError(f"Division by zero occurred at x = {x}")

def get_sign(value):
    if value > 0:
        return "Positive"
    elif value < 0:
        return "Negative"
    else:
        return "Zero"

if __name__ == '__main__':
    x = -3
    step = 0.5  # Step of 1/2
    sign = None
    while x <= 0.5:
        try:
            value = function_a(x)
            sign = get_sign(value)
            print(sign)
 # Break the loop if you find a solution
        except ValueError as e:
            print(e)  # Print the error message when division by zero occurs
            # Increment x and continue the loop
        x += step  # Increment by 0.5
