<h1 align="center">Diasfero</h1>



- The working website can be found [here.](https://fsmp.herokuapp.com/)
- GitHub [here.](https://github.com/Aleksandre19/fsmp.git)


Diasfero is video portal in a healthcare area. A person can register on this site and make subscription in order to have access to the videos. This site has a mobile first approach markup. The site is divieded by sections for users easy use and navigation purpose. Once user is logged in: he or she can access to the videos by categories and sub categories, add a video in the "My List" and like a video. The user has a profile page where he or she can manage own accounts.

To enhance a user experience the site uses a javascript video slider which has a swipeable functionality on the tablet and lower devices. On the desktop and large devices the video slider maintains a swipeable functionality and additionally shows a arrows for a mouse navigation.

<h2 align="center"><img src="https://i.ibb.co/t8v4g5G/all-devices-black.png"></h2>
  

# User Experience (UX)

-   ### User stories

    - #### First time visitor
        1. As a first time visitor I want to easily and quikly understand what is the site about.
        2. As a first time visitor I want to know quikly if it is privite or company.
        3. As a first time visitor I  want to have ability to watch demo videos.
        4. As a firts time visitor I want to know how to access content.
        5. As a first time visitor I want to have FAQ

    - #### Returning visitor 
        1. As a returned visitor I want to have ability to contact to the site owner in case any additional questions.
        2. As a returned visitor I want have ability to make a subscription.
        3. As a returned visitor I want to have ability to choose a subscription's plans.

    - #### User of the site
        1. As a site user I want to have my profile page from where I can manage my account and quikly access to my videos.
        2. As a site user I want that videos be sorted by categories and subcategories.
        3. As a site user I want to have search field.
        4. As a site user I want to be able to truck upcomming events and incase of wish be able to save it.
        5. As a site user I want to make likes on the videos and have ability to save in "My List".
        6. As a site user I want that the site be mobile friendly. 



-   ### Strategy
    - Create a web-page's sketch
    - Create a design in Photoshop
    - Use a bootstrap to make a mobile friendly.
    - Create a site which will be written in a Django/Python.
    - Use a Django's all-auth functionality to create a user stories
    - Use a Javascript to create a swipeable video slider
    - Use a heroku for a deploiment and a GitHub for a repository  

- ### Structure
    - **The site has a main top manu which displays the maijor links.**
        - If is user is not registered a subscription link is shown
        - If a user is registered and has no subscription than the subscription link remains in the top menu
        - If a user is registered and has subscription so the subscription link disappears and the videos link appears
    - **On the right side of the site is a user icon.**
        - If a user is not authenticated/registered and clicks on that icon so he/she goes the authentication/registration page.
        - If a user is authenticated and has subscription so by clicking on that icon a profile links appears.
        - If a user is authenticated and has no subscription so the profile links disappears and appears a subscription and a logout links.
    - **The site has a video sliders by categories** 
        - On the mobiles and tablets video slider is only swipeabel.
        - On the desjtop devices swipable functionality remains and additionally appears a arrows on the both sids of the galleries.
    - **For accessing to the all videos the site has separate link in the top menu named by Videos**
        - On the desktop devices categories and sub categories are listed left side of the site.
            - When a user clicks one of the specific category's link in stead of disppearing other links from the side menu they remain unchanged and a user has ability to choose other link without navigating back.
        - On the mobile and tablet devices the side menu is hidden automatically  and it appears only when a user clicks on the select tag icon and covers around 25% of the page.
            - If a user's finger touches to the page and scrolls the side manu remains still.
            - If user's finger touches to the side manu and scrolls the page remains still.
        - To close the side menu a user clicks on the X icon
    - **The user has ability to leave a feedback from his profile page**
        -  The last leaved feedback is shown on the home page of the site when the user is logged in.
    - **In the footer section there are quick access links.** 
- ### Skeleton

    - I draw the site structure on a [balsmiq](https://balsamiq.cloud/) for all the type of divecies (Mobiles, Tablets, Desktops)
    - ##### Wireframes
    Desktops | Tablets | Mobiles
    -------- | -------- | -------
    [Home page not logged in](https://github.com/Aleksandre19/fsmpfiles/blob/0465d659bd405065d9b955fd9ccb5c8660f5394e/Desktop/home-not-logged-in.pdf) | [Home page not logged in](https://github.com/Aleksandre19/fsmpfiles/blob/0465d659bd405065d9b955fd9ccb5c8660f5394e/Tablets/tablet-home-not-logged-in.pdf) | [Home page not logged in](https://github.com/Aleksandre19/fsmpfiles/blob/0465d659bd405065d9b955fd9ccb5c8660f5394e/mobile/mobile-home-not-logged.pdf)
    [Home page logged in](https://github.com/Aleksandre19/fsmpfiles/blob/0465d659bd405065d9b955fd9ccb5c8660f5394e/Desktop/home-logged-in.pdf) | [Home page logged in](https://github.com/Aleksandre19/fsmpfiles/blob/0465d659bd405065d9b955fd9ccb5c8660f5394e/Tablets/tablet-home-logged-in.pdf) | [Home page logged in](https://github.com/Aleksandre19/fsmpfiles/blob/0465d659bd405065d9b955fd9ccb5c8660f5394e/mobile/mobile-home-logged-in.pdf)
    [Videos page](https://github.com/Aleksandre19/fsmpfiles/blob/0465d659bd405065d9b955fd9ccb5c8660f5394e/Desktop/videos.pdf) | [Videos page](https://github.com/Aleksandre19/fsmpfiles/blob/0465d659bd405065d9b955fd9ccb5c8660f5394e/Tablets/tablet-videos-page.pdf) | [Videos page](https://github.com/Aleksandre19/fsmpfiles/blob/0465d659bd405065d9b955fd9ccb5c8660f5394e/mobile/mobile-videos.pdf)
    [Subscription page](https://github.com/Aleksandre19/fsmpfiles/blob/0465d659bd405065d9b955fd9ccb5c8660f5394e/Desktop/subscription.pdf) | [Subscription page](https://github.com/Aleksandre19/fsmpfiles/blob/0465d659bd405065d9b955fd9ccb5c8660f5394e/Tablets/tablet-subscription.pdf) | [Subscription page](https://github.com/Aleksandre19/fsmpfiles/blob/0465d659bd405065d9b955fd9ccb5c8660f5394e/mobile/mobile-subscription.pdf)
    [Single video page](https://github.com/Aleksandre19/fsmpfiles/blob/0465d659bd405065d9b955fd9ccb5c8660f5394e/Desktop/single-video.pdf) | [Single video page](https://github.com/Aleksandre19/fsmpfiles/blob/0465d659bd405065d9b955fd9ccb5c8660f5394e/Tablets/tablet-single-video.pdf) | [Single video page](https://github.com/Aleksandre19/fsmpfiles/blob/0465d659bd405065d9b955fd9ccb5c8660f5394e/mobile/mobile-single-video.pdf)
    [Category page](https://github.com/Aleksandre19/fsmpfiles/blob/0465d659bd405065d9b955fd9ccb5c8660f5394e/Desktop/single-category.pdf) | [Category page](https://github.com/Aleksandre19/fsmpfiles/blob/0465d659bd405065d9b955fd9ccb5c8660f5394e/Tablets/tablet-category.pdf) | [Category page](https://github.com/Aleksandre19/fsmpfiles/blob/0465d659bd405065d9b955fd9ccb5c8660f5394e/mobile/mobile-categories.pdf)
    [Registration page](https://github.com/Aleksandre19/fsmpfiles/blob/0465d659bd405065d9b955fd9ccb5c8660f5394e/Desktop/registration.pdf) | [Registration page](https://github.com/Aleksandre19/fsmpfiles/blob/0465d659bd405065d9b955fd9ccb5c8660f5394e/Tablets/tablet-registration.pdf) | [Registration page](https://github.com/Aleksandre19/fsmpfiles/blob/0465d659bd405065d9b955fd9ccb5c8660f5394e/mobile/mobile-registration.pdf)
    [User profile page](https://github.com/Aleksandre19/fsmpfiles/blob/0465d659bd405065d9b955fd9ccb5c8660f5394e/Desktop/profile.pdf) | [User profile page](https://github.com/Aleksandre19/fsmpfiles/blob/0465d659bd405065d9b955fd9ccb5c8660f5394e/Tablets/tablet-profile.pdf) | [User profile page](https://github.com/Aleksandre19/fsmpfiles/blob/0465d659bd405065d9b955fd9ccb5c8660f5394e/mobile/mobile-profile.pdf)
    [Playlists page](https://github.com/Aleksandre19/fsmpfiles/blob/0465d659bd405065d9b955fd9ccb5c8660f5394e/Desktop/playlists.pdf) | [Playlists page](https://github.com/Aleksandre19/fsmpfiles/blob/0465d659bd405065d9b955fd9ccb5c8660f5394e/Tablets/tablet-playlists.pdf) | [Playlists page](https://github.com/Aleksandre19/fsmpfiles/blob/0465d659bd405065d9b955fd9ccb5c8660f5394e/mobile/mobile-playlists.pdf)
    [Events page](https://github.com/Aleksandre19/fsmpfiles/blob/0465d659bd405065d9b955fd9ccb5c8660f5394e/Desktop/events.pdf) | [Events page](https://github.com/Aleksandre19/fsmpfiles/blob/0465d659bd405065d9b955fd9ccb5c8660f5394e/Tablets/tablet-profile-event.pdf) | [Events page](https://github.com/Aleksandre19/fsmpfiles/blob/0465d659bd405065d9b955fd9ccb5c8660f5394e/mobile/mobile-profile-events.pdf)
    [Contact page](https://github.com/Aleksandre19/fsmpfiles/blob/0465d659bd405065d9b955fd9ccb5c8660f5394e/Desktop/contact.pdf) | [Contact page](https://github.com/Aleksandre19/fsmpfiles/blob/0465d659bd405065d9b955fd9ccb5c8660f5394e/Tablets/tablet-contact.pdf) | [Contact page](https://github.com/Aleksandre19/fsmpfiles/blob/0465d659bd405065d9b955fd9ccb5c8660f5394e/mobile/mobile-contact.pdf)
    [Account page](https://github.com/Aleksandre19/fsmpfiles/blob/0465d659bd405065d9b955fd9ccb5c8660f5394e/Desktop/account.pdf) | [Account page](https://github.com/Aleksandre19/fsmpfiles/blob/0465d659bd405065d9b955fd9ccb5c8660f5394e/Tablets/tablet-account.pdf) | [Account page](https://github.com/Aleksandre19/fsmpfiles/blob/f3d81024785ccd8e829bafd2d23fa0f9d76180f7/mobile/mobile-sccount.pdf)
    [FAQ page](https://github.com/Aleksandre19/fsmpfiles/blob/0465d659bd405065d9b955fd9ccb5c8660f5394e/Desktop/FAQ.pdf) | [FAQ page](https://github.com/Aleksandre19/fsmpfiles/blob/0465d659bd405065d9b955fd9ccb5c8660f5394e/Tablets/tablet-faq.pdf) | [FAQ page](https://github.com/Aleksandre19/fsmpfiles/blob/f3d81024785ccd8e829bafd2d23fa0f9d76180f7/mobile/mobile-faq.pdf)
    [Authentication page](https://github.com/Aleksandre19/fsmpfiles/blob/0465d659bd405065d9b955fd9ccb5c8660f5394e/Desktop/Authentication.pdf) | [Authentication page](https://github.com/Aleksandre19/fsmpfiles/blob/0465d659bd405065d9b955fd9ccb5c8660f5394e/Tablets/tablet-authentication.pdf) | [Authentication page](https://github.com/Aleksandre19/fsmpfiles/blob/f3d81024785ccd8e829bafd2d23fa0f9d76180f7/mobile/mobile-authentication.pdf)
-   I made list of the databases and theirs fields in IOS Pages program and converted to the PDF.
    -   [Databases](https://github.com/Aleksandre19/fsmpfiles/blob/f0f4e9a9a8cfa2b71d187f0ca51072dd2e75f21e/databases_sketches.pdf)
- ### Design
    - I draw the designe of the site in the photoshop.
    - ##### Design PNG files
    Desktops | Mobiles
    -------- | --------
    [Home page not logged in](https://github.com/Aleksandre19/fsmpfiles/blob/92c67c17e2cdfe0d9ad4d5541f649fb11b0f29b0/design/desktop/home-not-logged-in.png) | [Home page not logged in](https://github.com/Aleksandre19/fsmpfiles/blob/92c67c17e2cdfe0d9ad4d5541f649fb11b0f29b0/design/mobile/home-not-logged-in.png)
    [Home page logged in](https://github.com/Aleksandre19/fsmpfiles/blob/92c67c17e2cdfe0d9ad4d5541f649fb11b0f29b0/design/desktop/home-not-logged-in.png) | [Home page logged in](https://github.com/Aleksandre19/fsmpfiles/blob/92c67c17e2cdfe0d9ad4d5541f649fb11b0f29b0/design/mobile/home-logged-in.png)
    [Videos page](https://github.com/Aleksandre19/fsmpfiles/blob/92c67c17e2cdfe0d9ad4d5541f649fb11b0f29b0/design/desktop/videos.png) | [Videos page](https://github.com/Aleksandre19/fsmpfiles/blob/92c67c17e2cdfe0d9ad4d5541f649fb11b0f29b0/design/mobile/videos.png)
    [Subscription page](https://github.com/Aleksandre19/fsmpfiles/blob/92c67c17e2cdfe0d9ad4d5541f649fb11b0f29b0/design/desktop/subscription.png) | [Subscription page](https://github.com/Aleksandre19/fsmpfiles/blob/92c67c17e2cdfe0d9ad4d5541f649fb11b0f29b0/design/mobile/subscription.png)
    [Single video page](https://github.com/Aleksandre19/fsmpfiles/blob/92c67c17e2cdfe0d9ad4d5541f649fb11b0f29b0/design/desktop/single_video.png) | [Single video page](https://github.com/Aleksandre19/fsmpfiles/blob/92c67c17e2cdfe0d9ad4d5541f649fb11b0f29b0/design/mobile/single-video.png)
    [Category page](https://github.com/Aleksandre19/fsmpfiles/blob/92c67c17e2cdfe0d9ad4d5541f649fb11b0f29b0/design/desktop/category.png) | [Category page](https://github.com/Aleksandre19/fsmpfiles/blob/92c67c17e2cdfe0d9ad4d5541f649fb11b0f29b0/design/mobile/category.png)
    [Registration page](https://github.com/Aleksandre19/fsmpfiles/blob/92c67c17e2cdfe0d9ad4d5541f649fb11b0f29b0/design/desktop/registration.png) | [Registration page](https://github.com/Aleksandre19/fsmpfiles/blob/92c67c17e2cdfe0d9ad4d5541f649fb11b0f29b0/design/mobile/registration.png)
    [User profile page](https://github.com/Aleksandre19/fsmpfiles/blob/92c67c17e2cdfe0d9ad4d5541f649fb11b0f29b0/design/desktop/profile.png) | [User profile page](https://github.com/Aleksandre19/fsmpfiles/blob/3fe6ca7ec642b14eb791bb0206b5ff19cd8fe3e9/design/mobile/profile.png)
    [Playlists page](https://github.com/Aleksandre19/fsmpfiles/blob/92c67c17e2cdfe0d9ad4d5541f649fb11b0f29b0/design/desktop/playlist.png) | [Playlists page](https://github.com/Aleksandre19/fsmpfiles/blob/92c67c17e2cdfe0d9ad4d5541f649fb11b0f29b0/design/mobile/profile.png)
    --- | [Events page](https://github.com/Aleksandre19/fsmpfiles/blob/92c67c17e2cdfe0d9ad4d5541f649fb11b0f29b0/design/mobile/profile-events.png)
    [Contact page](https://github.com/Aleksandre19/fsmpfiles/blob/92c67c17e2cdfe0d9ad4d5541f649fb11b0f29b0/design/desktop/contact.png) | [Contact page](https://github.com/Aleksandre19/fsmpfiles/blob/92c67c17e2cdfe0d9ad4d5541f649fb11b0f29b0/design/mobile/contact.png)
    [Account page](https://github.com/Aleksandre19/fsmpfiles/blob/92c67c17e2cdfe0d9ad4d5541f649fb11b0f29b0/design/desktop/account.png) | [Account page](https://github.com/Aleksandre19/fsmpfiles/blob/3fe6ca7ec642b14eb791bb0206b5ff19cd8fe3e9/design/mobile/account.png)
    [FAQ page](https://github.com/Aleksandre19/fsmpfiles/blob/92c67c17e2cdfe0d9ad4d5541f649fb11b0f29b0/design/desktop/faq.png) | [FAQ page](https://github.com/Aleksandre19/fsmpfiles/blob/92c67c17e2cdfe0d9ad4d5541f649fb11b0f29b0/design/mobile/faq.png)
    [Authentication page](https://github.com/Aleksandre19/fsmpfiles/blob/92c67c17e2cdfe0d9ad4d5541f649fb11b0f29b0/design/desktop/authentication.png) | [Authentication page](https://github.com/Aleksandre19/fsmpfiles/blob/92c67c17e2cdfe0d9ad4d5541f649fb11b0f29b0/design/mobile/authentication.png)
    
 # Testing
-   [HTML Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Ffsmp.herokuapp.com%2F)
    -   **Warrning** - Attribute for javascript tag was not necessary.
        - I removed it.
    - **Error** - For dublicated IDs.
    - **Warrning** - br tag was had closing /
    - **Warrning** - Section tag didn't have a H element. I changed the section element to the div element because there was not necessary to be section tag.
    - **Error** - In the search input element was not space between the attributes.
    - **Error** - There was missing a h3 closing element.
    - **Error** - In the header and footer logo had style with ID attribute. I chenged it to the class attribute.
    - **Error** - The  aria-describedby attribute was used unnecessary.
-   [CSS Validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Ffsmp.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
    -   **Error** - Font size in rem was not recognized. I converted to px.
    -   **Error** - There was ```background-position-y: top left;``` instead of ```background-position: top left;```
    -   **Error** - There was ```all: revert !important;``` instead of ```fill: revert !important;```
    -   **Error** - The ```background-position: cover;``` was not recognized and i deleted it.
-   [Javascript Validator](https://jshint.com)
    - All Javascript is written in ES6 and I ignored errors for ES6.
    - **Error** - There was missing semicolon on four places.
-   [Python Validator](http://pep8online.com)
    - Python codes were tested and were found the folowing errors which were fixed.
        - White space end of the code.
        - missing whitespace around operator.
        - Unexpected spaces to assign operator.
        - blank line contains whitespace.
        - continuation line missing indentation or outdented.
        - whitespace before ':'.
        - Empty line has a white space.
    - I gnored a too long string's error.
-   **Lighthouse**
    - ![Lighthouse](https://i.ibb.co/NxfkrRj/lighthouse.png)
-   **Stripe and Registration Testing**
    -   Clicked on the subscription link or user icon top right corner.
    -   Clicked Sing Up.
    -   Filled up with required information and clicked Sing Up button.
        - Here was email verification sending problem. There was missed email host configuration which i added at the end of the settings.py
    -   Recived verification email and verified the email.
    -   Logged in and was redirected to the subscription plans page.
    -   Choosed a plan by clicking on the choose button.
    -   Redirected to the checkout page.
    -   Filled the fields with required information and used Stripe's test card number ```4242 4242 4242 4242  04/24  242  42424```.
    -   Clicked on Subscription button and after couple of seconds it was done and i had access to the videos.
    -   Checked Stripe account and payment was received and subscription was created.
-   **Contact Testing**
    -   Clicked on contact link in top main menu.
    -   Filled up with required information and clicked Send A Message button.
    -   Alert window popuped which said that my email has been sent.
    -   Checked email account and there was new email inbox.
-   **Browser and responsiveness Testing**
    -   The site was tested only on google chrome.
    -   The site responsiveness was tested by google's Inspect tool.
# Technologies Used
## Languages Used
-   [HTML](https://html.com)
-   [CSS](https://www.w3.org/Style/CSS/Overview.en.html)
-   [JavaScript](https://www.javascript.com)
-   [Python](https://www.python.org)
## Frameworks, Libraries & Programs Used
-   [Boostrap 4.5](https://getbootstrap.com/docs/4.5/getting-started/introduction/)
    -   It was used to make the site responsive, style it and make structure.
-   [Django](https://www.djangoproject.com)
    -   It was used for backend.
-   [hover.css](https://ianlunn.github.io/Hover/)
    -   It was used to animate the links of the top main menu.
-   [Google Fonts](https://fonts.google.com)
    - It was used for font styles.
- [EmailJs](https://www.emailjs.com)
    - It was used to send a email from contact page.
- [FontAwesome](https://fontawesome.com)
    - It was used for some some icons.
- [Balsamiq](https://balsamiq.com)
    - It was used to make a site's sketches.
- [Photoshop](https://www.adobe.com/se/products/photoshop.html?mv=search&mv=search&sdid=LZ32SYVR&ef_id=CjwKCAjwyvaJBhBpEiwA8d38vJ92jpPSjxSaHrkldilpyLHidAg3-Q5x0Q1Y87XIbJbkkt25j1YLORoCl-YQAvD_BwE:G:s&s_kwcid=AL!3085!3!393367673656!e!!g!!photoshop!1469952956!58520335113&gclid=CjwKCAjwyvaJBhBpEiwA8d38vJ92jpPSjxSaHrkldilpyLHidAg3-Q5x0Q1Y87XIbJbkkt25j1YLORoCl-YQAvD_BwE)
    - It was used to make a site's design.
- [JQuery](https://jquery.com)
    - It was used to some part of the codes.
- [Git](https://git-scm.com)
    - It was used for version control.
- [GitHub](https://github.com)
    - It was used for files repository.
- [Heroku](https://heroku.com)
    - It was used for deployment of the production site.
- [PostgreSQL](https://www.postgresql.org)
    - It was used for database.
- [AmazonS3](https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Categories=categories%23storage&trk=ps_a134p000006paz4AAA&trkCampaign=acq_paid_search_brand&sc_channel=PS&sc_campaign=acquisition_ND&sc_publisher=Google&sc_category=Storage&sc_country=ND&sc_geo=EMEA&sc_outcome=acq&sc_detail=amazon%20s3&sc_content=S3_e&sc_matchtype=e&sc_segment=495122625044&sc_medium=ACQ-P%7CPS-GO%7CBrand%7CDesktop%7CSU%7CStorage%7CS3%7CND%7CEN%7CText%7Cxx%7CEU&s_kwcid=AL!4422!3!495122625044!e!!g!!amazon%20s3&ef_id=CjwKCAjwyvaJBhBpEiwA8d38vIGhb17BBtEhUmoOJW5EYVtr8g9yjUA-MjBeRDEtQgoDAULz9sGA_RoCwu8QAvD_BwE:G:s&s_kwcid=AL!4422!3!495122625044!e!!g!!amazon%20s3&awsf.Free%20Tier%20Types=*all)
    - It was used for deployment of the static files and images.
-   [Stripe](https://stripe.com)
    - It was used to set up subscription.
-   [django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
    - It was used for creating of user stories.
# Deoployment
-   ### The site files were deployed on GitHub.
    -   Created a GitHub account
    -   Clicked on the GutHub icon left top corner.
    - Under the GitHub icon clicked on the New green button
    - Specified a repository name.
    - Wrote a description.
    - Clicked on public radio button to make the repository poublic.
    - And finally clicked on the Create repositoty greeb icon.
    - In the terminal I write the following commands to deploy the site on the GitHub.
        ```
            git init
            git commit -m "Initial commit"
            git branch -M main
            git remote add origin https://github.com/Aleksandre19/fsmp.git
            git push -u origin main
        ```
    -   **Repository cloning**
        -   Click on the green button named by code.
        - Copy the link in the opened small window.
-   ### Deployment on the Heroku
    -   Create account on the [Heroku](heroku.com).
    - Click on the new button.
    - Choose a create new app.
    - Write app's name.
    - Sett a region.
    - Click on create app.
    
    -   1.  Creating a if statment for DATABASES 
    -   1.  Installing a gunicorn
```
pip3 install gunicorn webserver
```
1. Freeze to requirements.txt
1. Creating a Procfile
```
web: gunicorn boutique_ado.wsgi:application
```
1. Login to heroku account
```
heroku login -i 
```
1. Disabling a colectstatic files 
```
heroku config:set DISABLE_COLLECTSTATIC=1 --app aleks-boutique-ado
```
1. Stting up a hosts in a settings.py
1. Adding a remote heroku
```
heroku git:remote -a aleks-boutique-ado
```
1. Adding a SECRET_KEY on heroku
1. Change SECRET_KEY in settings.py
1. Set up DEBUG to a True if ther is 'DEVELOPMENT' in os.environ()
### Creating an AWS Account
1. CORS Configuration
```
<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
<CORSRule>
<AllowedOrigin>*</AllowedOrigin>
<AllowedMethod>GET</AllowedMethod>
<MaxAgeSeconds>3000</MaxAgeSeconds>
<AllowedHeader>Authorization</AllowedHeader>
</CORSRule>
</CORSConfiguration>
```
### Connecting Django to S3
1.  Installing a boto3 
```
pip3 install boto3
```
1.  Installing a django-storages 
```
pip3 install django-storages
```


# Content
-   Design was drawed by be.
- I didn't have a time to write a real content.

# Not working
- Upcoming event on the home page for logged in users has only Javascript functionality.

