# 🛍️ ClothingStore

An interactive web application for an online clothing store, built with Django and PostgreSQL.

---

## 🚀 How to Run the Project Locally

1. **Clone the repository**:

    ```bash
    git clone https://github.com/KarasunoAs9/pet-project
    cd clothing_store
    ```

2. **Create a virtual environment and install dependencies**:

    **Windows**:
    ```bash
    python -m venv .venv
    .venv\Scripts\activate
    pip install -r requirements.txt
    ```

    **Mac/Linux**:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

3. **Set up the PostgreSQL database**:

    Ensure PostgreSQL is installed and running. Create a database named `clothing-store`:

    ```bash
    createdb clothing-store
    ```

4. **Import data into the database**:

    Use the provided `db_dump.sql` file to populate the database:

    ```bash
    psql -U postgres -d clothing-store < db_dump.sql
    ```

    **PostgreSQL password**: `1111`

5. **Apply migrations**:

    ```bash
    python manage.py migrate
    ```

6. **Run the development server**:

    ```bash
    python manage.py runserver
    ```

7. **Open the browser**:

    Go to [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## 📂 Project Structure

```csharp
clothing_store/
├── clothing_store/         # Project settings
├── reviews/                # Reviews module
├── shopping/               # Shopping module
├── store/                  # Main store app
├── app_auth/               # Authentication and registration
├── static/                 # Static files
├── media/                  # Media files (images, etc.)
├── templates/              # HTML templates
├── db_dump.sql             # Database dump
├── requirements.txt        # Python dependencies
└── README.md               # Project setup instructions
