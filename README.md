# mtg-winchester-draft

# Running locally
To run ReasonReact app locally:
1. Run `npm install`
2. Run `npm run server` to set up bucklescript output at http://localhost:8000
3. In another terminal, run `npm start` to set up watch build
4. Access http://localhost:8000, saved changes should rebuild and hot reload

To run python app locally:
Currently, flask serves production build of React app, so build that first.
1. Run `npm install`
2. Run `npm run heroku-postbuild` to build production bundle
3. (one time) Run `export FLASK_APP=wsgi.py`
4. Run `flask run`