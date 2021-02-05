import pandas as pd
from flask_caching import Cache
from sklearn import datasets

from .server import app

# Setup flask chaching
CACHE_CONFIG = {"CACHE_TYPE": "simple"}
cache = Cache()
cache.init_app(app.server, config=CACHE_CONFIG)

# Other option is:
# 'CACHE_REDIS_URL': os.environ.get('REDIS_URL', 'redis://localhost:6379')


# Load iris dataset and cache.
@cache.memoize()
def global_store_iris():
    iris_raw = datasets.load_iris()
    iris = pd.DataFrame(iris_raw["data"], columns=iris_raw["feature_names"])
    return iris
