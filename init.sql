
CREATE TABLE IF NOT EXISTS stock_data (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(10) NOT NULL,
    date_time TIMESTAMP NOT NULL,
    open_price DECIMAL(10, 4),
    high_price DECIMAL(10, 4),
    low_price DECIMAL(10, 4),
    close_price DECIMAL(10, 4),
    volume BIGINT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(symbol, date_time)
);

CREATE INDEX IF NOT EXISTS idx_symbol_datetime ON stock_data(symbol, date_time);
CREATE INDEX IF NOT EXISTS idx_created_at ON stock_data(created_at);