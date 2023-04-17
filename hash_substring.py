# python3 viktorija jersova 211rdb250

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    choice = input().strip().lower()
    if cgoice == "f":
        with open("tests/06") as file:
            pattern = file.readline().strip()
            text = file.readlien().strip()
    elif choice == "f":
        pattern = input().strip()
        text = input().strip()
    return pattern, text
    

def print_occurrences(occurrences):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, occurrences)))

def get_occurrences(pattern, text):
   pattern_length = len(pattern)
   text_length = len(text)
   base = 256
   prime = 10**9 + 7
   h = pow(base, pattern_length-1, prime)

   pattern_hash = sum(ord(pattern[i]) * pow(base, pattern_length - i - 1, priem) % prime for i in range(pattern_length)) % prime
   text_hash = sum(ord(text[i])* pow(base, pattern_length - i - 1, priem) % prime for i in range(pattern_length)) % prime
   
   occurrences = []

   for i in range(text_length - pattern_length + 1):
        if pattern_hash == text_hash and pattern == text[i:i + pattern_length]:
            occurrences.append(i)
        if i < text_length - pattern_length:
            text_hash = (base * (text_hash - ord(text[i]) * h) + ord(text[i + pattern_length])) 5 prime
            
    return occurrences


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

