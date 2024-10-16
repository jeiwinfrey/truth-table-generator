`TRUTH-TABLE-GENERATOR`


[<img src="https://cdn-icons-png.flaticon.com/512/6295/6295417.png" align="right" width="25%" padding-right="350">]()

#### <code> DISCREET STRUCTURES PROJECT</code>

#####  Table of Contents

- [ Overview](#-overview)
- [ Repository Structure](#-repository-structure)
- [ Getting Started](#-getting-started)
    - [ Prerequisites](#-prerequisites)
    - [ Installation](#-installation)
    - [ Usage](#-usage)
- [ Contributing](#-contributing)

---

##  Overview of the Program Flow

1. **Input of the Logical Equation**: Either from the text box or from a txt file.
2. **Preprocess Input**: Remove all blank spaces and convert the alphabet characters to lowercase.
3. **Validate Logical Equation**: Check if the logical equation is valid (Character checking which includes parentheses, operators, and letters p and q).
   - If invalid, display an error message and exit.
4. **Extract Variables**: Extract variables from the logical equation to determine the number of columns to show in the table (whether p, q, or both).
5. **Generate Truth Table**: Generate the truth table for the variables.
6. **Populate Truth Table**: Populate the truth table for each variable.
7. **Evaluate Logical Equation**:
   - Initialize operand and operator stacks.
   - Iterate through each character in the logical equation.
   - If '(' is found: push to operator stack.
   - If ')' is found: Pop from the parentheses stack to get the position of the most recent '('.
   - Perform calculations for the expression within the parentheses.
   - If operand (p, q): push to operand stack.
   - If operator (^, v, ->, <->, ~): handle precedence and perform calculations using the calculate function, then push the operator to the operator stack.
   - Perform remaining calculations in the operator stack.
   - Store the final result.
8. **Print Truth Table**: Print the truth table.
9. **Display Result**: Display the result in the result label.


---


##  Repository Structure

```sh
└── truth-table-generator/
    ├── Documentation of the Truth Table - Jeiwinfrey P. Ulep.pdf
    ├── Jeiwinfrey P. Ulep Screenshots of Outputs.docx.pdf
    ├── README.md
    └── ulepJeiwinfreyTruthTable.py
```

---


##  Getting Started

###  Prerequisites

**Python**: `version 3.12`

###  Installation

Build the project from source:

1. Clone the truth-table-generator repository:
```sh
❯ git clone https://github.com/jeiwinfrey/truth-table-generator
```

2. Navigate to the project directory:
```sh
❯ cd truth-table-generator
```

3. Install the required dependencies:
```sh
❯ pip install -r requirements.txt
```

###  Usage

To run the project, execute the following command:

```sh
❯ python main.py
```

**Enter Logical Equation**:
  - In the text box, enter the logical equation by inputting/typing your logical equation using the allowed characters.
  - Click the “Input from TXT File” button, then it pops up a file selection. After, select your .txt file containing your logical equation. The content will be loaded into the input box.
- **Evaluate the Logic Equation**:
  - Click the “Evaluate” button to process the logical equation you inputted in the text box.
  - The result will be displayed automatically if the logical equation input is from a .txt file.
- **Display Truth Table**: The Truth Table result will be displayed in the output below the buttons.

---


##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://github.com/jeiwinfrey/truth-table-generator/issues)**: Submit bugs found or log feature requests for the `truth-table-generator` project.
- **[Submit Pull Requests](https://github.com/jeiwinfrey/truth-table-generator/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/jeiwinfrey/truth-table-generator/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/jeiwinfrey/truth-table-generator
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>




