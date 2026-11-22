def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

print(f"10°C = {celsius_to_fahrenheit(10):.1f}°F")
print(f"100°C = {celsius_to_fahrenheit(100):.1f}°F")

print(f"50°F = {fahrenheit_to_celsius(50):.1f}°C")
print(f"212°F = {fahrenheit_to_celsius(212):.1f}°C")