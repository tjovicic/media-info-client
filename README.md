# Media info client

Python client for determining video formats using Mediainfo. 

It assumes files are accessed using https://github.com/tjovicic/google-drive-client.

## Run locally
`docker-compose up -d`

# Stop locally
`docker-compose down --rmi all -v --remove-orphans`

## Cloud Run
```
{
  gcloud builds submit --tag gcr.io/<project>/mediainfo
  gcloud beta run deploy mediainfo \
  --image gcr.io/<project>/mediainfo \
  --platform managed \
  --region <region> \
  --update-env-vars GOOGLE_CLIENT_URL=https://google-client-test.a.run.app
}
```


## Learn more
https://developers.google.com/drive/api/v3/enable-shareddrives

https://pymediainfo.readthedocs.io/en/stable/