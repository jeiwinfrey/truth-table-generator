import tkinter as tk
from tkinter import ttk
from tkinter import font, filedialog
from tabulate import tabulate

truthTable = {}

# Function to calculate implication (->)
def implication(p, q): 
    ans = []
    for i in range(len(p)):
        if p[i] == 1 and q[i] == 0:
            ans.append(0)
        else:
            ans.append(1)
    return ans

# Function to calculate negation (~)
def negation(p): 
    ans = []
    for i in range(len(p)):  
        if p[i] == 0:
            ans.append(1)
        else:
            ans.append(0)
    return ans

# Function to calculate conjunction (^)
def conjunction(p, q): 
    ans = []
    for i in range(len(p)):
        if p[i] == 1 and q[i] == 1:
            ans.append(1)
        else:
            ans.append(0)
    return ans

# Function to calculate disjunction (v)
def disjunction(p, q): 
    ans = []
    for i in range(len(p)):
        if p[i] == 1 or q[i] == 1:
            ans.append(1)
        else:
            ans.append(0)
    return ans

# Function to calculate equivalence (<->)
def equivalence(p, q): 
    ans = []
    for i in range(len(p)):
        if p[i] == q[i]:
            ans.append(1)
        else:
            ans.append(0)
    return ans

# Function to print the truth table
def printTable(variables, truthTable, logEq):
    headers = variables + [logEq]
    rows = []
    for i in range(len(truthTable["ans"])):
        row = []
        for var in variables:
            if truthTable[var][i]:
                row.append(1)
            else:
                row.append(0)
        row.append(truthTable["ans"][i])
        rows.append(row)
    return tabulate(rows, headers=headers, tablefmt="double_outline", stralign="center", numalign="center")

# Function to extract variables from the logical equation ('p', 'q', or 'p,q')
def extractVariables(logEq):
    variables = set()
    for char in logEq:
        if char in "pq":
            variables.add(char)
    return sorted(list(variables)) 

# Function to check for allowed operators and balance of parentheses (Makes sure close parenthesis matches with the most recent open parenthesis)
def checkParenthesis(logEq):
    if not logEq:
        return 0

    st = []  # stack for parenthesis checking
    allowedChars = "pq()-<>^~v"
    for i in range(len(logEq)):
        char = logEq[i]

        # valid characters p, q, (, ), -, <, >, ^, ~, v
        if char not in allowedChars:
            return 0

        # valid parenthesis
        if char == '(':
            st.append(char)
        else:
            if st and char == ')':
                if st[-1] != '(':
                    return 0
                else:
                    st.pop()

    if not st:
        return 1
    else:
        return 0

# Function to validate the logical equation's operands (p,q) and operators (-, <, >, ^, ~, v)
def validLogEq(logEq):
    if not checkParenthesis(logEq):
        return 0

    operand = []
    operator = []
    stack = []
    i = 0
    size = len(logEq)
    negateNext = False

    while i < size:
        char = logEq[i]
        
        # Handle negation operator (~)
        if char == '~':
            if i + 1 < size and logEq[i + 1] in "pq~(":
                negateNext = True
            else:
                return 0

        # Handle operands (p, q)
        elif char in "pq":
            if negateNext:
                operand.append(f"~{char}")
                negateNext = False
            else:
                operand.append(char)
            if operator and operator[-1] == '~':
                operator.pop()

        # Ensure operators are beside parentheses or operands
        elif char in "^v":
            if i + 1 < size and logEq[i + 1] in "pq~(":
                operator.append(char)
            else:
                return 0

        # Handle parentheses
        elif char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                return 0

        i += 1

    return 1 if not stack else 0

# Function to calculate the result based on the operator
def calculate(operand1, optr, operand2=None):
    if optr == "^":
        return conjunction(truthTable[operand1], truthTable[operand2])
    if optr == "v":
        return disjunction(truthTable[operand1], truthTable[operand2])
    if optr == "->":
        return implication(truthTable[operand1], truthTable[operand2])
    if optr == "<->":
        return equivalence(truthTable[operand1], truthTable[operand2])
    if optr == "~":
        return negation(truthTable[operand1])

# Function to evaluate the logical equation (With precedence followed)
def evaluation(logEq):
    operand = []
    operator = []

    precedence = {'~': 3, '^': 2, 'v': 2, '->': 1, '<->': 1}
    i = 0
    size = len(logEq)

    while i < size:
        char = logEq[i]

        if char == '(':  # (
            operator.append(char)

        elif char == ')':  # )
            while operator and operator[-1] != '(':
                optr = operator.pop()
                if optr == '~':
                    oprd = operand.pop()
                    truthTable[oprd + optr] = calculate(operand1=oprd, optr=optr)
                    operand.append(oprd + optr)
                else:
                    oprd2 = operand.pop()
                    oprd1 = operand.pop()
                    truthTable[oprd1 + optr + oprd2] = calculate(operand1=oprd1, operand2=oprd2, optr=optr)
                    operand.append(oprd1 + optr + oprd2)
            operator.pop()  # pop '('

        elif char in "pq":
            operand.append(char)

        elif char in "^v":
            while operator and operator[-1] in precedence and precedence[operator[-1]] >= precedence[char]:
                optr = operator.pop()
                if optr == '~':
                    oprd = operand.pop()
                    truthTable[oprd + optr] = calculate(operand1=oprd, optr=optr)
                    operand.append(oprd + optr)
                else:
                    oprd2 = operand.pop()
                    oprd1 = operand.pop()
                    truthTable[oprd1 + optr + oprd2] = calculate(operand1=oprd1, operand2=oprd2, optr=optr)
                    operand.append(oprd1 + optr + oprd2)
            operator.append(char)

        elif char == '<':
            operator.append("<->")
            i += 2

        elif char == '-':
            if i + 1 < size and logEq[i + 1] == '>':
                while operator and operator[-1] in precedence and precedence[operator[-1]] >= precedence["->"]:
                    optr = operator.pop()
                    if optr == '~':
                        oprd = operand.pop()
                        truthTable[oprd + optr] = calculate(operand1=oprd, optr=optr)
                        operand.append(oprd + optr)
                    else:
                        oprd2 = operand.pop()
                        oprd1 = operand.pop()
                        truthTable[oprd1 + optr + oprd2] = calculate(operand1=oprd1, operand2=oprd2, optr=optr)
                        operand.append(oprd1 + optr + oprd2)
                operator.append("->")
                i += 1

        elif char == '~':
            operator.append(char)

        i += 1

    while operator:
        optr = operator.pop()
        if optr == '~':
            oprd = operand.pop()
            truthTable[oprd + optr] = calculate(operand1=oprd, optr=optr)
            operand.append(oprd + optr)
        else:
            oprd2 = operand.pop()
            oprd1 = operand.pop()
            truthTable[oprd1 + optr + oprd2] = calculate(operand1=oprd1, operand2=oprd2, optr=optr)
            operand.append(oprd1 + optr + oprd2)

    truthTable["ans"] = truthTable[operand[0]]
    return truthTable["ans"]

# Function to generate the truth table's value for the variable/s (p,q)
def generateTruthTable(numVars):
    table = []
    for i in range(2 ** numVars):
        row = [(i >> j) & 1 for j in range(numVars)]
        table.append(row)
    return table

# Function to read input (lowering alphabet and removing blank spaces), evaluate, and display the result
def evaluateAndDisplay():
    logEq = inputText.get("1.0", tk.END).strip().replace(" ", "").lower()
    if not validLogEq(logEq=logEq):
        resultLabel.config(text="Invalid logical equation")
        return

    variables = extractVariables(logEq)
    table = generateTruthTable(len(variables))

    for i in range(len(variables)):
        var = variables[i]
        truthTable[var] = []
        for j in range(len(table)):
            truthTable[var].append(table[j][i])

    evaluation(logEq)
    result = printTable(truthTable=truthTable, logEq=logEq, variables=variables)
    resultLabel.config(text=result)

# Function to input logical equation from a text file
def inputFromTxtFile():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read().strip()
            inputText.delete("1.0", tk.END)
            inputText.insert(tk.END, content)
            evaluateAndDisplay()

# Function to create the operator table (For user guide)
def createOperatorTable():
    header = ["Operator", "Symbol"]
    data = [
        ["Bi-conditional", "<->"],
        ["Implication", "->"],
        ["Conjunction", "^"],
        ["Disjunction", "v"],
        ["Negation", "~"]
    ]
    return tabulate(data, headers=header, tablefmt="double_outline", stralign="center", numalign="center")

# Create main window
root = tk.Tk()
root.title("Logical Equation Evaluator")

# Applying a theme
style = ttk.Style()
style.theme_use('clam') 

# Create input text box
inputLabel = tk.Label(root, text="Enter Logical Equation:", font=("Courier", 14))
inputLabel.pack(pady=5)
inputText = tk.Text(root, height=2, width=60, font=("Courier", 12))
inputText.pack(pady=5)

# Create table guide
operatorTable = createOperatorTable()
operatorTableLabel = tk.Label(root, text=operatorTable, font=("Courier", 10), justify=tk.LEFT)
operatorTableLabel.pack(pady=5)

# Create input from TXT file button
inputFromTxtButton = ttk.Button(root, text="Input from TXT File", command=inputFromTxtFile)
inputFromTxtButton.pack(pady=5)

# Create evaluate button
evaluateButton = ttk.Button(root, text="Evaluate", command=evaluateAndDisplay)
evaluateButton.pack(pady=5)

# Create output label for the table
monospaceFont = font.Font(family="Courier", size=10)
resultLabel = tk.Label(root, text="", justify=tk.CENTER, font=monospaceFont)
resultLabel.pack(pady=20)

# Run the GUI event loop
root.mainloop()