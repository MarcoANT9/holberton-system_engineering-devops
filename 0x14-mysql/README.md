# 0x14. MySQL

This project is focused on the MySQL data query applied to the two web servers
provided by Holberton School.

## TASKS:

#### Task 0.Install MySQL :
Install MySQL on both web-01 and web-02 servers.

    MySQL distribution is be 5.7.x.
    This task does not have file attached to it.

#### Task 1. Let us in:
In order for us to verify that the servers are properly configured, a user and password for both MySQL databases are created so that Holberton's
checker has access to them.

    A MySQL user named holberton_user on both web-01 and web-02 with the host name set to localhost and their passwords.
    holberton_user has permission to check the primary/replica status of the databases.
    This task does not have a file attached to it.

#### Task 2. If only you could see what I've seen with your eyes:
This task creates a table and one row in the primary MySQL server (web-01) to be replcated by the secundary (web-02).

    The database is named tyrell_corp.
    Within the tyrell_corp database exists a table named nexus6 that has at least one entry in it.
    holberton_user has SELECT permissions on the table.
    This task does not have a file attached to it.

#### Task 3. Quite an experience to live in fear, isn't it?
Before the primary-replica synchronization, there is one thing that needs to be done.
On the primary MySQL server (web-01), a new user for the replica server is created.

    The name of the new user is replica_user, with the host name set to %, the password is arbitrary.
    replica_user has the appropriate permissions to replicate the primary MySQL server.
    holberton_user needs SELECT privileges on the mysql.user table in order to check that replica_user was created with the correct permissions.
    This task also has no files attached to it.

#### Task 4. Setup a Primary-Replica infrastructure using MySQL:
This task links the replica infrastructure.

    MySQL primary is hosted on web-01 (bind-address is not used).
    MySQL replica is hosted on web-02.
    Setup replication for the MySQL database named tyrell_corp.
    The MySQL primary configuration is submitted as attached file, named: 4-mysql_configuration_primary.
    The MySQL replica configuration is submitted as attached file, named: 4-mysql_configuration_replica.

#### Task 5. MySQL backup:
This task takes care of the backup algorithm for the databases.

    The MySQL dump contains all MySQL databases.
    The MySQL dump is named backup.sql.
    The MySQL dump file is compressed to a tar.gz archive.
    This file name format is <day-month-year.tar.gz>.
    The user to connect to the MySQL database is root.
    The Bash script accepts one argument that is the password used to connect to the MySQL database.
