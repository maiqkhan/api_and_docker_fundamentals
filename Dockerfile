# Start from python image in container
FROM python:3.12.3-slim-bookworm 

# copy uv and uvx folders from astral wbsite into bin folder
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/  

#Change working directoy
WORKDIR /app

# add virtual environment in app folder
ENV PATH="/app/.venv/bin:$PATH"

# Copy UV files into app folder to install packages
COPY .python-version pyproject.toml uv.lock ./

# install packages in container
RUN uv sync --locked 

# Copy main.py which contains API
COPY main.py ./

# Expose port 8000
EXPOSE 8000

#Run the uvicorn
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]