def calculate_result(x, y, z):
    try:
        result = (y - z) / x
        total_result = result * 100
        return total_result
    except ZeroDivisionError:
        print("Error: Division by zero. Please enter a non-zero value for total PI/BI.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# Get user input for total PI/BI, total triangles, and total squares
x = int(input("Enter total PI/BI:"))
y = int(input("Enter Total Triangle:"))
z = int(input("Enter Total Square:"))

# Calculate the result
result = calculate_result(x, y, z)

# Print the result if calculation was successful
if result is not None:
    print("Total Result:", result, "%")
