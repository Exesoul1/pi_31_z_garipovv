class Resume:
    def __init__(self):
        self.name = ""
        self.email = ""
        self.phone = ""
        self.summary = ""
        self.experience = []
        self.education = []
        self.skills = []
        self.languages = []
        self.certifications = []


    def __str__(self) -> str:
        return (
            f"=== {self.name} ===\n"
            f"Email: {self.email}\n"
            f"Телефон: {self.phone}\n"
            f"О себе: {self.summary}\n"
            f"Навыки: {', '.join(self.skills)}\n"
            f"Опыт: {len(self.experience)} позиций\n"
            f"Образование: {len(self.education)} записей"
        )


class ResumeBuilder:
    def __init__(self):
        self.resume = Resume()


    def set_name(self, name: str):
        self.resume.name = name
        return self


    def set_contacts(self, email: str, phone: str = ""):
        self.resume.email = email
        self.resume.phone = phone
        return self


    def set_summary(self, text: str):
        self.resume.summary = text
        return self


    def add_experience(self, company: str, years: int, role: str = ""):
        self.resume.experience.append({"company": company, "years": years, "role": role})
        return self


    def add_education(self, degree: str, school: str):
        self.resume.education.append({"degree": degree, "school": school})
        return self


    def add_skill(self, skill: str):
        self.resume.skills.append(skill)
        return self


    def add_language(self, lang: str):
        self.resume.languages.append(lang)
        return self


    def add_certification(self, cert: str):
        self.resume.certifications.append(cert)
        return self


    def build(self) -> Resume:
        return self.resume


class Director:
    @staticmethod
    def build_standard(name: str, email: str, skills: list[str]) -> Resume:
        return (
            ResumeBuilder()
            .set_name(name)
            .set_contacts(email)
            .add_skill(skills[0] if skills else "")
            .build()
        )


    @staticmethod
    def build_extended(name: str, email: str, phone: str, skills: list[str], experience: list[dict]) -> Resume:
        builder = ResumeBuilder().set_name(name).set_contacts(email, phone)
        for skill in skills:
            builder.add_skill(skill)
        for exp in experience:
            builder.add_experience(exp["company"], exp["years"], exp.get("role", ""))
        return builder.build()


# Пример 
if __name__ == "__main__":
    # Стандартное резюме — быстро и просто
    resume1 = Director.build_standard(
        name="Анна Иванова",
        email="anna@example.com",
        skills=["Python", "SQL"]
    )
    print(resume1)

    print("-" * 30)


    # Расширенное резюме — через билдер пошагово
    resume2 = (
        ResumeBuilder()
        .set_name("Иван Петров")
        .set_contacts("ivan@example.com", "+7-900-123-45-67")
        .set_summary("Разработчик с 5-летним опытом")
        .add_experience("Яндекс", 3, "Backend Developer")
        .add_experience("Сбер", 2, "Junior Developer")
        .add_education("Бакалавр", "МГУ")
        .add_skill("Python")
        .add_skill("Docker")
        .add_language("Английский")
        .build()
    )
    print(resume2)
