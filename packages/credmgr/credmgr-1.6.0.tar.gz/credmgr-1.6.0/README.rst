CredentialManager
=================

Client for interacting with Credential Manager API

- API version: 1.0
- Package version: 1.6.0

Requirements
------------

Python 3.7+

Installation & Usage
--------------------

.. code-block:: sh

    pip install credmgr

Then import the package:

.. code-block:: python

    from credmgr import CredentialManager

Getting Started
---------------

.. code-block:: python

    credential_manager = CredentialManager(api_token="api_token")

    # List all Reddit apps
    reddit_apps = credential_manager.reddit_apps()
    for reddit_app in reddit_apps:
        print(reddit_app.name)

    # Create a Reddit app
    redditApp = credential_manager.reddit_app.create(
        name="reddit_app_name",
        client_id="client_id",
        client_secret="client_secret",
        user_agent="user_agent",
        redirect_uri="redirect_uri",
    )

    # Get the app by id
    reddit_app = credential_manager.reddit_app(1)

    # Edit the Reddit app
    reddit_app.edit(client_id="client_id_2")

    # Delete the app
    reddit_app.delete()
