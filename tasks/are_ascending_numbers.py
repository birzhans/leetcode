# No. 2042

def are_numbers_ascending(s):
    tokens = s.split()
    last_number = None
    
    for token in tokens:
        if token.isnumeric():
            current_number = int(token)
            if last_number and current_number <= last_number:
                return False
            last_number = current_number
    return True

s = "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"
print(are_numbers_ascending(s))            

        