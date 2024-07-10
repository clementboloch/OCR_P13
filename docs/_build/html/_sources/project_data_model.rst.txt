Project Data Model
==================

The project database structure and data models are defined in Django models within the `lettings` and `profiles` apps.

Profiles App
------------

Model: Profile
^^^^^^^^^^^^^^

- **File**: `profiles/models.py`
- **Description**: Represents a user profile that extends the built-in User model with additional information.
- **Fields**:
  - `id`: Primary key, auto-generated.
  - `user`: A one-to-one relationship with the built-in User model. The profile is deleted if the user is deleted.
  - `favorite_city`: An optional field to store the user's favorite city, with a maximum length of 64 characters.

Lettings App
------------

Model: Address
^^^^^^^^^^^^^^

- **File**: `lettings/models.py`
- **Description**: Represents an address.
- **Fields**:
  - `id`: Primary key, auto-generated.
  - `number`: A positive integer field for the address number, validated to be at most 9999.
  - `street`: A string field for the street name, maximum length of 64 characters.
  - `city`: A string field for the city name, maximum length of 64 characters.
  - `state`: A string field for the state, maximum length of 2 characters, validated to have a minimum length of 2 characters.
  - `zip_code`: A positive integer field for the zip code, validated to be at most 99999.
  - `country_iso_code`: A string field for the country ISO code, maximum length of 3 characters, validated to have a minimum length of 3 characters.


Model: Letting
^^^^^^^^^^^^^^

- **File**: `lettings/models.py`
- **Description**: Represents a letting.
- **Fields**:
  - `id`: Primary key, auto-generated.
  - `title`: A string field for the letting title, maximum length of 256 characters.
  - `address`: A one-to-one relationship with the Address model. The letting is deleted if the address is deleted (`OneToOneField` pointing to the `Address` model).
