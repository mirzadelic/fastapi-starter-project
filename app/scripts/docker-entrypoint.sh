#!/bin/bash
alembic upgrade head
python server.py
