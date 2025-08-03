# Auction Bidding System

A simple auction program available in both command-line and web interface versions. Allows multiple bidders to place bids and automatically determines the highest bidder.

## Features

- **Multi-bidder support**: Add unlimited number of bidders
- **Real-time bid tracking**: Stores all bids in memory during the auction
- **Automatic winner determination**: Finds and announces the highest bidder
- **Two Interface Options**: 
  - Command-line version with privacy screen clearing
  - Web-based Streamlit interface for modern user experience
- **Input validation**: Handles numeric bid amounts

## How It Works

1. The program prompts each bidder to enter their name and bid amount
2. All bids are stored securely during the auction process
3. After each bid, you can choose to add more bidders or end the auction
4. When the auction ends, the program automatically determines and announces the winner

## Usage

### Running the Program

**Command Line Version:**
```bash
python auction.py
```

**Streamlit Web App Version:**
```bash
streamlit run auction_streamlit.py
```
Then open your browser to `http://localhost:8501` to access the web interface.

### Example Session

```
Enter you Name :
John

Enter your bid : $ 150.50

Are there any other bidders? Type 'Yes' or 'No'
Yes

Enter you Name :
Sarah

Enter your bid : $ 200.75

Are there any other bidders? Type 'Yes' or 'No'
No

The winner is Sarah with $200.75 bid
```

## Code Structure

### Main Components

- **Bidding Loop**: Collects bidder information and bid amounts
- **Data Storage**: Uses a dictionary to store bidder names and their corresponding bids
- **Winner Determination**: `find_highest_bidder()` function processes all bids to find the maximum
- **Privacy Feature**: Screen clearing between bidders

### Key Functions

#### `find_highest_bidder(bidding_dictionary)`
- **Purpose**: Determines the auction winner
- **Parameters**: Dictionary containing bidder names and bid amounts
- **Returns**: Prints the winner's name and winning bid amount
- **Algorithm**: Iterates through all bids to find the maximum value

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/auction-bidding-system.git
```

2. Navigate to the project directory:
```bash
cd auction-bidding-system
```

3. Install dependencies (for Streamlit version):
```bash
pip install streamlit
```

4. Run the program:

**Command Line Version:**
```bash
python auction.py
```

**Streamlit Web App Version:**
```bash
streamlit run auction_streamlit.py
```

## Requirements

- Python 3.x
- Streamlit (for web interface): `pip install streamlit`
- No other external dependencies required

## Technical Details

- **Language**: Python
- **Web Framework**: Streamlit (for web interface)
- **Data Structure**: Dictionary for O(1) bid storage and retrieval
- **Input Handling**: Built-in `input()` and `float()` functions (CLI) / Streamlit widgets (Web)
- **Screen Clearing**: Uses newline characters for cross-platform compatibility (CLI version)

## Potential Improvements

- [ ] Add input validation for bid amounts (prevent negative bids)
- [ ] Implement bid history tracking
- [ ] Add minimum bid requirements
- [ ] Include bidder registration system
- [ ] Add auction time limits
- [ ] Implement bid increment rules
- [ ] Add GUI interface
- [ ] Save auction results to file

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Create a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

If you have any questions or suggestions, please feel free to reach out or create an issue in this repository.

---

**Note**: This is a basic implementation suitable for learning purposes and small-scale auctions. For production use, consider adding proper error handling, data persistence, and security measures.
