class IncError(Exception):
    pass


class Incrementer:

    def inc(self, value):

        def is_natural_int(info):
            if type(info) is int and info > 0:
                return True
            return False

        if is_natural_int(value):
            return value + 1

        if type(value) is list:
            for i in range(len(value)):
                if is_natural_int(value[i]):
                    value[i] = value[i] + 1
                else:
                    raise IncError(value)
            return value

        raise IncError(value)
