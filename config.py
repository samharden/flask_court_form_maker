import os
#basedir = os.path.abspath(os.path.dirname(__file__))

#print 'basedir = ', basedir
#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app//odyssey.db')
#SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
#SQLALCHEMY_TRACK_MODIFICATIONS = False
WTF_CSRF_ENABLED = True
SECRET_KEY = 'not-much-of-a-secret'
print "In Config"