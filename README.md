# Skillify: Student Skill Analyzer & Job Readiness Predictor

An end-to-end machine learning application that predicts whether a student is job-ready from quiz performance in Aptitude, DSA, DBMS and OS. It combines data preparation, model training and validation, and a deployed Flask app with analytics dashboards and personalized learning recommendations.

**Live Demo:** https://skillify-yjbs.onrender.com/
*(Hosted on Render's free tier, so the first request after idle may take about a minute.)*

---

## Problem Statement

Students often don't know which technical areas are holding them back before placements. Skillify turns quiz scores into a data-driven readiness prediction and a learning path, so students can see where to improve.

## Machine Learning Pipeline

### 1. Data
- **Source:** synthetic student performance data generated to mimic realistic score distributions across four subject areas (`data/`).
- **Records:** **[N]** samples
- **Target:** `job_ready` (Yes / No), **[describe the rule used to label it, e.g. weighted score threshold]**
- **Class balance:** **[X% ready / Y% not ready]**

### 2. Features
| Feature | Description |
|---|---|
| `aptitude_score` | Score in the aptitude quiz |
| `dsa_score` | Score in the DSA quiz |
| `dbms_score` | Score in the DBMS quiz |
| `os_score` | Score in the OS quiz |

### 3. Data Preparation
- Cleaning and validation with **pandas** (missing values, score range checks)
- Feature scaling with scikit-learn **[StandardScaler, if used]**
- Stratified train/test split (**[80/20]**)

### 4. Model Development
- **Model:** Logistic Regression (scikit-learn)
- **Baseline comparison:** **[Random Forest / Decision Tree / LightGBM]**
- **Tuning:** **[GridSearchCV over C and penalty, if done]**
- The trained estimator is saved as `job_ready_model.pkl` and loaded by the Flask app at runtime.

### 5. Model Validation
Evaluated on a held-out test set with **[X]-fold cross-validation**.

| Model | Accuracy | Precision | Recall | F1 |
|---|---|---|---|---|
| Logistic Regression | [ ] | [ ] | [ ] | [ ] |
| [Comparison model] | [ ] | [ ] | [ ] | [ ] |

Confusion matrix and feature coefficients: see `[notebook name].ipynb` or `[image path]`.

### 6. Deployment and Monitoring
- The model is served inside the Flask app and returns a readiness prediction after each quiz.
- Every quiz result is stored with a timestamp, so score history can be analysed and the model can later be retrained on real student data.

### Limitations
- The model is trained on synthetic data, so its accuracy reflects the labeling rule rather than real-world placement outcomes.
- Next step: collect consented real student data and validate against actual placement results.

---

## Application Features

- Secure student signup and login
- Student profile (branch, projects, internships, skills, confidence level)
- Branch-based quizzes for Aptitude, DSA, DBMS and OS
- Category-wise result summary
- Analytics dashboard with score history and performance insights
- Personalized learning path based on weak areas
- Job readiness prediction using the trained model
- Optional PostgreSQL and Cloudinary support for production

## Architecture

```
Browser → Flask routes (app.py) → Jinja templates
                 │
                 ├── Database (SQLite local / PostgreSQL production)
                 └── job_ready_model.pkl (Logistic Regression)
```

**Flow:** signup/login → profile → quizzes → results stored → analytics → ML prediction → learning path.

## Tech Stack

| Area | Tools |
|---|---|
| Machine Learning | Python, scikit-learn, pandas, NumPy, Pickle |
| Backend | Flask, Gunicorn |
| Database | SQLite (local), PostgreSQL (production) |
| Frontend | HTML, CSS, JavaScript, Jinja2 |
| Media | Cloudinary (profile images) |
| Deployment | Render |

## Repository Structure

```
app.py                 Main Flask application
init_db.py             Database initialization
train_model.py         Model training script
job_ready_model.pkl    Trained model
data/                  Questions and dataset files
templates/             HTML templates
static/                CSS, JS, images, uploads
requirements.txt       Dependencies
Procfile               Production start command
```

## Database Tables

- `users`: account and profile data
- `student_details`: branch, projects, internships, skills, confidence
- `quiz_results`: quiz score history
- `admin_users`: admin accounts

## Run Locally

```bash
git clone <repo-url>
cd skillify
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
python init_db.py
python train_model.py         # optional: retrain the model
python app.py
```

## Environment Variables (Production)

| Variable | Purpose |
|---|---|
| `SECRET_KEY` | Flask session secret |
| `DATABASE_URL` | PostgreSQL connection string (falls back to SQLite if unset) |
| `CLOUDINARY_CLOUD_NAME`, `CLOUDINARY_API_KEY`, `CLOUDINARY_API_SECRET` | Profile image uploads |

## Deployment (Render)

- Service type: Web Service, Python 3
- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn app:app`
- Note: the free tier has an ephemeral filesystem, so use PostgreSQL for persistent data.

## Future Improvements

- Train and validate on real student data
- Compare Random Forest, LightGBM and XGBoost; add hyperparameter tuning
- Track experiments and model versions with MLflow
- Add time-based analysis of score progression per student
- Resume parsing with NLP and internship/job recommendations
- Richer dashboard visualizations

## Author

**Cancy Khandelwal**: B.Tech CSE, Lovely Professional University
GitHub: github.com/Cancy-988 | Email: cancykhandelwal@gmail.com
