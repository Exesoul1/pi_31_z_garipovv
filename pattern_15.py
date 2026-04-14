from dataclasses import dataclass, field


@dataclass
class Email:
    from_addr: str
    to: list[str]
    subject: str
    cc: list[str] = field(default_factory=list)
    bcc: list[str] = field(default_factory=list)
    text_body: str = ""
    html_body: str = ""
    attachments: list[str] = field(default_factory=list)

    def __str__(self) -> str:
        return (
            f"От: {self.from_addr}\n"
            f"Кому: {', '.join(self.to)}\n"
            f"Тема: {self.subject}\n"
            f"Вложений: {len(self.attachments)}"
        )



class EmailBuilder:
    def __init__(self):
        self._from_addr = ""
        self._to = []
        self._cc = []
        self._bcc = []
        self._subject = ""
        self._text_body = ""
        self._html_body = ""
        self._attachments = []

    def set_from(self, addr: str):
        self._from_addr = addr
        return self

    def add_to(self, addr: str):
        self._to.append(addr)
        return self

    def add_cc(self, addr: str):
        self._cc.append(addr)
        return self

    def add_bcc(self, addr: str):
        self._bcc.append(addr)
        return self

    def set_subject(self, subject: str):
        self._subject = subject
        return self

    def set_text_body(self, text: str):
        self._text_body = text
        return self

    def set_html_body(self, html: str):
        self._html_body = html
        return self

    def add_attachment(self, path: str):
        self._attachments.append(path)
        return self

    def build(self) -> Email:
        if not self._from_addr or not self._to or not self._subject:
            raise ValueError("Отправитель, получатель и тема — обязательные поля")
        return Email(
            from_addr=self._from_addr,
            to=self._to.copy(),
            subject=self._subject,
            cc=self._cc.copy(),
            bcc=self._bcc.copy(),
            text_body=self._text_body,
            html_body=self._html_body,
            attachments=self._attachments.copy()
        )


class Director:
    def __init__(self, builder: EmailBuilder):
        self.builder = builder

    def build_welcome_email(self, to_addr: str, username: str) -> Email:
        return (
            self.builder
            .set_from("welcome@company.com")
            .add_to(to_addr)
            .set_subject(f"Добро пожаловать, {username}!")
            .set_text_body(f"Привет, {username}! Рады видеть вас в нашей команде.")
            .set_html_body(f"<h1>Привет, {username}!</h1><p>Рады видеть вас в нашей команде.</p>")
            .build()
        )


    def build_password_reset_email(self, to_addr: str, reset_link: str) -> Email:
        return (
            self.builder
            .set_from("security@company.com")
            .add_to(to_addr)
            .set_subject("Сброс пароля")
            .set_text_body(f"Перейдите по ссылке для сброса: {reset_link}")
            .set_html_body(f"<p>Перейдите по <a href='{reset_link}'>ссылке</a> для сброса пароля.</p>")
            .build()
        )


if __name__ == "__main__":
    director = Director(EmailBuilder())
    
    email1 = director.build_welcome_email("user@example.com", "Иван")
    print(email1)
    print("-" * 40)

    email2 = director.build_password_reset_email(
        "user@example.com",
        "https://app.com/reset/abc123"
    )
    print(email2)
    print("-" * 40)

    email3 = (
        EmailBuilder()
        .set_from("noreply@company.com")
        .add_to("client@example.com")
        .add_cc("manager@company.com")
        .set_subject("Ваш счёт №1234")
        .set_html_body("<h1>Счёт</h1>")
        .add_attachment("invoice_1234.pdf")
        .build()
    )
    print(email3)
