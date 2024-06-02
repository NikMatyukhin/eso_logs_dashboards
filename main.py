import dotenv

from src.app import create_app

if __name__ == "__main__":
    dotenv.load_dotenv(".env")

    app = create_app()
    app.run_server(debug=True)
