# Secret Auction Program

A fun **Python console project** from Angela Yu’s Python Bootcamp — the **Secret Auction Program** lets multiple bidders enter their names and bids in secret. The program then determines and displays the highest bidder as the winner.

---

## 📜 ASCII Art Logo

```text
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\
```

---

## 💡 Features
- **Multiple bidders**: Each person enters their name and bid without seeing others' bids.
- **Secret clearing**: Clears the console after each bidder for privacy.
- **Automatic winner detection**: Finds the highest bidder.
- **Color output**: Uses `colorama` to make the winner announcement stand out.

---

## 📂 Project Structure
```
secret_auction/
│
├── art.py         # Contains the ASCII logo
├── main.py        # Main program logic
├── README.md      # Documentation
```

---

## 🚀 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/secret-auction.git
   cd secret-auction
   ```

2. Install dependencies:
   ```bash
   pip install colorama
   ```

3. Run the program:
   ```bash
   python main.py
   ```

---

## 🖥 Example Output
```
Welcome to the secret auction program.
What is your name?: Alice
What's your bid?: $100
Are there any other bidders? Type 'yes' or 'no': yes

Welcome to the secret auction program.
What is your name?: Bob
What's your bid?: $150
Are there any other bidders? Type 'yes' or 'no': no

🏆 The winner is Bob with a bid of $150
```

---

## 📦 Requirements
- Python 3.x
- `colorama` library for colored output.

---

## 📄 License
This project is licensed under the MIT License.
