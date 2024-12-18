# Flipkart ETL Pipeline 🛒📊

## 📋 Project Overview
This Apache Airflow-based ETL (Extract, Transform, Load) pipeline is designed to scrape and process hourly dataset updates from Flipkart, providing an automated and scalable data management solution.

## ✨ Key Features
- **Hourly Data Extraction**: Automated scraping of Flipkart product data
- **Docker Compose Support**: Easy setup and deployment
- **Robust ETL Process**: Comprehensive data extraction, transformation, and loading
- **Scalable Architecture**: Flexible pipeline design for seamless data management

## 🛠 Prerequisites
- Docker Desktop
- Docker CLI
- Python 3.8+
- Apache Airflow 2.x

## 🚀 Quick Start
### Using Docker Compose
1. Clone the repository:
   ```bash
   git clone https://github.com/SachinPrasanth777/Flipkart-ETL-Pipeline
   ```
2. Build and start the services:
   ```bash
   docker-compose up --build
   ```
3. Access Services:
   ### Airflow Web UI
   - **URL**: `http://localhost:8080`
   - **Username**: `airflow`
   - **Password**: `airflow`
   ### PgAdmin UI
   - **URL**: `http://localhost:5050`
   - **Username**: `admin@admin.com`
   - **Password**: `root`
   ### Minio UI (Object Storage)
   - **URL**: `http://localhost:9090`
   - **Username**: `airflow1234`
   - **Password**: `airflow1234`

## 📦 Project Structure
```
ETL-Pipeline/
│
├── dags/                   
│   ├── functions/          
│   │   ├── constants.py    
│   │   └── functions.py    
│   └── task.py     
│
├── docker-compose.yml      
├── Dockerfile              
└── requirements.txt        
```

## 📂 Functions Breakdown
### `dags/functions/constants.py`
Contains constant variables used across the ETL pipeline, such as:
- Scraping configurations
- Database connection parameters
- Predefined paths and URLs

### `dags/functions/functions.py`
Includes utility functions that support the ETL process:
- Data preprocessing methods
- Scraping helpers
- Data validation functions
- Logging and error handling utilities

### Scraping Configuration
Modify `dags/task.py` and supporting files in `functions/` to:
- Adjust scraping parameters
- Configure target product categories
- Set up data storage locations

## 📊 ETL Pipeline Workflow
1. **Extract**
   - Scrape product data from Flipkart
   - Handle rate limiting and anti-scraping measures
   - Capture product details, prices, ratings
2. **Transform**
   - Clean and normalize scraped data
   - Remove duplicates
   - Convert data types
3. **Load**
   - Store processed data in PostgreSQL
   - Store and update the same in MiniO

## 🕒 Scheduling
- **Frequency**: Hourly data updates
- **Configurable Intervals**: Easily modify in DAG definition

## 🔍 Monitoring
- Airflow Web UI for task tracking
- Detailed logging
- Task success/failure notifications
- PgAdmin UI for database monitoring
- MiniO UI for viewing buckets

## 🤝 Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 License
Distributed under the MIT License.

## 📞 Contact
Sachin Prasanth
- GitHub: [@SachinPrasanth777](https://github.com/SachinPrasanth777)

---

**Disclaimer**: Ensure compliance with Flipkart's terms of service and robots.txt when scraping data.

## 🖼️ Project Visualization
![Workflow](https://github.com/user-attachments/assets/1d6f8849-ae67-4d79-8f6e-323d8824116a)
