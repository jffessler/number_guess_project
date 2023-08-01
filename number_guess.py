class randomNumber:

    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        bounds_set = set()
        random_number_str = ""
        random_number = -1

        def oneDigit():
            #import time
            import time
            #use time method to generate a random number from 0-9
            current_time = time.time()
            time_string = repr(current_time)
            final_str_num = time_string[-2]
            # final_num = int(final_str_num)
            # print(final_num)
            return final_str_num
        
        #building the random number
        bounds = self.upper_bound + 1 - self.lower_bound
        str_bounds = repr(bounds)

        if self.lower_bound < 0 or self.upper_bound < 0:
            return print("Range must be greater than or equal to 0")
        else:
            #making a set of all potential numbers
            for x in range(self.lower_bound, self.upper_bound+1):
                bounds_set.add(x)
                print(bounds_set)

        while random_number not in bounds_set:
                #selecting random digits
                print(random_number)
                for x in range(len(str_bounds)):
                    print(f'loop {x}')
                    one_digit = oneDigit()
                    print(f'one_digit {one_digit}')
                    random_number_str += one_digit
                random_number = int(random_number_str)
                # print(random_number)

        return print(random_number)
        
        

number = randomNumber(1,10)