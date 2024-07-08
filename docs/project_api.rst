Project API Description
=======================

This project is a Django application with three main components: `lettings`, `profiles`, and the main site `oc_lettings_site`. Each of these components contains a `views.py` file which handles HTTP requests for their respective parts of the application.

Components
----------

1. `oc_lettings_site`
2. `lettings`
3. `profiles`

oc_lettings_site API
=====================

Index View
----------

**File:** `oc_lettings_site/views.py`

**Function:** `index`

**Description:** Renders the main index page of the website.

**URL Pattern:** Root URL `/`

**Method:** GET

**Parameters:** None

**Returns:** HTML of the index page.

Lettings API
============

Index View
----------

**File:** `lettings/views.py`

**Function:** `index`

**Description:** Renders the index page for lettings, listing all available lettings.

**URL Pattern:** `/lettings/`

**Method:** GET

**Parameters:** None

**Returns:** HTML of the lettings index page.

Letting Detail View
-------------------

**File:** `lettings/views.py`

**Function:** `letting`

**Description:** Renders the detail page for a specific letting.

**URL Pattern:** `/lettings/<int:letting_id>/`

**Method:** GET

**Parameters:** `letting_id` (integer)

**Returns:** HTML of the specific letting's detail page.

Profiles API
============

Profiles List View
------------------

**File:** `profiles/views.py`

**Function:** `profiles_list`

**Description:** Renders a list of user profiles.

**URL Pattern:** `/profiles/`

**Method:** GET

**Parameters:** None

**Returns:** HTML of the profiles list page.
