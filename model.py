from collections import defaultdict


def nfa_to_dfa(states, alphabet, start_state, final_states, nfa_transitions):
    dfa_transitions = defaultdict(dict)

    def epsilon_closure(closure_states):
        closure = set(closure_states)
        for state in closure_states:
            if "$" in nfa_transitions[state]:
                closure.update(epsilon_closure(nfa_transitions[state]["$"]))
        return closure

    def move(move_states, move_symbol):
        next_states_move = set()
        for state in move_states:
            if move_symbol in nfa_transitions[state]:
                next_states_move.update(nfa_transitions[state][move_symbol])
        return next_states_move

    unprocessed_states = [frozenset(epsilon_closure({start_state}))]
    dfa_start_state = unprocessed_states[0]
    dfa_final_states = set()

    while unprocessed_states:
        current_state = unprocessed_states.pop()

        if final_states.intersection(current_state):
            dfa_final_states.add(current_state)

        for symbol in alphabet:
            next_states = epsilon_closure(move(current_state, symbol))
            if not next_states:
                continue

            dfa_transitions[current_state][symbol] = frozenset(next_states)

            if frozenset(next_states) not in dfa_transitions:
                unprocessed_states.append(frozenset(next_states))

    dfa_states = set(dfa_transitions.keys())
    dfa_states.add(dfa_transitions.values())

    return dfa_states, alphabet, dfa_start_state, dfa_final_states, dfa_transitions


def is_accepted_by_dfa(dfa, string):
    states, alphabet, start_state, final_states, transitions = dfa

    current_state = start_state
    for symbol in string:
        if symbol not in alphabet:
            return False
        if symbol not in transitions[current_state]:
            return False
        current_state = transitions[current_state][symbol]

    return current_state in final_states


def rename_dfa(dfa):
    states, alphabet, start_state, final_states, transitions = dfa
    temp_states = {start_state: 'q0'}
    new_states = ['q0']
    i = 1
    for state in states:
        if state != start_state:
            temp_states[state] = 'q' + str(i)
            new_states.append('q' + str(i))
            i += 1
    for final_state in final_states:
        if final_state not in temp_states.keys():
            temp_states[final_state] = 'q' + str(i)
            new_states.append('q' + str(i))

    new_start_state = temp_states[start_state]

    new_final_states = set()
    for state in final_states:
        new_final_states.add(temp_states[state])
    new_transitions = {}
    for state in states:
        new_transitions[temp_states[state]] = {}
        for symbol in alphabet:
            if symbol in transitions[state]:
                new_transitions[temp_states[state]][symbol] = temp_states[transitions[state][symbol]]

    return new_states, alphabet, new_start_state, new_final_states, new_transitions
