FOOTER = """
<!--------------------------------------------------------------------------- EOF -->
    {}
    <script src="https://zodiacfra.github.io/scripts/slideshow.js"></script>
</body>
"""

FOOTER_NEXT_PAGE_BUTTON = """
<h2 style="text-align: right;"><a href='./older_works.html'>Older ⭢</a></h2>
"""

################################################################################

PROJECT_INTRO = """
<h2>{}</h2><h3>{}</h3><h3>{}</h3>
    <p>{}</p>
"""

PROJECT_LINK = """<a href="./projects/{}.html">{}</a>"""

PROJECT_TEMPLATE = """
<!----------------------------------------------------------------------------->
    <div class="article_container">
        <div class="article_text">
            {}
        </div><div></div>
        {}
    </div>
"""

# Used for project pages
PROJECT_DEFAULT_LAYOUT = """
    <div class="project_layout">
        {}
    </div>
"""

################################################################################

SLIDESHOW_PROJECT_TEMPLATE = """
        <{} class="slideshow_container" {} data-cycle="{}">
            {}
        </{}>
"""

YT_VIDEO_PROJECT_TEMPLATE = """
        <{} class="video_container" {}>
            <iframe style="border:0;" class="embedded_video" src="{}">
            </iframe>
        </{}>
"""

VIDEO_PROJECT_TEMPLATE = """
    <{} {}>
        <video class="project_video" controls muted autoplay loop>
          <source src="{}.mp4" type="video/mp4">
        </video>
    </{}>
"""

################################################################################

HEADER = """
<!doctype html>
<html lang="en">
<head>
    <title>Zodiac - {}</title>
    <meta charset="utf-8">
    <meta name="author" content="Zødiac">
    <meta name="description" content="Personal website">
    <meta name="keywords" content="Blender, DIY, Zodiac, ZodiacFRA, AI, Programmation">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🔳</text></svg>">
    <link rel="stylesheet" href="{}/style.css">
</head>

<body>
    <header>
        <div style="margin-right: 100px;">
            <h1><a href='{}/index.html'>Zødiac</a></h1>
            <h3 style='margin-top: -16px'>Code & 3d Art</h3>
        </div>
        <div class="header_icons">
          <a href="{}/3d.html" class="header_block">
            <img class="header_icon" style="height: auto; width: 33px; margin-top: 9px;" src="{}/media/misc/layers-svgrepo-com.svg">
            <h2 class="header_link">3D</h2>
          </a>
          <a href="{}/code.html" class="header_block">
            <img class="header_icon" style="height: auto; width: 44px; margin-top: 12px;" src="{}/media/misc/keyboard-svgrepo-com.svg">
            <h2 class="header_link">Code</h2>
          </a>
          <a href="{}/contact.html" class="header_block">
            <img class="header_icon" style="height: auto; width: 40px; margin-top: 12px;" src="{}/media/misc/email-svgrepo-com.svg">
            <h2 class="header_link">Contact</h2>
          </a>

        </div>
    </header>
<!--------------------------------------------------------------------------- HEADER END -->
"""
