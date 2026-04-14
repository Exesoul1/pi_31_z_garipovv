from copy import deepcopy


class SenderInfo:
    def __init__(self, name: str, email: str, reply_to: str = ""):
        self.name = name
        self.email = email
        self.reply_to = reply_to or email


    def __str__(self) -> str:
        return f"{self.name} <{self.email}>"


class EmailTemplate:
    def __init__(self, subject: str, html_body: str, sender: SenderInfo, recipients: list[str] = None):
        self.subject = subject
        self.html_body = html_body
        self.sender = sender
        self.recipients = recipients or []


    def personalize(self, name: str, **kwargs) -> None:
        self.subject = self.subject.replace("{{name}}", name)
        self.html_body = self.html_body.replace("{{name}}", name)
        for key, value in kwargs.items():
            self.html_body = self.html_body.replace(f"{{{{{key}}}}}", str(value))


    def __str__(self) -> str:
        return (
            f"От: {self.sender}\n"
            f"Тема: {self.subject}\n"
            f"Кому: {self.recipients}\n"
            f"Тело: {self.html_body[:60]}..."
        )


    def clone(self) -> "EmailTemplate":
        return deepcopy(self)


class TemplateRegistry:
    def __init__(self):
        self._templates = {}


    def register(self, name: str, template: EmailTemplate):
        self._templates[name] = template


    def get(self, name: str) -> EmailTemplate:
        if name not in self._templates:
            raise ValueError(f"Шаблон '{name}' не найден")
        return self._templates[name].clone()


if __name__ == "__main__":
    registry = TemplateRegistry()
    registry.register("welcome", EmailTemplate(
        subject="Добро пожаловать, {{name}}!",
        html_body="<h1>Привет, {{name}}!</h1><p>Рады видеть вас.</p>",
        sender=SenderInfo("Команда сервиса", "noreply@service.com"),
    ))

    for user in [("Анна", "anna@example.com"), ("Иван", "ivan@example.com")]:
        tpl = registry.get("welcome")
        tpl.recipients = [user[1]]
        tpl.personalize(user[0])
        print(tpl)
        print("---")
