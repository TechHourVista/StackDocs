# StackDocs Administrative Papers Web App



![Project Logo](/path/to/your/logo.png)

## Description

Administrative Papers Web App is a Django-based web application that allows users to seek and offer help for administrative problems through posts and comments. Users can create posts to describe their administrative issues or provide solutions to other users' problems. Additionally, they can interact by commenting on posts to share more insights or ask for clarifications.

## Features

- [x] User Registration and Authentication: New users can sign up and existing users can log in to the platform.

- [x] Create and Edit Posts: Users can create new posts to describe their administrative problems and also edit their own posts if needed.

- [x] Commenting: Users can post comments on other users' posts to offer help or ask for more details.

- [x] Search and Filter: The application provides search and filter options to help users find relevant posts.

- [ ] User Profiles: Users have their profiles where they can view and manage their posts and comments.

## Installation

Follow these steps to set up the project locally on your machine:

1. Clone the repository from GitHub:
```
git clone https://github.com/TechHourVista/StackDocs.git
```
2. Install the required dependencies. We recommend using a virtual environment:
```
python -m venv env
source env/bin/activate # On Windows: env\Scripts\activate
pip install -r requirements.txt
```

3. Set up the database:
```
python manage.py migrate
python manage.py createsuperuser 
```

4. Run the development server:
```
python manage.py runserver
```

5. Access the web app at http://localhost:8000/ in your web browser.

<details>
<summary><strong>Usage</strong></summary>

1. Register or log in with your existing account to access the platform.

2. Once logged in, you can create a new post describing your administrative problem or view and interact with other users' posts.

3. To comment on a post, click on the post title and scroll down to the comment section. Type your comment and submit it.

4. You can also search for specific posts by using the search bar or use the filter options to narrow down the results.

5. In your user profile, you can manage your posts and comments.

</details>


```topojson
{
  "type": "Topology",
  "transform": {
    "scale": [0.0005000500050005, 0.00010001000100010001],
    "translate": [100, 0]
  },
  "objects": {
    "example": {
      "type": "GeometryCollection",
      "geometries": [
        {
          "type": "Point",
          "properties": {"prop0": "value0"},
          "coordinates": [4000, 5000]
        },
        {
          "type": "LineString",
          "properties": {"prop0": "value0", "prop1": 0},
          "arcs": [0]
        },
        {
          "type": "Polygon",
          "properties": {"prop0": "value0",
            "prop1": {"this": "that"}
          },
          "arcs": [[1]]
        }
      ]
    }
  },
  "arcs": [[[4000, 0], [1999, 9999], [2000, -9999], [2000, 9999]],[[0, 0], [0, 9999], [2000, 0], [0, -9999], [-2000, 0]]]
}
```