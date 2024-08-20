import graphviz


def draw_dfa(dfa):
    states, alphabet, start_state, final_states, transitions = dfa

    graph = graphviz.Digraph(format='png')
    graph.attr(rankdir='LR')  # Left to right layout

    for state in states:
        node_label = state
        if state == start_state:
            graph.node(state, label=node_label, shape='circle')
            graph.node('', label='', shape='none')
            graph.edge('', state)
            continue
        if state in final_states:
            graph.node(state, label=node_label, shape='doublecircle')
            continue
        graph.node(state, label=node_label, shape='circle')

    trash_state = ""
    for state in states:
        if state not in transitions:
            continue
        if transitions[state] == {}:
            trash_state = state
            graph.node(state, label=state, shape='circle')
            break

    for state in states:
        if state not in transitions:
            continue
        for symbol, next_state in transitions[state].items():
            if isinstance(next_state, set):
                next_state = ', '.join(next_state)
            graph.edge(state, next_state, label=symbol)

    for state in states:
        for symbol in alphabet:
            if state not in transitions:
                graph.edge(state, trash_state, label=symbol)
                continue
            if symbol not in transitions[state]:
                graph.edge(state, trash_state, label=symbol)

    graph.render('dfa_graph', view=True)
