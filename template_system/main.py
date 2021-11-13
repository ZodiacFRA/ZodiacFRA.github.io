import json
import glob
from os import path

from templates.misc import *
from templates.slideshow_project_template import *
from templates.video_project_template import *


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
        project_data["name"],
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


def create_project_page(project_data):
    pass


def do_page(page_name, header, footer):
    with open(f'./content/{page_name}.json', 'r') as f:
        page_projects = json.loads(f.read())
    page = header
    for project_data in page_projects:
        # Slideshows are also used for static images
        if project_data["type"] == "slideshow":
            page += create_slideshow(project_data)
        elif project_data["type"] == "video":
            page += create_video(project_data)
        if "page_name" in project_data:
            create_project_page(project_data)
    page += footer
    with open(f'../{page_name}.html', 'w') as f:
        f.write(page)


if __name__ == '__main__':
    do_page("index", HEADER, MAIN_FOOTER)
    do_page("older_works", HEADER, OLDER_WORKS_FOOTER)
