import os
import json
import streamlit.components.v1 as components

from pollination_streamlit.selectors import get_api_client

from pollination_streamlit_io import (
    auth_user, select_account, select_project)

import streamlit as st

api_client = get_api_client()

st.header("Auth User")

auth_user('auth-user', access_token=api_client.jwt_token)

account = select_account(
    'select-account', access_token=api_client.jwt_token) or ''
st.json(account or '{}')

if account and 'name' in account:
    st.subheader('Hi ' + account['name'] + ', select a project:')
    owner = None
    if 'username' in account:
        owner = account['username']
    elif 'account_name' in account:
        owner = account['account_name']

    project = select_project(
        'select-project', access_token=api_client.jwt_token, project_owner=owner)
    st.json(project or '{}')
