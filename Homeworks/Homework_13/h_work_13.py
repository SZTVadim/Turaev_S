class Test:
    def __init__(self, name, status="new", duration=None):
        self.name = name
        self.status = status
        self.duration = duration

    def can_run(self):
        return self.status == "new"

    def finish(self, result, duration):
        if not self.can_run():
            return False

        if result != "passed" and result != "failed":
            return False

        self.status = result
        self.duration = duration
        return True

    def is_slow(self):
        if self.duration is None:
            return None

        return self.duration >= 5


test_spec = Test("Тест ввода спецсимвола")

test_auth = Test("Тест авторизации")
test_auth.finish("passed", 6)

test_symb = Test("Тест на длину символов ")
test_symb.finish("failed", 3)
test_symb.finish("passed", 4)


print(test_spec.name, test_spec.can_run(), test_spec.is_slow(), test_spec.status)
print(test_auth.name, test_auth.can_run(), test_auth.is_slow(), test_auth.status)
print(test_symb.name, test_symb.can_run(), test_symb.is_slow(), test_symb.status)