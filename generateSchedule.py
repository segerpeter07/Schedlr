from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("report.html")



def generateSchedule(graph):
    nodes = graph.nodes

    blocks = {}
    colors = []

    for node in nodes:
        if node.color not in colors:
            colors.append(node.color)

    for color in colors:
        blocks[color] = []


    for node in nodes:
        blocks[node.color] = [blocks[node.color],node.name]

    template_vars = {"title":"Faculty Candidates' Weekend 2019",
                    "blocks":blocks}

    html_out = template.render(template_vars)

    HTML(string=html_out).write_pdf("report.pdf")