from pprint import pprint

from utils import *
from html_templates import *
from html_snippets_creators import *


def create_aggregation_page(data, page_name, footer='', timesort_projects=False):
    """ Aggregation pages are all created in the root dir """
    if timesort_projects:
        data = sort_projects_by_date(data)

    # Make an exception for the index page
    if page_name == "Index":
        html = get_header("Home")
    else:
        html = get_header(page_name)
    # Add the body of the page
    for project_data in data:
        html += get_project_snippet(project_data)
    # Add the footer
    html += footer

    with open(f'../{get_safe_name(page_name)}.html', 'w') as f:
        f.write(html)


def create_project_page(project_data):
    html = get_header(project_data["name"], '..')
    # If it contains a string, use it to load the html, otherwise generate it
    if project_data["create_project_page"]:
        project_body = load_html(project_data["create_project_page"])
        subtext = ''
    else:
        project_img_dir_path = os.path.join(
            "./media/",
            project_data.get("image_folder_name", '')
        )
        images = get_files_from_directory('.' + project_img_dir_path, ".webp")
        project_body = '\n'.join(
            ["""<img src="{}">""".format(image) for image in images]
        )
        project_body = PROJECT_DEFAULT_LAYOUT.format(project_body)
        subtext = project_data.get("subtext", "")
    html += PROJECT_INTRO.format(
        project_data["name"],
        " - ".join(project_data["created_with"]),
        project_data["date"],
        subtext
    )
    html += project_body
    html += "</body>"
    with open(f'../projects/{project_data["safe_name"]}.html', 'w') as f:
        f.write(html)


def create_custom_page(name, header, body, footer, output_path="../"):
    html = header + body + footer
    print(html)
    output_path = os.path.join(output_path, get_safe_name(name))
    with open(f'{output_path}.html', 'w') as f:
        f.write(html)


if __name__ == '__main__':
    data = load_JSON_files("./data/")
    # Create the "Themed aggregation pages"
    merged_data = [v for k, v in data.items()]
    merged_data = sum(merged_data, [])
    create_aggregation_page(
        get_projects_per_tags(merged_data, ["blender", "cinema 4d"]),
        "3D",
        footer=FOOTER.format(''),
        timesort_projects=True
    )
    create_aggregation_page(
        get_projects_per_tags(merged_data, ["code", "python", "c\+\+"]),
        "Code",
        footer=FOOTER.format(''),
        timesort_projects=True
    )
    # Create the single project pages
    # The projects which needs their own specific pages will have the
    # "create_project_page" attribute containing the name of the file to create
    for json_filepath, json_data in data.items():
        for project in json_data:
            if "create_project_page" in project:
                create_project_page(project)
    # Create the index page, which will contain all the projects defined in
    # index.json
    index_data = data.pop("index.json", None)
    if index_data is None:
        print(f"index.json file needed")
        exit()
    create_aggregation_page(
        data=index_data,
        page_name="Index",
        footer=FOOTER.format(FOOTER_NEXT_PAGE_BUTTON)
    )

    # Create the "Older works" page
    create_aggregation_page(
        data=[v for k, v in data.items()][0],
        page_name="Older works",
        footer=FOOTER.format('')
    )

    # create_custom_page(
    #     "Contact",
    #     get_header("Contact"),
    #     load_html("contact.html"),
    #     FOOTER.format('')
    # )
