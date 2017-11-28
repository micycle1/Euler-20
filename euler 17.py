def euler_17():
    return sum (len(word) for n in range(1, 1000) for word in n_to_string(n)) + sum(len(word) for word in ["one", "thousand"])

def n_to_string(n):
    words = []
    tens = ["", "", 'twenty', 'thirty', 'forty', 'fifty', 'sixty',
                'seventy', 'eighty', 'ninety']
    digits = ["", 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
                  'eight', 'nine']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
                 'sixteen', 'seventeen', 'eighteen', 'nineteen']

    if len(str(n)) == 3 or len(str(n)) == 1:
        words.append(digits[int(str(n)[0])])
    
    if len(str(n)) == 3:
        words.append("hundred")
        
        if not ((str(n)[2] is "0") and (str(n)[1] is "0")):
            words.append("and")
            
        if str(n)[1] == "0" or int(str(n)[1]) > 1:
            words.append(digits[int(str(n)[2])])
            
        if str(n)[1] == "1":
            words.append(teens[int(str(n)[2])])
            
        words.append(tens[int(str(n)[1])])
            
    if len(str(n)) == 2:
        if int(str(n)[0]) > 1:
            words.append(tens[int(str(n)[0])])
            words.append(digits[int(str(n)[1])])
        else:
            words.append(teens[int(str(n)[1])])
            
    return words
