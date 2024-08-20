from draw import draw_dfa
from model import is_accepted_by_dfa, nfa_to_dfa, rename_dfa

string = input()
string = string.split(' ')
q = int(string[0])
s = int(string[1])
a = int(string[2])
m = int(string[3])
n = int(string[4])

alphabet = {}
accept_states = {}
transitions = {}
start_state = 'q'
states = {}

for i in range(q):
    states[i] = 'q' + str(i)
    transitions[states[i]] = {}


for i in range(s):
    alphabet[i] = input()

q0 = input()
start_state = 'q' + q0

for i in range(a):
    accept_states[i] = 'q' + input()

for i in range(m):
    string = input()
    string = string.split(' ')
    start = 'q' + string[0]
    symbol = string[1]
    end = 'q' + string[2]
    if start not in transitions:
        transitions[start] = {}
    if symbol not in transitions[start]:
        transitions[start][symbol] = set()
    transitions[start][symbol].add(end)

nfa = (
    set(states.values()),
    set(alphabet.values()),
    start_state,
    set(accept_states.values()),
    transitions
)

dfa = nfa_to_dfa(*nfa)

new_dfa = rename_dfa(dfa)
draw_dfa(new_dfa)

for i in range(n):
    string = input()
    if is_accepted_by_dfa(dfa, string):
        print('Yes')
    else:
        print('No')
