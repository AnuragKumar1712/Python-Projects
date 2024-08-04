### Simple ATM Simulator Project Description

#### Overview
The Simple ATM Simulator is a basic Python-based project designed to simulate the functionality of an Automated Teller Machine (ATM). This program allows users to perform essential banking operations such as checking their balance, depositing money, and withdrawing money. It offers an interactive and user-friendly interface through command-line inputs.

#### Features
1. **PIN Authentication**
   - The program starts by prompting the user to enter their PIN. If the entered PIN matches the predefined user PIN, access to the ATM functions is granted. Otherwise, the program exits, ensuring security.

2. **Main Menu**
   - Once authenticated, users are presented with a main menu that includes the following options:
     - Check Balance
     - Deposit Money
     - Withdraw Money
     - Exit

3. **Check Balance**
   - Users can check their current balance at any time. The balance is displayed in a user-friendly format.

4. **Deposit Money**
   - Users can deposit a specified amount of money into their account. The program updates the balance accordingly and provides confirmation of the successful deposit.

5. **Withdraw Money**
   - Users can withdraw a specified amount of money from their account. The program checks if the user has sufficient balance before proceeding with the withdrawal. If the balance is insufficient, an error message is displayed. Otherwise, the balance is updated, and confirmation of the successful withdrawal is provided.

6. **Exit**
   - Users can exit the program at any time by selecting the exit option. The program thanks the user and terminates.

#### How It Works
1. **Initialization**: The program initializes with a default balance of $1000 and a predefined user PIN.
2. **PIN Verification**: Users must enter the correct PIN to access the main menu.
3. **Main Menu Operations**:
   - **Check Balance**: Displays the current balance.
   - **Deposit Money**: Prompts the user for an amount to deposit and updates the balance.
   - **Withdraw Money**: Prompts the user for an amount to withdraw, checks the balance, and updates it if sufficient funds are available.
   - **Exit**: Ends the session and exits the program.

#### Conclusion
The Simple ATM Simulator is an excellent project for beginners to practice Python programming. It covers basic input/output operations, conditional statements, loops, and simple arithmetic operations. This project demonstrates how to create a simple yet functional simulation of a real-world banking system.
