drop TABLE if EXISTS t_token;
CREATE TABLE IF NOT EXISTS t_token(
access_token varchar(512),
create_time TIMESTAMP,
expires_time TIMESTAMP
);