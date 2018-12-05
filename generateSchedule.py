from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader


def generateSchedule(graph):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template("report.html")
    
    nodes = graph.nodes
    blocks = {}
    colors = []

    # Format data
    for node in nodes:
        if node.color not in colors:
            colors.append(node.color)

    for color in colors:
        blocks[color] = []

    for node in nodes:
        cur = blocks[node.color]
        blocks[node.color] = cur + [node.name]

    # Generate Template
    template_vars = {"title":"Faculty Candidates' Weekend 2019",
                    "blocks":blocks}

    html_out = template.render(template_vars)

    # Generate PDF
    HTML(string=html_out).write_pdf("report.pdf")