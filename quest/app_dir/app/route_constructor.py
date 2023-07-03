from hashlib import md5

ROUTE_TEMPLATE = """

@app.route("/{path}")
def {task_name}():
    return render_template("{template}")

"""


def _add_page(ansr: str, templ_name: str, func_name: str):
    path = _get_path(ansr)
    with open(r'runner.py', 'a') as f:
        f.write(ROUTE_TEMPLATE.format(path=path, task_name=func_name, template=templ_name))


def _get_path(answer: str) -> str:
    path = md5(answer.encode('utf-8')).hexdigest()
    return path


if __name__ == "__main__":
    answer = input("Введите правильный ответ: ")
    template_name = input("Введите имя шаблона: ")
    task_name = input("Введите имя функции: ")
    _add_page(answer, template_name, task_name)
