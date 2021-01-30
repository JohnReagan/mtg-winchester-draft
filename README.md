# mtg-winchester-draft

# Running locally
To run ReasonReact app locally:
1. Run `npm install`
2. Run `npm run server` to set up bucklescript output at http://localhost:8000
3. In another terminal, run `npm start` to set up watch build
4. Access http://localhost:8000, saved changes should rebuild and hot reload

To run python app locally:
One time python setup
1. Set up and activate virtual environment for python under venv directory
2. Run `export FLASK_APP=wsgi.py`

Currently, flask serves production build of React app, so build that first. Note front end changes will require rebuilding production bundle.
1. Run `npm install`
2. Run `npm run heroku-postbuild` to build production bundle
3. Run `pip install -r requirements.txt`
4. Run `flask run` to serve from http://127.0.0.1:5000/ 