from playsound import playsound

def function_sound():
    playsound('elMatadoor.mp3')

def get_hops(start, end):
    sum = 0
    for x in range(8):
        c1 = ord(start[-(x+1)])-96
        c2 = ord(end[-(x+1)]) - 96
        print(c1)
        print(c2)
        print(end[-(x+1)])
        sum += (c2 - c1) * (26**x)
        print(x)
        print(sum)
    return sum

