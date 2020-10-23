https://cs50.harvard.edu/extension/2020/fall/psets/7/fiftyville/#:~:text=Write%20SQL%20queries%20to%20solve%20a%20mystery.

-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Write SQL queries to solve a mystery.
-- The CS50 Duck has been stolen! The town of Fiftyville has called upon you to solve the mystery of the stolen duck. Authorities believe that the thief stole the duck and then, shortly afterwards, took a flight out of town with the help of an accomplice. Your goal is to identify:
-- Who the thief is,
-- What city the thief escaped to, and
-- Who the thief’s accomplice is who helped them escape
-- All you know is that the theft took place on July 28, 2020 and that it took place on Chamberlin Street.

-- TABLES
-- TABLE crime_scene_reports(id INTEGER, year INTEGER, month INTEGER, day INTEGER, street TEXT, description TEXT, PRIMARY KEY(id);
-- TABLE interviews (id INTEGER, name TEXT, year INTEGER, month INTEGER, day INTEGER, transcript TEXT, PRIMARY KEY(id);
-- TABLE courthouse_security_logs (id INTEGER, year INTEGER, month INTEGER, day INTEGER, hour INTEGER, minute INTEGER, activity TEXT, license_plate TEXT, PRIMARY KEY(id));
-- TABLE atm_transactions (id INTEGER, account_number INTEGER, year INTEGER, month INTEGER, day INTEGER, atm_location TEXT, transaction_type TEXT, amount INTEGER,PRIMARY KEY(id));
-- TABLE bank_accounts (account_number INTEGER, person_id INTEGER, creation_year INTEGER, FOREIGN KEY(person_id) REFERENCES people(id));
-- TABLE airports (id INTEGER, abbreviation TEXT, full_name TEXT, city TEXT, PRIMARY KEY(id));
-- TABLE flights (id INTEGER, origin_airport_id INTEGER, destination_airport_id INTEGER, year INTEGER, month INTEGER, day INTEGER, hour INTEGER, minute INTEGER, PRIMARY KEY(id), FOREIGN KEY(origin_airport_id) REFERENCES airports(id), FOREIGN KEY(destination_airport_id) REFERENCES airports(id));
-- TABLE passengers (flight_id INTEGER, passport_number INTEGER, seat TEXT, FOREIGN KEY(flight_id) REFERENCES flights(id));
-- TABLE phone_calls (id INTEGER, caller TEXT, receiver TEXT, year INTEGER, month INTEGER, day INTEGER,duration INTEGER, PRIMARY KEY(id));
-- TABLE people (id INTEGER, name TEXT, phone_number TEXT, passport_number INTEGER, license_plate TEXT, PRIMARY KEY(id);

-- Step 1) Isolate the date. To do so, you should start with the SQL query: SELECT * FROM crime_scene_reports; so you can see what the data would look like
SELECT * FROM crime_scene_reports;
-- STEP 2) The date of the crime was July 28, 2020 and on Chamberlin Street so you should isolate those two dates. 
SELECT * FROM crime_scene_reports
WHERE year = '2020'
AND month = '07'
AND day = '28'
AND street = 'Chamberlin Street';
-- Step 3) After running the query, which states the following:  Theft of the CS50 duck took place at 10:15am at the Chamberlin Street courthouse. Interviews were conducted today with three witnesses who were present at the time — each of their interview transcripts mentions the courthouse.
            -- From this, we can gather there were 3 witnesses that were present to the crime the main component could be found in their interview transcripts which mentions the courthouse
            -- So with this, we can now do a basic search for interviews so that we can see the format
SELECT * FROM interviews
WHERE year = '2020'
AND month = '07'
AND day = '28';
        -- The main three witnesses are as follows: Ruth, Eugene, and Raymond
        -- Summary for Ruth: Within 10 minutes of the theft, he got into a car in the courthouse parking lot. Can find more information in the security footage from the courthouse parking lot
        -- Summary for Eugene: It was someone that Eugene recognised earlier in the morning. He was walking to the ATM on Fifer Street and saw the thief withdrawing some funds
        -- Summary for Raymond: As the thief was leaving the courthouse, they called someone for less than a minute. Was planning on taking the earliest flight out of fiftyvillege tomorrow. Requested that the person on the phone pay for the ticket instead

-- Step 4: We should chase down each of the leads starting with Eugene. I started with Eugene because he was the first to see the suspect
SELECT * FROM atm_transactions 
WHERE year = '2020'
AND month = '07'
AND day = '28'
AND atm_location = 'Fifer Street'
AND transaction_type = 'withdraw';
    -- The following bank accounts appeared
        -- 28500762 -- Amount Withdrawn was 48
        -- 28296815 -- Amount Withdrawn was 20
        -- 76054385 -- Amount Withdrawn was 60
        -- 49610011 -- Amount Withdrawn was 50
        -- 16153065 -- Amount Withdrawn was 80
        -- 25506511 -- Amount Withdrawn was 20
        -- 81061156 -- Amount Withdrawn was 30
        -- 26013199 -- Amount Withdrawn was 35 
-- Step 5: No one withdrew a large amount nor in multiple denominations from the same account so we will have to check each bank account manually
SELECT * FROM bank_accounts 
WHERE account_number = '28500762' 
OR account_number = '28296815'
OR account_number = '76054385'
OR account_number = '49610011'
OR account_number = '16153065'
OR account_number = '25506511'
OR account_number = '81061156'
OR account_number = '26013199';
    -- Account information: Account ID | person ID | Creation Year
        -- 49610011 | 686048 | 2010
        -- 26013199 | 514354 | 2012
        -- 16153065 | 458378 | 2012
        -- 28296815 | 395717 | 2014
        -- 25506511 | 396669 | 2014
        -- 28500762 | 467400 | 2014
        -- 76054385 | 449774 | 2015
        -- 81061156 | 438727 | 2018
    -- From the looks of it, there is nothing else we can glean from this info -- for now
-- Step 6: Ruth's information is: 10 mins after theft; security footage at the courthouse parking lot 
SELECT * FROM courthouse_security_logs
WHERE year = '2020'
AND month = '07'
AND day = '28'
AND activity LIKE "exit"
AND hour = 10
AND minute < 25;
    -- Information is as follows: 
    -- id | year | month | day | hour | minute | activity | license_plate
    -- 260 | 2020 | 7 | 28 | 10 | 16 | exit | 5P2BI95
    -- 261 | 2020 | 7 | 28 | 10 | 18 | exit | 94KL13X
    -- 262 | 2020 | 7 | 28 | 10 | 18 | exit | 6P58WS2
    -- 263 | 2020 | 7 | 28 | 10 | 19 | exit | 4328GD8
    -- 264 | 2020 | 7 | 28 | 10 | 20 | exit | G412CB7
    -- 265 | 2020 | 7 | 28 | 10 | 21 | exit | L93JTIZ
    -- 266 | 2020 | 7 | 28 | 10 | 23 | exit | 322W7JE
    -- 267 | 2020 | 7 | 28 | 10 | 23 | exit | 0NTHK55
-- Step 7: Raymond's testimony: phone_logs, and airplane ticket - the earliest out of the country
    -- To do this, I would recommend doing the airplane ticket first to see what would be the earliest one out because this will clearly which is the earliest flight out
SELECT * FROM airports;
    -- From this, we were able to get the abbreviation and the id for Fiftyvillege
        -- 8 | CSF | Fiftyville Regional Airport | Fiftyville
SELECT * FROM flights 
JOIN airports ON airports.id = flights.origin_airport_id
WHERE flights.year = '2020'
AND flights.month = '07'
AND flights.day = '29'
AND airports.id = 8 
ORDER BY flights.hour ASC;
    -- Earliest flight out of Fiftyville is 36 | 8 | 4 | 2020 | 7 | 29 | 8 | 20 | 8 | CSF | Fiftyville Regional Airport | Fiftyville
    -- From this, we can see that the destination_airport_id is 4
    -- This means that if create a query for this, we can see where the criminal is flying to
-- Step 8: Finding out where the criminal is flying to
SELECT full_name, city FROM airports
WHERE id = 4;
    -- The criminal is flying into Heathrow Airport, London (destination_airport_id = 4)
-- Step 9: We will want the passenger information:
SELECT * FROM passengers
JOIN flights ON passengers.flight_id = flights.id
JOIN airports ON airports.id = flights.origin_airport_id
WHERE flights.year = '2020'
AND flights.month = '07'
AND flights.day = '29'
AND airports.id = 8 
AND destination_airport_id = 4
ORDER BY flights.hour ASC;
    -- We wanted this information for the following reasons 1) we now have the flight ID and passport number which we can then cross-reference it to other data tables later on to narrow down the scope. 

    
-- Step 10: To find out the phone call
SELECT * FROM phone_calls
WHERE year = '2020'
AND month = '07'
AND day = '28'
ORDER BY duration ASC;
    -- Very suspicious from Raymond. There are no durations of less than a minute on July 28, 2020
    -- It could be a multitude of things but let's assume that the duration is in terms of seconds instead of minutes. This narrows things down to the following phone numbers for callers and receivers. 
    -- It is my belief that the duration is in seconds because no one is going to spend 595 hours on the phone w someone
    -- caller || receiver
    -- (499) 555-9472 | (892) 555-8872
    -- (031) 555-6622 | (910) 555-3251
    -- (286) 555-6063 | (676) 555-6554
    -- (367) 555-5533 | (375) 555-8161
    -- (770) 555-1861 | (725) 555-3243 
    -- (499) 555-9472 | (717) 555-1342
    -- (130) 555-0289 | (996) 555-8899
    -- (338) 555-6650 | (704) 555-2131
    -- (826) 555-1652 | (066) 555-9701 
    -- (609) 555-5876 | (389) 555-5198
    -- (751) 555-6567 | (594) 555-6254
-- Step 11: From this, we can now clearly link up with the people table with multiple joins
    -- The tables that should be used are people, passengers, flights
    -- I think we will need an intersect for the court_house_security for people
    -- I also think I should create a new variable for the list of suspected people for their phone numbers and license_plates

    -- Since we're using an intersect, we should split up the two SQL: first one will be the personal data that we had previously: phone number and license plate with people
        -- The second SQL will be the flight information
SELECT people.id, people.name, people.passport_number, people.phone_number FROM people
JOIN courthouse_security_logs ON people.license_plate = courthouse_security_logs.license_plate
WHERE phone_number IN ('(499) 555-9472 ', '(031) 555-6622', '(286) 555-6063 ', '(367) 555-5533', '(770) 555-1861', '(499) 555-9472', '(130) 555-0289', '(338) 555-6650', '(826) 555-1652', '(609) 555-5876', '(751) 555-6567') -- thief
AND people.license_plate IN ('5P2BI95', '94KL13X', '6P58WS2', '4328GD8', 'G412CB7', 'L93JTIZ', '322W7JE', '0NTHK55')
INTERSECT
SELECT people.id, people.name, people.passport_number, people.phone_number FROM people
JOIN passengers ON people.passport_number = passengers.passport_number
JOIN flights ON passengers.flight_id = flights.id 
WHERE flights.origin_airport_id = 8
AND flights.destination_airport_id = 4;
    -- From this, we were able to narrow it down to three suspects
        -- people.id | name | passport_number | phone_number
        -- 398010 | Ernest | 5773159633 | (367) 555-5533
        -- 560886 | Evelyn | 8294398571 | (499) 555-9472
        -- 686048 | Roger | 1695452385 | (130) 555-0289
-- Step 12: From here, we can link up people table and bank account
SELECT people.name FROM people 
JOIN bank_accounts ON people.id = bank_accounts.person_id
WHERE people.name IN ('Ernest', 'Evelyn', 'Roger')
INTERSECT 
SELECT people.name FROM people 
JOIN bank_accounts ON people.id = bank_accounts.person_id
WHERE account_number IN ('49610011', '26013199', '16153065', '28296815', '25506511', '28500762', '76054385', '81061156');
    -- The name that came up was Ernest. From this, we can easily ascertain that he is the criminal
-- Step 13: To find out the accomplice name, we should cross reference the people and phone logs
SELECT people.name, phone.calls.receiver FROM phone_calls 
WHERE caller = '(367) 555-5533'
AND year = '2020'
AND month = '07'
AND day = '28'
AND duration < 61;
    -- The receiver phone number is 375.555.8161
SELECT people.name FROM people
WHERE phone_number = '(375) 555-8161';
    -- The name of the accomplice is Berthold

The THIEF is: Ernest
The thief ESCAPED TO: London
The ACCOMPLICE is: Berthold
