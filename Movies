-- Write SQL queries to answer questions about a database of movies.
-- Table: 
    -- CREATE TABLE movies (id, title, year, PRIMARY KEY(id));
    -- CREATE TABLE stars (movie_id, person_id, FOREIGN KEY(movie_id), FOREIGN KEY(person_id);
    -- CREATE TABLE directors (movie_id, person_id, FOREIGN KEY(movie_id), FOREIGN KEY(person_id));
    -- CREATE TABLE ratings (movie_id, person_id, FOREIGN KEY(movie_id), FOREIGN KEY(person_id));
    -- CREATE TABLE people (movie_id, name, birth, PRIMARY KEY(id));

-- ASSIGNMENT: In 1.sql, write a SQL query to list the titles of all movies released in 2008.
    -- Your query should output a table with a single column for the title of each movie.

SELECT title FROM movies WHERE year = 2008; 

-- To check the correct answer: SELECT COUNT(title) FROM movies WHERE year = 2008;
-- Answer 1 column and 9545 rows

-- In 2.sql, write a SQL query to determine the birth year of Emma Stone.
    -- Your query should output a table with a single column and a single row (not including the header) containing Emma Stone’s birth year.
    -- You may assume that there is only one person in the database with the name Emma Stone.
SELECT birth FROM people WHERE name = 'Emma Stone';

-- In 3.sql, write a SQL query to list the titles of all movies with a release date on or after 2018, in alphabetical order.
    -- Your query should output a table with a single column for the title of each movie.
    -- Movies released in 2018 should be included, as should movies with release dates in the future.
SELECT title FROM movies WHERE year >= 2018 ORDER BY title ASC;

-- In 4.sql, write a SQL query to determine the number of movies with an IMDb rating of 10.0.
    -- Your query should output a table with a single column and a single row (not including the header) containing the number of movies with a 10.0 rating.
SELECT COUNT(movie_id) FROM ratings WHERE rating = 10.0;

-- In 5.sql, write a SQL query to list the titles and release years of all Harry Potter movies, in chronological order.
    -- Your query should output a table with two columns, one for the title of each movie and one for the release year of each movie.
    -- You may assume that the title of all Harry Potter movies will begin with the words “Harry Potter”, and that if a movie title begins with the words “Harry Potter”, it is a Harry Potter movie.
SELECT title, year FROM movies WHERE title LIKE "Harry Potter%" ORDER BY(year);

-- In 6.sql, write a SQL query to determine the average rating of all movies released in 2012.
    -- Your query should output a table with a single column and a single row (not including the header) containing the average rating.
SELECT AVG(rating) FROM ratings WHERE movie_id IN
(SELECT id FROM movies WHERE year = "2012");

-- In 7.sql, write a SQL query to list all movies released in 2010 and their ratings, in descending order by rating. For movies with the same rating, order them alphabetically by title.
    -- Your query should output a table with two columns, one for the title of each movie and one for the rating of each movie.
    -- Movies that do not have ratings should not be included in the result.

-- What you want to do:
    -- 1) Isolate the two tables that you contains the data you need: movies and ratings
    -- 2) If the film doesn't have a rating it should be NULL;
-- SELECT movie_id FROM ratings where rating IS NULL; -- nothing popped up
-- SELECT movie_id FROM ratings where rating = 0; -- nothing popped up
-- SELECT movie_id FROM ratings WHERE rating <= 0; -- nothing showed up
-- SELECT movie_id FROM ratings WHERE rating = ' '; -- nothing showed up
    -- So from this, we can assume that there isn't any ratings that IS NULL populated nor have ratings that is in the toilet nor equal to 0.

SELECT movies.title, ratings.rating FROM movies 
JOIN ratings ON ratings.movie_id = movies.id
WHERE year = '2010'
ORDER BY ratings.rating DESC, title ASC;

-- In 8.sql, write a SQL query to list the names of all people who starred in Toy Story.
    -- Your query should output a table with a single column for the name of each person.
    -- You may assume that there is only one movie in the database with the title Toy Story.
-- What you want to do:
    -- 1) Isolate the three tables that you contains the data you need: people, stars and movies
    -- 2) So from this, it looks like we will need 2 JOINs

SELECT people.name FROM people
JOIN stars ON stars.person_id = people.id 
JOIN movies ON movies.id = stars.movie_id 
WHERE title = 'Toy Story';
-- In 9.sql, write a SQL query to list the names of all people who starred in a movie released in 2004, ordered by birth year.
    -- Your query should output a table with a single column for the name of each person.
    -- People with the same birth year may be listed in any order.
    -- No need to worry about people who have no birth year listed, so long as those who do have a birth year are listed in order.
    -- If a person appeared in more than one movie in 2004, they should only appear in your results once.
-- What you want to do:
    -- 1) Isolate the three tables that you contains the data you need: people, stars and movies
    -- 2) So from this, it looks like we will need 2 JOINs

SELECT DISTINCT people.name FROM stars 
JOIN people ON stars.person_id = people.id 
JOIN movies ON movies.id = stars.movie_id 
WHERE movies.year = '2004'
--GROUP BY people.name
ORDER BY people.birth ASC;

-- In 10.sql, write a SQL query to list the names of all people who have directed a movie that received a rating of at least 9.0.
    -- Your query should output a table with a single column for the name of each person.

-- What you want to do:
    -- 1) Isolate the four tables that you contains the data you need: ratings, movie, people and directors
    -- 2) So from this, it looks like we will need 2 JOIN

SELECt DISTINCT people.name FROM PEOPLE
JOIN directors ON people.id = directors.person_id
JOIN movies ON directors.movie_id = movies.id
JOIN ratings ON movies.id = ratings.movie_id
WHERE ratings.rating >= '9.0';

-- In 11.sql, write a SQL query to list the titles of the five highest rated movies (in order) that Chadwick Boseman starred in, starting with the highest rated.
    -- Your query should output a table with a single column for the title of each movie..
    
-- What you want to do:
    -- 1) Isolate the four tables that you contains the data you need: people, stars, ratings, movies
    -- 2) So from this, it looks like we will need 1 JOIN and 2 Nested

SELECT movies.title FROM movies 
JOIN ratings ON movies.id = ratings.movie_id 
WHERE id IN (SELECT movie_id FROM stars WHERE person_id = 
(SELECT id FROM people WHERE name ="Chadwick Boseman")) 
ORDER BY ratings.rating DESC 
LIMIT 5;
-- In 12.sql, write a SQL query to list the titles of all movies in which both Johnny Depp and Helena Bonham Carter starred.
    -- Your query should output a table with a single column for the title of each movie.
    -- You may assume that there is only one person in the database with the name Johnny Depp.
    -- You may assume that there is only one person in the database with the name Helena Bonham Carter.

-- Need to figure out which tables that will be required: people, stars, movies
-- https://stackoverflow.com/questions/61536261/cs50-pset7-movies-sql-12 Recommends using INTERSECT instead since 2 Nested and 2 JOINs kept on failing me.

SELECT movies.title FROM movies 
JOIN stars ON movies.id = stars.movie_id
JOIN people ON stars.person_id = people.id
WHERE people.name = 'Johnny Depp'
INTERSECT
SELECT movies.title FROM movies 
JOIN stars ON movies.id = stars.movie_id
JOIN people ON stars.person_id = people.id
AND people.name = 'Helena Bonham Carter';

-- In 13.sql, write a SQL query to list the names of all people who starred in a movie in which Kevin Bacon also starred.
    -- Your query should output a table with a single column for the name of each person.
    -- There may be multiple people named Kevin Bacon in the database. Be sure to only select the Kevin Bacon born in 1958.
    -- Kevin Bacon himself should not be included in the resulting list.

-- What you want to do:
    -- 1) Isolate the three tables that you contains the data you need: people, stars, movie
    -- 2) So from this, it looks like we will need 2 JOINS and 1 NESTED

SELECT DISTINCT name FROM people
JOIN stars ON people.id = stars.person_id
JOIN movies ON stars.movie_id = movies.id
WHERE movies.id IN
-- https://stackoverflow.com/questions/59706969/pset7-movies-stuck-on-12-and-13-sql
(SELECT movies.id FROM movies
    JOIN stars on stars.movie_id = movies.id
    JOIN people ON stars.person_id = people.id
    WHERE people.name = 'Kevin Bacon' 
    AND people.birth = '1958')
    AND people.name != 'Kevin Bacon';

