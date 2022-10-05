#Source code from https://github.com/PranayT17/Finding-FIRST-and-FOLLOW-of-given-grammar
#Edited by Joshua Edgel
#12/6/2021

import sys
sys.setrecursionlimit(60)

def first(string):
    first_ = set()
    if string in non_terminals:
        alternatives = productions_dict[string]

        for alternative in alternatives:
            first_2 = first(alternative)
            first_ = first_ |first_2

    elif string in terminals:
        first_ = {string}

    elif string=='' or string=='#':
        first_ = {'#'}

    else:
        first_2 = first(string[0])
        if '#' in first_2:
            i = 1
            while '#' in first_2:
                first_ = first_ | (first_2 - {'#'})
                if string[i:] in terminals:
                    first_ = first_ | {string[i:]}
                    break
                elif string[i:] == '':
                    first_ = first_ | {'#'}
                    break
                first_2 = first(string[i:])
                first_ = first_ | first_2 - {'#'}
                i += 1
        else:
            first_ = first_ | first_2
            
    return  first_

search_file = 'Input.txt'
terminals = []
non_terminals = []
productions = []

with open(search_file, 'r') as sf:
    i = 0
    for line in sf:
        i = i + 1
        non_terminals.append(line[0])
        productions.append(line.split("\n"))

        for c in line:
            if c.islower():
                terminals.append(c)


productions_dict = {}

for nT in non_terminals:
    productions_dict[nT] = []


for production in productions:
    nonterm_to_prod = production[0].split("->")
    alternatives = nonterm_to_prod[1].split("|")
    for alternative in alternatives:
        productions_dict[nonterm_to_prod[0]].append(alternative)


FIRST = {}

for non_terminal in non_terminals:
    FIRST[non_terminal] = set()


for non_terminal in non_terminals:
    FIRST[non_terminal] = FIRST[non_terminal] | first(non_terminal)

print("{: ^20}{: ^20}".format('Non Terminals','First'))
for non_terminal in non_terminals:
    print("{: ^20}{: ^20}".format(non_terminal,str(FIRST[non_terminal])))
