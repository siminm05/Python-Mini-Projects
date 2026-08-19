# Library Management System
A command-line Python utility that manages a library catalogue, allowing users to track books, handle checkouts and organize inventory

### Features:
1. Dynamic Cataloguing: add new books or delete existing ones by their list index
2. Borrow and Return System: tracks book availability and blocks deletion for currently borrowed books
3. Multi-Criteria Search: look up books instantly by filtering through titles, authors or genres
4. Input Enforcement: guarantees data integrity by rejecting empty text values and handling crashes

### Concepts Used:
- List of dictionaries for data structuring
- Menu-driven interface loops
- Modular functional programming
- Strict string sanitation using .lower().strip()
- Substring pattern matching with the in operator
- Element pop manipulation and index offsetting
