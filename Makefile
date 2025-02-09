install-packages:
	@pip install -r requirements.txt

start-Q2:
	@cd Q\ 2/app && uvicorn main:app --reload --port 8000

start-Q4:
	@cd Q\ 4/app && uvicorn main:app --reload --port 8000