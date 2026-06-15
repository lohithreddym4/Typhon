from app.languages.language_config import LanguageConfig


LANGUAGES = {

    "python": LanguageConfig(
        name="python",
        file_extension=".py",
        image="typhon-python",
        run_command=[
            "python",
            "/sandbox/main.py"
        ]
    )

}