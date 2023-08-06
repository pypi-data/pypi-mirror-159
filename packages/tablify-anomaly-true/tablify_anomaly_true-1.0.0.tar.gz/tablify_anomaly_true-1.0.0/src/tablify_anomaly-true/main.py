import re
regex_str = "\\x1b\[(33|0|32|31|36|35)m"


def centered(text: str, width: int) -> str:
    length = len(re.sub(regex_str, "", text))
    if length > width:
        return text[:width]
    else:
        is_unequal = (width - length) % 2 != 0
        spacing = (width - length) // 2
        if is_unequal:
            return " "*(spacing + 1) + text + " "*(spacing)
        return " "*spacing + text + " "*spacing


def hasInd(lst: list, ind: int) -> bool:
    if type(lst) != list:
        return False
    return ind in range(len(lst))


def setToIndex(lst: list, ind: int, val: str) -> list:
    if hasInd(lst, ind):
        lst[ind] = val
    else:
        for x in range(ind+1):
            if ind == x:
                lst.append(val)
            elif not hasInd(lst, x):
                lst.append('')


def process_input(inp, cF=False) -> str:
    input_type = type(inp)
    result_input = inp
    if input_type is int or input_type is float:
        result_input = str(inp)
        result_input = f"\x1b[33m{result_input}\x1b[0m" if cF else result_input
    elif input_type is bool:
        result_input = str(inp)
        if cF:
            result_input = f"\x1b[32m{result_input}\x1b[0m" if inp else f"\x1b[31m{result_input}\x1b[0m"
    elif input_type is list:
        result_input = str(inp)
        result_input = f"\x1b[36m{result_input}\x1b[0m" if cF else result_input
    elif input_type is dict:
        result_input = str(inp)
        result_input = f"\x1b[36m{result_input}\x1b[0m" if cF else result_input
    elif input_type is str and cF:
        result_input = f"\x1b[35m{result_input}\x1b[0m"
    return result_input


class Table:
    def __init__(self, inst: list, console_friendly=False):
        self.result = inst if type(inst) is list else []
        if hasInd(inst, 0) and type(inst[0]) is not list:
            self.result = []
        self.inst = inst
        self.lengths = {"max": 1, "lines": []}
        self.console = console_friendly
        self.table = self.generate()

    def __call__(self):
        return self.table

    def __str__(self):
        return self.table

    def generate(self):
        if not self.inst:
            return "Invalid input type."

        # Create a new list that is compatible with the processing algorithm
        if hasInd(self.inst, 0) and type(self.inst[0]) is dict:
            keys = {}
            n = 0
            for x in self.inst:
                for y in x.keys():
                    if not y in keys:
                        keys[y] = n
                        n += 1
            self.result.append(list(keys.keys()))
            for x in self.inst:
                line_list = []
                for key in x:
                    setToIndex(line_list, keys[key], process_input(
                        x[key], self.console))
                self.result.append(line_list)
        if type(self.inst) is dict:
            self.result.append(["(index)"])
            for key in self.inst:
                self.result.append([key])
            keys = {}
            a, n = 1, 1
            for x in self.inst:
                for y in self.inst[x].keys():
                    if not y in keys:
                        self.result[0].append(y)
                        keys[y] = n
                        n += 1
                for key in self.inst[x]:
                    setToIndex(self.result[a], keys[key],
                               process_input(self.inst[x][key], self.console))
                a += 1

        for sub_list in self.result:
            if type(sub_list) is not list:
                return f"Invalid parameter formatting.\nExpected list, got {type(sub_list)}"
            else:
                line_n = 0
                if self.lengths["max"] < len(sub_list):
                    self.lengths["max"] = len(sub_list)
                for _str in sub_list:
                    if type(_str) is not (str):
                        return f"Invalid input type.\nExpected string, got {type(_str)}"
                    else:
                        length = len(re.sub(regex_str, "", _str))
                        if not hasInd(self.lengths["lines"], line_n):
                            self.lengths["lines"].append(length)
                        elif self.lengths["lines"][line_n] < length:
                            self.lengths["lines"][line_n] = length
                        line_n += 1

        # Draw Table
        tableStr = "┌" + "─" * (self.lengths["lines"][0] + 2)
        for i in range(1, len(self.lengths["lines"])):
            tableStr += "┬" + "─" * (self.lengths["lines"][i] + 2)
        tableStr += "┐"

        for i in range(len(self.result)):
            tableStr += "\n│"
            for j in range(0, self.lengths["max"]):
                if hasInd(self.result[i], j):
                    tableStr += centered(self.result[i][j],
                                         self.lengths["lines"][j] + 2) + "│"
                else:
                    tableStr += " " * (self.lengths["lines"][j] + 2) + "│"
            if i != len(self.result) - 1:
                tableStr += "\n├" + "─" * (self.lengths["lines"][0] + 2)
                for j in range(1, self.lengths["max"]):
                    tableStr += "┼" + "─" * (self.lengths["lines"][j] + 2)
                tableStr += "┤"
            else:
                tableStr += "\n└" + "─" * (self.lengths["lines"][0] + 2)
                for j in range(1, self.lengths["max"]):
                    tableStr += "┴" + "─" * (self.lengths["lines"][j] + 2)
                tableStr += "┘"
        return tableStr

    def draw(self):
        print(self.table)

    def update(self, inst, console_friendly=False):
        self.inst = inst
        self.lengths = {"max": 1, "lines": []}
        self.result = inst if type(inst) is list else []
        if hasInd(inst, 0) and type(inst[0]) is not list:
            self.result = []
        self.console = console_friendly
        self.table = self.generate()
