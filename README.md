on```
# Aedion_AI  Project  
```
```
# Author: Collins Akoja Nathaniels  
```
# Framework: Flask (Python)  



## Overview
```
This project is a simple AI-powered Flask API with two key features:
1. Image Analysis – Simulates detection of normal or abnormal patterns in an uploaded image.  
2. Text Analysis – Analyzes symptom descriptions and returns a quick advisory.  

It also includes an Ethics Filter that ensures all AI responses remain safe and neutral.
```

##  How to Run

###  Create Virtual Environment
```on terminal run
python -m venv myenv
venv\Scripts\activate       
# this is  for Windows
```

### Install Requirements
```terminal
pip install -r requirements.txt
```

### Run the App
```terminal/cmd
python app.py
```

## You will see something like:
```
 Running on http://127.0.0.1:5000/
```


##  API Endpoints

###  Home
```GET   
Returns a welcome message and available endpoints.
```
###  Analyze Image
```
 POST /analyze_image
Upload an image file.
```
Example (using URL):
## terminal 
```curl -X POST -F "image= normal.jpg" http://127.0.0.1:5000/analyze_image
```

## Response Example:
``` json
{
  "label": "abnormal",
  "mean_color": 134.2,
  "edge_score": 58.3,
  "advisory": "Possible irregular skin pattern. Please consult a dermatologist.",
  "time_taken_sec": 0.42
}
```

###  Analyze Text
``` POST /analyze_text
Send a JSON body containing a “symptom” string.
```

## run on terminal :
```
curl -X POST -H "Content-Type: application/json" -d '{"symptom": "I have a headache and fever"}' http://127.0.0.1:5000/analyze_text
```

## Response : 
``` json
{
  "analysis": "Possible mild infection. Rest and hydrate.",
  "time_taken_sec": 0.33
}

```
## File Structure
```
#   AedionAI_Project
 #  app.py                # Flask API app
 #  image_classifier.py   # Image analyzer
 # text_analyzer.py      # Symptom text analyzer
 # ethics_filter.py      # Filters unsafe responses
 # requirements.txt      # Dependencies
  # README.md             # Project instructions
```
##  Ethics Filter
```All AI outputs were checked to avoid unsafe claims or medical confirmations.  
Unsafe phrases like “You are confirmed to have…” are replaced with:
statements like  Visit a Doctor for confirmation.
```

## Status
````- [x] Image analyzer working  
- [x] Ethics filter active  
- [x] Flask app tested  
- [ ]  (Add) text_analyzer.py for full completion  
```
```
# End of Project 
```