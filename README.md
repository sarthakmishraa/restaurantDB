# restaurantDB
Data Model Query Language - Project  on "Enhancing Restaurant Operations with a Robust Database Management System"

<h2>**Problem statement:**</h2>
A restaurant database system addresses the challenge of effectively managing and organizing vast amounts of data
pertaining to restaurant operations, including menu items, cuisines, restaurant information, reviews, owner and financial
reporting. The system will serve as a centralized repository for all data and provide a streamlined approach to managing the
restaurant's various processes.
By implementing a restaurant database system, restaurants can reduce operational costs, enhance the customer experience, and make data-driven decisions to improve overall performance.
While Excel files have limitations in handling large data sets and conducting complex queries, database systems offer more advanced features for managing and querying data. These systems provide faster search and retrieval, support data analysis and reporting, and enable data sharing and collaboration. Furthermore, database systems allow for the creation of user roles and permissions to regulate access to sensitive data, and ensure data integrity and security through constraints and backups. In summary, a database system offers a more secure and efficient way to manage restaurant data compared to an Excel file.

<h2>**Target User:**</h2>
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

<h2>**Project description:**</h2>
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

https://github.com/sarthakmishraa/restaurantDB/assets/56118819/327d3ff4-c98b-4a90-8485-0d4e9e2e6827

