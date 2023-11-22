CREATE TABLE IF NOT EXISTS IS601_S_Accounts(
    id int AUTO_INCREMENT PRIMARY KEY,
    account varchar(12) unique DEFAULT (LPAD(user_id, 12, "0")),
    user_id int,
    balance int DEFAULT 0,
    account_type varchar(30) not null,
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP
)