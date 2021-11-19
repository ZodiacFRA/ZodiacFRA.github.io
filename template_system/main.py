import re
import json
import glob
from os import path

from templates.slideshow_project_template import *
from templates.video_project_template import *
from templates.projects import *
from templates.footer import *
from templates.header import *


def create_slideshow(project_data):
    images = ""
    for image_name in project_data["thumbnail_images"]:
        images += SLIDESHOW_IMAGE_TEMPLATE.format(path.join(
            "./images/",
            project_data.get('image_folder_name', ""),
            f"{image_name}.webp"
        ))

    template = SLIDESHOW_PROJECT_TEMPLATE_NO_LINK
    if "page_name" in project_data and project_data["page_name"]:
        template = SLIDESHOW_PROJECT_TEMPLATE
    res = template.format(
        ", ".join(project_data.get("tags", []) + project_data["created_with"]),
        project_data.get("page_name", ""),
        project_data["name"],
        " - ".join(project_data["created_with"]),
        project_data["date"],
        project_data.get("subtext", ""),
        project_data.get("page_name", ""),
        project_data.get("slideshow_speed", 3000),
        images
    )
    return res


def create_video(project_data):
    template = VIDEO_PROJECT_TEMPLATE_NO_LINK
    if "page_name" in project_data and project_data["page_name"]:
        template = VIDEO_PROJECT_TEMPLATE
    res = template.format(
        ", ".join(project_data.get("tags", []) + project_data["created_with"]),
        project_data.get("page_name", ""),
        project_data["name"],
        " - ".join(project_data["created_with"]),
        project_data["date"],
        project_data.get("subtext", ""),
        project_data["video_link"],
    )
    return res


def populate_page(page_projects, header, footer):
    page = header
    for project_data in page_projects:
        # Slideshows are also used for static images
        if project_data["type"] == "slideshow":
            page += create_slideshow(project_data)
        elif project_data["type"] == "video":
            page += create_video(project_data)
    page += footer
    return page


def create_presentation_page(page_name, header, footer):
    with open(f'./content/{page_name}.json', 'r') as f:
        page_projects = json.loads(f.read())
    with open(f'../{page_name}.html', 'w') as f:
        f.write(populate_page(page_projects, header, footer))


def create_project_page(project_name, header, content):
    with open(f'../projects/{project_name}.html', 'w') as f:
        f.write(header + content)


def create_aggregation_page(page_name, header, tags):
    projects = sort_projects_by_date(get_all_json_content())
    page_projects = []
    for project_data in projects:
        project_tags = " ".join(project_data.get("tags", []) + project_data["created_with"])
        for tag in tags:
            if re.search(tag, project_tags, re.IGNORECASE):
                page_projects.append(project_data)
    with open(f'../{page_name}.html', 'w') as f:
        f.write(populate_page(page_projects, header, ""))


def get_all_json_content():
    res = []
    for json_file in glob.glob("./content/*.json"):
        with open(json_file, 'r') as f:
            res += json.loads(f.read())
    return res


def sort_projects_by_date(projects_data):
    """ Returns all projects based on creation year (month not taken into account)
    Most recent first """
    projects_data.sort(key=lambda x: x["date"].split(' ')[-1], reverse=True)
    return projects_data


def get_header(tab_name, path):
    return HEADER.format(tab_name, *([path] * 9))


if __name__ == '__main__':
    create_presentation_page("index", get_header("Home", "."), MAIN_FOOTER)
    create_presentation_page("older_works", get_header("Older Works", "."), OLDER_WORKS_FOOTER)
    # Should be called in the page creation
    create_project_page("ile", get_header("Ile des morts project", ".."), ILE)
    create_project_page("tau", get_header("Tau project", ".."), TAU)
    create_project_page("tower", get_header("Semiotic Tower project", ".."), TOWER)
    create_project_page("typhoon", get_header("Typhoon project", ".."), TYPHOON)
    create_project_page("up_down", get_header("Up / Down project", ".."), UP_DOWN)
    create_project_page("arm", get_header("Arm Rig project", ".."), ARM)

    # Those pages will be created with all the projects having matching tags
    # Make sure to escape regex characters in the tags !
    create_aggregation_page("3d", get_header("3d projects", "."), ["blender", "cinema 4d"])
    create_aggregation_page("code", get_header("Code projects", "."), ["code", "python", "c\+\+"])
