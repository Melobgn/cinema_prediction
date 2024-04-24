docker build -t melobgn/django_cinapps ./cinapps/.
docker push melobgn/django_cinapps

docker build -t melobgn/api_cinapps ./API_s/.
docker push melobgn/api_cinapps

docker build -t melobgn/cron_cinapps ./automatisation/.
docker push melobgn/cron_cinapps


az container create --resource-group RG_BUGNONM --file deploy.yaml