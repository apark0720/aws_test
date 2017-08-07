## Univentures

### Background and Overview
Univentures provides a platform for student startups to easily recruit team members and for students to find startups to join. 
Univentures will have a two way search: 1) students will be able to search for startups to join 2) startups will be able to advertise open positions and search the existing memberbase.


### Functionality and MVP

#### User Authentication 
- Only users with university email account can join Univentures
- Users can select to create account as a startup
- Users can setup their profile information

#### Startup profile pages
- Startups can manage their profile page 
- Profile page displays information about their company and team members
- Startups select tags that are relevant to their job postings
- Student users can contact startups

#### Tags
- Student users must select maximum two profile tags
- Student users may select multiple skill tags
- Startups must select company type tag
- Startups must select profile tags 
- Startups may select multiple skill tags

#### Search 
- Users can select tags to specify their search query
- Results will show filtered data

#### Competitions
- Displays information about upcoming startup competitions
- Users are redirected with competition website url


### Design Docs
* [View Wireframes][wireframes]
* [DB schema][schema]

[wireframes]: docs/wireframes
[schema]: docs/schema.md


### Technologies
#### Backend
- Python/Django
- PostgreSQL 
- AWS Elastic Beanstalk (Amazon RDS)

#### Frontend
- React.js with Redux
- Bootstrap

### Implementation Timeline

**Day 1 (Sat)**
Research the technologies and tools
- Initially decided to use a JAVA / Spring MVC framework but decided against it because of time constraints. 
- Instead, we decided to use a Django backend with a PostgreSQL db, React frontend with bootstrap for responsive design, and AWS for hosting. Since python is the most widely used language in an academic setting, it will be easier to find people to collaborate with if we need to scale. 

**Day 2 (Sun)**
Research the technologies and tools
- Created sample django CRUD app to learn basic structure of a django app
- Experimented with docker technology for unified container on both development and production servers. Also since Alex's macbook died and was having trouble making our sample django CRUD app to function perfectly on both machines. Ended up scrapping docker after many many many hours and decided to both work on a Ubuntu Linux development environment.


**Day 3 (Mon)**
Setup basic structure of the app
- Initialize django app and host on AWS (Alex & YoungEun)
- Setup backend DB and create tables (Alex)
- Setup frontend connection (YoungEun)
User auth
- Setup user auth backend(users can signup/login/logout) (Alex)
Company profile
- Setup company backend(users can select to create account as startup) (YoungEun)

**Day 4 (Tue)**
Session Forms
- Style login modal and nav bar (Alex)
- Style signup form (YoungEun)
Profile pages
- Setup backend/frontend for user profile page (Alex)
- Setup backend/frontend for company profile page (YoungEun)

**Day 5 (Wed)**
Index pages
- Setup frontend for user index component (YoungEun)
- Setup frontend for company index component (YoungEun)
Tags
- Setup backend for tags (Alex)
- Add tag features in profile pages (Alex)

**Day 6 (Thu)**
Root
- Style main index page (Alex)
Search
- Setup backend for search (YoungEun)
- Setup frontend for search (YoungEun)

**Day 7 (Fri)**
Competitions
- Setup backend/frontend for competitions (Alex)
Frontend
- Review and unify overall frontend styling

**Day 8 (Sat)**
Contact 
- Research on how to implement messaging (email, Zendesk, internal messaging etc.) (Alex & YoungEun)
- Implement messaging feature

**Day 9 (Sun)**
- Refine overall code 
- Design and setup basic logic for competition application management feature


### Bonus Features (TBD)

#### Terms of use and privacy policy

#### Contact 
- Users can send each other messages 
- Receiving messages gives users notification through the website and email 
- Users may reply directly via email (possibly implement Zendesk)

#### Competition application management
- Users can select to create competition account
- Competition users can host competition and receive student applications 
- Competition users can create application forms 
- Application form tool provides example questions from previous competitions 
- Competition users can manage applications (sort/filter, approve/deny, send messages)


### Resources

#### Git
https://github.com/appacademy/sf-job-search-curriculum/blob/master/projects/git-workflow.md 
https://www.atlassian.com/git/tutorials/comparing-workflows#feature-branch-workflow 
https://chris.beams.io/posts/git-commit/

#### AWS
http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-rds.html