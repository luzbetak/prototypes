Average Daily Price Increase Calculator
=======================================

This Go program calculates the average daily price increase for a dataset stored in a MySQL database. It retrieves price data from the database, computes the daily increases, and outputs the average over a specified number of days.

## Prerequisites

- Go 1.16 or higher
- MySQL database with the required table and data
- MySQL Go driver (`github.com/go-sql-driver/mysql`)

## Setup

1. **Install Go**: If you haven't already installed Go, download and install it from the official [Go website](https://golang.org/dl/).

2. **Install MySQL Driver**: Run the following command to install the MySQL driver for Go:
   ```sh
   go get -u github.com/go-sql-driver/mysql
   ```

3. **Set up the MySQL Database**:
   - Create a MySQL database named `gemini`.
   - Create a table named `pi_cycle_indicator`.
   - Populate the table with price data that includes columns like `dt1` (date) and `price` (daily price).

4. **Configure the Program**:
   - Modify the `user`, `password`, `host`, `database`, and `dbtable` constants in the program to match your MySQL configuration.

## Usage

1. **Run the Program**:
   - You can change the number of days over which the average is calculated by modifying the `days` variable in the `main()` function.
   - Build and run the program using the following commands:
     ```sh
     go build -o avg_daily_increase
     ./avg_daily_increase
     ```

2. **Output**:
   - The program will output the average daily price increase over the specified number of days to the console.

## Example

```sh
Average daily increase over the last 30 days: 1.2345
```

## Notes

- The program uses the `LAG` window function to compute the difference between the current day's price and the previous day's price.
- The average is calculated by excluding any null values in the daily increases.

