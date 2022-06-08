import os
import re
import glob
import json

from html_templates import *


def get_json_data(filepath):
    with open(filepath, 'r') as f:
        data = json.loads(f.read())
    return data


def get_files_from_directory(dir_path, file_type=''):
    if not os.path.isdir(dir_path):
        print(f"""[-] - Directory not found: {dir_path}""")
        return []
    return [f for f in glob.glob(os.path.join(dir_path, f"*{file_type}"))]


def load_JSON_files(dir_path):
    json_filepaths = get_files_from_directory(dir_path, ".json")
    data = {}
    for json_filepath in json_filepaths:
        tmp = get_json_data(json_filepath)
        for project in tmp:
            project["safe_name"] = get_safe_name(project["name"])
        data[os.path.basename(json_filepath)] = tmp
    return data


def sort_projects_by_date(data):
    """
    Returns all projects based on creation year
    - Month not taken into account
    - Most recent first
    """
    data.sort(key=lambda x: x["date"].split(' ')[-1], reverse=True)
    return data


def get_header(tab_name, path='.'):
    return HEADER.format(tab_name, *([path] * 9))


def get_safe_name(page_name):
    return page_name.replace('/', '').replace(' ', '_').lower()


def get_projects_per_tags(data, tags):
    matching_projects = []
    for project_data in data:
        project_tags = " ".join(project_data.get("tags", []) + project_data["created_with"])
        for tag in tags:
            if re.search(tag, project_tags, re.IGNORECASE):
                matching_projects.append(project_data)
    return matching_projects


def load_html(filename):
    filepath = os.path.join("./projects_html", filename)
    with open(filepath, 'r') as f:
        html = f.read()
    return html
