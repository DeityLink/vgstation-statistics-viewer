import os

# Non-Flask, SQLAlchemy, lib stuff, just for our use!
basedir = os.path.abspath(os.path.dirname(__file__))

# General settings
debug = True
host = '0.0.0.0'
port = 5000

# Path to stat files. Default value MUST be changed.
STATS_DIR = os.path.join(basedir, 'test-statfiles')
# This is where files get moved to once they're batch processed. They will never be used again and are kept around only for debugging the server code.
PROCESSED_DIR = os.path.join(STATS_DIR, 'processed')
# Files that could not be parsed.
UNPARSABLE_DIR = os.path.join(STATS_DIR, 'unparsable')

# Database
SQLALCHEMY_TRACK_MODIFICATIONS = False  # On production, set this to false.
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db', 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db', 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = debug  # Track on debug

# No longer used due to Manager implementation
# Load from arguments
# if len(sys.argv) > 1:
#     if sys.argv[1] == 'debug':
#         debug = True
#         SQLALCHEMY_TRACK_MODIFICATIONS = True


# App settings
MATCHES_PER_PAGE = 24  # Works best as a multiple of 3
