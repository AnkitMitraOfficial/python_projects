try:
    def add(a, b):
        return a + b

    def subtract(a, b):
        # Returns the difference
        return a  - b

    def divide(a, b):
        # Returns the quotient
        return a / b

    def mod(a, b):
        # Returns the reminder
        return a % b

    def power(a, b):
        # Returns the value after exponention
        return a ** b

    def multiply(a, b):
        return a * b

except Exception as e:
    print('Error: ', e)