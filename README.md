### aio_app

#### Run
````python
git clone https://github.com/flatline-dot/aio_app.git
cd aio_app/
docker-compose up -d
````

#### Run make_requests.py
````python
source env/bin/activate
pip install -r requirements.txt
python3 make_requests.py --n <NUMBER OF REQUESTS> --attachment_depth <ATTACHMENT_DEPTH_JSON>
