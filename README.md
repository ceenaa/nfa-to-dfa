# NFA to DFA Converter and Sequence Validator
## Overview
This project implements a tool to convert a Nondeterministic Finite Automaton (NFA) into a Deterministic Finite Automaton (DFA), checks if a given sequence is accepted by the DFA, and visualizes the DFA as a graph. The tool is designed to help in understanding and verifying finite automaton concepts by providing a clear conversion and visualization process.

## Features
* NFA to DFA Conversion: Converts any given NFA into an equivalent DFA using state transitions and epsilon closures.
* Sequence Validation: Checks if a given input sequence is accepted by the constructed DFA.
* Graphical Visualization: Draws the DFA using graph visualization tools to provide an intuitive representation of state transitions.

## Project Structure
* main.py: The main entry point of the application. It handles user input, converts the NFA to a DFA, and checks if sequences are accepted by the DFA.
* model.py: Contains the core logic for NFA to DFA conversion, DFA state validation, and DFA renaming.
* draw.py: Handles the graphical representation of the DFA using the graphviz library.

## Dependencies
* Python 3.x
* graphviz library for drawing the DFA graph

You can install the required dependencies using:

```
pip install -r requirements.txt
```

## Usage
1. Run the Main Program: The main.py file is the entry point. You will be prompted to input the details of the NFA, including the states, alphabet, transitions, start state, and final states.
```
python main.py
```
2. Input Format:

* Number of states q, alphabet size s, number of accepting states a, number of transitions m, and number of sequences n.
* Followed by the alphabet symbols, start state, accepting states, and transitions in the format start_state symbol end_state.
  
3. Validation: After converting the NFA to DFA, the program will validate whether the provided sequences are accepted by the DFA.

4. Graphical Output: The resulting DFA will be saved as an image (dfa_graph.png) in the root directory, providing a visual representation of the DFA.

## Example
Suppose you have the following NFA:

* States: q0, q1, q2
* Alphabet: 0, 1
* Start State: q0
* Accepting States: q2
* Transitions:
  * q0 --0--> q0, q1
  * q1 --1--> q2
After running the tool, the equivalent DFA will be generated, and you will be able to check if specific sequences are accepted by this DFA. Additionally, a graphical representation of the DFA will be saved.

### Sample DFA

![dfa_graph](https://github.com/user-attachments/assets/9845e118-cc8d-472b-8440-95ce0697e28e)

