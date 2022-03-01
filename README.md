# pygui_tutorial2022
Project tutorial for UNCLE ENGINEER class
This project contains 5 tabs in GUI, 1 tab is WIP.
- TAB1: (Crypto) Currenct exchange in THB
  - 3 inputs
    - currency name (BTC, ETH, ADA, etc.)
    - number of currency (A positive int or integer)
    - currenct value (In THB)
  - output
    - A pop up with total THB value (Number of currency * value)
- TAB2: Searching data in wikipedia (Using wikipedia and webbrowser library)
  - Input -> A keyword that user required to search in wikipedia
  - Output -> A brief data from wiki search (5 sentence) and a url link that linked to a specific website.
- TAB3: Betting
  - When click the betting game in the left side of GUI (The data that clicked will be shown in table on the right side)
  - When click reset, the whole data in table will be blanked
  - When click save, the whole data in table will be stored to 'transaction.csv'
  - Shortcut F1 can show the order history that stored in 'transaction.csv'
- TAB4: Point (CRUD and csv file)
  - The data will stored in 'member.csv'
  - avaliable to CRUD plus delete all
  - Auto focus on the first entry form when click any button
  - Memberid will not be duplicated
