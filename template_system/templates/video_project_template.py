VIDEO_PROJECT_TEMPLATE = """
<!--------------------------------------------------------------------------- {} -->
    <div class="article_container">
        <div class="article_text">
          <h2><a href="./projects/{}.html">{}</a></h2>
          <h3>{}</h3><h3>{}</h3>
          <p>{}</p>
        </div><div></div>
        <div class="video_container">
            <iframe style="border:0;" class="embedded_video" src="{}">
            </iframe>
        </div>
    </div>"""

VIDEO_PROJECT_TEMPLATE_NO_LINK = """
<!--------------------------------------------------------------------------- {} -->
    <div class="article_container">
        <div class="article_text">
          <h2>{}{}</h2>
          <h3>{}</h3><h3>{}</h3>
          <p>{}</p>
        </div><div></div>
        <div class="video_container">
            <iframe style="border:0;" class="embedded_video" src="{}">
            </iframe>
        </div>
    </div>"""
