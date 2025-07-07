from collections import Counter

class PersonInfo:
    def __init__(self, fi, age, *deps):
        self.fi = fi
        self.age = age
        self.deps = deps

    def short_name(self):
        """Краткая запись Фамилия И."""
        # todo Здесь нужно написать код
        parts = self.fi.split()
        if len(parts) >= 2:
            return f"{parts[1]} {parts[0][0]}."
        else:
            return self.fi

    def path_deps(self):
        """Путь до подразделения"""
        # todo Здесь нужно написать код
        return " --> ".join(self.deps)

    def new_salary(self):
        """Новая зарплата"""
        # todo Здесь нужно написать код
        combined_deps = "".join(self.deps)
        letter_counts = Counter(combined_deps)
        most_common_letter = letter_counts.most_common(3)
        total_count = sum(count for letter, count in most_common_letter)
        return 1337 * self.age * total_count

