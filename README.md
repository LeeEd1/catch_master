# Catch Master
Catch Master is a family-run business specialising in a wide range of fishing equipment. The website enables customers to browse and purchase products with an integrated payment system. Registered users can manage their profile information and view past orders. The site also features a showcase section, where users can display and celebrate their fishing successes by sharing photos of past catches.

## About
![Am I Responsive](/media/readme/amiresponsive.PNG)

## UX:

### Site purose

At Catch Master, we aim to provide anglers of all experience levels with the fishing gear they need, whether it’s for a quick trip or a serious fishing expedition.

### Site goal

The goal of Catch Master is to be the go to online destination for anglers by providing high quality, affordable fishing gear and gain registered users along the way. We aim to make the shopping experience simple and enjoyable with a showcase section to hopefully entice anonymous users to register.

### Audience

The site is aimed at anyone with an interest in fishing, regardless of age or experience level. We especially encourage younger users, as we believe fishing is a fantastic outdoor hobby to help kids get active and engaged with nature. However, parental assistance is required for any purchases made on the website.

### Communication

The communication of the page is designed to be easily understood by any user. It features clear buttons, a user friendly modal pop up and employs easy to read fonts with distinctly displayed colours, aiming for universal accessability.

### New user goals

- Be able to easily navigate the site.
- Browse all products.
- be able to purchase without registering.
- Be able to register if interested.

### Registered user goals

- 
- Be able to sign in and sign out.
- Ability to save/update profile information.
- Be able to add/edit/delete a catch.
- Ability to review past purchases.



### Future user goals

- To be able to comment on other catches on the site.
- To be able to add things to a wishlist
- To be able to 
- To earn badges or rewards for engagement, such as adding catches or leaving reviews.

### Super user

- As a super user I want to be able to edit or remove catches.
- Add/edit/delete products to the store.

## Design:

### Wireframes

Please refer to [WIREFRAMES.md](WIREFRAMES.md)

### Typography

Due to my time constraints and how difficult I found this project I stuck with default fonts.

### Color scheme

My color scheme was onyx, white and red(buttons) as shown below:

![Coolors](/static/images/readme-img/colors.png)

I chose to fully utilize bootstrap colours.

### Images

I do not hold any rights to the images that are uploaded by url, rights for images by file will be down to the uploader.
This page is for educational purposes only!

### Responsiveness

While creating my page I fully utilized [Bootstrap](https://getbootstrap.com/docs/4.4/getting-started/introduction/) for my responsive design.

## Features

![Landing page](/media/readme/landing.png)
Above is the landing page new users will see, It features a navbar with associated links and also my account link where they can register if they want. It also features a welcome box where they can click straight to products.

![User landing](/media/readme/userland.PNG)

The landing page for registered users is the same bar the extra links in My Account drop down as shown. Site admin is only accessible by Superuser.

![Product page](/media/readme/products2.PNG)

Above is the products page which unregistered and registered users will see, It features a list of the products and a filter option to filter by category.

![Product super](/media/readme/products1.PNG)

Above is the page a super user will see with edit and delete buttons.

![Product detail](/media/readme/detail.PNG)

above is the product details page to select quantity size(if applicable). The edit and delete buttons are only visible by superuser.

![Profile](/media/readme/profile.PNG)

Above is the profile page that logged in users will see.

![Catch cam](/media/readme/catchcam.PNG)

Above is the catch cam page for registered users only, the edit and delete buttons are configured to only be deleted by the owner or the super user.

![Add Product](/media/readme/add-product.PNG)

Above is the add product page with form, this is only accessible by Superuser.

![Edit Product](/media/readme/edit-product.PNG)

Above is the edit product form which is only accessible by superuser. This form pre fills with the data that is existing.

![Delete Product](/media/readme/delete.PNG)

Above is the delete modal when delete is clicked. This is only accesible by super user.

### Messages

![Messages](/media/readme/messages.PNG)

The page features built in messages as shown above in the example. These are error, success and info and they change depending on the action.

### Database design

![DataBase](/media/readme/db.PNG)

Above is my database design which I created using lucid chart, I am using posgresSQL which is a relational database.

## Testing:

Please refer to [TESTING.md](TESTING.md)

### Bugs

During the creation of Catch Master I was continuously using dev tools throughout to check for design issues/bugs where I corrected along the way. To my knowledge there are no known bugs to date.

## Technologies used

- GitHub - Used for my repository
- Gitpod - Used for my editor
- Heroku - Used to deploy the app
- postgreSQL - For my database
- AWS - For my static and media files.
- Stripe - For payment

### Languages used

- HTML
- CSS and Bootstrap library
- Javascript and Jquery library
- Python

## Deployment

My site was deployed to [heroku](https://www.heroku.com/) View the live site here [Here](https://catch-master-7d5d93ad4a60.herokuapp.com/)

### Repository

My repository is stored [Here](https://github.com/LeeEd1/catch_master).

#### Cloning

To clone a repository you will need to follow the steps below.

1. Locate the repository you wish to clone. [Here](https://github.com/LeeEd1/catch_master) is my repo for example.
2. Click the <>code button to the left of open.
3. Choose which you prefer HTTPS, SSH or GitHub CLI then click Copy to clipboard.
4. Open terminal or shell and change the current working directory to the one where you want the cloned repo.
5. In your terminal you will need to type the following command to clone the repo.
    `
    git clone https://github.com/LeeEd1/catch_master.git
    `
6. Press enter to create your local clone.

#### Forking

To fork a repository you will need to follow the steps below.

1. Locate the repository you wish to fork. [Here](https://github.com/LeeEd1/catch_master) is my repo for example.
2. Click the fork button located towards the top of the page inbetween unwatch and star.
3. Once you have clicked this you should have a copy in your Github account.

#### Requirements

Once you have cloned/forked a repository you will need to install the dependancies in the requiremnts.txt file, you can do this by running the command below:

`
pip3 install -r requirements.txt
`

If any packages are installed after cloning or forking you will need to freeze the requirements.txt file by running the command below:

`
pip3 freeze > requirements.txt
`

#### Environment Variables

You will need to hide your environment variables containing sensitive data such as secret keys or your database to stop these being pushed to github. I chose to put my variables directly in gitpod and heroku, the steps to do this are as follows.

Gitpod:

1. Click the profile icon in the top right corner of the Gitpod window and select User Settings.
2. In the left hand panel click variables.
3. Click New variable
3. Enter variable name. eg. VARIABLE_NAME
4. Enter Value.
5. Enter scope. (* for all repositories or username/repo-name for a specific repository)
6. Click add variable to save.

Heroku:

1. Navigate to your app in heroku and click settings.
2. Scroll down to config vars and click reveal config vars.
3. Enter your config vars eg. VARIABLE_NAME and value
4. Click add to save the variable

Note: 

Once your app is live in heroku you can place all of your config vars here. Heroku will automatically make them available for your app so you dont need to hard code them or use the export command.

#### Git:

Throughout my fourth project, I took extra care to ensure my commits were concise and detailed with the aim of assisting other developers who might work on a project after me. I utilised descriptive tags such as FIX, FEAT, CHORE and DOCS paired with short clear commit messages to ensure clarity and maintain a professional workflow.

FEAT: Use this tag if the commit introduces a new feature or functionality to the project. These changes enhance the project by adding new capabilities or tools for users or developers.

FIX: Use this tag if the commit addresses and resolves a bug or error in your code. These changes ensure the code behaves as intended by correcting specific issues or flaws.

CHORE: Use this tag if you are cleaning up code or making adjustments that do not introduce a new feature or resolve a bug. These changes are typically focused on maintenance, organisation or improving the clarity and structure of the codebase.

DOCS: Use this tag if you are creating or updating a project’s documentation such as README.md, TESTING.md or WIREFRAMES.md. These changes ensure the documentation is accurate, up-to-date and helpful for users and developers.

## Live deployment

### Database

1. To create my database I navigated to [postgreSQL](https://dbs.ci-dbs.net/) from code institute.
2. Enter your email and click submit.
3. Add the config var DATABASE_URL and your database url from postgreSQL as the value.
4. Go to the database section in your settings.py and comment out SQLite connection and add this below:
    DATABASES = {
    'default': dj_database_url.parse('your-database-url-here')
} IMPORTANT! Do not commit this as your database will be visible on github.
5. Run the following command to check your connected to external database:
    `
    python3 manage.py showmigrations
    `
6. If you are connected you should see a list of migrations and none of them will be checked.
7. you can then run migrations by using the following command.
    `
    python3 manage.py migrate
    `
8. Then load in the fixtures making sure categories is first by running the following commands:
    `
    python3 manage.py loaddata categories
    `
    `
    python3 manage.py loaddata products
    `
9. Create a Super user for your database by running the following command:
    `
    python3 manage.py createsuperuser
    `

10. To provent exposing our database url, Change the database setting back to SQLite database in settings.py.



### Heroku 

To deploy your app on heroku, you will need to follow the steps below.

1. Log into heroku.
2. Click the new button and select 'Create New App'.
3. Choose a name for your app and set the region to the region closest to you.
4. Choose a connection method, I used github as the deployment method.
5. Search for your repository and click connect.
6. Click the settings tab and reveal config vars.
7. Update the necessary config variables for your project.
8. Navigate back to deploy and select automatic deployment.

### AWS

1. Navigate to [AWS](https://aws.amazon.com/) and create a account on free tier.
2. Search for s3 service in AWS console and click Create bucket.
3. Choose a unique bucket name and select region. 
4. Uncheck "Block all Public access".
5. Navigate to the "properties tab" and activate "Static website hosting".
6. Set index.html  as the index document and click save. 
7. Navigate back to the Permissions tab, click edit on the CORS configuration and set the below configuration:
    ```
     [
       {
         "AllowedHeaders": ["Authorization"],
         "AllowedMethods": ["GET"],
         "AllowedOrigins": ["*"],
         "ExposeHeaders": []
       }
     ]
     ```
8. Under the Permissions tab click "Bucket Policy," create a policy using the policy generator (choose "S3 Bucket Policy," set the principal to "*," enter your bucket's ARN, add the statement and generate the policy), copy generated JSON into the bucket policy editor and save the changes.
9. Navigate to IAM to create a User Group, you will need to add a policy to user group and then create a user to go in the group. Once created download the csv file and copy these values into your live environment.
10. In your settings.py file you will need to update your name and region to match your bucket.

## Credits:

### Content

- [Color Hex](https://www.color-hex.com/color-palette/64222) For my color choices.
- [Font Awesome](https://fontawesome.com/) For my icons.
- [Google fonts](https://fonts.google.com/) For my fonts.

### Media

I do not hold any rights to any images displayed on this site as they are uploaded by photo URL, this site is purely educational purposes only.

### People

- I would like to thank my mentor [Spencer barriball](https://github.com/5pence) for his support throughout my fourth project and again pointing me in the right direction.
- I would like to thank my friend [Nicholas Mobey](https://www.linkedin.com/in/nicolas-mobey-79149049) for his continuous support.
- I would like to thank the [CI Tutor support](https://learn.codeinstitute.net/ci_support/level5diplomainwebappdevelopment/tutor) for their ongoing support throughout my projects.