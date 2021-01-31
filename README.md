# mtg-winchester-draft

# Running locally
One time python setup
1. Set up and activate virtual environment for python under venv directory
2. Run `export FLASK_APP=wsgi.py`
3. Run `pip install -r requirements.txt`

To run locally:
1. Run `npm install`
2. Run `npm start` to set up bundle output at http://localhost:3000
3. In another terminal, run `npm run start-api` to start flask api at http://localhost:5000
4. Access http://localhost:3000, saved changes should rebuild and hot reload