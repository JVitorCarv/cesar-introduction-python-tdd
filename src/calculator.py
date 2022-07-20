class InvalidArgumentError(Exception):
    pass


class Calculator:
    def verify_input(self, *info):
        for i in info:
            if type(i) is not int and type(i) is not float:
                raise InvalidArgumentError(f'{i} is not a valid number')

    def add(self, *nums):
        if type(nums) == list:
            raise InvalidArgumentError()

        self.verify_input(*nums)
        sum_total = 0
        if len(nums) == 0:
            return 0
        for num in nums:
            sum_total += num
        return sum_total
