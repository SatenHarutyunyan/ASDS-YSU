# asds-ysu
Repository for Applied Statistics &amp; Data Science Program in Yerevan State University (ASDS-YSU)

## About
This repository contains multiple (stand-alone) projects.

Clone the Repo and and do the following steps:

1. `python3 -m venv .<project_name>`   ex. pyton3 -m venv .recipe
2. `source .<project_name>/bin/activate`
3. `pip install -U pip`
4. `pip install -r requirements/<project_name>.txt`

In workspace you will see files like `<project_name>`.py which is the `main.py` for the corresponding project.


# Projects

## 1. AutoML

Status: In process

## 2. Recipe

Status: In progress

## 3. social_sentiment

Using PySpark engine, project solves the problem of  `real time` prediction for posts
from social sites (Facebook, Twitter), to determinie whether 
posts are containing offensive language or not.

Project Structure

```
        .   
    │───data
    │   │-tweet_sentiments.csv
    │───services
    │   │-facebook.py  //
    │   │-twitter.py  // not implemented
    │───spark
    │   │──core
    │   │  │-session.py
    │   │  │-context.py
    │   │  │-streaming.py
    │   │──ml
    │   │  │-estimator.py
    │   │  │-pipeline.py
    │   │  │-transformer.py
    └───utils
        │-schema.py
          
```

**make sure you have the `spark` properly installed on your machine.**

__Build__

```bash
python3 - venv .social_sentiment
source .social_sentiment/bin/activate
pip install -U pip
pip install -r requirements/social_sentiment.txt
```

__Run__

```bash
python social_sentiment.py localhost 4455 // start the engine
nc -lk 4455 // write streams here
```

*Click to see the attached video-demo.*

[![Watch the video](https://upload.wikimedia.org/wikipedia/commons/f/f3/Apache_Spark_logo.svg)](https://youtu.be/KxamtBWWlAg)
