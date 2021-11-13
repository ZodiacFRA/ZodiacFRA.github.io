SLIDESHOW_PROJECT_TEMPLATE = """
<!--------------------------------------------------------------------------- {} -->
    <div class="article_container">
        <div class="article_text">
          <h2><a href="./projects/{}.html">{}</a></h2>
          <h3>{}</h3><h3>{}</h3>
          <p>{}</p>
        </div><div></div>
        <a class="slideshow_container" href="./projects/{}.html" data-cycle="{}">
            {}</a>
    </div>"""

SLIDESHOW_PROJECT_TEMPLATE_NO_LINK = """
<!--------------------------------------------------------------------------- {} -->
    <div class="article_container">
        <div class="article_text">
          <h2>{}{}</h2>
          <h3>{}</h3><h3>{}</h3>
          <p>{}</p>
        </div><div></div>
        <a class="slideshow_container" href="./projects/{}.html" data-cycle="{}">
            {}</a>
    </div>"""

SLIDESHOW_IMAGE_TEMPLATE = """<img src="{}">\n\t\t\t\t\t\t"""
