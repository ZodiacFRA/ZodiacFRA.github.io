import os

from utils import *
from html_templates import *


def get_slideshow_images_html(project_data):
    project_img_dir_path = os.path.join(
        "./media/",
        project_data.get("image_folder_name", '')
    )
    if "thumbnail_images" in project_data:
        # Use only the specified images (there can be only one)
        images = project_data["thumbnail_images"]
        images = [os.path.join(project_img_dir_path, i + ".webp") for i in images]
    else:
        # Use all the images from the project's folder, if the project has no
        # specific folder, no images will be used and a warning will be issued
        images = get_files_from_directory('.' + project_img_dir_path, ".webp")
        # Remove a single . from the path
        images = [i[1:] for i in images]
    return '\n'.join(["""<img src="{}">""".format(image) for image in images])


def get_project_snippet(project_data):
    # Create the "intro" part of the snippets html (title, date etc)
    if "create_project_page" in project_data:
        link = project_data["safe_name"]
        title = '⭢ ' + project_data["name"]
        intro = PROJECT_INTRO.format(
                    PROJECT_LINK.format(link, title),
                    " - ".join(project_data["created_with"]),
                    project_data["date"],
                    project_data.get("subtext", "")
                )
        tag = 'a'
        href = f"""href="./projects/{link}.html" """
    else:
        link = ''
        title = project_data["name"]
        intro = PROJECT_INTRO.format(
                    title,
                    " - ".join(project_data["created_with"]),
                    project_data["date"],
                    project_data.get("subtext", "")
                )
        tag = 'div'
        href = ''

    # Now add the media itself
    if project_data["type"] == "slideshow":
        images = get_slideshow_images_html(project_data)
        content = SLIDESHOW_PROJECT_TEMPLATE.format(
            tag,
            href,
            project_data.get("slideshow_speed", 3000),
            images,
            tag
        )
    elif project_data["type"] == "yt":
        content = YT_VIDEO_PROJECT_TEMPLATE.format(
            tag,
            href,
            project_data["video_link"],
            tag
        )
    elif project_data["type"] == "video":
        try:
            video_link = os.path.join(
                "./media/",
                project_data["image_folder_name"],
                project_data["video_link"]
            )
        except:
            print(project_data)
        content = VIDEO_PROJECT_TEMPLATE.format(
            tag,
            href,
            video_link,
            tag
        )
    else:
        print(f"""[-] - Unknown type (skipping): {project_data["type"]}""")
    return PROJECT_TEMPLATE.format(
        intro,
        content
    )
