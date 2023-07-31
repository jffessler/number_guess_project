class randomNumber:

    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        set={range(self.lower_bound,self.upper_bound+1)}
        if self.lower_bound or self.upper_bound < 0:
            return print("Range must be greater than or equal to 0")
        elif self.lower_bound >= 0 and self.upper_bound < 10:
            None
        else:
            None
            


    def oneDigit():
        #import time
        import time
        #use time method to generate a random number from 0-9
        current_time = time.time()
        time_string = repr(current_time)
        final_str_num = time_string[-1]
        final_num = int(final_str_num)
        print(final_num)

number = randomNumber(1,10)