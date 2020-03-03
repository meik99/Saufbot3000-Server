
class Warning:
    def wrong_pump_count(self, correct_count, actual_count):
        return "Number of pins for pump control is unusual. Should be {}, but is {}.".format(correct_count, actual_count)