CREATE DATABASE familycollector;

CREATE USER family_admin WITH PASSWORD 'password';

GRANT ALL PRIVILEGES ON DATABASE familycollector TO family_admin;

ALTER DATABASE familycollector OWNER TO family_admin;

