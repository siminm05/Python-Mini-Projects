'''
Anagram Checker

Given: s1 = "listen"  s2 = "silent
Rules:
- ignore capitalization and spaces
- dont use sorter(), Counter
'''

def main():
    s1 = "a gentleman" #"listen"
    s2 = "elegant man" #"silent"
    output = soln(s1,s2)
    print(output)

def soln(s1,s2):
    freq1 = {}
    freq2 = {}

    for i in s1.lower():
        if i.isalpha():
            if i not in freq1:
                freq1[i] = 1
            else:
                freq1[i] += 1

    for j in s2.lower():
        if j.isalpha():
            if j not in freq2:
                freq2[j] = 1
            else:
                freq2[j] += 1

    answer = False
    for i in freq1:
        for j in freq2:
            if i == j:
                if freq1[i] == freq2[j]:
                    answer = True
                else:
                    return False
    return answer
main()
