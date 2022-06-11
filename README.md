# CapturEat-API

Table of Contents
- [Installation](#installation)
- [API Documentation](#api-documentation)

# Installation
1. Go to cloud shell
2. Clone the repository
3. Create a directory inside /logs/ called model
4. Put the model inside of the newly created directory
5. Go to Cloud Shell
6. Run the following
```sh
cd /CapturEat-API
gcloud builds submit --tag gcr.io/$PROJECT-ID/$IMAGE-NAME
```
7. Go to Cloud Run
8. Create Service
9. Select the container
10. Write the service name
11. Click "Allow unauthenticated invocations"
12. Set the container port to ```8080```

# API Documentation
**URL**: ```https://captureat-***-et.a.run.app```

**Method**: ```GET```

**Code**: ```200```

**Response**: 
```
Server OK!
```

**URL**: ```https://captureat-***-et.a.run.app/predict```

**Method**: ```GET```

**Code**: ```200```

**Response**: 
```
Hello from Predict!
```

**URL**: ```https://captureat-***-et.a.run.app```

**Method**: ```POST```

**Data**: an image with key "image"

**Code**: ```200```
**Response**: 
```
{
    "recipe": [
        {
            "cleaned_ingredients": string,
            "id": integer,
            "image_link": string,
            "image_name": string,
            "instructions": string,
            "title": string
        }
    ]
}
```
