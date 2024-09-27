package main

/* -------------------------------------------------------------------------------------- */
import (
	"database/sql"
	"fmt"
	"log"

	_ "github.com/go-sql-driver/mysql"
)

/* -------------------------------------------------------------------------------------- */
const (
	user     = "user"
	password = "password"
	host     = "localhost"
	database = "database"
	dbtable  = "pi_cycle_indicator"
)

/* -------------------------------------------------------------------------------------- */
func calculateAverageDailyIncrease(days int) float64 {

	// Connect to the MySQL database
	connStr := fmt.Sprintf("%s:%s@tcp(%s)/binance", user, password, host)
	db, err := sql.Open("mysql", connStr)
	if err != nil {
		log.Printf("Error connecting to database: %v", err)
		return 0.0
	}
	defer db.Close()

	// Prepare the SQL query
	query := fmt.Sprintf(`
        SELECT ROUND(AVG(daily_increase), 4) AS avg_daily_increase
        FROM (
            SELECT dt1, (price - LAG(price) OVER (ORDER BY dt1)) AS daily_increase
            FROM binance.klines_1d
            WHERE dt1 >= CURDATE() - INTERVAL %d DAY
        ) AS price_changes
        WHERE daily_increase IS NOT NULL;
    `, days)

	// Execute the query
	var avgDailyIncrease sql.NullFloat64
	err = db.QueryRow(query).Scan(&avgDailyIncrease)
	if err != nil {
		log.Printf("Error executing query: %v", err)
		return 0.0
	}

	// Check if the result is valid
	if avgDailyIncrease.Valid {
		return avgDailyIncrease.Float64
	} else {
		return 0.0
	}
}

/* -------------------------------------------------------------------------------------- */
func main() {

	days := 30
	avgIncrease := calculateAverageDailyIncrease(days)
	fmt.Printf("Average daily increase over the last %d days: %.4f\n", days, avgIncrease)
}

/* -------------------------------------------------------------------------------------- */
