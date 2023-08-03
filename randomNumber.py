class randomNumber:

    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        
    def random_number(self):
        #initialization
        bounds_set = set()
        random_number = -1
        #building the random number
        #checking for bounds issue and making a set of all potential numbers
        if self.lower_bound < 0 or self.upper_bound < 0:
            return print("Range must be greater than or equal to 0")
        else:
            None
            # for x in range(self.lower_bound, self.upper_bound+1):
            #     bounds_set.add(x)
        #selecting random digits, building the random number
        # print(bounds_set)
        # while random_number not in bounds_set:
        while random_number not in range(self.lower_bound,self.upper_bound+1):
            random_number_str = ""
            for x in range(len(repr(self.upper_bound+1))):
                one_digit = self.oneDigit()
                random_number_str += one_digit
            random_number = int(random_number_str)
        return random_number

    def oneDigit(self):
        #import time
        import time
        #use time method to generate a random number from 0-9
        current_time = time.time()
        time.sleep(0.00001)
        time_string = repr(current_time)
        final_str_num = time_string[-2]
        return final_str_num
        

# number = randomNumber(0,1000)
# print(number.random_number())