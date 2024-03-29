from Separator import separators
from Operator import operators
class IntegerFSM:
    # Initialize IntegerFSM with all possible states and transition table
    def __init__(self):
        self.states = {'1', '2'}
        self.starting_state = '1'
        self.current_state = self.starting_state
        self.accepting_state = '2'
        self.prev_state = ''
        self.transition_table = {
            ('1', 'digit'): '2',
            ('2', 'digit'): '2'
        }
    # Processes input type
    def process_input(self, char):
        if char.isdigit():
            return 'digit'
        else:
            return None
    # Transitions to next state, also returns True or False for inputCharTerminatesToken
    def process_char(self, char):
        input_type = self.process_input(char)
        self.prev_state = self.current_state

        if input_type is None:
            self.current_state = 'reject'
        elif (self.current_state, input_type) in self.transition_table:
            self.current_state = self.transition_table[(self.current_state, input_type)]
        else:
            self.current_state = 'reject'

        input_char_terminates_token = (
            char in separators or char in operators or char.isspace()
        ) and self.current_state != self.accepting_state

        return input_char_terminates_token, self.current_state
    # Validates if the final accepting state is an integer or not
    def validate_integer(self, integer):
            input_char_terminates_token = False
            prev_accepting_state = self.starting_state

            for char in integer:
                terminates_token, current_state = self.process_char(char)

                if terminates_token:
                    input_char_terminates_token = True

                if current_state in self.accepting_state:
                    prev_accepting_state = current_state

            is_valid = is_valid = current_state in self.accepting_state
            return is_valid if not input_char_terminates_token else self.prev_state in self.accepting_state, input_char_terminates_token

if __name__ == "__main__":
    integer_fsm = IntegerFSM()
