# tradetracker

## Getting started

### Requirements
1. Install [Docker](https://docs.docker.com/get-docker)
2. Install [Python 3](https://wiki.python.org/moin/BeginnersGuide/Download)
3. Install [Node.js](https://nodejs.org/en/download/)
4. A [python virtual environment](https://docs.python.org/3/tutorial/venv.html) for your workspace

### Development server
1. Create a new `.env` file based on `.env.example`
2. Activate python virtual environment `source ./bin/activate`
3. Run command `docker-compose up`
    - to start with a new database, run `docker-compose up -V`

### Development server with debugger
1. Create a new `.env` file based on `.env.example`
2. Activate python virtual environment `source ./bin/activate`
3. Add debugger configuration in [VS Code](https://code.visualstudio.com/docs/containers/docker-compose#_python) (Step 1 - 3)
4. Run command `source ./scripts/debug-mode.sh`
    - to start with a new database, run `source ./scripts/debug-mode.sh -V`
5. Launch debugger from the Debug tab in VS Code

### Quick links
- [Client (localhost)](http://localhost)
- [GraphiQL (localhost:8000/graphql/)](http://localhost:8000/graphql/)
- [Django admin (localhost:8000/admin)](http://localhost:8000/admin)

### Create new Django superuser
```
docker exec -it tradetracker_web_1 python manage.py createsuperuser
```