# restaurantDB
Data Model Query Language - Project  on "Enhancing Restaurant Operations with a Robust Database Management System"

<h2>Problem statement:</h2>
A restaurant database system addresses the challenge of effectively managing and organizing vast amounts of data
pertaining to restaurant operations, including menu items, cuisines, restaurant information, reviews, owner and financial
reporting. The system will serve as a centralized repository for all data and provide a streamlined approach to managing the
restaurant's various processes.
By implementing a restaurant database system, restaurants can reduce operational costs, enhance the customer experience, and make data-driven decisions to improve overall performance.
While Excel files have limitations in handling large data sets and conducting complex queries, database systems offer more advanced features for managing and querying data. These systems provide faster search and retrieval, support data analysis and reporting, and enable data sharing and collaboration. Furthermore, database systems allow for the creation of user roles and permissions to regulate access to sensitive data, and ensure data integrity and security through constraints and backups. In summary, a database system offers a more secure and efficient way to manage restaurant data compared to an Excel file.

<h2>Target User:</h2>
A variety of individuals and businesses in the food industry, as well as by consumers who are interested in finding
new dining options. Some examples of who might use this database include: Restaurant owners: Restaurant owners can use the database to find out what types of cuisines are popular in their area and to
see what their competitors are offering on their menus. They can also use the database to research different locations for potential new restaurant locations.
Food critics: Food critics can use the database to find new restaurants to review and to research the different types of cuisines available in a particular area.
Food bloggers: Food bloggers can use the database to create content about different types of restaurants and to share
information about the different types of cuisines available in a particular area.
Consumers: Consumers can use the database to find new restaurants to try, to look up menus and ratings of different restaurants in their area, and to find restaurants that serve
specific types of cuisine.
A group of database administrators, developers, and IT specialists may be in charge of maintaining and upgrading the database, but that leaves us wondering who will be in charge of it. This team would be in charge of making sure the database is efficient, dependable, and secure as well as adding new data and making sure it is correct and current A real-world example of how this database may be applied is by a meal delivery service like Uber Eats or GrubHub. The corporation may utilize the database to add restaurants to its platform and notify customers about the many cuisines that are available in their neighborhood.
Database administrators for the firm would be in charge of maintaining the data's accuracy and timeliness as well as adding new eateries to the platform when they became available.

<h2>Project description:</h2>
* restaurants(res_id, name, address, city, zip_code,
phone_number, website)

* restaurant_info(res_id, tax_code, certificate)

* owner(res_id, owner_name, owner_address,
owner_city, owner_zip_code, owner_phone_number)

* cuisines(cuisine_id, cuisine_name, calories,
ingredients)

* menu_items(res_id, cuisine_id, dish_name,
description, price)

* reviews(res_id, reviewer_email, rating, comments)

<h2>Data Generation:</h2>
Under the data generation heading in PostgreSQL, you can mention that you generated fake data for each table using the website generatedata.com. This allowed you to quickly create a large dataset of 500 rows for each table, which helped to test the database system's performance and functionality with a realistic amount of data. By generating fake data, you were able to simulate a real-world scenario where the database would be handling a significant amount of information, providing valuable insights into the system's scalability and ability to handle large data sets.
Before using the generatedata.com website to generate fake data for our PostgreSQL database, we conducted extensive research to ensure the authenticity and reliability of the data. We analyzed the website's features and reviews, as well as the methodology behind the data generation algorithms to ensure that they align with industry standards and best practices. Additionally, we cross-checked the generated data with actual data sets to ensure that they accurately represent real-world scenarios. We are confident that the data generated through
this process is robust, reliable, and aligned with industry standards.
Furthermore, generating fake data allowed us to test the database system's functionality without the risk of compromising any actual customer or business data. This helped to ensure the system's security and minimize any potential risks during the testing phase. By simulating realistic data sets, we were able to test the system's functionality in a controlled environment and identify any potential bottlenecks or issues that could arise when handling a large volume of data. This approach helped us to optimize the database system's performance and ensure that it could handle the demands of a real-world scenario. Overall, generating fake data was a crucial step in testing and optimizing the database system's functionality and performance.

<h2>Data validation and cleansing</h2>
Data cleaning and validation are essential steps in maintaining the accuracy and integrity of a restaurant database. Data cleaning involves identifying and removing or correcting inaccurate, incomplete, or irrelevant data. This process may include removing duplicates, correcting misspellings or typos, and verifying the accuracy of the data. For example, if the
database contains a record of a restaurant's address, data cleaning may involve verifying the spelling of the street name, ensuring the correct zip code is included, and correcting any
other errors or inconsistencies.
Data validation involves verifying the accuracy, completeness, and consistency of the data in the database. This process may include checking that data is within a specified range, ensuring that data conforms to a specific format, and verifying that relationships between data tables are valid. For example, data validation may involve checking that a restaurant's phone number is in a valid format, ensuring that the relationship between a menu item and its associated cuisine is accurate, and verifying that a restaurant's address is in a valid format.

<h2>Flask Deployment :</h2>
For integrating the PostgreSQL database with Flask, we used the psycopg2 library. psycopg2 is a PostgreSQL adapter for the Python programming language that allows Python applications to connect to a PostgreSQL database and execute SQL queries. It provides a simple and efficient way to connect to a PostgreSQL database, send queries, and retrieve results. To use psycopg2 with Flask, we first installed it using pip, the package installer for Python. We then imported the library into our Flask application and used it to connect to the PostgreSQL database using the database credentials.

![Flask Deployment on localhost](https://github.com/sarthakmishraa/restaurantDB/blob/main/media/flask_cmd.JPG)

We used the psycopg2.connect() function to establish a connection to the database and created a cursor object to execute SQL queries. We then used the cursor object to execute SQL queries and retrieve results. We used the cursor.execute() method to execute SQL queries and the cursor.fetchall() method to retrieve the results of the query. We also used the cursor.commit() method to commit changes made to the database. Overall, psycopg2 was a valuable tool for integrating the PostgreSQL database with Flask.

![DB Integration using psycopg2](https://github.com/sarthakmishraa/restaurantDB/blob/main/media/code1_flask_db_integration.JPG)

It provided a simple and efficient way to connect to the database and execute SQL queries, which allowed us to easily manipulate the data in the database through our Flask
application.

![Restaurant relation method to fetch data using select query](https://github.com/sarthakmishraa/restaurantDB/blob/main/media/code1_res_show.JPG)

In addition to its core functionality, psycopg2 also offers several advanced features that make it an ideal choice for integrating PostgreSQL with Flask. For instance, psycopg2
supports prepared statements, which can improve the performance of the application by reducing the overhead of query parsing and optimization. Prepared statements can also enhance the security of the application by preventing SQL injection attacks. Furthermore, psycopg2 provides support for asynchronous I/O, which can enable high-performance database interactions and improve the overall responsiveness of the application. These advanced features make psycopg2 a powerful tool for integrating PostgreSQL with Flask and enable developers to build fast, secure, and responsive applications.

![UI Home page](https://github.com/sarthakmishraa/restaurantDB/blob/main/media/home.JPG)

https://github.com/sarthakmishraa/restaurantDB/assets/56118819/327d3ff4-c98b-4a90-8485-0d4e9e2e6827

