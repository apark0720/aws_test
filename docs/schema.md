## users
column name       | data type | details
------------------|-----------|-----------------------
id                | integer   | not null, primary key
email             | string    | not null, unique
password_digest   | string    | not null, unique
session_token     | string    | not null, unique
name              | string    | not null
profile_url       | string    |

## company
column name       | data type | details
------------------|-----------|-----------------------
id                | integer   | not null, primary key
user_id           | integer   | not null, unique, foreign key (references user)
logo_url          | integer   | not null
address           | string    | not null
email_address     | string    | not null
phone             | integer   | 

## tags
column name       | data type | details
------------------|-----------|----------------------
id                | integer   | not null, primary_key
tag_name          | integer   | not null, unique
user_id           | integer   | not null, foreign key (references user)
company_id        | integer   | not null, foreign key (references company)

## competitions
column name       | data type | details
------------------|-----------|-----------------------
id                | integer   | not null, primary key
url               | integer   | not null
