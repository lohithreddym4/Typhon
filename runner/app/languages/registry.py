from app.languages.language_config import LanguageConfig


LANGUAGES = {

    "python": LanguageConfig(
        name="python",
        file_extension=".py",
        image="typhon-python",
        run_command=[
            "python",
            "/sandbox/python/main.py"
        ],
        container_path="/sandbox/python/main.py"
    ),
    "java": LanguageConfig(
        name="java",
        file_extension=".java",
        image="typhon-java",
        run_command=[
            "bash",
            "-c",
            "javac /sandbox/Main.java && java -cp /sandbox Main"
        ],
        container_path="/sandbox/Main.java"
    ),
    "cpp": LanguageConfig(
        name="cpp",
        file_extension=".cpp",
        image="typhon-cpp",
        run_command=[
            "bash",
            "-c",
            "g++ /sandbox/main.cpp -o /sandbox/main && /sandbox/main"
        ],
        container_path="/sandbox/main.cpp"
    )

}