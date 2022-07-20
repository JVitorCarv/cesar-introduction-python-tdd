class InvalidArgumentError(Exception):
    pass


class MultError(Exception):
    pass


class Calculator:
    def verify_input(self, *info):
        for i in info:
            if type(i) is not int and type(i) is not float:
                raise InvalidArgumentError(f'{i} is not a valid number')

    def add(self, *nums):
        self.verify_input(*nums)

        sum_total = 0
        for num in nums:
            sum_total += num
        return sum_total

    def sub(self, *nums):
        if len(nums) == 0:
            return 0

        self.verify_input(*nums)

        res = nums[0]
        if len(nums) == 1:
            return res
        for i in range(len(nums) - 1):
            res -= nums[i + 1]
        return res

    def mult(self, *nums):
        self.verify_input(*nums)

        res = 1
        for num in nums:
            res *= num
        if res == 0:
            raise MultError("Multiplication by zero")
        return res

    def div(self, *nums):
        self.verify_input(*nums)

        if 0 in nums:
            return 0
        res = nums[0]
        for i in range(len(nums) - 1):
            res /= nums[i+1]
        return res

    def avg(self, *nums):
        if len(nums) == 0:
            return 0
        total = self.add(*nums)
        res = total / len(nums)
        return res
