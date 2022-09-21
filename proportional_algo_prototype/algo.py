class Algo:

    def __init__(self, budgets):
        self.budgets = []
        self.counters = []
        self.target_ratios = []
        self.actual_ratios = []
        self.last_arrangement = []
        self.update_params(budgets)

    def info(self):
        result = []

        for i in range(len(self.budgets)):
            rec = {
                'Budget': f'{self.budgets[i]:,.0f}',
                'Target ratio': f'{self.target_ratios[i] * 100:.2f}%',
                'Views': f'{self.counters[i]}',
                'Actual ratio': f'{self.actual_ratios[i] * 100:.2f}%',
                'Error': f'{self.__error(self.target_ratios[i], self.actual_ratios[i]):.03f}'
            }
            result.append(rec)

        return result

    def visit(self, n_cards):
        self.last_arrangement = [self.__view() for i in range(n_cards)]

    def __view(self):
        total_count = sum(self.counters)
        delta = 1 / (total_count + 1)
        best_improvement = self.__error_delta(
            target=self.target_ratios[0],
            actual=self.counters[0] / (total_count + 1),
            delta=delta
        )
        best_index = 0
        for i in range(len(self.counters)):
            cur_error_delta = self.__error_delta(
                target=self.target_ratios[i],
                actual=self.counters[i] / (total_count + 1),
                delta=delta
            )
            if cur_error_delta < best_improvement:
                best_index = i
                best_improvement = cur_error_delta
        self.counters[best_index] += 1
        total_count += 1
        self.actual_ratios = [counter / total_count for counter in self.counters]

        return best_index

    def __error_delta(self, target, actual, delta):
        return self.__error(target, actual + delta) - self.__error(target, actual)

    def __error(self, target, actual):
        if actual > target:
            return actual / target - 1

        return target - actual

    def update_params(self, budgets):
        self.budgets = budgets
        n = len(budgets)
        total = sum(budgets)
        total_count = sum(self.counters)
        if len(self.counters) != len(budgets):
            self.counters = [0 for _ in budgets]
            self.last_arrangement = []

        self.target_ratios = [x / total for x in budgets]
        self.actual_ratios = [self.counters[i] / total_count if total_count != 0 else 0 for i in range(n)]

    def reset_counters(self):
        self.counters = [0 for _ in self.budgets]
        self.last_arrangement = []
