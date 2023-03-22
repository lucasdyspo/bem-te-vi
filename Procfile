web: gunicorn bemtevi.wsgi --chdir backend --limit-request-line 8188 --log-file -
worker: REMAP_SIGTERM=SIGQUIT celery --workdir backend --app=bemtevi worker --loglevel=info
beat: REMAP_SIGTERM=SIGQUIT celery --workdir backend --app=bemtevi beat -S redbeat.RedBeatScheduler --loglevel=info
