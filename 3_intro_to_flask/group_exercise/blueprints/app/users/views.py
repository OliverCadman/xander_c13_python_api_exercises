"""
A blueprint view for 'users' resource.

Flask blueprints allow us to create a more modular Flask project, 
where each resource is placed in its own file. This is a better alternative
to having all views in a single file, as modularity promotes SOC and good
code organisation.
"""


def user_group():
    """GET a list of users or POST a single user."""
    pass


def user_item(user_id):
    """GET a user by ID."""
    pass
