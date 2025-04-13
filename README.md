# MiniLang Interpreter Project

This project is a **Mini Programming Language Interpreter** built in Python that performs lexical analysis, parsing, and evaluation of a small custom language. It satisfies the requirements of a domain-specific language (DSL) by supporting variable declarations, arithmetic expressions, scoping, and output via a `print` statement.

---

## What's Included in This Version

This final version includes a complete interpreter that:

- Tokenizes a simplified, C-like custom language
- Parses statements and expressions into an Abstract Syntax Tree (AST)
- Evaluates nested blocks using scoped environments
- Correctly supports shadowing, variable reassignment, and arithmetic logic
- Built entirely in Python using standard libraries

---

## **Features**

✔️ Supports custom MiniLang syntax with:

- Variable declarations for `int`, `float`, `bool`, and `string`
- Arithmetic operations: `+`, `-`, `*`, `/`
- Nested `{ ... }` blocks and scoping behavior
- Reassignment of variables within nested scopes
- `print(expr);` to output evaluated results

✔️ Outputs the result directly to the terminal and tracks variables with scoping rules.

---

## **Files Overview**

- **`lexer.py`** – Tokenizer for MiniLang keywords, literals, and operators
- **`parser.py`** – Recursive-descent parser that converts tokens into AST nodes
- **`ast_nodes.py`** – Defines all AST node classes (`Block`, `Assign`, `Print`, etc.)
- **`interpreter.py`** – Walks the AST and evaluates expressions using scoped environments
- **`main.py`** – Loads and runs the interpreter from a source file
- **`test_program.txt`** – Contains sample MiniLang code to be interpreted

---

## **How It Works**

### Input (`test_program.txt`)

```mini
{
  int x = 10;
  float y = x + 2.5;
  {
    int x = 5;
    y = y + x;
  }
  print(y);
}
```

### Output ( 17.5 )

---

## **MiniLang Grammar Used**

```
<program>       ::= <block>
<block>         ::= '{' <stmt_list> '}'
<stmt_list>     ::= <stmt> <stmt_list> | ε
<stmt>          ::= <decl> ';' | <assign> ';' | <print> ';' | <block>
<decl>          ::= <type> ID '=' <expr>
<assign>        ::= ID '=' <expr>
<print>         ::= 'print' '(' <expr> ')'
<expr>          ::= <term> { ('+' | '-') <term> }*
<term>          ::= <factor> { ('*' | '/') <factor> }*
<factor>        ::= INT | FLOAT | STRING | ID | '(' <expr> ')'
<type>          ::= 'int' | 'float' | 'bool' | 'string'
```

---

## **Installation & Running the Project**

0. **Clone the Repository**  
   If you haven't already, clone the project from GitHub:

```bash
git clone https://github.com/manthony0602/HCSC415-MiniLang_Interpreter-Project.git
cd HCSC415-MiniLang_Interpreter-Project
```

---

1. **(Optional) Set Up a Virtual Environment**  
   It's a good practice to use a virtual environment to keep dependencies isolated:

```bash
python3 -m venv venv
source venv/bin/activate      # For macOS/Linux
venv\Scripts\activate         # For Windows
```

2. **Install Dependencies**  
   There are **no third-party dependencies**. The entire interpreter uses Python's standard library — so you're good to go right out of the box.

3. **Run the Interpreter**  
   Once inside the project folder, run:

```bash
python3 main.py
```

4. **View the Output**  
   The interpreter reads and executes the MiniLang source code found in `test_program.txt`. The result will be printed directly to your terminal.

Example:

```bash
17.5
```

5. **Customize the Source Code**  
   You can modify the file `test_program.txt` to test your own MiniLang programs. The syntax supports:

   - Declarations like `int x = 10;`
   - Arithmetic like `y = x + 2.5;`
   - Nested blocks `{ ... }` with scoping
   - Output via `print(expr);`

   Simply save your changes and re-run the following in the terminal:

   ```bash
   python3 main.py
   ```

---

### **Requirements**

- Python 3.6 or higher (tested on Python 3.10+)
- No external libraries needed

---

## **Assumptions & Design Decisions**:

    - Variable types (`int`, `float`, etc.) are not enforced at runtime. They're used only for declaration.
    - Shadowing is allowed within nested `{}` blocks.
    - Arithmetic expressions follow proper operator precedence (which are handled via recursive parsing).
    - String literals are parsed but not currently used in operations.
    - Only void-style `print(expr);` output is supported for side effects.

    ---
    ---

## Author

- Mason Brown
- Morehouse College - Computer Science
