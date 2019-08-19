CREATE TABLE routes (
	route_id VARCHAR(50) NOT NULL,
	short_name VARCHAR(50) NOT NULL,
	long_name VARCHAR(100),
	PRIMARY KEY (route_id)
);

CREATE TABLE stops (
	route_id VARCHAR(50) NOT NULL REFERENCES routes(route_id),
	stop_id VARCHAR(10) NOT NULL,
	stop_name VARCHAR(100) NOT NULL,
	price NUMERIC,
	PRIMARY KEY (route_id, stop_id)
);

CREATE TABLE times (
	route_id VARCHAR(50) NOT NULL REFERENCES routes(route_id),
	trip_id VARCHAR(100) NOT NULL,
	stop_id VARCHAR(10) NOT NULL,
	stop_sequence INTEGER NOT NULL,
	arrival_time TIME NOT NULL,
	departure_time TIME NOT NULL,
	trip_date DATE NOT NULL,
	PRIMARY KEY (route_id, trip_id, stop_id)
);