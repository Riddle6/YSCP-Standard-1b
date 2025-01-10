# YSCP-Standard-1b
A Python project to explore debugging and error handling using Visual Studio Code and GitHub Codespaces

# Budget Tracker Project

## **Overview**
This Python project tracks a user's budget by adding income and expenses and displays transactions and the current balance.

---

## **Errors and Debugging**

### **1. Syntax Error**
- **Error**: Missing colon in the `if __name__ == "__main__":` block.
- **How to Identify**: IDE flagged the missing colon.
- **Solution**: Add the colon to fix the syntax error.

### **2. Run-Time Error**
- **Error**: File not found when trying to load transactions from a file.
- **How to Identify**: Program crashed when the file was not found.
- **Solution**: Added a `try-except` block to handle the error.

### **3. Logic Error**
- **Error**: Incorrect balance calculation in `add_transaction`.
- **How to Identify**: Balance was incorrect after transactions.
- **Solution**: Adjusted logic to correctly update the balance.

---

## **Reflection**

### **1. Interpreted vs. Compiled Languages**
- **Python (Interpreted)**: Easier to debug because errors are identified during execution.
- **C++ (Compiled)**: Requires compilation but often runs faster.

### **2. High-Level vs. Low-Level Languages**
- **High-Level (Python)**: Abstracts hardware details, improving readability and usability.
- **Low-Level (Assembly)**: Offers greater control but is harder to write and debug.

---

## **Key Takeaways**
- Syntax errors are quickly identified by the IDE.
- Debugging run-time errors improves program reliability.
- Logical errors require careful testing and validation.
