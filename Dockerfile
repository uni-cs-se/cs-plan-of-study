FROM python:latest
COPY . . 
RUN pip install fastapi httpx asyncio uvicorn
EXPOSE 8000
CMD ["uvicorn", "api:app", "--reload"]
