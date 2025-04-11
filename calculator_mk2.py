import tkinter as tk

def calculator(iv):
    operand_list = []
    operator_list = []

    operand = ""
    operator = ""
    count = 0

    while '(' in iv:
        for i, ch in enumerate(iv):
            if ch == '(':
                start = i
            elif ch == ')':
                end = i
                break
        result = calculator(iv[start+1:end])
        iv = iv[:start] + str(result) + iv[end+1:]

    for bar in iv:
        count += 1
        if bar.isdigit():
            operand += bar
            if operator != "":
                operator_list.append(operator)
            operator = ""
        if not bar.isdigit() or count == len(iv):
            operator += bar
            if operand != "":
                operand_list.append(int(operand))
            operand = ""

    priority_operator = [["**"], ["*", "/", "%", "//"], ["+", "-"]]

    for ops in priority_operator:
        count = 0
        if "**" in operator_list:
            count = len(operator_list) - 1
            while count >= 0:
                if operator_list[count] == '**':
                    operand_list[count] = operand_list[count] ** operand_list[count+1]
                    del operand_list[count+1]
                    del operator_list[count]
                count -= 1
        else:
            while count < len(operator_list):
                if operator_list[count] in ops:
                    o = operator_list[count]
                    if o == "*":
                        operand_list[count] = operand_list[count] * operand_list[count+1]
                    elif o == "/":
                        operand_list[count] = operand_list[count] / operand_list[count+1]
                    elif o == "//":
                        operand_list[count] = operand_list[count] // operand_list[count+1]
                    elif o == "%":
                        operand_list[count] = operand_list[count] % operand_list[count+1]
                    elif o == "+":
                        operand_list[count] = operand_list[count] + operand_list[count+1]
                    elif o == "-":
                        operand_list[count] = operand_list[count] - operand_list[count+1]
                    del operand_list[count+1]
                    del operator_list[count]
                    count = 0
                    continue
                count += 1

    return operand_list[0]

# tkinter 이용 GUI 구현 간단하게
def cal() :
    result = calculator(entry.get())
    result_label.config(text=f"결과: {result}")
    

window = tk.Tk()
window.title("처음 만드는 GUI")
window.geometry("400x300")

label = tk.Label(window, text="수식을 입력하세요")
label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="계산", command=cal)
button.pack()

result_label = tk.Label(window, text="결과가 여기에 표시됩니다")
result_label.pack()

window.mainloop()