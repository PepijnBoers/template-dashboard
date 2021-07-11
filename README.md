# Template for simple web application
GitHub template that can be used for the creation of (interactive) web applications using Plotly's [Dash](https://plotly.com/dash/).

## Properties

- Automatic Flake8 code quality check on push/pull request
- Automatic pytests on `/tests/` with push/pull request
- Basic folder structure
- Requirements and setup file

## Heroku
The app can be easily deployed with the use of [Heroku](https://www.heroku.com/). The following commands (1) create Heroku application, (2) push master to Heroku remote, (3) start a dyno and (4) open the webapp.

```
heroku create
git push heroku master
heroku ps:scale web=1
heroku open
```

## Imports
When importing functions from files in the `dashboard` directory make sure to important them as follows:
```python
from .file import function
```

### Reference links

- [Sidebar example](https://dash-bootstrap-components.opensource.faculty.ai/examples/simple-sidebar/)
- [Iris k-mean example](https://dash-bootstrap-components.opensource.faculty.ai/examples/iris/)
- [Spliting callback definitions in multiple files](https://community.plotly.com/t/splitting-callback-definitions-in-multiple-files/10583/2)
- [Sharing data between callbacks](https://dash.plotly.com/sharing-data-between-callbacks)
