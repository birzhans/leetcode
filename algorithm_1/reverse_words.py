def reverse_words(s):
    words = s.split()
    result = ''
    for word in words:
        reversed_word = word[::-1]
        result += reversed_word + ' '
        
    return result[:-1]

 s = "Let's take LeetCode contest"
 print(reverse_words(s))