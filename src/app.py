from src import AppFactory

appFactory = AppFactory()
appFactory.init_with_api()
appFactory.init_with_db()
appFactory.init_with_query_inspect()

app = appFactory.app


if __name__ == "__main__":
    app.run()
