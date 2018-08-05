#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Delete old branches. Defaults to > 3 months
"""
import datetime
import json
import os


import requests


def main():
    delete_old_branches()


def delete_old_branches(max_months=3):
    # Get all branches
    token = os.environ['GITLAB_TOKEN']
    token = open(os.path.expanduser('~/.config/gitlab')).read().strip()

    branches_url = 'https://gitlab.com/api/v4/projects/1591562/repository/branches'
    headers = {'Private-Token': token, 'content-type': 'application/json'}
    s = requests.Session()
    branches = []
    page = 1
    while True:
        params = {'per_page': 100, 'page': page}
        res = s.get(branches_url, headers=headers, params=params)
        repos = res.json()
        if repos:
            for repo in repos:
                if repo['name'] != 'master':
                    branches.append((repo['name'], repo['commit']['created_at']))
            page += 1
        else:
            break

    # Delete old branches
    max_age = datetime.timedelta(days=30*max_months)
    to_delete = []
    for name, ctime in branches:
        ctime = ctime[:ctime.find('T')]
        created_time = datetime.datetime.strptime(ctime, '%Y-%m-%d')
        branch_age = datetime.datetime.now() - created_time
        if branch_age > max_age:
            to_delete.append(name)

    for branch_name in to_delete:
        delete_url = '{}/{}'.format(branches_url, branch_name)
        s.delete(delete_url, headers=headers)


def lambda_handler(*args):
    # For run on AWS Lambda
    import base64
    import boto3

    client = boto3.client('kms')
    encrypted_gitlab_token = 'AQICAHhTH9iFUXSe2SisnI/nV9WRq6R8Ez2U5kEUMGVej/D3OQGWmi9PgDfzdLTopgwpUhRjAAAAcjBwBgkqhkiG9w0BBwagYzBhAgEAMFwGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMbTM5BHfFwFimHlqaAgEQgC9m27xNr+hEEDLqtsw/4R/l/Z0MBz1hX+owrPknaH8EkuyJl5xm6rKbG1WCvjM2fQ=='  # noqa
    gitlab_token = client.decrypt(
        CiphertextBlob=base64.b64decode(encrypted_gitlab_token)
    )['Plaintext'].decode('ascii')

    class_id = os.environ['class_id']
    token = gitlab_token
    create_weekly_mr_stats_issue(class_id, token, ping_class=True)


if __name__ == "__main__":
    main()
