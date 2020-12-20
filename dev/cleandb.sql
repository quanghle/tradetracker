SELECT 'CREATE DATABASE test'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'test')\gexec
\c test
DROP DATABASE postgres WITH (FORCE);
CREATE DATABASE postgres;
\c postgres