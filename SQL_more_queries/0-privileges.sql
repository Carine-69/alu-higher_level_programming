--list all the privileges of the MySQL users_0d_1 and user_0d_2 on your server (in locoalhost).
--cat 0_rpivileges.sql | mysql -lpocalhost -u root -p
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';

